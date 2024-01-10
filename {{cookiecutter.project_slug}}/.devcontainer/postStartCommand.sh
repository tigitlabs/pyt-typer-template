#!/bin/bash
# .devcontainer/postStartCommand.sh
echo "🏗️ Post create command"
# Check if the script is running on GitHub Codespaces
if [[ -n "${CODESPACES}" || -n "${GITHUB_CODESPACE_TOKEN}" ]]; then
    printf "Running in GitHub Codespaces.\nNo need to run any commands."
fi
