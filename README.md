## Установка

1. Склонируйте репозиторий 

```
git clone https://github.com/ardash-ds/rest_api_python.git
```

2. Установите виртуальное окружение и активируйие его


Для windows:
```
python -m venv venv
venv\scripts\activate
```

Для linux:
```
python3 -m venv venv
source venv/bin/activate
```

3. Установите зависимости

```
pip install -r requirements.txt
```

4. Добавьте в корень проекта файл с переменными окружения .env


5. Выполните команды для сборки проекта

```
make build
make migrations
make population
make app
```


Адрес свагера: [http://127.0.0.1:8000/docs/]


## Архитектура

```
apps
├── core
│   ├──  block.py
│   └──  user.py
│
├── models
│   ├──  block.py
│   └──  user.py
│
├── urls
│   ├──  block.py
│   └──  user.py
│
├── views
│   ├──  block.py
│   └──  user.py
│ 
├── serializers
│   ├──  block.py
│   └──  user.py
...


```
