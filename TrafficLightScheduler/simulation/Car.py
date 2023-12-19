class Car:
    def __init__(self, car_data):
        self.car_data = car_data
        self.target_intersections = None
        self.path = None
        self.position_index = 0
        self.cost_of_path = 0
        self.id = None

    def tick(self, simulation):
        # move on street
        if self.cost_of_path > 0:
            self.cost_of_path -= 1

        # check if now at intersection
        if self.cost_of_path > 0:
            return

        (start, end) = self.path[self.position_index]

        # traffic light is already used
        # TODO find a better way to do this
        if simulation.used_traffic_lights_matrix[start][end] == 1:
            return

        # queue at intersection - check red light
        traffic_lights = simulation.traffic_lights_matrix[start][end]
        if traffic_lights == 0:
            return

        # do nothing if finished
        if self.reached_target():
            return

        # move to next street
        simulation.used_traffic_lights_matrix[start][end] = 1
        self.position_index += 1
        (start, end) = self.path[self.position_index]
        self.cost_of_path = simulation.cost_matrix[start][end]

    def reached_target(self):
        return self.path[self.position_index] == self.path[-1] and self.cost_of_path == 0

    def get_score(self, time):
        return 0

    def get_position(self):
        return self.path[self.position_index]

    def __repr__(self):
        position = self.get_position()
        return f"Car#{self.id} from {position[0]} to {position[1]} ({self.cost_of_path})"
