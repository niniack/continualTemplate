#!/bin/bash

# Check if an argument is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 path_to_workspace_folder"
    exit 1
fi

# Set the workspace_folder variable using the first argument
workspace_folder="$1"

# Define the path to the .env file
ENV_FILE="$workspace_folder/.devcontainer/.env"

# Check if the .env file exists
if [ -f "$ENV_FILE" ]; then
    echo "Loading environment variables from .devcontainer/.env"
    
    # Load environment variables and check if the command was successful
    export $(grep -v '^#' "$ENV_FILE" | xargs) && echo "Environment variables loaded successfully."
else
    echo "Error: .env file not found in the provided workspace folder. Exiting."
    exit 1
fi

# If everything went well, open the devcontainer
devcontainer open .
