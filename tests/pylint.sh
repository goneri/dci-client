#!/bin/sh

set -eu
files=$(git diff --diff-filter=AM --name-only HEAD~1 -- "client/*.py")
pylint --rcfile=.pylintrc ${files}