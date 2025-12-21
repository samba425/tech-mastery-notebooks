FROM python:3.11-slim

WORKDIR /app

RUN pip install flask flask-socketio flask-cors

COPY server.py .
COPY client.html .

EXPOSE 5000

CMD ["python", "server.py"]


