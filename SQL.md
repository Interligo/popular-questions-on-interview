### Сборник теоретических вопросов по SQL

***

* Что такое транзакция? Какие у неё есть свойства?

Транзакция базы данных - это логическая единица работы, которая переводит базу данных из одного завершенного состояния в другое завершенное состояние. Например, если вы создаете, обновляете или удаляете запись из таблицы, вы выполняете в этой таблице транзакцию. Транзакции имеют следующие четыре стандартных свойства, обычно обозначаемых аббревиатурой ACID.

1. `Атомарность` – обеспечивает, чтобы все операции входящие в единицу работы были завершены успешно. В противном случае транзакция прерывается в момент сбоя, и все предыдущие операции возвращаются в прежнее состояние;

2. `Согласованность` — обеспечивает, чтобы база данных надлежащим образом изменяла состояние при успешной транзакции;

3. `Изолированность` — позволяет транзакциям работать независимо друг от друга и прозрачно;

4. `Долговечность` — гарантирует, что результат совершенной транзакции сохранится в случае сбоя системы.

В теории баз данных под транзакцией понимают одну из команд SQL - `SELECT`, `INSERT`, `UPDATE`, `DELETE`.

***

* Что такое уровни изолированности транзакций? Какие они бывают?

Условное значение, определяющее, в какой мере в результате выполнения логически параллельных транзакций в СУБД допускается получение несогласованных данных. Шкала уровней изолированности транзакций содержит ряд значений, проранжированных от наинизшего до наивысшего; более высокий уровень изолированности соответствует лучшей согласованности данных, но его использование может снижать количество физически параллельно выполняемых транзакций. И наоборот, более низкий уровень изолированности позволяет выполнять больше параллельных транзакций, но снижает точность данных. 

`Read uncommitted (чтение незафиксированных данных)` - низший (первый) уровень изоляции. Если несколько параллельных транзакций пытаются изменять одну и ту же строку таблицы, то в окончательном варианте строка будет иметь значение, определенное всем набором успешно выполненных транзакций. При этом возможно считывание не только логически несогласованных данных, но и данных, изменения которых ещё не зафиксированы.

`Read committed (чтение фиксированных данных)` - большинство промышленных СУБД по умолчанию используют именно этот уровень. На этом уровне обеспечивается защита от чернового, «грязного» чтения, тем не менее, в процессе работы одной транзакции другая может быть успешно завершена и сделанные ею изменения зафиксированы. В итоге первая транзакция будет работать с другим набором данных.

`Repeatable read (повторное чтение)` - уровень, при котором читающая транзакция «не видит» изменения данных, которые были ею ранее прочитаны. При этом никакая другая транзакция не может изменять данные, читаемые текущей транзакцией, пока та не окончена.

`Serializable (упорядочиваемость)` - самый высокий уровень изолированности; транзакции полностью изолируются друг от друга, каждая выполняется так, как будто параллельных транзакций не существует. Только на этом уровне параллельные транзакции не подвержены эффекту «фантомного чтения».

***

* Что такое вложенные транзакции?

Транзакции, которые вызываются при вызове иной транзации.

```python
Транзакция 1: Пополнить счёт пользователя
Транзакция 2: Дать скидку пользователю
Транзакция 3: Регистрация (создать пользователя)
```

Если нам необходимо после регистрации пользователя дать ему скидку и пополнить счет, то транзакции 1 и 2 будут вложены в 3 транзакцию.

***

* Что такое курсор и зачем он нужен?

Это поименованная область памяти, содержащая результирующий набор select запроса.

***

* Какая разница между PostgreSQL и MySQL?

**MySQL** имеет поддержку не всех функций и возможностей SQL. Это сделано для того, чтобы работать с MySQL было просто и удобно. Но если для проекта необходимо какое-то расширение, разработчики его могут добавить не в ущерб стандарту.

**PostgreSQL** поддерживает все новые стандарты SQL, из-за этого данный проект довольно сложный и не настолько популярный как MySQL.

***

* Что такое VACUUM в PostgreSQL?

Команда позволяющая провести сборку мусора и, возможно, проанализировать базу данных.

`VACUUM` высвобождает пространство, занимаемое «мёртвыми» кортежами. При обычных операциях Postgres кортежи, удалённые или устаревшие в результате обновления, физически не удаляются из таблицы; они сохраняются в ней, пока не будет выполнена команда VACUUM. Таким образом, периодически необходимо выполнять VACUUM, особенно для часто изменяемых таблиц.

