"""
This code demonstrates how a lock can be used to control access to shared data.
Code from - https://realpython.com/intro-to-python-threading/#basic-synchronization-using-lock
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
        self.lock = threading.Lock()

    def update(self):
        """
        Simulates a thread accessing a database and updating its data.
        A thread increments the value of the database and goes to sleep
        (to simulate race condition situations - for educational purposes).
        After waking up it writes the new value to the database. Since
        we use locks, the race condition never happens. Only 1 thread
        can run the code defined by the lock at a time. If another
        thread tried to access it, it is made to wait until the lock
        is released.
        """
        logging.info(f"Thread {threading.current_thread().name}: starting "
                     f"update")
        logging.info(f"Thread {threading.current_thread().name}: Acquiring lock!")

        with self.lock:
            logging.info(
                f"Thread {threading.current_thread().name}: lock acquired!")
            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy
            logging.info(
                f"Thread {threading.current_thread().name}: Releasing lock!")
        logging.info(f"Thread {threading.current_thread().name}: finishing "
                     f"update")


def main():
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