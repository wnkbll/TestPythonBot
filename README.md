# Telegram bot
### Как запустить
1) Поменять имя файла `.env-example` на `.env-prod`
2) Поменять значение ключа `TOKEN` на токен Telegram Bot API
3) Запустить `docker compose build && docker compose up` 

### Возможные ошибки: 
`exec /app/scripts/bot.sh: no such file or directory`:
1) Скачать утилиту `dos2unix` (https://dos2unix.sourceforge.io/)
2) Перейти в папку со скриптом и выполнить `dos2unix bot.sh`
