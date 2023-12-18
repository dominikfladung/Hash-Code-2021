from TrafficLightScheduler.simulation.Car import Car
from TrafficLightScheduler.simulation.Simulation import Simulation
import numpy as np


class SimulationFactory:
    @staticmethod
    def make_from_input(input_str, name):
        with open("../../inputs/" + input_str + ".txt", 'r', encoding='utf-8') as file:
            content = file.read().splitlines()

        # params
        params = content[0].split(' ')
        simulation = Simulation(name)
        simulation.max_duration = int(params[0])
        simulation.number_of_intersections = int(params[1])
        simulation.number_of_streets = int(params[2])
        simulation.number_of_cars = int(params[3])
        simulation.bonus_points = int(params[4])

        simulation.city_plan_matrix = [[None for _ in range(simulation.number_of_intersections)]
                                       for _ in range(simulation.number_of_intersections)]
        simulation.cost_matrix = np.zeros((simulation.number_of_intersections,
                                           simulation.number_of_intersections), dtype=int)
        simulation.traffic_lights_matrix = np.zeros((simulation.number_of_intersections,
                                                     simulation.number_of_intersections), dtype=int)

        # streets
        streets = content[1:simulation.number_of_streets + 1]
        for i in range(simulation.number_of_streets):
            street = streets[i].split(' ')
            start_intersection = int(street[0])
            end_intersection = int(street[1])
            name = street[2]
            cost = int(street[3])
            simulation.city_plan_matrix[start_intersection][end_intersection] = name
            simulation.cost_matrix[start_intersection][end_intersection] = cost

        # cars
        cars = content[simulation.number_of_streets + 1:]
        for i in range(simulation.number_of_cars):
            simulation.cars.append(Car(cars[i].split(' ')))

        return simulation
