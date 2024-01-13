#!/bin/bash
# .devcontainer/postStartCommand.sh
ENV_FILE=".devcontainer/.env"
echo "🏗️ Post start command"
echo "Check if running on non GitHub Codespaces"
# Check if the file exists
if [ -f "$ENV_FILE" ]; then
    echo "Running on local host"
    set -o allexport
    source .devcontainer/.env
    set +o allexport
    echo "🧪 Login status for github cli"
    gh auth status
    echo "🧪 Login docker to ghcr.io for: ${GITHUB_USER}"
    echo $GITHUB_TOKEN | docker login ghcr.io -u $GITHUB_USER --password-stdin
    echo "🧪 Check github access via SSH"
    # Add github.com to known_hosts
    mkdir -p ~/.ssh
    touch ~/.ssh/known_hosts
    ssh-keyscan github.com >> ~/.ssh/known_hosts
    # ssh -T git@github.com
else
    printf "🐱Running in GitHub Codespaces.\nNo need to run any commands."
fi