***

* Что такое EXPLAIN? Какая разница между ним и EXPLAIN ANALYZE?

`EXPLAIN` выводит план выполнения. План выполнения показывает, как будут сканироваться таблицы, затрагиваемые оператором — просто последовательно, по индексу и т. д. — а если запрос связывает несколько таблиц, какой алгоритм соединения будет выбран для объединения считанных из них строк.

Иными словами, эта команда может **в точности рассказать**, что происходит, когда выполняется запрос.

Дополнительный параметр `ANALYZE` - выполнить команду и вывести фактическое время выполнения и другую статистику. По умолчанию этот параметр равен FALSE.

***

* Индексы в базах данных и их физическая реализация

Индексы – это специальные таблицы, которые могут быть использованы поисковым двигателем базы данных (далее – БД), для ускорения получения данных. Необходимо просто добавить указатель индекса в таблицу. Индекс помогает ускорить запросы на получение данных (SELECT [WHERE]), но замедляет процесс добавления и изменения записей (INSERT, UPDATE). Индексы могут быть добавлены или удалены без влияния на сами данные.

Сразу после создания, пока таблица не имеет индексов, таблица выглядит как куча (heap) данных.

Для того, чтобы добавить индекс, нам необходимо использовать команду CREATE INDEX, что позволит нам указать имя индекса и определить таблицу и колонку или индекс колонки и определить используется ли индекс по возрастанию или по убыванию.

```sql
CREATE INDEX имя_индекса ON имя_таблицы;
```

***

* Типы индексов

`Кластеризованный индекс` - такой индекс хранит реальные строки данных в листьях индекса. Важной характеристикой кластеризованного индекса является то, что все значения отсортированы в определенном порядке либо возрастания, либо убывания. Таким образом, таблица или представление может иметь только один кластеризованный индекс.

`Некластеризованный индекс` - в отличие от кластеризованного индекса, листья некластеризованного индекса содержат только те столбцы (ключевые), по которым определен данный индекс, а также содержит указатель на строки с реальными данными в таблице. Такие индексы не могут быть отсортированы.

`Составной индекс` - может содержать более одного столбца. Вы можете включить до 16 столбцов в индекс, но их общая длина ограничена 900 байтами. Как кластеризованный, так и некластеризованный индексы могут быть составными.

`Уникальный индекс` - обеспечивает уникальность каждого значения в индексируемом столбце. Если индекс составной, то уникальность распространяется на все столбцы индекса, но не на каждый отдельный столбец. К примеру, если вы создадите уникальных индекс на столбцах ИМЯ и ФАМИЛИЯ, то полное имя должно быть уникально, но отдельно возможны дубли в имени или фамилии.

`Покрывающий индекс` - позволяет конкретному запросу сразу получить все необходимые данные с листьев индекса без дополнительных обращений к записям самой таблицы.

***

* Почему таблица не может иметь два кластеризованных индекса?

Кластеризованный индекс – это и есть таблица. При создании кластеризованного индекса у таблицы, подсистема хранения данных сортирует все строки в таблице в порядке возрастания или убывания, согласно определению индекса. Кластеризованный индекс это не отдельная сущность как другие индексы, а механизм сортировки данных в таблице и облегчения быстрого доступа к строкам с данными.

***

* Если кластеризованная таблица даёт множество преимуществ, то зачем использовать кучу?

Кластеризованые таблицы отличны и большинство ваших запросов будут лучше выполнятся к таблицам, имеющим кластеризованный индекс. Но в некоторых случаях вы возможно захотите оставить таблицы в их естественном первозданном состоянии, т.е. в виде кучи, и создать лишь некластеризованные индексы для поддержания работоспособности ваших запросов.

***

* Представление (view) в SQL

Представления в SQL являются особым объектом, который содержит данные, полученные запросом SELECT из обычных таблиц. Это виртуальная таблица, к которой можно обратиться как к обычным таблицам и получить хранимые данные. Представление в SQL может содержать в себе как данные из одной единственной таблицы, так и из нескольких таблиц.

Представления нужны для того, чтобы упростить работу с базой данных и ускорить время ответа сервера. Так как представление — это уже результат некой выборки данных с помощью SELECT, то, очевидно, в следующий раз вместо запроса к нескольким таблицам достаточно просто обратиться к уже созданному представлению.

