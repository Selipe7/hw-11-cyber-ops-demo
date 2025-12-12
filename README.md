# Failed Login Rate Analysis

This project computes the failed login rate from a sample authentication log for reproducibility demonstration.

## Reproduce this

### Local Python environment
```bash
python -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt && python src/run.py

docker build -t capstone:dev . && docker run --rm -v "$PWD":/work capstone:dev
