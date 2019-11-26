#!/bin/bash -eu

set -euo pipefail
sort -t$'\t' -k 1 hightemp.txt | uniq -w 9
