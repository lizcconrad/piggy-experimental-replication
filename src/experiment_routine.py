import argparse
from pogg.pogg_routine import POGGExperimentsConfig
import re

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--composition_config",  type=str, help="path to the config which specifies paths to the desired ERG version")
parser.add_argument("-e", "--experiment_config",  type=str, help="path to the config which specifies experiments")
parser.add_argument("-r", "--run_name",  type=str, help="path to the config which specifies experiments")
parser.add_argument("-x", "--experiments_to_run",  type=str, help="list of experiment names to run; any name given must be in the provided experiment config")

args = parser.parse_args()

experiment_config_path = args.experiment_config
run_name = args.run_name
experiment_names = re.split(r',? ', args.experiments_to_run)


experiments_config = POGGExperimentsConfig(experiment_config_path, run_name)
# optionally pass in experiment type
experiments = experiments_config.get_all_experiments()

for i, experiment in enumerate(experiments):
    if experiment.experiment_name in experiment_names:
        print(f"Running {experiment.full_data_split_name}__{experiment.experiment_name} (experiment {i + 1} of {len(experiments)})...")
        experiment.run_experiment()
        experiment.store_experiment_results()
        experiment.store_experiment_report()
