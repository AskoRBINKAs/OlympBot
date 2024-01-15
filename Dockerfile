FROM python:3.10-alpine
WORKDIR /bot
COPY . .
RUN pip3 install -r req.txt
ENV TOKEN=PRODUCTION_TOKEN
ENTRYPOINT ["python3","main.py"]