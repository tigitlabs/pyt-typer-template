#!/bin/bash
# .devcontainer/postCreateCommand.sh
echo "🏗️ Post start command"
# Check if the script is running on GitHub Codespaces
if [[ -n "${CODESPACES}" || -n "${GITHUB_CODESPACE_TOKEN}" ]]; then
    printf "Running in GitHub Codespaces.\nNo need to run any commands."
fi

echo "🏃‍♂️ Install markdownlint"
npm install -g markdownlint-cli

echo "🏃‍♂️ Install devcontainer cli"
npm install -g @devcontainers/cli

echo "🏃‍♂️ Install python dependencies"
pip install -r requirements.txt