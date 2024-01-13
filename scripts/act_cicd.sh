#!/bin/bash
# act_cicd.sh

VERBOSE=0
# Check if verbose mode is enabled
if [ "$1" == "-v" ]; then
  VERBOSE=1
fi

# Check if verbose mode is enabled
if [ "$1" == "-vv" ]; then
  VERBOSE=1
  set -x
fi

# Debug print function
function debug_print() {
  if [ $VERBOSE -eq 1 ]; then
    echo "$1"
  fi
}

set -e

script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
debug_print "📂 Script directory: $script_dir"

project_root="$script_dir/.."
debug_print "📂 project root: $project_root"

workflows_dir="$project_root/.github/workflows"
debug_print "📂 workflows directory: $workflows_dir"
workflow_file="$workflows_dir/cicd.yml"

act pull_request \
--platform ubuntu-latest=ghcr.io/catthehacker/ubuntu:runner-22.04 \
--workflows "$workflow_file" \
--job cicd
