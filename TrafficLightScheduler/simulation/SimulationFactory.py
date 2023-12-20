from TrafficLightScheduler import MODULE_ROOT
from TrafficLightScheduler.simulation.Car import Car
from TrafficLightScheduler.simulation.Simulation import Simulation
import numpy as np


class SimulationFactory:
    @staticmethod
    def make_from_input(input_str, name, debug=False):
        with open(MODULE_ROOT + "/../inputs/" + input_str + ".txt", 'r', encoding='utf-8') as file:
            content = file.read().splitlines()

        # params
        params = content[0].split(' ')
        simulation = Simulation(name, debug)
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
        simulation.used_traffic_lights_matrix = np.zeros((simulation.number_of_intersections,
                                                          simulation.number_of_intersections), dtype=int)

        # streets
        streets = content[1:simulation.number_of_streets + 1]
        street_positions = {}
        simulation.street_positions = street_positions
        for i in range(simulation.number_of_streets):
            street = streets[i].split(' ')
            start_intersection = int(street[0])
            end_intersection = int(street[1])
            name = street[2]
            cost = int(street[3])
            simulation.city_plan_matrix[start_intersection][end_intersection] = name
            simulation.cost_matrix[start_intersection][end_intersection] = cost
            street_positions[name] = (start_intersection, end_intersection)

        # cars
        cars = content[simulation.number_of_streets + 1:]

        # search the edge for the street
        for i in range(simulation.number_of_cars):
            car_data = cars[i].split(' ')
            car = Car(car_data)
            car.id = i
            car.target_intersections = int(car_data[0])
            car.path = [street_positions[x] for x in car_data[1:]]
            simulation.cars.append(car)

        return simulation
