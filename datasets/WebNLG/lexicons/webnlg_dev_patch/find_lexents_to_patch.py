import json

for file in [
    "webnlg_dev_patch_lexicon_all_entries.json",
    "webnlg_dev_patch_lexicon_approved_entries.json",
    # "webnlg_dev_patch_lexicon_workspace.json"
]:
    with open(file, "r") as json_file:
        data = json.load(json_file)

        for edge_key in data["edge_entries"]:
            edge_entry_as_string = json.dumps(data["edge_entries"][edge_key])
            if not "child" in edge_entry_as_string or not "parent" in edge_entry_as_string:
                print(f"{edge_key} broken...")
                data["edge_entries"][edge_key]["flags"]["approved"] = False


    with open(file, "w") as json_file:
        json.dump(data, json_file, indent=4)