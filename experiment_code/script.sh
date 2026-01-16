DUMMY_INPUT="./data/dummy.fasta"
OUTPUT_DIR="output"
RESULT_CSV="output/results.csv"
YAML_CONFIG="config.yaml"
uv run main.py\
    "$DUMMY_INPUT" \
    "$OUTPUT_DIR" \
    "$RESULT_CSV" \
    "$YAML_CONFIG"