# ERG_2023 grammar with GP2 changes
export COMPOSITION_CONFIG=../ERG_versions/ERG_2023_GP2/ERG_2023_GP2_config.json
export RUN_NAME="post_perplexity" # name of directory containing all experiments for this run
# perplexity
export EXPERIMENT_CONFIG=../datasets/perplexity/configs/perplexity_Conrad_2026_config.json
export EXPERIMENT_NAME="hand_populated"
hatch run post-perplexity-config-refactor:run_experiments

# WebNLG
export EXPERIMENT_CONFIG=../datasets/WebNLG/configs/WebNLG_Conrad_2026_config.json
export EXPERIMENT_NAME="post_perplexity_no_numbers"
hatch run post-perplexity-config-refactor:run_experiments
