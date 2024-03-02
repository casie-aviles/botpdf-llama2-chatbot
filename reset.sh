#!/bin/bash

# Get the directory of the script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Delete files in the data directory
data_dir="$SCRIPT_DIR/data"
if [ -d "$data_dir" ]; then
    rm -f "$data_dir"/*
fi

# Remove the chroma_db_data directory
chroma_db_data_dir="$SCRIPT_DIR/chroma_db_data"
if [ -d "$chroma_db_data_dir" ]; then
    rm -rf "$chroma_db_data_dir"
fi

# Run the Streamlit application
streamlit run "$SCRIPT_DIR/frontend_chatbot.py"