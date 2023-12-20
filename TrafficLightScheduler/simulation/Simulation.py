import numpy as np
from TrafficLightScheduler import MODULE_ROOT


class Simulation:
    def __init__(self, name, debug=False):
        self.name = name
        self.debug = debug
        self.scheduler = None
        self.max_duration = 0
        self.number_of_intersections = 0
        self.number_of_streets = 0
        self.number_of_cars = 0
        self.bonus_points = 0

        self.street_positions = None
        self.traffic_lights_matrix = None
        self.used_traffic_lights_matrix = None
        self.city_plan_matrix = None
        self.cars = []

        self.score = 0
        self.current_time = 0

    def run(self, scheduler):
        self.scheduler = scheduler
        debug_cars = self.get_debug_cars()
        if self.debug:
            print("[T0] " + str(debug_cars))

        for i in range(self.max_duration):
            self.current_time = i
            self.tick()
            if self.debug:
                print("[T" + str(i + 1) + "] " + str(self.get_debug_cars()))

        submission = self.scheduler.create_submission(self)
        self.save_submission(submission)

        return self.score

    def get_debug_cars(self):
        street_keys = list(self.street_positions.keys())
        street_values = list(self.street_positions.values())
        debug_cars = [str(car) + " - " + street_keys[street_values.index(car.get_position())] for car in self.cars if
                      not car.reached_target()]
        return debug_cars

    def tick(self):
        self.scheduler.tick(self)
        for car in self.cars:
            if not car.reached_target():
                car.tick(self)

        self.finish_cars()
        # reset used traffic lights
        self.used_traffic_lights_matrix = np.zeros((self.number_of_intersections,
                                                    self.number_of_intersections), dtype=int)

    def finish_cars(self):
        finished_cars = [car for car in self.cars if car.reached_target()]
        for car in finished_cars:
            self.score += self.bonus_points + self.max_duration - self.current_time
            if self.debug:
                print(f"Car#{car.id} finished at {self.current_time}: " + str(car.car_data))

        # remove finished cars
        self.cars = [car for car in self.cars if not car.reached_target()]

    def save_submission(self, submission):
        """Save the submission to the outputs folder"""
        with open(MODULE_ROOT + "/../outputs/" + self.name + ".txt", 'w', encoding='utf-8') as file:
            file.write(submission)
