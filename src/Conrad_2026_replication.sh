## RUN ALL DATASETS USING post-perplexity VERSION OF PIGGY ##
# ERG_2023 grammar with GP2 changes
export COMPOSITION_CONFIG=../ERG_versions/ERG_2023_GP2/ERG_2023_GP2_config.json
export RUN_NAME="post_perplexity" # name of directory containing all experiments for this run
# perplexity
export EXPERIMENT_CONFIG=../datasets/perplexity/configs/perplexity_Conrad_2026_config.json
export EXPERIMENT_NAMEs="hand_populated"
hatch run post-perplexity-config-refactor:run_experiments

# WebNLG
export EXPERIMENT_CONFIG=../datasets/WebNLG/configs/WebNLG_Conrad_2026_config.json
export EXPERIMENT_NAMEs="post_perplexity_no_numbers"
hatch run post-perplexity-config-refactor:run_experiments



## RUN ALL DATASETS USING post-webnlg VERSION OF PIGGY ##
export COMPOSITION_CONFIG=../ERG_versions/ERG_2023_webnlg/ERG_2023_webnlg_config.json
export RUN_NAME="post_webnlg" # name of directory containing all experiments for this run
# WebNLG
export EXPERIMENT_CONFIG=../datasets/WebNLG/configs/WebNLG_Conrad_2026_config.json
export EXPERIMENT_NAMEs="post_webnlg_dev"
hatch run post-webnlg:run_experiments


# run experiment routine on each dataset

# diff against Conrad_2026_results to confirm replication success



# activate environment with post-WebNLG version of PIGGY

# run experiment routine on each dataset

# diff against Conrad_2026_results to confirm replication success

# diff against post-perplexity to see improvements



# activate environment with post-Logic2Text version of PIGGY

# run experiment routine on each dataset

# diff against Conrad_2026_results to confirm replication success

# diff against post-WebNLG to see improvements

# diff against post-perplexity to see improvements