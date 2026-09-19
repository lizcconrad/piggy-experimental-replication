# ERG_2023 grammar with WebNLG changes
export COMPOSITION_CONFIG=../ERG_versions/ERG_2023_webnlg/ERG_2023_webnlg_config.json
export RUN_NAME="post_webnlg" # name of directory containing all experiments for this run

# WebNLG
export EXPERIMENT_CONFIG=../datasets/WebNLG/configs/WebNLG_Conrad_2026_dev_config.json
export EXPERIMENT_NAMES="post_webnlg_dev, post_webnlg_dev_patch"
hatch run post-webnlg:run_experiments

export EXPERIMENT_CONFIG=../datasets/WebNLG/configs/WebNLG_Conrad_2026_test_config.json
export EXPERIMENT_NAMES="post_webnlg_test_imported_only","post_webnlg_test_hand_populated"
hatch run post-webnlg:run_experiments