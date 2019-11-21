from city_processor import CityDatabase, CityOverheadTimes, ISSDataRequest
import time
import threading


class CityOverheadTimeQueue:
    def __init__(self) -> None:
        """
        Instantiates an attribute called data_quere as an empty list
        """
        self.data_queue = []

    def put(self, overhead_time: CityOverheadTimes) -> None:
        """
        Responsible fir adding to the queue. Accept a overhead_time 
        parameter and append it to the data_queue list.
        """
        self.data_queue.append(overhead_time)

    def get(self) -> CityOverheadTimes:
        """
        Responsible for removing an element from a Queue. Each all to this emethod should 
        return the element at index 0 and delete it from the list. Use the del keyword to
        delete the element as this will also automatically move all the other elements 
        so there will be no empty spaces.
        """
        element = self.data_queue[0]
        del self.data_queue[0]
        return element

    def __len__(self) -> int:
        """
        Returns the length of the data_queue
        """
        return len(self.data_queue)


class ProducerThread(threading.Thread):
    def __init__(self, cities: list, queue: CityOverheadTimeQueue) -> None:
        """
        Initializes the class with a list of City Objects as well as a CityOverheadTimeQueue
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
            print(f"Added {count}")
            count += 1


class ConsumerThread(threading.Thread):
    pass


def main():
    db = CityDatabase('./city_locations_test.xlsx')
    queue = CityOverheadTimeQueue()
    for city in db.city_db:
        queue.put(ISSDataRequest.get_overhead_pass(city))
    pt = ProducerThread(db.city_db, queue)
    pt.start()
    pt.join()


if __name__ == '__main__':
    main()
