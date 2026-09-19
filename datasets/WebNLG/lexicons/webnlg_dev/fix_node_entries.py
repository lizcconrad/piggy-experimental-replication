import json

import re

camel_case_pattern = r'(?<=[a-z])(?=[A-Z])'
snake_case_pattern = r',*_'
parse_pattern = camel_case_pattern

# WebNLG
# Russian_Football_League -> Russian Football League
def webnlg(x):
    tokens = [t for t in re.split(snake_case_pattern, x)]
    return " ".join(tokens)

for file in ["webnlg_dev_lexicon_workspace.json", "webnlg_dev_lexicon_approved_entries.json",
             "webnlg_dev_lexicon_all_entries.json"]:
    with open(file, "r") as f:
        json_entries = json.load(f)

    for key, entry in json_entries["node_entries"].items():
        if entry["lexicon_entry"]["comp_fxn"] == "prepositional_relationship":
            entry["lexicon_entry"]["comp_fxn"] = "prepositional_modifier"

            # add new keys
            entry["lexicon_entry"]["prepositional_modifier_SEMENT"] = {
                "comp_fxn": "object_of_preposition",
                "preposition_SEMENT": entry["lexicon_entry"]["preposition_SEMENT"],
                "object_of_preposition_SEMENT": entry["lexicon_entry"]["ground_SEMENT"]
            }

            entry["lexicon_entry"]["modified_SEMENT"] = entry["lexicon_entry"]["figure_SEMENT"]

            # pop old keys
            entry["lexicon_entry"].pop("preposition_SEMENT")
            entry["lexicon_entry"].pop("figure_SEMENT")
            entry["lexicon_entry"].pop("ground_SEMENT")

    with open(file, "w") as f:
        json.dump(json_entries, f, indent=4)
    print(":3")