```sql
CREATE VIEW info_order
AS SELECT onum, amt, cname
FROM orders, customers
WHERE orders.cnum = customers.cnum
```

***

* Партицирование

Это метод разделения больших (исходя из количества записей, а не столбцов) таблиц на много маленьких. И желательно, чтобы это происходило прозрачным для приложения способом.

После создания основной таблицы можно создать партиции, что означает – наследованные таблицы.

```sql
create table users (
    id             serial primary key,
    username       text not null unique,
    password       text,
    created_on     timestamptz not null,
    last_logged_on timestamptz not null
);

create table users_1 () inherits (users);
```

***

* Case

Оператор `CASE` в зависимости от указанных условий возвращает одно из множества возможных значений. В примере условием является проверка на NULL. Если это условие выполняется, то возвращается текст «Нет в наличии», в противном случае (ELSE) возвращается значение цены.

```sql
SELECT DISTINCT product.model, 
    CASE 
    WHEN price IS NULL 
    THEN 'Нет в наличии' 
    ELSE CAST(price AS CHAR(20)) 
    END price 
FROM Product LEFT JOIN 
    PC ON Product.model = PC.model
WHERE product.type = 'pc';
```

***

* ER-диаграммы

Схема «сущность-связь» (также ERD или ER-диаграмма) — это разновидность блок-схемы, где показано, как разные «сущности» (люди, объекты, концепции и так далее) связаны между собой внутри системы. 

***

* Нормальные формы, преимущества и недостатки нормализации

`Нормализация` - это процесс сокращения повторений информации в базе данных. Нормализуются в базе данных не только данные, но и имена, включая имена объектов и форм.

`Нормальная форма` - это мера глубины, до которой должна быть выполнена нормализация базы данных.

Обычно в процессе нормализации используются следующие три нормальные формы:

1. Целью первой нормальной формы является разделение базы данных на логические единицы, называемые таблицами.

2. Целью второй нормальной формы является выделение данных, только отчасти зависящих от ключа, и помещение этих данных в другую таблицу.

3. Целью третьей нормальной формы является удаление из таблиц данных, не зависящих от ключа.

Хотя большинство успешно работающих баз данных в некоторой степени нормализованы, нормализация имеет один существенный недостаток: замедление работы базы данных.

***

* Схемы "Снежинка" и "Звезда"

**Многомерная схема** специально разработана для моделирования систем хранилищ данных.

Звезда - в этой схеме центр звезды может иметь одну таблицу фактов и несколько связанных таблиц измерений. Это известно как схема звезды, поскольку ее структура напоминает звезду. Схема «звезда» — это самый простой тип схемы хранилища данных. Он также известен как схема соединения звездой и оптимизирован для запросов больших наборов данных.

Снежинка - это логическое расположение таблиц в многомерной базе данных, так что диаграмма ER напоминает форму снежинки. Схема «Снежинка» является расширением схемы «Звезда» и добавляет дополнительные измерения. Таблицы измерений нормализуются, что разбивает данные на дополнительные таблицы.

***

* Аналитические функции

Аналитические оконные функции, или функции распределения (distribution function), предоставляют информацию о распределении данных и используются в основном для статистического анализа. 

1. `FIRST_VALUE` - возвращает первое значение в упорядоченном наборе значений.

2. `LAST_VALUE` - возвращает последнее значение из упорядоченного набора значений.

3. `LAG` - обеспечивает доступ к строке с заданным физическим смещением перед началом текущей строки. 

4. `LEAD` - обеспечивает доступ к строке на заданном физическом смещении после текущей строки.

5. `PERCENT_RANK` - вычисляет относительный ранг строки из группы строк.

6. `PERCENTILE_CONT` - вычисляет процентиль на основе постоянного распределения значения столбца.

7. `PERCENTILE_DISC` - вычисляет определенный процентиль для отсортированных значений из всего набора строк или в пределах определенных секций набора строк.

8. `CUME_DIST` - вычисляет интегральное распределение значений в группе значений. Другими словами, CUME_DIST вычисляет относительное положение указанного значения в группе значений.

***

* Базовые команды SQL:

`SHOW DATABASES` - SQL-команда, которая отвечает за просмотр доступных баз данных.

