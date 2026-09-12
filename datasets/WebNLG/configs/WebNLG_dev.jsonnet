{
    dataset_name: "WebNLG",
    data_dir: "../datasets/WebNLG/pogg_formatted_data",
    evaluation_dir: "../evaluation/WebNLG",
    output_dir: "../output/WebNLG",
    reports_dir: "../reports/WebNLG",
    lexicons_dir: "../datasets/WebNLG/lexicons",
    graph_rel_dir: "graphs/modified_triplesets",
    lexicons: {
        "webnlg_dev": {
            "lexicon_dir": "../datasets/WebNLG/lexicons/webnlg_dev",
            "auto_filler_settings": {
                "auto_fill": true,
                "auto_approve": false,
                "auto_create_templates": false,
                "template_files": [
                    "../configuration_data/lexicon_templates/webnlg/webnlg_dev_templates.json"
                ],
                "blocked_templates": [
                ],
                "template_dump_file": "../configuration_data/lexicon_templates/webnlg/webnlg_dev_templates.json"
            }
        },
    },
    experimental_setups: {
        "webnlg_dev": {
            "composition_config": "../ERG_versions/ERG_2023_webnlg/ERG_2023_webnlg_config.json",
            "lexicon_name": "webnlg_dev",
            "SEMENT_processing": [],
            "result_processing": []
        }
    },
    categories: [
        "Airport",
        "Artist",
        "Astronaut",
        "Athlete",
        "Building",
        "CelestialBody",
        "City",
        "ComicsCharacter",
        "Company",
        "Food",
        "MeanOfTransportation",
        "Monument",
        "Politician",
        "SportsTeam",
        "University",
        "WrittenWork"
    ],
    split_structure: {
        dev: {
            "1triples": [x for x in $.categories],
            "2triples": [x for x in $.categories],
            "3triples": [x for x in $.categories]
        }
    }
}
