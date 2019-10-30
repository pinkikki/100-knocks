#!/bin/bash -eu

set -euo pipefail
sed -e 's/\t/ /g' hightemp.txt
