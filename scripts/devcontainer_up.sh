#!/bin/bash
# devcontainer_test.sh
set -e

script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
echo "📂 Script directory: $script_dir"
workspace_folder=$(realpath "$script_dir"/..)
echo "📂 Workspace folder: $workspace_folder"
devcontainer_json="$workspace_folder/.devcontainer/devcontainer.json"
echo "📄 Devcontainer json: $devcontainer_json"

export DOCKER_BUILDKIT=1
echo "🧪 Make sure devcontainer cli is available"
if [ ! $(command -v devcontainer) &> /dev/null ]; then
  echo "🚫 devcontainer could not be found"
  echo "Install devcontainer cli"
fi

echo "🏗️ Building image"
id_label="devcontainer=pyt-typer-template"
devcontainer up --id-label ${id_label} --workspace-folder "${workspace_folder}"

echo "ℹ️ Now you can attach to the running container with:"
echo "devcontainer exec --workspace-folder ${workspace_folder} --id-label ${id_label} /bin/bash"
echo "Run ./scripts/pre_commit.sh"
