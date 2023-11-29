import argparse

from TrafficLightScheduler.schedulers.SchedulerFactory import SchedulerFactory
from TrafficLightScheduler.simulation.SimulationFactory import SimulationFactory

parser = argparse.ArgumentParser(
    prog='TrafficLightScheduler',
    description='A program to solve the HashCode2021 challenge '
                'e.g.  python -m TrafficLightScheduler --input "a.txt" --scheduler "round_robin"')

parser.add_argument('-i', '--input', type=str, required=True)
parser.add_argument('-s', '--scheduler', type=str, required=True)
parser.add_argument('-so', '--scheduler-options', type=str)

args = parser.parse_args()

scheduler = SchedulerFactory.create(args.scheduler, args.scheduler_options)
simulation = SimulationFactory.make_from_input(args.input)
simulation.run(scheduler)
