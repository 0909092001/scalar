#!/usr/bin/env bash
# AI System Workshop - macOS/Linux one-click starter
set -e

cd "$(dirname "$0")"

echo "=========================================="
echo "  AI System Workshop - Starting Jupyter"
echo "=========================================="
echo

if [ ! -d ".venv" ]; then
  echo "Creating virtual environment (.venv)..."
  python3 -m venv .venv
fi

source .venv/bin/activate

echo "Installing dependencies (first time may take a minute)..."
pip install -q --upgrade pip
pip install -q pandas numpy scikit-learn matplotlib seaborn jupyter

echo
echo "Launching Jupyter Notebook..."
python -m jupyter notebook
