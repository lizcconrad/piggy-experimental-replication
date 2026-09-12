
CONFIGURATION_DATA_DIR=../../../configuration_data

# generic (for testing during dev)
jsonnet --tla-code input='(import "WebNLG.jsonnet")' $CONFIGURATION_DATA_DIR/experiment_config_template.jsonnet > "WebNLG_config.json"
# ignores experiments for perplexity version of code
jsonnet --tla-code input='(import "WebNLG_dev.jsonnet")' $CONFIGURATION_DATA_DIR/experiment_config_template.jsonnet > "WebNLG_config_dev.json"

# Conrad 2026
jsonnet --tla-code input='(import "WebNLG_Conrad_2026.jsonnet")' $CONFIGURATION_DATA_DIR/experiment_config_template.jsonnet > "WebNLG_Conrad_2026_config.json"


# diffs
#jsonnet --tla-code input='(import "WebNLG_diff_config.jsonnet")' $CONFIGURATION_DATA_DIR/diff_template.jsonnet > "perplexity_diff_config.json"
