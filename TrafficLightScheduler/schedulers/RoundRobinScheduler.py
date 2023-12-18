from TrafficLightScheduler.schedulers.Scheduler import Scheduler
from TrafficLightScheduler.simulation.Simulation import Simulation
from TrafficLightScheduler.simulation.SimulationFactory import SimulationFactory
from itertools import cycle


class RoundRobinScheduler(Scheduler):
    def __init__(self, options):
        super().__init__(options)
        self.quantum = int(options)
        self.cycles = {}
        self.active_streets = {}

    def tick(self, simulation: Simulation):
        traffic_lights_matrix = simulation.traffic_lights_matrix
        for i in range(simulation.number_of_intersections):
            if i not in self.cycles:
                # initialize cycle
                self.cycles[i] = cycle([x for x in range(simulation.number_of_intersections) if
                                        simulation.city_plan_matrix[i][x] is not None])
                self.active_streets[i] = next(self.cycles[i])
                traffic_lights_matrix[i][self.active_streets[i]] = self.quantum
            else:
                current_street = self.active_streets[i]
                if traffic_lights_matrix[i][current_street] > 0:
                    traffic_lights_matrix[i][current_street] -= 1
                    if traffic_lights_matrix[i][current_street] == 0:
                        self.active_streets[i] = next(self.cycles[i])
                        traffic_lights_matrix[i][self.active_streets[i]] = self.quantum


if __name__ == "__main__":
    print("RoundRobinScheduler")
    scheduler = RoundRobinScheduler(6)
    _simulation = SimulationFactory.make_from_input("a", "RoundRobinScheduler_6_a")
    _simulation.run(scheduler)
