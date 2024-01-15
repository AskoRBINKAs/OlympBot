# OlympBot

## Run and deploy (docker)
You must have docker installed on your system
In ``Dockerile`` you must change TOKEN on yours
```
docker build . -t olymp/bot
docker run -t olymp/bot
```

## Run for development
* Optional: You can work in docker

Else, create virtual environment for python:

* Windows:
```
python -m venv venv
venv/Scripts/activate
pip install -r req.txt
```

* Linux or MacOS:
```
python3 -m venv venv
source venv/bin/activate
pip install -r req.txt
```

You can provide token into ``config.py`` or set ENV