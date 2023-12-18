class Simulation:
    def __init__(self):
        self.scheduler = None
        self.max_duration = 0
        self.number_of_intersections = 0
        self.number_of_streets = 0
        self.number_of_cars = 0
        self.bonus_points = 0

        self.current_time = 0

        self.traffic_lights_matrix = None
        self.city_plan_matrix = None
        self.cost_matrix = None
        self.score = 0

    def run(self, scheduler):
        self.scheduler = scheduler
        pass

    def tick(self):
        pass

    def get_score(self):
        pass

    def generate_submission(self):
        pass

    def save_submission(self):
        pass
