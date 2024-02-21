import threading
import time


class Doctor(threading.Thread):
    running = True

    def __init__(self, index, left_screw: threading.Lock, right_screw: threading.Lock):
        super().__init__()
        self.index = index
        self.left = left_screw
        self.right = right_screw

    def run(self) -> None:
        while self.running:
            self.try_to_eat()
            time.sleep(1)

    def try_to_eat(self):
        if not self.left.locked() and not self.right.locked():
            self.left.acquire()
            self.right.acquire()
            print(f"Doctor {self.index + 9} BLAST!")
            self.left.acquire(timeout=1)
            self.right.release()
            self.left.release()
            time.sleep(2)
            self.running = False


def main():
    screws = [threading.Lock() for i in range(5)]
    doctors = [
        Doctor(index=i, left_screw=screws[i], right_screw=screws[(i + 1) % 5])
        for i in range(5)
    ]

    for doc in doctors:
        doc.start()
        # time.sleep(0.1)


if __name__ == "__main__":
    main()
