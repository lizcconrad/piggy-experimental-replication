import json
from pogg.data_handling import POGGDataset

config_file = "/Users/lizcconrad/Documents/PhD/POGG/pogg-experimental-replication/datasets/WebNLG/configs/WebNLG_Conrad_2026_dev_config.json"
with open(config_file) as f:
    config_json = json.load(f)

dataset = POGGDataset(config_json)
print(":3")