### Python Design Patterns (шаблоны/паттерны проектирования)

***

Шаблоны проектирования - это распространенный способ решения хорошо известных проблем. 
Традиционно шаблоны проектирования разделены на три основные категории: **порождающие**, **структурные** и **поведенческие**.

В основу шаблонов были положены два принципа:

*1. Программировать нужно для интерфейсов, а не для конкретных реализаций.*

```python
try:
  bird.quack()
except AttributeError:
  self.lol()
```

В этой программе никакой интерфейс для утки не определяется. Но это отличный пример программирования для интерфейса, а не для конкретной реализации. 
С утиной типизацией программа не беспокоится о сущности объекта. Она просто хочет знать, может ли объект делать то, что необходимо. То есть интересуется исключительно интерфейсом. 
Может ли объект крякать? Тогда пусть крякает!

*2. Композицию следует предпочитать наследованию.*

```python
class User(DbObject):
    pass

# Или же можно написать следующую реализацию:

class User:
    _persist_methods = ['get', 'save', 'delete']

    def __init__(self, persister):
        self._persister = persister

    def __getattr__(self, attribute):
        if attribute in self._persist_methods:
            return getattr(self._persister, attribute)
```

Преимущества второго варианта очевидны. Экземпляр persister вводится прямо во время выполнения программы! 
Таким образом, сегодня это может быть реляционная база данных, а завтра что-то другое. Важно лишь, чтобы сохранялся необходимый интерфейс (опять эти надоедливые утки).

***

**Creational Patterns (порождающие шаблоны)**:

Они имеют дело с созданием классов или объектов. Они служат для абстрагирования от специфики классов.

* Abstract Factory (абстрактная фабрика) - позволяет создавать семейства связанных объектов, не привязываясь к конкретным классам создаваемых объектов. 
Каждая конкретная фабрика имеет соответствующую вариацию продукта.

* Builder (строитель) - позволяет создавать сложные объекты пошагово. 
Строитель даёт возможность использовать один и тот же код строительства для получения разных представлений объектов.

* Factory Method (фабричный метод) - определяет общий интерфейс для создания объектов в суперклассе, позволяя подклассам изменять тип создаваемых объектов.

* Prototype (прототип) - позволяет копировать объекты, не вдаваясь в подробности их реализации.

* Singleton (одиночка) - гарантирует, что у класса есть только один экземпляр, и предоставляет к нему глобальную точку доступа.

***

**Structural Patterns (структурные шаблоны)**:

Они объединяют объекты и классы в более крупные структуры, сохраняя при этом гибкость и эффективность этих структур.

* Adapter (адаптер) - позволяет объектам с несовместимыми интерфейсами работать вместе.

* Bridge (мост) - разделяет один или несколько классов на две отдельные иерархии — абстракцию и реализацию, позволяя изменять их независимо друг от друга.

* Composite (компоновщик) - позволяет сгруппировать объекты в древовидную структуру, а затем работать с ними так, как будто это единичный объект.

* Decorator (декоратор) - позволяет динамически добавлять объектам новую функциональность, оборачивая их в полезные «обёртки».

* Facade (фасад) - предоставляет простой интерфейс к сложной системе классов, библиотеке или фреймворку.

* Flyweight (легковес) - позволяет вместить бóльшее количество объектов в отведённую оперативную память. 
Легковес экономит память, разделяя общее состояние объектов между собой, вместо хранения одинаковых данных в каждом объекте.

* Proxy (заместитель) - позволяет подставлять вместо реальных объектов специальные объекты-заменители. 
Эти объекты перехватывают вызовы к оригинальному объекту, позволяя сделать что-то до или после передачи вызова оригиналу.

***

**Behavioural Patterns (поведенческие паттерны)**:

Они имеют дело с алгоритмами в целом и распределением ответственности между взаимодействующими объектами.

* Chain of Responsibility (цепочка обязанностей) - позволяет передавать запросы последовательно по цепочке обработчиков. 
Каждый последующий обработчик решает, может ли он обработать запрос сам и стоит ли передавать запрос дальше по цепи.

* Iterator (итератор) - даёт возможность последовательно обходить элементы составных объектов, не раскрывая их внутреннего представления.

* Memento (снимок) - позволяет делать снимки состояния объектов, не раскрывая подробностей их реализации. 
Затем снимки можно использовать, чтобы восстановить прошлое состояние объектов.

* State (состояние) - позволяет объектам менять поведение в зависимости от своего состояния. Извне создаётся впечатление, что изменился класс объекта.

* Template Method (шаблонный метод) - определяет скелет алгоритма, перекладывая ответственность за некоторые его шаги на подклассы. 
Паттерн позволяет подклассам переопределять шаги алгоритма, не меняя его общей структуры.

* Command (команда) - превращает запросы в объекты, позволяя передавать их как аргументы при вызове методов, ставить запросы в очередь, логировать их, а также поддерживать отмену операций.

* Mediator (посредник) - позволяет уменьшить связанность множества классов между собой, благодаря перемещению этих связей в один класс-посредник.

* Observer (наблюдатель) - создаёт механизм подписки, позволяющий одним объектам следить и реагировать на события, происходящие в других объектах.

* Strategy (стратегия) - определяет семейство схожих алгоритмов и помещает каждый из них в собственный класс, после чего алгоритмы можно взаимозаменять прямо во время исполнения программы.

* Visitor (посетитель) - позволяет создавать новые операции, не меняя классы объектов, над которыми эти операции могут выполняться.

***

> P.S. Более подробно со ВСЕМИ шаблонами можно ознакомиться [здесь](https://refactoring.guru/ru/design-patterns/python). 

***
