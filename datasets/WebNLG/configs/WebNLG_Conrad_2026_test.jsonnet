{
    dataset_name: "WebNLG",
    data_dir: "../datasets/WebNLG/pogg_formatted_data",
    evaluation_dir: "../Conrad_2026_results/evaluation/WebNLG",
    output_dir: "../Conrad_2026_results/output/WebNLG",
    reports_dir: "../Conrad_2026_results/reports/WebNLG",
    lexicons_dir: "../datasets/WebNLG/lexicons",
    graph_rel_dir: "graphs/modified_triplesets",
    lexicons: {
        "post_webnlg_test_imported_only" : {
            "lexicon_dir": "../datasets/WebNLG/lexicons/webnlg_test_imported_only",
            "auto_filler_settings": {
                "auto_fill": false,
                "auto_approve": false,
                "auto_create_templates": false,
                "template_files": [
                ],
                "blocked_templates": [
                ],
                "template_dump_file": "../configuration_data/lexicon_templates/perplexity/webnlg_test_templates.json",
                "imported_lexicon_paths": [
                    "../datasets/WebNLG/lexicons/webnlg_dev"
                ]
            }
        },
        "post_webnlg_test_hand_populated" : {
            "lexicon_dir": "../datasets/WebNLG/lexicons/webnlg_test_hand_populated",
            "auto_filler_settings": {
                "auto_fill": false,
                "auto_approve": false,
                "auto_create_templates": false,
                "template_files": [
                ],
                "blocked_templates": [
                ],
                "template_dump_file": "../configuration_data/lexicon_templates/perplexity/webnlg_test_templates.json",
                "imported_lexicon_paths": [
                    "../datasets/WebNLG/lexicons/webnlg_dev"
                ]
            }
        }
    },
    experimental_setups: {
        "post_webnlg_test_imported_only": {
            "composition_config": "../ERG_versions/ERG_2023_webnlg/ERG_2023_webnlg_config.json",
            "lexicon_name": "post_webnlg_test_imported_only",
            "SEMENT_processing": [],
            "result_processing": []
        },
        "post_webnlg_test_hand_populated": {
            "composition_config": "../ERG_versions/ERG_2023_webnlg/ERG_2023_webnlg_config.json",
            "lexicon_name": "post_webnlg_test_hand_populated",
            "SEMENT_processing": [],
            "result_processing": []
        }
    },
    split_structure: {
        "test": ["1triples", "2triples", "3triples"]
    }
}
