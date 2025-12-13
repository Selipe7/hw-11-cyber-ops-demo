# Failed Login Rate Analysis

This project computes the failed login rate from a sample authentication log for reproducibility demonstration.

## Reproduce this
## Data Note

The `data/input.csv` file contains synthetic authentication log data created for demonstration purposes. No real user data is included.

### Local Python environment
```bash
python -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt && python src/run.py

docker build -t capstone:dev . && docker run --rm -v "$PWD":/work capstone:dev
