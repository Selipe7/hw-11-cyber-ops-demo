FROM python:3.11-slim
WORKDIR /work
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT ["python", "src/run.py"]
