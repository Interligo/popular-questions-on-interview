* Что такое транзакция? Какие у неё есть свойства?

Транзакция — это осуществление одного или нескольких изменений базы данных. Например, если вы создаете, обновляете или удаляете запись из таблицы, вы выполняете в этой таблице транзакцию. Транзакции имеют следующие четыре стандартных свойства, обычно обозначаемых аббревиатурой ACID.

1. `Атомарность` – обеспечивает, чтобы все операции входящие в единицу работы были завершены успешно. В противном случае транзакция прерывается в момент сбоя, и все предыдущие операции возвращаются в прежнее состояние;

2. `Согласованность` — обеспечивает, чтобы база данных надлежащим образом изменяла состояние при успешной транзакции;

3. `Изолированность` — позволяет транзакциям работать независимо друг от друга и прозрачно;

4. `Долговечность` — гарантирует, что результат совершенной транзакции сохранится в случае сбоя системы.

* Что такое уровни изолированности транзакций? Какие они бывают?

Условное значение, определяющее, в какой мере в результате выполнения логически параллельных транзакций в СУБД допускается получение несогласованных данных. Шкала уровней изолированности транзакций содержит ряд значений, проранжированных от наинизшего до наивысшего; более высокий уровень изолированности соответствует лучшей согласованности данных, но его использование может снижать количество физически параллельно выполняемых транзакций. И наоборот, более низкий уровень изолированности позволяет выполнять больше параллельных транзакций, но снижает точность данных. 

`Read uncommitted (чтение незафиксированных данных)` - низший (первый) уровень изоляции. Если несколько параллельных транзакций пытаются изменять одну и ту же строку таблицы, то в окончательном варианте строка будет иметь значение, определенное всем набором успешно выполненных транзакций. При этом возможно считывание не только логически несогласованных данных, но и данных, изменения которых ещё не зафиксированы.

`Read committed (чтение фиксированных данных)` - большинство промышленных СУБД по умолчанию используют именно этот уровень. На этом уровне обеспечивается защита от чернового, «грязного» чтения, тем не менее, в процессе работы одной транзакции другая может быть успешно завершена и сделанные ею изменения зафиксированы. В итоге первая транзакция будет работать с другим набором данных.

`Repeatable read (повторное чтение)` - уровень, при котором читающая транзакция «не видит» изменения данных, которые были ею ранее прочитаны. При этом никакая другая транзакция не может изменять данные, читаемые текущей транзакцией, пока та не окончена.

`Serializable (упорядочиваемость)` - самый высокий уровень изолированности; транзакции полностью изолируются друг от друга, каждая выполняется так, как будто параллельных транзакций не существует. Только на этом уровне параллельные транзакции не подвержены эффекту «фантомного чтения».

* Что такое вложенные транзакции?

Транзакции, которые вызываются при вызове иной транзации.

```python
Транзакция 1: Пополнить счёт пользователя
Транзакция 2: Дать скидку пользователю
Транзакция 3: Регистрация (создать пользователя)
```

Если нам необходимо после регистрации пользователя дать ему скидку и пополнить счет, то транзакции 1 и 2 будут вложены в 3 транзакцию.

* Что такое курсор и зачем он нужен?

Это поименованная область памяти, содержащая результирующий набор select запроса.

* Какая разница между PostgreSQL и MySQL?

**MySQL** имеет поддержку не всех функций и возможностей SQL. Это сделано для того, чтобы работать с MySQL было просто и удобно. Но если для проекта необходимо какое-то расширение, разработчики его могут добавить не в ущерб стандарту.

**PostgreSQL** поддерживает все новые стандарты SQL, из-за этого данный проект довольно сложный и не настолько популярный как MySQL.

* Что такое VACUUM в PostgreSQL?

Команда позволяющая провести сборку мусора и, возможно, проанализировать базу данных.

`VACUUM` высвобождает пространство, занимаемое «мёртвыми» кортежами. При обычных операциях Postgres кортежи, удалённые или устаревшие в результате обновления, физически не удаляются из таблицы; они сохраняются в ней, пока не будет выполнена команда VACUUM. Таким образом, периодически необходимо выполнять VACUUM, особенно для часто изменяемых таблиц.

* Что такое EXPLAIN? Какая разница между ним и EXPLAIN ANALYZE?



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
