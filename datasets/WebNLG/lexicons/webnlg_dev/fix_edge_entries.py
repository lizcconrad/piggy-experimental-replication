import json

empty_entry = {
    "entry_type": "edge",
    "lexicon_entry": {
        "comp_fxn": "",
    },
    "auto_info": {
        "attempted_templates": [
        ],
        "string_to_parse": "",
        "name_of_created_template": "",
        "template_example_string": "",
        "template_used": "",
        "blocked_templates": []
    },
    "flags": {
        "auto_filled": False,
        "complete": False,
        "approved": False,
        "valid": True,
        "create_template_from": False
    },
    "tags": []
}


for file in ["webnlg_dev_lexicon_all_entries.json", "webnlg_dev_lexicon_approved_entries.json", "webnlg_dev_lexicon_workspace.json"]:
    with open(file, "r") as json_file:
        data = json.load(json_file)

        for edge_key in data["edge_entries"]:
            data["edge_entries"][edge_key] = empty_entry


    with open(file, "w") as json_file:
        json.dump(data, json_file, indent=4)
