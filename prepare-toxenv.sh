#!/bin/bash
set -ex

# collect posargs
envbindir=$1
toxinidir=$2

# purge previous build artifacts
rm -rf ./dist

# build & install package
poetry install -v
poetry build -f sdist

pkg_name=$(ls ./dist | grep .tar.gz)
${envbindir}/pip install ${toxinidir}/dist/${pkg_name}
