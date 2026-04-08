FROM python:3.9-slim

WORKDIR /app
ENV PYTHONPATH=/app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# NOTE: agent.py is an ADK file, not a native Streamlit app.
# If you build this locally, you may need a separate app.py for Streamlit.
CMD ["streamlit", "run", "agent.py", "--server.port=8501", "--server.address=0.0.0.0"]
