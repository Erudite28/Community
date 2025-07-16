FROM ubuntu
RUN apt update && apt install -y python3
COPY app.py /app/
WORKDIR /app
CMD ["python3", "app.py"]