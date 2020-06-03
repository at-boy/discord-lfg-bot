# discord-lfg-bot
Discord Bot for organizing games like Dungeons &amp; Dragons

This is very early development, right now it does nothing but read message looking for '!?lfg' if found it would reply with info about usage

You need to get a discord bot token for it to work

You can run the bot directly from your commandline with this command
```
DISCORD_BOT_TOKEN='<INSERT DISCORD BOT TOKEN>' python3 discord-lfg-bot.py
```

You can build the Docker Image with this command run from within the project directory
```
docker build -t discord-lfg-bot:latest .
```

You can run the Docker Image with this command
```
docker run -it --rm -e 'DISCORD_BOT_TOKEN=<INSERT DISCORD BOT TOKEN>' discord-lfg-bot:latest
```
