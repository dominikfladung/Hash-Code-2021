import random

from TrafficLightScheduler.schedulers.Scheduler import Scheduler
from TrafficLightScheduler.simulation.Simulation import Simulation
from itertools import cycle

from TrafficLightScheduler.simulation.SimulationFactory import SimulationFactory


class RandomScheduler(Scheduler):
    def __init__(self, options):
        super().__init__(options)
        self.cycles = {}
        self.active_streets = {}
        self.quantums = {}
        self.max_quantum = int(options) if options is not None else 2

    def tick(self, simulation: Simulation):
        traffic_lights_matrix = simulation.traffic_lights_matrix
        for i in range(simulation.number_of_intersections):
            if i not in self.cycles:
                # initialize cycle
                vertex = [x for x in range(simulation.number_of_intersections) if
                          simulation.city_plan_matrix[x][i] is not None]
                self.cycles[i] = cycle(vertex)
                self.active_streets[i] = next(self.cycles[i])
                self.quantums[i] = [random.randint(0, self.max_quantum) if
                                    simulation.city_plan_matrix[x][i] is not None else None for x in
                                    range(simulation.number_of_intersections)]
                traffic_lights_matrix[self.active_streets[i]][i] = self.quantums[i][self.active_streets[i]]
            else:
                current_street = self.active_streets[i]
                if traffic_lights_matrix[current_street][i] > 0:
                    traffic_lights_matrix[current_street][i] -= 1
                    if traffic_lights_matrix[current_street][i] == 0:
                        self.active_streets[i] = next(self.cycles[i])
                        traffic_lights_matrix[self.active_streets[i]][i] = self.quantums[i][self.active_streets[i]]

    def create_submission(self, simulation: Simulation):
        submission = [simulation.number_of_intersections]
        for from_vertex in range(simulation.number_of_intersections):
            submission.append(from_vertex)
            column = [(i, row[from_vertex]) for (i, row) in enumerate(simulation.city_plan_matrix)]
            streets = [(i, row) for (i, row) in column if row is not None]
            submission.append(len(streets))
            for street in streets:
                quantum = self.quantums[from_vertex][street[0]]
                submission.append(street[1] + " " + str(quantum))

        return "\n".join([str(x) for x in submission])


if __name__ == '__main__':
    score = 0
    while score <= 1001:
        scheduler = RandomScheduler(1)
        simulation = SimulationFactory.make_from_input("a", "random_a")
        score = simulation.run(scheduler)
