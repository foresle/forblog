Title: Joplin server smtp
Date: 2022-03-30 14:00
Category: Tutorial
Tags: joplin, server, my_config, smtp
Slug: joplin_server_smtp
Authors: foresle
Summary: Додаємо email до Joplin сервер

#### Перша частина: [Підіймаємо власний Joplin сервер]({filename}/install_joplin_server.md)

Email потрібний для того, щоб ви могли відновити пароль або змінити пошту в обліковому записі Joplin.

### Система

**Ubuntu 20.04 LTS**

### Інструкція

Я використав Gmail в якості smtp серверу.
Якщо ви будете використовувати її теж, не забудьте ввімкнути цей параметр: [Доступ для менш безпечних додатків](https://myaccount.google.com/lesssecureapps) 


#### Додайте в конфіг такі рядки

Файл `.env`

```env
MAILER_ENABLED=1
MAILER_HOST=smtp.gmail.com
MAILER_PORT=465
MAILER_SECURE=1
MAILER_AUTH_USER=<ВАШ EMAIl>
MAILER_AUTH_PASSWORD=<ПАРОЛЬ>
MAILER_NOREPLY_NAME=JoplinServer
MAILER_NOREPLY_EMAIL=noreply@example.com
```

#### Перезапустіть контейнер

```sh
sudo docker restart <ID>
```

Щоб дізнатися id контейнерів:
```sh
sudo docker ps
```


### Джерела

[Форум Joplin](https://discourse.joplinapp.org/t/joplin-server-2-2-6-email-settings/18608/5)
