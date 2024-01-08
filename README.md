# Sabalansētas ēdienkartes plānošana
Grupas dalībnieki:
- Elizabete Citskovska
- Kirils Bondars
- Dmitrijs Sizovs
- Artūrs Zvirgzdiņš
- Miks Šics
- Katrīna Kate Mālniece

# Risinājuma apskatīšana
Risinājuma mājaslapa: https://www.diet.id.lv/ 
<br><br> Testa lietotājs
<br>email: `test@test.test`, password: `123`


# Development Windows
## Install programs
```console
git clone https://github.com/kirilsbondars/diet-app
cd diet-app/src
pip install virtualenv
virtualenv venv
venv\Scripts\activate
pip3 install -r requirements.txt
```
## Set up MySQL
```mysql
CREATE DATABASE diet_app;
CREATE USER 'diet_app_user'@'localhost' IDENTIFIED BY '123';
GRANT ALL PRIVILEGES ON *.* TO 'diet_app_user'@'localhost' WITH GRANT OPTION;
```

## Run Flask
```console
python app.py
```

# Instalācijas instrukcija (Ubuntu 22.04 LTS)
## Install programs
```console
sudo apt install python3 git gunicorn mysql-server python3-flask python3-pip python3-venv -y
```
## Clone git
```console
git clone https://github.com/kirilsbondars/diet-app
cd diet-app/src
python3 -m venv .venv
. .venv/bin/activate
pip3 install -r requirements.txt
```
## Set up MySQL
```console
sudo mysql
```
```mysql
CREATE DATABASE diet_app;
CREATE USER 'diet_app_user'@'localhost' IDENTIFIED BY '123';
GRANT ALL PRIVILEGES ON *.* TO 'diet_app_user'@'localhost' WITH GRANT OPTION;
exit;
```
## Change config.py
```console
nano diet-app/src/config.py
```
edit config.py content
```python
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://diet_app_user:123@localhost/diet_app'
```
## Test Flask
```console
python3 diet-app/src/app.py
```
## Gunicorn

```console
cd /diet-app/src
gunicorn --config gunicorn_config.py app:app
```

