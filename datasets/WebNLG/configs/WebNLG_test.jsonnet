{
    dataset_name: "WebNLG",
    data_dir: "../datasets/WebNLG/pogg_formatted_data",
    evaluation_dir: "../evaluation/WebNLG",
    output_dir: "../output/WebNLG",
    reports_dir: "../reports/WebNLG",
    lexicons_dir: "../datasets/WebNLG/lexicons",
    graph_rel_dir: "graphs/modified_triplesets",
    lexicons: {
        "webnlg_test": {
            "lexicon_dir": "../datasets/WebNLG/lexicons/webnlg_test",
            "auto_filler_settings": {
                "auto_fill": false,
                "auto_approve": false,
                "auto_create_templates": false,
                "template_files": [
                ],
                "blocked_templates": [
                ],
                "template_dump_file": "../configuration_data/lexicon_templates/webnlg/webnlg_test_templates.json"
            },
            "imported_lexicon_paths": [
                "../datasets/WebNLG/lexicons/webnlg_dev"
            ]
        },
    },
    experimental_setups: {
        "webnlg_test": {
            "composition_config": "../ERG_versions/ERG_2023_webnlg/ERG_2023_webnlg_config.json",
            "lexicon_name": "webnlg_test",
            "SEMENT_processing": [],
            "result_processing": []
        }
    },
    split_structure: ["test"]
}
