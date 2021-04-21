* Базовые команды SQL:

* Что такое ORM?

* Базовые команды ORM SQLAlchemy:

* Подключение к популярным БД:

**SQLite**

```python
import sqlite3
from sqlite3 import Error


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print('Connection to SQLite DB successful')
    except Error as e:
        print(f'The error "{e}" occurred')
    return connection
    
    
connection = create_connection('E:\\some_app.sqlite')
```

**MySQL**

`pip install mysql-connector-python` - в отличие от SQLite, в Python по умолчанию нет модуля, который можно использовать для подключения к базе данных MySQL. 
Для этого необходимо установить драйвер Python для MySQL. 

```python
import mysql.connector
from mysql.connector import Error


def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print('Connection to MySQL DB successful')
    except Error as e:
        print(f'The error "{e}" occurred')
    return connection
        
        
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print('Database created successfully')
    except Error as e:
        print(f'The error "{e}" occurred')    
        
        
create_database_query = 'CREATE DATABASE some_app'
create_database(connection, create_database_query)
connection = create_connection('localhost', 'root', '', 'some_app')
```

**PostgreSQL**

`pip install psycopg2` - как и в случае MySQL, для PostgreSQL в стандартной библиотеке Python нет модуля для взаимодействия с базой данных.

```python
from psycopg2 import OperationalError

def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print('Connection to PostgreSQL DB successful')
    except OperationalError as e:
        print(f'The error "{e}" occurred')
    return connection
    
    
def create_database(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print('Query executed successfully')
    except OperationalError as e:
        print(f'The error "{e}" occurred')


create_database_query = 'CREATE DATABASE some_app'
create_database(connection, create_database_query) 
connection = create_connection('some_app', 'postgres', 'abc123', '127.0.0.1', '5432')
```

> P.S. Хорошая статья о работе (на чистом SQL) с SQLite, MySQL, PostgreSQL [здесь](https://proglib.io/p/kak-podruzhit-python-i-bazy-dannyh-sql-podrobnoe-rukovodstvo-2020-02-27).
