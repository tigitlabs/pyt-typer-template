#!/bin/bash
# devcontainer_test.sh
set -e

script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

devcontainer_json=".devcontainer/devcontainer.json"
workspace_folder=$script_dir

export DOCKER_BUILDKIT=1
echo "🧪 Make sure devcontainer cli is available"
if [ ! $(command -v devcontainer) &> /dev/null ]; then
  echo "🚫 devcontainer could not be found"
  echo "Install devcontainer cli"
fi

echo "🏗️ Building image"
id_label="test-container=cicd"
devcontainer up --id-label ${id_label} --workspace-folder "${workspace_folder}"

# Run actual test
echo "(*) Running test..."
devcontainer exec --workspace-folder "${workspace_folder}" --id-label ${id_label} /bin/sh -c 'set -e; ./pre-commit.sh'

echo "(*) Docker image details..."
docker images

# Clean up
docker rm -f $(docker container ls -f "label=${id_label}" -q)

# Exit immediately if a command exits with a non-zero status
set -e

# Check if the file "test-project/test.sh" exists
if [ -f "test-project/test.sh" ]; then
  # Change the current directory to "test-project"
  cd test-project

  # Check if the current user is root
  if [ "$(id -u)" = "0" ]; then
    # If the user is root, make "test.sh" executable
    chmod +x test.sh
  else
    # If the user is not root, use sudo to make "test.sh" executable
    sudo chmod +x test.sh
  fi

  # Execute "test.sh"
  ./test.sh
else
  # If "test.sh" does not exist, list all files in the current directory
  ls -a
fi