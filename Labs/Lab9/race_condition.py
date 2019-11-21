"""
This code emulates a race condition.
Code from - https://realpython.com/intro-to-python-threading/#race-conditions
"""
import concurrent.futures
import time
import logging
import threading


class FakeDatabase:
    """
    A fake database which maintains a value. This is accessed and
    shared by multiple threads.
    """

    def __init__(self):
        """
        Initialize the value that is shared.
        """
        self.value = 0

    def update(self):
        """
        Simulates a thread accessing a database and updating its data.
        A thread increments the value of the database and goes to sleep
        (to allow a race confition to happen - for educational purposes).
        After waking up it writes the new value to the database.
        """
        logging.info(f"Thread {threading.current_thread().name}: starting "
                     f"update")
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy
        logging.info(f"Thread {threading.current_thread().name}: finishing "
                     f"update")


def main():
    """
    Creates 2 threads that access the shared fake database.
    This causes a race condition to happen.
    """
    database = FakeDatabase()
    logging.info("Testing update. Starting value is %d.", database.value)
    t1 = threading.Thread(target=database.update)
    t2 = threading.Thread(target=database.update)

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    logging.info("Testing update. Ending value is %d.", database.value)


if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    main()