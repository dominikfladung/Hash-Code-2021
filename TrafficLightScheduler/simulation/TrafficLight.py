from TrafficLightScheduler.simulation.TrafficLightState import TrafficLightState


class TrafficLight:
    def __init__(self):
        self.state = TrafficLightState.RED
        self.street = None
        self.intersection = None
        self.car_queue = []
