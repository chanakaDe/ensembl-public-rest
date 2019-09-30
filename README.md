# Ensembl Public REST API

The public RESTful API for the Ensembl Gene Autocomplete data table. ( A demo repository created in order to demonstrate REST API skills )

### Tech

Ensembl Public REST API uses a number of open source projects to work properly:

* Flask
* flask_restful
* flask_script
* flask_migrate
* marshmallow
* flask_sqlalchemy
* flask_marshmallow
* marshmallow-sqlalchemy
* psycopg2
* pymysql

### Installation

Clone this repository and enter the repository. You need to have `python` and `pip` installed in your working environment.

```
git clone https://github.com/chanakaDe/ensembl-public-rest.git
cd ensembl-public-rest
```
Then you have to creates a virtual environment.
```
python3.6 -m venv env
```
Or if you have python, use following command:
```
python -m venv env
```
Then you need to activate the virtual environment.
```
source env/bin/activate
```
Then you need to install all the dependencies.
```
pip install -r requirements.txt
```

#### Optional
If you need to change the database connection, use `config.py` file to change `SQLALCHEMY_DATABASE_URI` parameter.

```
SQLALCHEMY_DATABASE_URI = "mysql://anonymous@ensembldb.ensembl.org:3306/ensembl_website_97"
```
This is a public database and users don't need to enter any password.

Finally start the server.
```
python run.py
```
If you configured everything correctly, you will see following output in your terminal.
```
Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
Restarting with stat
Debugger is active!
Debugger PIN: xxx:xxx:xxx
```
For more information about the testing of Ensembl Public REST API : [TESTING.md](https://github.com/chanakaDe/ensembl-public-rest/blob/master/TESTING.md)

For more information about the deployment of Ensembl Public REST API : [DEPLOY.md](https://github.com/chanakaDe/ensembl-public-rest/blob/master/DEPLOY.md)