`CREATE DATABASE` - Команда для создания новой базы данных.

`USE` - С помощью этой SQL-команды USE <database_name> выбирается база данных, необходимая для дальнейшей работы с ней.

`SOURCE` - позволит выполнить сразу несколько SQL-команд, содержащихся в файле с расширением .sql.

```sql
SOURCE <file.sql>
```

`DROP DATABASE` - Стандартная SQL-команда для удаления целой базы данных.

`SHOW TABLES` - С помощью этой несложной команды можно увидеть все таблицы, которые доступны в базе данных.

`CREATE TABLE` - SQL-команда для создания новой таблицы.

`DESCRIBE` - можно просмотреть различные сведения (тип значений, является ключом или нет) о столбцах таблицы.

```sql
DESCRIBE <table_name>
```

`INSERT` - отвечает за добавление данных в таблицу.

`UPDATE` - SQL-команда для обновления данных таблицы.

`DELETE` - используется для удаления данных из таблицы.

```sql
DELETE FROM <table_name>
```

`DROP TABLE` - удалить всю таблицу целиком.

`SELECT` - для получения данных из выбранной таблицы.

`SELECT DISTINCT` - для получения только уникальных данных.

`WHERE` - для указания условий в запросе. Иногда используется совместно с `IN` 

```sql
SELECT <col_name1>, <col_name2>, …
    FROM <table_name>
    WHERE <col_namen> IN (<value1>, <value2>, …);
```

`GROUP BY` - используется с агрегатными функциями, такими как `COUNT`, `MAX`, `MIN`, `SUM` и `AVG`, для группировки выходных значений.

`HAVING` - Ключевое слово HAVING было добавлено в SQL по той причине, что WHERE не может использоваться для работы с агрегатными функциями.

```sql
SELECT COUNT(course_id), dept_name
    FROM course
    GROUP BY dept_name
    HAVING COUNT(course_id)>1;
```

`ORDER BY` - используется для сортировки результатов запроса по убыванию или возрастанию. `ORDER BY` отсортирует по возрастанию, если не будет указан способ сортировки `ASC` или `DESC`.

`BETWEEN` - используется для выбора значений данных из определённого промежутка. 

`LIKE` - Оператор LIKE используется в WHERE, чтобы задать шаблон поиска похожего значения.

Есть два свободных оператора, которые используются в LIKE:

1. `%` (ни одного, один или несколько символов);

2. `_` (один символ).

`JOIN` - используется для связи двух или более таблиц с помощью общих атрибутов внутри них.

```sql
SELECT <col_name1>, <col_name2>, …
    FROM <table_name1>
    JOIN <table_name2>
    ON <table_name1.col_namex> = <table2.col_namex>;
```

***

`VIEW` - это виртуальная таблица SQL, созданная в результате выполнения выражения. Она содержит строки и столбцы и очень похожа на обычную SQL-таблицу. VIEW всегда показывает самую свежую информацию из базы данных.

```sql
CREATE VIEW <view_name> AS
    SELECT <col_name1>, <col_name2>, …
    FROM <table_name>
    WHERE <condition>;
```

***

* Что такое ORM?

ORM (Object-Relational Mapping, объектно-реляционное отображение, или преобразование) — технология программирования, которая связывает базы данных с концепциями объектно-ориентированных языков программирования, создавая «виртуальную объектную базу данных». 

***

* MetaData и Table в SQLAlchemy:

MetaData - это контейнер, который содержит информацию о схеме базы данных (таблицах, индексах, типах данных и тд).

Table - содержит описание таблиц, для генерации запросов.

```python
metadata = MetaData()

domains = Table(
    'domains',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, unique=True),
    Column('owner', String)
)
```

***

![](https://github.com/Interligo/popular-questions-on-python-interview/blob/main/SQL_JOINS.jpg)

***

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

***

> P.S. Хорошая статья о работе (на чистом SQL) с SQLite, MySQL, PostgreSQL [здесь](https://proglib.io/p/kak-podruzhit-python-i-bazy-dannyh-sql-podrobnoe-rukovodstvo-2020-02-27).
> 
> [Практикум](http://bdis.umeta.ru/db/db_course/labs/index.html) по курсу "Введение в моделирование данных, базы данных и SQL".
> 
> [Упражнения](https://www.sql-ex.ru/) по SQL.
