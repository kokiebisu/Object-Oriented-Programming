from city_processor import CityDatabase, CityOverheadTimes, ISSDataRequest
import time
import threading
import math


class CityOverheadTimeQueue:
    def __init__(self) -> None:
        """
        Instantiates an attribute called data_quere as an empty list
        """
        self.data_queue = []
        self.access_queue_lock = threading.Lock()

    def put(self, overhead_time: CityOverheadTimes) -> None:
        """
        Responsible fir adding to the queue. Accept a overhead_time 
        parameter and append it to the data_queue list.
        :param overhead_time: a CityOverheadTimes object
        """
        with self.access_queue_lock:
            self.data_queue.append(overhead_time)

    def get(self) -> CityOverheadTimes:
        """
        Responsible for removing an element from a Queue. Each all to this emethod should 
        return the element at index 0 and delete it from the list. Use the del keyword to
        delete the element as this will also automatically move all the other elements 
        so there will be no empty spaces.
        :return: a CityOverheadTimes object
        """
        with self.access_queue_lock:
            if not self.data_queue:
                exit()
            element = self.data_queue[0]
            del self.data_queue[0]
            return element

    def __len__(self) -> int:
        """
        Returns the length of the data_queue
        :return: an int
        """
        return len(self.data_queue)


class ProducerThread(threading.Thread):
    def __init__(self, cities: list, queue: CityOverheadTimeQueue) -> None:
        """
        Initializes the class with a list of City Objects as well as a CityOverheadTimeQueue
        :param cities: a list
        :param queue: a CityOverheadTimeQueue object
        """
        super().__init__()
        self.cities = cities
        self.queue = queue

    def run(self) -> None:
        """
        Executes when the thread starts. Loops over each City and pass it to the 
        ISSDataRequest.get_overheadpass() method. It then proceeds to add the city to
        the queue. After reading in 5 cities, the thread should sleep for 1 second.
        """
        count = 1
        for city in self.cities:
            if count == 5:
                time.sleep(1)
                count = 1
            overhead_time = ISSDataRequest.get_overhead_pass(city)
            self.queue.put(overhead_time)
            print(f"Producer Thread: {count}")
            count += 1


class ConsumerThread(threading.Thread):
    """
    Responsible for consuming data from the queue and printing it out to the console.
    """

    def __init__(self, queue: CityOverheadTimeQueue) -> None:
        """
        Initializes the ConsumerThread with the same queue as the one the producer has. 
        It also implements a data_incoming boolean attribute that is set to True. This 
        attribute should change to False after the producer thread has joined the main
        thread and finished processing all the cities.
        :param queue: a CityOverheadTimeQueue object
        """
        super().__init__()
        self.queue = queue
        self.data_incoming = True
        # should change to False after the producer thread has joined the main thread
        # and finished processing all the cities

    def run(self) -> None:
        """
        Gets an item from the queue and print it to the console and then sleep for 0.5 seconds.
        While processing the queue, if the queue is empty, it puts the thread to sleep for 0.75
        seconds.
        """
        while self.data_incoming or len(self.queue) > 0:
            if not self.queue:
                time.sleep(0.75)
            print(f"Consumer Thread: {self.queue.get()}")
            time.sleep(0.5)

    def stop_incoming(self) -> None:
        """
        Stops the run method.
        """
        self.data_incoming = False


def divide_list(dividing_list: list, n: int) -> generator:
    """
    Divides the list into smaller n sized lists
    :param dividing_list: a list
    :param n: an int
    """
    for i in range(0, len(dividing_list), n):
        yield dividing_list[i:i + n]


def main():
    """
    Drives the program
    """
    db = CityDatabase('./city_locations_test.xlsx')
    divided_list = list(divide_list(db.city_db, math.ceil(len(db.city_db)/4)))
    first = divided_list[0]
    second = divided_list[1]
    third = divided_list[2]
    fourth = divided_list[3]
    queue = CityOverheadTimeQueue()
    for city in db.city_db:
        queue.put(ISSDataRequest.get_overhead_pass(city))

    # Creating Threads
    pt1 = ProducerThread(first, queue)
    pt2 = ProducerThread(second, queue)
    pt3 = ProducerThread(third, queue)
    pt4 = ProducerThread(fourth, queue)
    ct = ConsumerThread(queue)

    # Starting Threads
    pt1.start()
    pt2.start()
    pt3.start()
    pt4.start()
    ct.start()

    # Running Methods
    pt1.run()
    pt2.run()
    pt3.run()
    pt4.run()
    ct.run()

    # Joining with main thread
    pt1.join()
    pt2.join()
    pt3.join()
    pt4.join()
    ct.stop_incoming()
    ct.join()


if __name__ == '__main__':
    main()
