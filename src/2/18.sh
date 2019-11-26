#!/bin/bash -eu

set -euo pipefail
sort -t$'\t' -k 3 -r hightemp.txt
