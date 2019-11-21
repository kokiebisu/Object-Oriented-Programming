from city_processor import CityDatabase, CityOverheadTimes, ISSDataRequest


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


def main():
    db = CityDatabase('./city_locations_test.xlsx')
    queue = CityOverheadTimeQueue()
    for city in db.city_db:
        queue.put(ISSDataRequest.get_overhead_pass(city))
        print(queue.get())


if __name__ == '__main__':
    main()
