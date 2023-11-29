"""SchedulerFactory module."""
from TrafficLightScheduler.schedulers.LeastTrafficScheduler import LeastTrafficScheduler
from TrafficLightScheduler.schedulers.LotteryScheduler import LotteryScheduler
from TrafficLightScheduler.schedulers.RandomScheduler import RandomScheduler
from TrafficLightScheduler.schedulers.RoundRobinScheduler import RoundRobinScheduler
from TrafficLightScheduler.schedulers.VirtualRoundRobinScheduler import VirtualRoundRobinScheduler


class SchedulerFactory:
    """Factory class for schedulers"""

    @staticmethod
    def create(schedular_name, options):
        if schedular_name == "least_traffic":
            return LeastTrafficScheduler(options)
        elif schedular_name == "lottery":
            return LotteryScheduler(options)
        elif schedular_name == "random":
            return RandomScheduler(options)
        elif schedular_name == "round_robin":
            return RoundRobinScheduler(options)
        elif schedular_name == "virtual_round_robin":
            return VirtualRoundRobinScheduler(options)

        raise Exception("Unknown scheduler: " + schedular_name)
