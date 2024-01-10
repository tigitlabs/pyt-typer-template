#!/bin/bash
# .devcontainer/initializeCommand.sh
echo "🏗️ Initialize command"
# Check if the script is running on GitHub Codespaces
if [[ -n "${CODESPACES}" || -n "${GITHUB_CODESPACE_TOKEN}" ]]; then
    printf "Running in GitHub Codespaces.\nNo need to export any keys."
    exit 0
fi