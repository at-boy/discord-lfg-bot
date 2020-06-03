FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY discord-lfg-bot.py ./

CMD [ "python", "./discord-lfg-bot.py" ]
