import numpy as np


class Simulation:
    def __init__(self, name):
        self.name = name
        self.scheduler = None
        self.max_duration = 0
        self.number_of_intersections = 0
        self.number_of_streets = 0
        self.number_of_cars = 0
        self.bonus_points = 0

        self.traffic_lights_matrix = None
        self.city_plan_matrix = None
        self.cost_matrix = None
        self.cars = []

        self.score = 0
        self.current_time = 0

    def run(self, scheduler):
        self.scheduler = scheduler
        for i in range(self.max_duration):
            self.current_time = i
            self.tick()
            print("Time: " + str(i))

        submission = self.generate_submission()
        self.save_submission(submission)

    def tick(self):
        self.scheduler.tick(self)
        for car in self.cars:
            if not car.is_finished():
                car.tick(self)
                if car.is_finished():
                    self.score += self.bonus_points + self.max_duration - self.current_time

    def generate_submission(self):
        return str(self.score)

    def save_submission(self, submission):
        """Save the submission to the outputs folder"""
        with open("../../outputs/" + self.name + ".txt", 'w', encoding='utf-8') as file:
            file.write(submission)
