#!/bin/bash
set -e

if [ "$1" = 'runserver' ]; then
    shift
    cd src
    exec python -m pelican -lr content -s core/settings.py -o output -b 0.0.0.0 --ignore-cache $@
elif [ "$1" = 'lint' ]; then
    shift
    OPTS=${@:-'.'}
    echo "-- black --" && black --check --diff $OPTS || EXIT=$?
    echo "-- ruff --" && ruff $OPTS || EXIT=$?
    MYPY_OPTS=${@:-'src/'}
    echo "-- mypy --" && mypy $MYPY_OPTS || EXIT=$?
    exit ${EXIT:-0}
elif [ "$1" = 'fmt' ]; then
    shift
    OPTS=${@:-'.'}
    echo "-- black --" && black $OPTS
    echo "-- ruff --" && ruff --fix $OPTS
    exit 0
elif [ "$1" = 'release' ]; then
    shift
    cd src
    export SITEURL=https://lukzmu.github.io
    exec python -m pelican content -s core/settings.py -o output
fi

exec "$@"
