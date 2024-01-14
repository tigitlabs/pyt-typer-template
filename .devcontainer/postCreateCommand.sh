#!/bin/bash
# .devcontainer/postCreateCommand.sh
echo "🏗️ Post create command"
# TODO this needs to be fixed
# Check if the script is running a local host
ENV_FILE=".devcontainer/.env"
echo "Check if running on non GitHub Codespaces"
# Check if the file exists
if [ -f "$ENV_FILE" ]; then
    printf "Runnig on local host. \nLoad environment variables from ${ENV_FILE}"
    echo "Load environment variables from ${ENV_FILE}"
    # Get absolute path of .env file
    ENV_FILE=$(realpath ${ENV_FILE})
    # Add loading of variables to ~/.bashrc
    echo "Add env file ${ENV_FILE} to ~/.bashrc"
    echo "### Load env variables" >> ~/.bashrc
    echo "# Added from postStartCommand.sh" >> ~/.bashrc
    echo "set -o allexport" >> ~/.bashrc
    echo "source ${ENV_FILE}" >> ~/.bashrc
    echo "set +o allexport" >> ~/.bashrc
    echo "### Load env variables" >> ~/.bashrc
else
    printf "Running in GitHub Codespaces.\nNo need to run any commands."
fi

echo "🏃‍♂️ Install markdownlint"
npm install -g markdownlint-cli

echo "🏃‍♂️ install pip requierments"
pip install -r requirements.txt
