FROM pypy:latest
WORKDIR /app
COPY . /app
CMD python watch_next.py