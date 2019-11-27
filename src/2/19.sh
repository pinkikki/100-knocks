#!/bin/bash -eu

set -euo pipefail
cut -f 1 hightemp.txt | sort | uniq -c | sort -nr
