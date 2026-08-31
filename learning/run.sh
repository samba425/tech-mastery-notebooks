#!/usr/bin/env bash
# Wrapper to run the learning helper
cd "$(dirname "$0")"
python3 learn.py "$@"
