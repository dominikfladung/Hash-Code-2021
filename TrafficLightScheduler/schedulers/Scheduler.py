from abc import ABC, abstractmethod


class Scheduler(ABC):
    def __init__(self, options):
        self.options = options

    @abstractmethod
    def tick(self):
        pass
