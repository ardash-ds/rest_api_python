## Установка

Если у вас Windows, используйте WSl для разворачивания проекта:
Для установки WSL выполните следующие команды:
```
wsl --install
wsl --update
```

1. Склонируйте репозиторий 

```
git clone https://github.com/ardash-ds/rest_api_python.git
```

2. Установите виртуальное окружение, активируйие его и установите зависимости
(Этот шаг можно пропустить)


Для windows:
```
python -m venv venv
venv\scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

Для linux:
```
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

3. Добавьте в корень проекта файл с переменными окружения .env


4. Выполните команды для сборки проекта

```
make build
make migrations
make population
make app
```


Адрес свагера: [http://localhost:8000/docs/]

Данные для авторизации

```
username: user1 / user2 / user3 / user4 ... / user 10
password: string (для всех)
```

## Архитектура

```
project_dir
│
├── apps
│    ├── user
│    │    ├── core
│    │    │     └──  user.py
│    │    │
│    │    ├── models
│    │    │     └──  user.py
│    │    │
│    │    ├── serializers
│    │    │     └──  user.py
│    │    │
│    │    ├── urls
│    │    │     └──  user.py
│    │    │ 
│    │    └── views
│    │          └──  user.py
│    │    
│    └── block
│         ...  
│ 
├── config
│    ├── settings.py
│    ├── celery.py
│   ...
│
├── core
│    ├── serices
│    └── tasks
├── docker
│    ├── compose
│    └── Dockerfile
...

```
