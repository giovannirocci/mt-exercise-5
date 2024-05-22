#! /bin/bash
scripts=$(dirname "$0")
base=$scripts/..
tools=$base/tools
mkdir -p $tools
# install JoeyNMT scripts
git clone https://github.com/siri-web/JoeyNMT-hotfixed $tools/joeynmt_hotfix
