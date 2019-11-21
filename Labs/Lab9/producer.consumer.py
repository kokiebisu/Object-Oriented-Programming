class CityOverheadTimeQueue:
    def __init__(self) -> None:
        """
        Instantiates an attribute called data_quere as an empty list
        """
        data_queue = []

    def put(self, overhead_time: city_processor.CityOverheadTimes) -> None:
        """
        Responsible fir adding to the queue. Accept a overhead_time 
        parameter and append it to the data_queue list.
        """
        pass

    def get(self) -> city_processor.CityOverheadTime:
        """
        Responsible for removing an element from a Queue.Each all to this emethod should 
        return the element at index 0 and delete it from the list. Use the del keyword to
        delete the element as this will also automatically move all the other elements 
        so there will be no empty spaces.
        """
        pass

    def __len__(self) -> int:
        """
        Returns the length of the data_queue
        """
        pass


def main():
    pass


if __name__ == '__main__':
    main()
