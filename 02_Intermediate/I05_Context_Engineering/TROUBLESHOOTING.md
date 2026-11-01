# Troubleshooting
- Import failure: install requirements using the same interpreter that launches Streamlit.
- Invalid JSON: use double-quoted strings, JSON arrays/objects, and no trailing commas. Compare sample_data/examples.json.
- Empty input: supply a meaningful value within the limit described by the validation error.
- Provider failure: verify account access, quota, configuration, and allowed HTTPS destination. Never share raw secret values. Local mode remains available.
- Port collision: append `--server.port 8502` to the launch command.
- Theme missing: launch from this folder; the project includes .streamlit/config.toml.
- Unexpected retained output: the result records the last submitted input; click Run experiment to refresh or Reset workspace to clear it.
- Slow input: keep experiments below the input limits; do not use this teaching UI for unbounded production data.
- Visual review: browser screenshots, keyboard navigation, and narrow viewport checks remain separate from automated UI tests.
