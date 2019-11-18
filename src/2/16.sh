#!/bin/bash -eu

set -euo pipefail
split -l $1 hightemp.txt 16_split
