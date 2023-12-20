import argparse
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import freeze_support

from TrafficLightScheduler.schedulers.SchedulerFactory import SchedulerFactory
from TrafficLightScheduler.simulation.SimulationFactory import SimulationFactory


def generate_submissions(args):
    num_processes = 6  # Number of processes (adjust as needed)
    with ProcessPoolExecutor(max_workers=num_processes) as executor:
        inputs = ['a', 'b', 'c', 'd', 'e', 'f']
        futures = [executor.submit(generate_submission, args, char) for char in inputs]
        results = [future.result() for future in futures]
    return results


def generate_submission(args, input_str):
    scheduler = SchedulerFactory.create(args.scheduler, args.scheduler_options)
    suffix = "_" + args.scheduler_options if args.scheduler_options else ""
    name = args.scheduler + "_" + input_str + suffix
    simulation = SimulationFactory.make_from_input(input_str, name, args.debug)
    score = simulation.run(scheduler)
    print(f"Score for {name}: {score}")


parser = argparse.ArgumentParser(
    prog='TrafficLightScheduler',
    description='A program to solve the HashCode2021 challenge '
                'e.g.  python -m TrafficLightScheduler --input "a" --scheduler "round_robin"')

parser.add_argument('-i', '--input', type=str)
parser.add_argument('-s', '--scheduler', type=str, required=True)
parser.add_argument('-so', '--scheduler-options', type=str)
parser.add_argument('--debug', action='store_true', default=False)

args = parser.parse_args()

if __name__ == '__main__':
    freeze_support()
    if args.input:
        generate_submission(args, args.input)
    else:
        generate_submissions(args)

