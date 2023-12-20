from abc import ABC, abstractmethod
from TrafficLightScheduler.simulation.Simulation import Simulation


class Scheduler(ABC):
    def __init__(self, options):
        self.options = options

    @abstractmethod
    def tick(self, simulation: Simulation):
        pass

    @abstractmethod
    def create_submission(self, simulation: Simulation):
        pass
