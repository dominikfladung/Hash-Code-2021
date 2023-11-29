from TrafficLightScheduler.simulation.Simulation import Simulation


class SimulationFactory:
    @staticmethod
    def make_from_input(input_str):
        return Simulation()
