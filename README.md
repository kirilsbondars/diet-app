# Sabalansētas ēdienkartes plānošana
Grupas dalībnieki:
- Elizabete Citskovska
- Kirils Bondars
- Dmitrijs Sizovs
- Artūrs Zvirgzdiņš
- Miks Šics
- Katrīna Kate Mālniece

# Instalācijas instrukcija (Ubuntu 22.04 LTS)
## Clone rep
```console
kirils@KirilsPC:~$ sudo apt update
kirils@KirilsPC:~$ sudo apt install python3 git gunicorn python-flask, mysql
kirils@KirilsPC:~$ git clone https://github.com/kirilsbondars/diet-app
kirils@KirilsPC:~$ cd diet-app
kirils@KirilsPC:~/diet-app$ pip3 install -r requirements.txt
```
setup mysql change file config to be able to connect to mysql
## Test Flask
```console
kirils@KirilsPC:~/diet-app$ cd src
kirils@KirilsPC:~/diet-app/src$ flask --app app run
```
## Gunicorn
```
import os

workers = int(os.environ.get('GUNICORN_PROCESSES', '2'))
threads = int(os.environ.get('GUNICORN_THREADS', '4'))
bind = os.environ.get('GUNICORN_BIND', '0.0.0.0:8080')

forwarded_allow_ips = '*'

secure_scheme_headers = { 'X-Forwarded-Proto': 'https' }
```

```console
gunicorn --config gunicorn_config.py app:app
```
