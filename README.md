# Discord Radio Bot
- With these codes, you can create a radio bot that works on Discord using a .m3u8 streaming link!
## Installation(Docker Compose)
- docker-compose file:
```
version: '3.7'
services:
  discord-radio-bot:
    environment:
      - BOT_TOKEN=your discord bot token!
      - RADIO_URL=your .m3u8 stream link!
    build:
      context: .
      dockerfile: Dockerfile
    restart: always
    ports:
      - '3000:3000'
```

- Shell:
```
docker-compose up --build -d
```
