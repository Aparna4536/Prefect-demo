name: Run Prefect ML Pipeline

on:
  push:
    branches: ["main"]
  workflow_dispatch:

jobs:
  run-pipeline:
    runs-on: ubuntu-latest

    steps:
      - name: Check out repository
        uses: actions/checkout@v6

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: pip install prefect scikit-learn joblib

      - name: Run pipeline
        run: python prefect_pipeline.py
