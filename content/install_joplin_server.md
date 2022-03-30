Title: Підіймаємо власний Joplin сервер
Date: 2022-03-27 17:00
Category: Tutorial
Tags: joplin, server, my_config
Slug: install_joplin_server
Authors: foresle
Summary: Свій сервер для нотаток

### Система

**Ubuntu 20.04 LTS**

### Інструкція

#### Оновлюємо репозиторії, та встановлюємо такі пакети

```sh
sudo apt update
sudo apt upgrade
sudo apt install ufw nginx vim git postgresql
```

#### Також потрібно встановити Docker

Офіційна [інструкція](https://docs.docker.com/engine/install/).

#### Створюємо конфіг для Joplin

Файл `.env`

```env
APP_BASE_URL=<Ваш білий IP>
APP_PORT=22300
DB_CLIENT=pg
POSTGRES_PASSWORD=<Пароль>
POSTGRES_DATABASE=joplin
POSTGRES_USER=joplin
POSTGRES_PORT=5432
POSTGRES_HOST=127.0.0.1
```

#### Створюємо БД

```sh
sudo -u postgres psql
create user "joplin" with encrypted password '<Пароль>';
create database joplin owner joplin;
```

#### Вмикаємо Joplin Server

```sh
sudo docker run -d  --restart always --env-file /home/joplin/.env --net=host --add-host=host.docker.internal:127.0.0.1 -p 22300:22300 joplin/server:latest
```

#### Налаштовуємо проксі

Конфіг Nginx:

```
server {
	listen 80 default_server;

	server_name _;
		
	client_max_body_size 20M;

	location / {
		proxy_set_header Host $host;
		proxy_set_header X-Real-IP $remote_addr;
		proxy_pass http://127.0.0.1:22300;
	}
}
```

Шлях до файлу `/etc/nginx/sites-available/`

Зробіть символічне посилання та видаліть дефолтний конфіг

```sh
cd /etc/nginx/sites-enable/
ln -s /etc/nginx/sites-available/<Назва конфігу>
sudo rm default
```

Перевіряємо чи все ок

```sh
sudo nginx -t && sudo nginx -s reload
```

#### Закриваємо інші порти для безпеки

```sh
sudo ufw allow 80
sudo ufw allow 22
sudo ufw enable
```

### Підсумок

Ми отримали власний Joplin сервер.

**P.S.:** дефолтний юзер `admin@localhost` `admin`

### Джерела

[Офіційна інструкція для Joplin Server](https://github.com/laurent22/joplin/blob/dev/packages/server/README.md)
