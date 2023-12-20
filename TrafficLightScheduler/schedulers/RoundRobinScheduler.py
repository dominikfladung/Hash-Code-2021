from TrafficLightScheduler.schedulers.Scheduler import Scheduler
from TrafficLightScheduler.simulation.Simulation import Simulation
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
                vertex = [x for x in range(simulation.number_of_intersections) if
                         simulation.city_plan_matrix[x][i] is not None]
                self.cycles[i] = cycle(vertex)
                self.active_streets[i] = next(self.cycles[i])
                traffic_lights_matrix[self.active_streets[i]][i] = self.quantum
            else:
                current_street = self.active_streets[i]
                if traffic_lights_matrix[current_street][i] > 0:
                    traffic_lights_matrix[current_street][i] -= 1
                    if traffic_lights_matrix[current_street][i] == 0:
                        self.active_streets[i] = next(self.cycles[i])
                        traffic_lights_matrix[self.active_streets[i]][i] = self.quantum

    def create_submission(self, simulation: Simulation):
        submission = [simulation.number_of_intersections]
        for from_vertex in range(simulation.number_of_intersections):
            submission.append(from_vertex)
            column = [row[from_vertex] for row in simulation.city_plan_matrix]
            streets = [x for x in column if x is not None]
            submission.append(len(streets))
            for street in streets:
                submission.append(street + " " + str(self.quantum))

        return "\n".join([str(x) for x in submission])
