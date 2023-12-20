"""SchedulerFactory module."""
from TrafficLightScheduler.schedulers.RandomScheduler import RandomScheduler
from TrafficLightScheduler.schedulers.RoundRobinScheduler import RoundRobinScheduler


class SchedulerFactory:
    """Factory class for schedulers"""

    @staticmethod
    def create(schedular_name, options):
        if schedular_name == "random":
            return RandomScheduler(options)
        elif schedular_name == "round_robin":
            return RoundRobinScheduler(options)

        raise Exception("Unknown scheduler: " + schedular_name)
