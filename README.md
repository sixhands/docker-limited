# Docker Limited Scripts

### docker-up
Собирает и запускает контейнеры с помощью docker-compose up
Обязательно должен запускаться из той директории, в которой присутствует файл docker-compose.yml

```bash
sudo docker-up
sudo docker-up --no-build
```

### docker-down
Останоавливает и удаляет запущенный контейнер. Запускать нужно только из той папки, в которой лежит файл
docker-compose.yml

```bash
sudo docker-down
```
### docker-clear
Удаляет все мусорные контейнеры с сервера. Допускается запуск из любой директории.
```bash
sudo docker-clear
```
### docker-images
Отображает список существующих на сервере образов.
```bash
sudo docker-images
```
### docker-ps
Отображает список контейнеров на сервере.
```bash
sudo docker-ps
sudo docker-ps --all
```
### docker-logs
Отображает список логов конкретного контейнера. Нужно запускать из той папки, в которой содержится файл docker-compose.yml
```bash
sudo docker-logs
```
###docker-prx
Добавляет в конфигурационный файл apache проксирование роута на заданный порт localhost. Повторный запуск скрипта приводит к перезаписи файла

Аргументы:
1. Название проекта
2. Роут, запрос по которому должен проксироваться
3. Порт, на который должен проксироваться запрос
```bash
sudo docker-prx biohac /api/ 7071
```