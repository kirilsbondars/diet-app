# Sabalansētas ēdienkartes plānošana
Grupas dalībnieki:
- Elizabete Citskovska
- Kirils Bondars
- Dmitrijs Sizovs
- Artūrs Zvirgzdiņš
- Miks Šics
- Katrīna Kate Mālniece

# Instalācijas instrukcija (Ubuntu 22.04 LTS)
## Install programs
```console
kirils@KirilsPC:~$ sudo apt install python3 git gunicorn mysql-server python3-flask python3-pip python3-venv -y
```
## Clone git
```console
kirils@KirilsPC:~$ git clone https://github.com/kirilsbondars/diet-app
kirils@KirilsPC:~$ pip3 install -r diet-app/requirements.txt
kirils@KirilsPC:~$ cd diet-app
kirils@KirilsPC:~$ python3 -m venv env
```
## Set up MySQL
```console
kirils@KirilsPC:~$ sudo mysql
mysql> CREATE DATABASE diet_app;
mysql> CREATE USER 'diet_app_user'@'localhost' IDENTIFIED BY '123';
mysql> GRANT ALL PRIVILEGES ON *.* TO 'diet_app_user'@'localhost' WITH GRANT OPTION;
mysql> exit;
```
## Change config.py
```console
kirils@KirilsPC:~$ nano diet-app/src/config.py
```
edit config.py content
```python
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://diet_app_user:123@localhost/diet_app'
```
## Test Flask
```console
kirils@KirilsPC:~$ python3 diet-app/src/app.py
```
## Gunicorn

```console
kirils@KirilsPC:~$ cd /diet-app/src
kirils@KirilsPC:~$ gunicorn --config gunicorn_config.py app:app
```
