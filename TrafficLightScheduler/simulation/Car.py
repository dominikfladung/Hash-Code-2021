class Car:
    def __init__(self, car_row):
        self.target_intersection = int(car_row[0])
        self.path = car_row[1:]
        self.current_street = 0

    def tick(self, simulation):
        if self.is_finished():
            return
        traffic_light = simulation.traffic_lights_matrix
        self.current_street += 1

    def is_finished(self):
        return self.path[self.current_street] == self.path[-1]

    def get_score(self, time):
        return 0
