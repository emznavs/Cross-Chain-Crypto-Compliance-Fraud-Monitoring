#!/usr/bin/env bash
source ../venv/bin/activate
python scripts/etl.py
python scripts/features.py
python scripts/anomaly.py
