import os
import json
import string_processing

from pogg.lexicon import POGGLexicon, POGGLexiconAutoFiller
from pogg.data_handling import POGGDataset

# each experiment has a composition config, but each lexicon does not, so when working on a lexicon I just have to pick one
composition_config = "../ERG_versions/ERG_2023_GP2/ERG_2023_GP2_config.json"
experiment_config = "../datasets/WebNLG/configs/WebNLG_config.json"
str_processing_fxn = getattr(string_processing, "webnlg")

# name of lexicon being worked on
lexicon_name = "webnlg_dev"

with open(experiment_config, "r") as f:
    config_json = json.load(f)

dataset = POGGDataset(config_json)

lexicon_info = config_json["lexicons"][lexicon_name]
auto_filler_settings = lexicon_info["auto_filler_settings"]

if auto_filler_settings["auto_fill"]:
    auto_filler = POGGLexiconAutoFiller(composition_config, auto_filler_settings["template_files"],
                                        auto_approve=auto_filler_settings["auto_approve"],
                                        global_blocked_templates=auto_filler_settings["blocked_templates"],
                                        string_processing_fxn=str_processing_fxn,
                                        auto_create_templates=auto_filler_settings["auto_create_templates"],
                                        dump_file=auto_filler_settings["template_dump_file"])
else:
    auto_filler = None

lexicon = POGGLexicon(config_json["lexicons"][lexicon_name]["lexicon_dir"], dataset,
                      imported_lexicon_paths=lexicon_info["imported_lexicon_paths"], auto_filler=None)

# remove splits already worked through
# one_triples = dataset.get_data_split("WebNLG", "dev", "1triples")
one_airport = dataset.get_data_split("WebNLG", "dev", "1triples", "Airport")
one_artist = dataset.get_data_split("WebNLG", "dev", "1triples", "Artist")
one_astronaut = dataset.get_data_split("WebNLG", "dev", "1triples", "Astronaut")
one_athlete = dataset.get_data_split("WebNLG", "dev", "1triples", "Athlete")
one_building = dataset.get_data_split("WebNLG", "dev", "1triples", "Building")
one_celestial = dataset.get_data_split("WebNLG", "dev", "1triples", "CelestialBody")
one_city = dataset.get_data_split("WebNLG", "dev", "1triples", "City")
one_comics = dataset.get_data_split("WebNLG", "dev", "1triples", "ComicsCharacter")
one_company = dataset.get_data_split("WebNLG", "dev", "1triples", "Company")
one_food = dataset.get_data_split("WebNLG", "dev", "1triples", "Food")
one_transport = dataset.get_data_split("WebNLG", "dev", "1triples", "MeanOfTransportation")
one_monument = dataset.get_data_split("WebNLG", "dev", "1triples", "Monument")
one_politician = dataset.get_data_split("WebNLG", "dev", "1triples", "Politician")
one_sports = dataset.get_data_split("WebNLG", "dev", "1triples", "SportsTeam")
one_university = dataset.get_data_split("WebNLG", "dev", "1triples", "University")
one_written = dataset.get_data_split("WebNLG", "dev", "1triples", "University")
all_ones = dataset.get_data_split("WebNLG", "dev", "1triples")

two_airport = dataset.get_data_split("WebNLG", "dev", "2triples", "Airport")
two_artist = dataset.get_data_split("WebNLG", "dev", "2triples", "Artist")
two_astronaut = dataset.get_data_split("WebNLG", "dev", "2triples", "Astronaut")
two_athlete = dataset.get_data_split("WebNLG", "dev", "2triples", "Athlete")
two_building = dataset.get_data_split("WebNLG", "dev", "2triples", "Building")
two_celestial = dataset.get_data_split("WebNLG", "dev", "2triples", "CelestialBody")
two_city = dataset.get_data_split("WebNLG", "dev", "2triples", "City")
two_comics = dataset.get_data_split("WebNLG", "dev", "2triples", "ComicsCharacter")
two_company = dataset.get_data_split("WebNLG", "dev", "2triples", "Company")
two_food = dataset.get_data_split("WebNLG", "dev", "2triples", "Food")
two_transport = dataset.get_data_split("WebNLG", "dev", "2triples", "MeanOfTransportation")
two_monument = dataset.get_data_split("WebNLG", "dev", "2triples", "Monument")
two_politician = dataset.get_data_split("WebNLG", "dev", "2triples", "Politician")
two_sports = dataset.get_data_split("WebNLG", "dev", "2triples", "SportsTeam")
two_university = dataset.get_data_split("WebNLG", "dev", "2triples", "University")
two_written = dataset.get_data_split("WebNLG", "dev", "2triples", "University")
all_twos = dataset.get_data_split("WebNLG", "dev", "2triples")

three_airport = dataset.get_data_split("WebNLG", "dev", "3triples", "Airport")
three_artist = dataset.get_data_split("WebNLG", "dev", "3triples", "Artist")
three_astronaut = dataset.get_data_split("WebNLG", "dev", "3triples", "Astronaut")
three_athlete = dataset.get_data_split("WebNLG", "dev", "3triples", "Athlete")
three_building = dataset.get_data_split("WebNLG", "dev", "3triples", "Building")
three_celestial = dataset.get_data_split("WebNLG", "dev", "3triples", "CelestialBody")
three_city = dataset.get_data_split("WebNLG", "dev", "3triples", "City")
three_comics = dataset.get_data_split("WebNLG", "dev", "3triples", "ComicsCharacter")
three_company = dataset.get_data_split("WebNLG", "dev", "3triples", "Company")
three_food = dataset.get_data_split("WebNLG", "dev", "3triples", "Food")
three_transport = dataset.get_data_split("WebNLG", "dev", "3triples", "MeanOfTransportation")
three_monument = dataset.get_data_split("WebNLG", "dev", "3triples", "Monument")
three_politician = dataset.get_data_split("WebNLG", "dev", "3triples", "Politician")
three_sports = dataset.get_data_split("WebNLG", "dev", "3triples", "SportsTeam")
three_university = dataset.get_data_split("WebNLG", "dev", "3triples", "University")
three_written = dataset.get_data_split("WebNLG", "dev", "3triples", "University")
all_threes = dataset.get_data_split("WebNLG", "dev", "3triples")
removal_splits = [all_ones, two_airport, two_artist, two_astronaut, two_athlete, two_building, two_celestial, two_city, two_comics,
                  two_company, two_food, two_transport, two_monument, two_politician, two_sports, two_university]



data_split = dataset.get_data_split("WebNLG", "dev")
lexicon.set_workspace_split(data_split, removal_splits=None)

lexicon.update_lexicon_files(show_approved=False)


auto_filler.dump_new_templates(lexicon.node_entries)

