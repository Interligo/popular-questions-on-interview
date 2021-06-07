### SOLID 

Набор принципов проектирования для разработки программного обеспечения при помощи ООП.

***

* **Single Responsibility Principle** (принцип единственной ответственности):

Принцип единственной ответственности требует того, чтобы **один класс выполнял только одну работу**.

Класс User отвечает за свойства пользователя, в то время как класс UserDB отвечает за управление базой данных пользователя. 

```python
class User:
    def __init__(self, name: str):
            self.name = name
    
    def get_name(self):
        pass


class UserDB:
    def get_user(self, id) -> User:
        pass

    def save(self, user: User):
        pass
```

***

* **Open-Closed Principle** (принцип открытости/закрытости):

Программные сущности (**классы, модули, функции**) должны быть **открыты для расширения, но не модификации**.

Класс Discount отвечает за предоставление скидки покупателям. Если необходимо удвоить скидку для VIP покупателей, то, исходя из принципа открытости/закрытости, необходимо написать класс VIPDiscount, который делает это расширяя, но не изменяя класс Discount. 

```python
class Discount:
    def __init__(self, customer, price):
      self.customer = customer
      self.price = price
      
    def get_discount(self):
      return self.price * 0.2


class VIPDiscount(Discount):
    def get_discount(self):
      return super().get_discount() * 2
```

***

* **Liskov Substitution Principle** (принцип подстановки Лисков):

Данный принцип соответствует одному из базовых принципов ООП — **полиморфизму**.

Клиент должен иметь возможность использовать любой подкласс базового класса, не замечая разницы между ними, и следовательно, без каких-либо изменений поведения программы при выполнении. Это означает, что **клиент полностью изолирован и не подозревает об изменениях в иерархии классов**.

Проще говоря, это значит, что подкласс должен соответствовать родительскому классу или супер классу.

```python
class User():
  def __init__(self, color, board):
    create_pieces()
    self.color = color
    self.board = board
    
  def move(self, piece:Piece, position:int):
      piece.move(position)
      chessmate_check()
      
      
  board = ChessBoard()
  user_white = User("white", board)
  user_black = User("black", board)
  pieces = user_white.pieces
  horse = helper.get_horse(user_white, 1)
  user.move(horse)
```

***

* **Interface Segregation Principle** (принцип разделения интерфейсов):

**Клиенты не должны зависеть от интерфейсов, которые они не используют**. Этот принцип устраняет недостатки реализации больших интерфейсов. 

Таким образом, единая реализация для всех общих методов между интерфейсами приведет к меньшей зависимости и более легкому тестированию.

```python
class IShape:
    def draw(self):
        raise NotImplementedError


class Circle(IShape):
    def draw(self):
        pass


class Square(IShape):
    def draw(self):
        pass


class Rectangle(IShape):
    def draw(self):
        pass
```

***

* **Dependecy Inversion Principle** (принцип инверсии зависимостей):

**Зависимость должна быть от абстракций, а не от конкретики**. Модули верхних уровней не должны зависеть от модулей нижних уровней. Классы и верхних, и нижних уровней должны зависеть от одних и тех же абстракций. Абстракции не должны зависеть от деталей. Детали должны зависеть от абстракций.

```python
class AuthenticationForUser():
  def __init__(self, connector:Connector):
		self.connection = connector.connect()
	
	def authenticate(self, credentials):
		pass
    
	def is_authenticated(self):
		pass	
    
	def last_login(self):
		pass


class AnonymousAuth(AuthenticationForUser):
	pass


class GithubAuth(AuthenticationForUser):
	def last_login(self):
		pass


class FacebookAuth(AuthenticationForUser):
	pass


class Permissions()
	def __init__(self, auth: AuthenticationForUser)
		self.auth = auth
		
	def has_permissions():
		pass
		
    
class IsLoggedInPermissions (Permissions):
	def last_login():
		return auth.last_log
```

***

* Парадигмы ООП:

1. Парадигма наследования - позволяет создавать сложные системы классов, избежать дублирования кода, упростить поддержку программ и многое другое.

```python
class A:
    def some_function(self):
        print("First function")
        
    def other_function(self):
        print("Second function")


class B:    
    def method_in_B(self):
        print("Third function")


class C(A):    
    def other_function(self):
        print("Replaced function")


class D(B, C):
    pass


d = D()
d.method_in_B()
d.some_function()
d.other_function()
```

2. Парадигма инкапсуляции - предлагает объединять переменные и методы, относящиеся к одному объекту в единый компонент. По сути соблюдение парадигмы инкапсуляции и заключается в создании классов.

3. Парадигма полиморфизма - позволяет вместо объекта базового типа использовать его потомка, при этом не указывая это явно. 

```python
class Parent:  
    def some_method(self):
        print("This is Parent object")


class Child1(Parent):  
    def some_method(self):
        print("This is Child1 object")


class Child2(Parent):  
    def some_method(self):
        print("This is Child2 object")
        
        
def who_am_i(obj):
    obj.some_method()


p = Parent()
c1 = Child1()
c2 = Child2()

who_am_i(p)
who_am_i(c1)
who_am_i(c2)
```
***
