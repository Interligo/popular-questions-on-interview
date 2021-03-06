### Сборник теоретических вопросов по теории тестирования

***

* О тестировании:

Тестирование программного обеспечения (Software Testing) — проверка соответствия реальных и ожидаемых результатов поведения программы, проводимая на конечном наборе тестов, выбранном определённым образом.

Цель тестирования — проверка соответствия ПО предъявляемым требованиям, обеспечение уверенности в качестве ПО, поиск очевидных ошибок в программном обеспечении, которые должны быть выявлены до того, как их обнаружат пользователи программы.

***

* Что такое пирамида тестирования?

Эталонное распределение количества тестов по категориям - модульное (unit) / интеграционное (acceptance, contract, component, API) / системное (End-to-End). Высокоуровневые тесты сложнее писать и поддерживать, кроме того, часто они дольше выполняются + обычно больше интеграций. Поэтому в пирамиде так мало длинных/сложных сценариев (e2e) и много простых быстрых (unit)

***

* Принципы тестирования:

    1. Тестирование демонстрирует наличие дефектов (Testing shows presence of defects). Тестирование только снижает вероятность наличия дефектов, которые находятся в программном обеспечении, но не гарантирует их отсутствия.

    2. Исчерпывающее тестирование невозможно (Exhaustive testing is impossible). Полное тестирование с использованием всех входных комбинаций данных, результатов и предусловий физически невыполнимо (исключение — тривиальные случаи).

    3. Раннее тестирование (Early testing). Следует начинать тестирование на ранних стадиях жизненного цикла разработки ПО, чтобы найти дефекты как можно раньше.

    4. Скопление дефектов (Defects clustering). Большая часть дефектов находится в ограниченном количестве модулей.

    5. Парадокс пестицида (Pesticide paradox). Если повторять те же тестовые сценарии снова и снова, в какой-то момент этот набор тестов перестанет выявлять новые дефекты.

    6. Тестирование зависит от контекста (Testing is context depending). Тестирование проводится по-разному в зависимости от контекста. Например, программное обеспечение, в котором критически важна безопасность, тестируется иначе, чем новостной портал.

    7. Заблуждение об отсутствии ошибок (Absence-of-errors fallacy). Отсутствие найденных дефектов при тестировании не всегда означает готовность продукта к релизу. Система должна быть удобна пользователю в использовании и удовлетворять его ожиданиям и потребностям.

Таким образом, исчерпывающее тестирование - недостижимо; гарантия отсутствия ошибок - недостижимо; тестирование демонстрирует наличие дефектов, а не их отсутствие; раннее тестирование сохраняет время и деньги (shift-left).

*** 

* Виды тестирования:

Все виды тестирования программного обеспечения, в зависимости от преследуемых целей, можно условно разделить на следующие группы:

1. **Функциональные** - основываются на функциях, выполняемых системой, и могут проводиться на всех уровнях тестирования (имитируют фактическое использование системы, но существует возможность упущения логических ошибок в программном обеспечении и вероятность избыточного тестирования). Иными словами, эти тесты базируются на функциях и особенностях, а также взаимодействии с другими системами, они **рассматривают внешнее поведение системы**.

**Функциональное тестирование** рассматривает заранее указанное поведение и основывается на анализе спецификаций функциональности компонента или системы в целом.

2. **Нефункциональные** тесты необходимы для определения характеристик программного обеспечения, которые могут быть измерены различными величинами. В целом, это тестирование того, **как система работает**. К этой группе относят нагрузочное и стрессовое тестирование, а также тестирование стабильности и надежности.

3. **Связанные с изменениями** - после проведения необходимых изменений, таких как исправление бага/дефекта, программное обеспечение должно быть **перетестировано** для подтверждения того факта, что проблема была действительно решена. 

К этой группе относятся: 

**Дымовое тестирование** (короткий цикл тестов, выполняемый для подтверждения того, что после сборки кода (нового или исправленного) устанавливаемое приложение, стартует и выполняет основные функции); 

**Регрессионное тестирование** (вид тестирования направленный на проверку изменений, сделанных в приложении или окружающей среде (починка дефекта, слияние кода, миграция на другую операционную систему, базу данных, веб сервер или сервер приложения), для подтверждения того факта, что существующая ранее функциональность работает как и прежде); 

Проверка согласованности/исправности (узконаправленное тестирование достаточное для доказательства того, что конкретная функция работает согласно заявленным в спецификации требованиям).

Также процесс тестирования можно поделить на **ручной** (человек руками тыкает на кнопки), **полуавтоматический** (тестировщик запускает тестовые сценарии) и **автоматический** (не предполагает участия человека: тесты должны запускаться автоматически, а не руками).

Кроме того, выделяют тестирование **черного ящика** (тестировщику ничего не известно про то, что внутри), **серого ящика** (известны какие-то детали реализации, но не вся целиком) и **белого ящика** (доступна любая необходимая информация, включая исходный код).

***

* Уровни тестирования:

Тестирование на разных уровнях производится на протяжении всего жизненного цикла разработки и сопровождения программного обеспечения. Уровень тестирования определяет то, над чем производятся тесты: над отдельным модулем, группой модулей или системой, в целом.

1. Компонентное или Модульное тестирование (Component Testing or Unit Testing) - проверяет функциональность и ищет дефекты в частях приложения.

Разница между компонентным и модульным тестированием заключается в том, что в компонентном тестировании в качестве параметров функций используют реальные объекты и драйверы, а в модульном тестировании - конкретные значения.

2. Интеграционное тестирование (Integration Testing) - предназначено для проверки связи между компонентами, а также взаимодействия с различными частями системы (операционной системой, оборудованием либо связи между различными системами).

3. Системное тестирование (System Testing) - предназначено для проверки как функциональных, так и не функциональных требований в системе в целом. При этом выявляются дефекты, такие как неверное использование ресурсов системы, непредусмотренные комбинации данных пользовательского уровня, несовместимость с окружением, непредусмотренные сценарии использования, отсутствующая или неверная функциональность, неудобство использования и т.д. 

4. Приемочное тестирование (Acceptance Testing) - выполняется на основании набора типичных тестовых случаев и сценариев, разработанных на основании требований к данному приложению.

*** 

* Классы эквивалентности:

Это методика тестирования, при которой весь диапазон возможных входных значений делится на группы значений, эквивалентных по воздействию на систему.

***

* Метод граничных значений:

Это методика тестирования, которая направлена на проверку поведения системы на граничных значениях входных данных (границах классов эквивалентности).

***

* Метод попарного тестирования (Pairwise):

Это методика тестирования, основанная на предположении, что большинство дефектов возникает при взаимодействии не более двух факторов. Тестовые наборы, генерируемые при использовании данной методики охватывают все уникальные пары комбинаций факторов, что считается достаточным для обнаружения дефектов.

***

* Наиболее популярные техники составления тестового сценария:

    - классы эквивалентности;

    - граничные значения;

    - pairwise (попарное тестирование);

    - пользовательские сценарии;

    - traceability matrix (матрица трассируемости).

***

* Как создать план тестирования?

    - прочитать бизнесовые и системные требования;
    - выписать из каких компонент состоит система, понять связи между компонентами;
    - определить какие типы запросов будут использоваться для взаимодействия между компонентами;
    - обговорить с аналитиком/дев-лидом какие нефункциональные проверки надо делать;
    - обдумать отказоустойчивость;
    - запланить масштабирование;
    - учесть проверки безопасности;
    - определить процесс релиза продукта/сервиса;
    - понять как работает CI/CD;
    - получить расписание релизов;
    - определить инструменты, которые надо будет использовать при тестировании.

***

* Структуры построения авто-тестов:

    - ААА: Arrange, Action, Assert - подготовка данных, действие с подготовленными данными, проверка результата действия;
    - GWT: Given, When, Then - начальное состояние, триггер (действие пользователя), ожидаемый результат.

***

* Что такое **Test Double** (тестовые дублеры):

Это обозначение для объекта, который заменяет реальный объект в тестовых целях. 

Тестовые дублеры полезны при:

    - низкой скорости выполнения тестов с реальными объектами (работа с базой, файлами, почтовым сервером);
    
    - при необходимости запуска тестов независимо от окружения (например, для запуска на любой машине);
    
    - если система, в которой работает код, не дает возможности/сложно запустить код с определенным входным набором данных.

***

* Виды тестовых дублеров:

1. **Dummy** - это объекты, которые передаются в методы, но на самом деле не используются. В основном, это параметры методов.

2. **Fake** - это объекты, которые имеют внутреннюю реализацию, но обычно она сильно урезанная и их нельзя использовать в готовом коде.

3. **Stubs** - обеспечивают жестко зашитый ответ на вызовы во время тестирования. Также они могут сохранять в себе информацию о вызове (например параметры или количество этих вызовов) - такие иногда называют своим термином Test Spy.

4. **Mocks** - объекты, которые настраиваются (например специфично каждому тесту) и позволяют задать ожидания в виде своего рода спецификации вызовов, которые мы планируем получить. Проверки соответствия ожиданиям проводятся через вызовы к Mock-объекту.

Из всех этих дублеров только Mock работает на верификацию поведения. Остальные, как правило, используются для проверки состояния.

***

* Характеристика хорошего тест-кейса:

    - Корректное название, которое отражает проверяемую "идею";
    - Четкость в формулировании "шагов" и "ожиданий";
    - Атомарность и незасимость от других тест-кейсов;
    - Скорость в исполнении, поскольку тестов, как правило, очень много;
    - Легкость в поддержке или, иными словами, устойчивость к изменениям проверяемого элемента;
    - Проверяет одну "идею", что не исключает множества проверок внутри теста.

***

* Чек-лист покрытия тестами API

    - Минимум один тест с ответом 200 ОК;
    - Проверка работы кэша;
    - Проверка корректности моделей/схем JSON/наличия полей и их типов;
    - Необходимы тесты на проверку бизнес логики (например, проверка "плохих" статусов у пользователей);
    - Необходимы проверки измененного состояния (например, что изменения вносятся в БД);
    - Необходимы проверки на дублирование различных действий (например, дважды вызвать метод);
    - Различные негативные проверки;
    - Тестирование документации.

***

* Тест-дизайн:

Это этап процесса тестирования ПО, на котором проектируются и создаются тестовые случаи (тест-кейсы) в соответствии с определёнными ранее критериями качества и целями тестирования. Соответственно, тест-дизайнер – это сотрудник, в чьи обязанности входит создание набора тестовых случаев, обеспечивающих оптимальное тестовое покрытие приложения.

***

* Техники тест-дизайна:

1. Тестирование Классами Эквивалентности (Equivalence Class Testing) - тестовые данные разбиваются на определенные классы допустимых значений. В рамках каждого класса выполнение теста с любым значением тестовых данных приводит к эквивалентному результату. После определения классов необходимо выполнить хотя бы один тест в каждом классе.

2. Тестирование Граничных Значений (Boundary Value Testing) - эта техника основана на том факте, что одним из самых слабых мест любого программного продукта является область граничных значений. Для начала выбираются диапазоны значений – как правило, это классы эквивалентности. Затем определяются границы диапазонов. На каждую из границ создается 3 тест-кейса: первый проверяет значение границы, второй – значение ниже границы, третий – значение выше границы.

3. Таблица Принятия Решений (Decision Table Testing) - это удобный инструмент для фиксирования требований и описания функциональности приложения. Таблицами очень удобно описывать бизнес-логику приложения, и они могут служить отличной основой для создания тест-кейсов.

4. Тестирование Состояний и Переходов (State-Transition Testing) - система переходит в то или иное состояние в зависимости от того, какие операции над нею выполняются.

5. Метод Парного Тестирования (Pairwise testing) - метод парного тестирования основан на следующей идее: подавляющее большинство багов выявляется тестом, проверяющим либо один параметр, либо сочетание двух. Ошибки, причиной которых явились комбинации трех и более параметров, как правило, значительно менее критичны.

6. Доменный анализ (Domain Analysis Testing) - это техника основана на разбиении диапазона возможных значений переменной (или переменных) на поддиапазоны (или домены), с последующим выбором одного или нескольких значений из каждого домена для тестирования. Во многом доменное тестирование пересекается с известными нам техниками разбиения на классы эквивалентности и анализа граничных значений. Но доменное тестирование не ограничивается перечисленными техниками. Оно включает в себя как анализ зависимостей между переменными, так и поиск тех значений переменных, которые несут в себе большой риск (не только на границах).

7. Сценарий использования (Use Case Testing) - описывает сценарий взаимодействия двух и более участников (как правило – пользователя и системы). Пользователем может выступать как человек, так и другая система. Для тестировщиков Use Case являются отличной базой для формирования тестовых сценариев (тест-кейсов), так как они описывают, в каком контексте должно производиться каждое действие пользователя.

***

* Какие есть QA-метрики?

    - количество тестов (разделение по типам тестов);
    - количество дефектов с PROD по времени;
    - сколько дефектов заводят QA/DEV;
    - результаты по автоматизации с CI/CD.

***

* Что такое WebDriver и зачем он нужен?

WebDriver - это стандартизованный, не зависящий от языка программирования или ОС W3C протокол, который описывает команды и интерфейсы управления браузерами, и команды интроспекции и управления web-страницами.

***

* Chrome DevTools Protocol (CDP):

Протокол управления и интроспекции Blink-based браузеров - Chrome & Chromuim, его используют и утилиты DevTools.

***

* Консоль разработчика в браузере:

    - Elements - загруженная HTML, и все объекты на ней с их xPath;
    - Console - клиентское логирование, ошибки и предупреждения, отладочная информация;
    - Network - обмен со страницей, запросы, ответы, таймлайн.

***

* Что такое Cookie?

Cookie – это сравнительно небольшого размера данные. Сервер передает их на клиент в хедере Set-Cookie, и которые затем хранятся на клиенте и передаются обратно на сервер в каждом запросе в хедере Cookie. Они нужны для хранения state на клиенте - авторизации, настроек и т.п.

***

* Аттрибуты качества:

    - функциональная пригодность;
    - производительность;
    - совместимость;
    - легкость использования;
    - надежность;
    - защищенность;
    - сопровождаемость;
    - переносимость.

***

* Cерьёзность (severity) показывает степень ущерба, который наносится проекту существованием дефекта. Severity выставляется тестировщиком.

Градация Серьезности дефекта (Severity):

1. Блокирующий (S1 – Blocker) - тестирование значительной части функциональности вообще недоступно. Блокирующая ошибка, приводящая приложение в нерабочее состояние, в результате которого дальнейшая работа с тестируемой системой или ее ключевыми функциями становится невозможна.

2. Критический (S2 – Critical) - критическая ошибка, неправильно работающая ключевая бизнес-логика, дыра в системе безопасности, проблема, приведшая к временному падению сервера или приводящая в нерабочее состояние некоторую часть системы, то есть не работает важная часть одной какой-либо функции либо не работает значительная часть, но имеется workaround (обходной путь/другие входные точки), позволяющий продолжить тестирование.

3. Значительный (S3 – Major) - не работает важная часть одной какой-либо функции/бизнес-логики, но при выполнении специфических условий, либо есть workaround, позволяющий продолжить ее тестирование либо не работает не очень значительная часть какой-либо функции. Также относится к дефектам с высокими visibility – обычно не сильно влияющие на функциональность дефекты дизайна, которые, однако, сразу бросаются в глаза.

4. Незначительный (S4 – Minor) - часто ошибки GUI, которые не влияют на функциональность, но портят юзабилити или внешний вид. Также незначительные функциональные дефекты, либо которые воспроизводятся на определенном устройстве.

5. Тривиальный (S5 – Trivial) - почти всегда дефекты на GUI — опечатки в тексте, несоответствие шрифта и оттенка и т.п., либо плохо воспроизводимая ошибка, не касающаяся бизнес-логики, проблема сторонних библиотек или сервисов, проблема, не оказывающая никакого влияния на общее качество продукта.

***

* Срочность (priority) показывает, как быстро дефект должен быть устранён. Priority выставляется менеджером, тимлидом или заказчиком.

Градация Приоритета дефекта (Priority):

1. P1 Высокий (High) - критическая для проекта ошибка. Должна быть исправлена как можно быстрее.

2. P2 Средний (Medium) - не критичная для проекта ошибка, однако требует обязательного решения.

3. P3 Низкий (Low) - наличие данной ошибки не является критичным и не требует срочного решения. Может быть исправлена, когда у команды появится время на ее устранение.

***

* Тестовая документация:

Тест план (Test Plan) — это документ, который описывает весь объем работ по тестированию, начиная с описания объекта, стратегии, расписания, критериев начала и окончания тестирования, до необходимого в процессе работы оборудования, специальных знаний, а также оценки рисков.

* Тест план должен отвечать на следующие вопросы:

Что необходимо протестировать?

Как будет проводиться тестирование?

Когда будет проводиться тестирование?

Критерии начала тестирования.

Критерии окончания тестирования.

* Основные пункты тест плана:

Идентификатор тест плана (Test plan identifier);

Введение (Introduction);

Объект тестирования (Test items);

Функции, которые будут протестированы (Features to be tested;)

Функции, которые не будут протестированы (Features not to be tested);

Тестовые подходы (Approach);

Критерии прохождения тестирования (Item pass/fail criteria);

Критерии приостановления и возобновления тестирования (Suspension criteria and resumption requirements);

Результаты тестирования (Test deliverables);

Задачи тестирования (Testing tasks);

Ресурсы системы (Environmental needs);

Обязанности (Responsibilities);

Роли и ответственность (Staffing and training needs);

Расписание (Schedule);

Оценка рисков (Risks and contingencies);

Согласования (Approvals).

* Чек-лист:

Чек-лист (check list) — это документ, который описывает что должно быть протестировано. Чек-лист может быть абсолютно разного уровня детализации.

Чаще всего чек-лист содержит только действия, без ожидаемого результата. Чек-лист менее формализован.

* Тестовый сценарий:

Тестовый сценарий (test case) — это артефакт, описывающий совокупность шагов, конкретных условий и параметров, необходимых для проверки реализации тестируемой функции или её части.

* Атрибуты тест кейса:

Предусловия (PreConditions) — список действий, которые приводят систему к состоянию пригодному для проведения основной проверки. Либо список условий, выполнение которых говорит о том, что система находится в пригодном для проведения основного теста состояния.

Шаги (Steps) — список действий, переводящих систему из одного состояния в другое, для получения результата, на основании которого можно сделать вывод о удовлетворении реализации, поставленным требованиям.

Ожидаемый результат (Expected result) — что по факту должны получить.

***

* Этапы тестирования:

    1. Анализ продукта;

    2. Работа с требованиями;

    3. Разработка стратегии тестирования и планирование процедур контроля качества;

    4. Создание тестовой документации;

    5. Тестирование прототипа;

    6. Основное тестирование;

    7. Стабилизация;

    8. Эксплуатация.

***

* Quality Assurance VS Quality Control:

QA — обеспечение качества продукта — изучение возможностей по изменению и улучшению процесса разработки, улучшению коммуникаций в команде, где тестирование является только одним из аспектов обеспечения качества. Иными словами, обеспечение качества помогает компаниям соответствовать требованиям, удовлетворять потребностям клиентов и постоянно улучшать свои процессы и процедуры.

QC — контроль качества продукта — анализ результатов тестирования и качества новых версий выпускаемого продукта. Иными словами, суть контроля качества сводится к поиску дефектов и ошибок после создания продукта.

***

* Ошибка VS Дефект:

**Ошибка** - результат ошибки кодирования. 

**Дефект** - это отклонение от требований.

Дефект не обязательно означает, что в коде есть ошибка. Это может быть функция, которая не была реализована, но определена в требованиях программного обеспечения. Не все программные дефекты вызваны ошибками кодирования. Один из распространенных источников дорогостоящих дефектов вызван пробелами в требованиях, например непризнанными требованиями, которые приводят к ошибкам упущения разработчиком программы. Распространенным источником пробелов в требованиях являются нефункциональные требования, такие как тестируемость, масштабируемость, ремонтопригодность, удобство использования, производительность и безопасность.

Эти два термина имеют очень тонкую черту различия. Оба эти сущности являются недостатками, которые должны быть исправлены и, поэтому, иногда, эти термины взаимозаменяемо используются в разных компаниях и командах. 

***

* Verification VS Validation:

Верификация (verification) — это процесс оценки системы, чтобы понять, удовлетворяют ли результаты текущего этапа разработки условиям, которые были сформулированы в его начале.

Валидация (validation) — это определение соответствия разрабатываемого ПО ожиданиям и потребностям пользователя, его требованиям к системе.

***

* Что такое fixtures (фикстуры)?

Фикстуры - это функции, которые вызываются до или после выполнения теста. Они нужны, если тесту нужно выполнить специальную настройку — создать временный файл после теста, удалить временный файл; создать базу данных, удалить базу данных; создать базу данных, написать в нее что-то.

***

* Что такое mock (мок)?

Мок - это специальный объект, который подменяет собой настоящий объект. На любое обращение к методам, к атрибутам он возвращает тоже мок-объект.

```python
from unittest.mock import Mock


class AliveChecker:
    def __init__(self, session, target):
        self.session = session
        self.target = target
        
    def do_check(self):
        try:
            response = self.session.get(url)
        except Exception:  # Bad practices, only as example
            return False
        else:
            return response == 200
            
            
def test_with_mock():
    get_mock = Mock(return_value=200)
    mock_client = Mock()
    mock_client.get = get_mock
    alive_checker = AliveChecker(mock_client, 'test.com')
    assert.alive_checker()
    mock_client.get.assert_called_once_with(url)
```

***

* Что такое flaky тесты?

Нестабильные тесты — одна из основных проблем автоматизированного тестирования.

Известными методами борьбы с нестабильными тестами является:

- необходимо предварительно убедиться в стабильности самого теста сделав N десятков прогонов;
- можно попробовать декомпозировать сами тесты - например, уменьшить количество переходов по страницам;
- необходимо проанализировать статистику, а для этого требуется сервис с репортами, где собирается статистика прогонов;
- тесты нужно помечать как flaky автоматически;
- для целей анализа тесты нужно выполнять в произвольном порядке.

***

* Модуль unittest.

Этот модуль **встроен** в стандартную библиотеку Python. Обладает своими уникальными assert (`self.assertXXX`). Для создания теста требуется написать класс, имя которого должно начинаться с **Test**, и унаследовать его от **unittest.TestCase**.

Фикстуры: методы `setUp` и `tearDown`.

Запуск с помощью команды `python -m unittest test_name`.

```python
import unittest


class TestStat(unittest.TestCase)
    def test_name(self):
        pass


if __name__ == '__main__':
    unittest.main()
```

При наличии нескольких тестовых файлов и соблюдении шаблона наименования test*.py, можно передать имя директории при помощи -s флага и названия папки - `python -m unittest discover -s tests`

![](https://github.com/Interligo/popular-questions-on-python-interview/blob/main/unittest_asserts.jpeg)

***

* Модуль pytest.

Этот модуль необходимо установить перед использованием, поскольку он **не входит** в стандартную библиотеку Python. В нем можно пользоваться обычными **assert** (большой плюс этого модуля), которые выдают подробную информацию об ошибках. Для создания теста необходимо объявить обыкновенную функцию, имя которой начинается с **test_**. 

Фикстуры: `@pytest.fixture`. Фикстуре можно передать параметр **scope**. 

По умолчанию, scope='function', т.е. фикстура будет вызываться на каждую функцию, в которую её передали. 

Можно указать scope='module', и тогда фикстура будет выполняться один раз на модуль. Допустим, вы хотите один раз создать базу данных и не хотите после каждого теста удалять и накатывать все миграции. 

Запуск с помощью команды `python -m pytest`.

```python
import pytest


def test_on_range():
    assert kth_stat(range(10), 3) == 2
```

Ещё следует сказать о параметризации тестов. Хорошей практикой является написания для одного теста большого количества наборов параметров для тестирования.

```python
@pytest.mark.parametrize(
    ('iterable_obj', 'k', 'expected_answer'), [
        ([1, 4, 3], 1, 1),
        (range(10), 3, 2)
    ]
)
def test_on_range(iterable_obj, k, expected_answer):
    assert kth_stat(iterable_obj, k) == expected_answer
```

В pytest есть основной конфигурационный файл `pytest.ini`. В нем можно изменить поведение pytest по умолчанию.

***

* Модуль doctest.

Это модуль в стандартной библиотекн Python, предназначенная для тестирования документации. Как это работает? Doctest ищет в docstrings `>>>`, дальше исполняет их и сравнивает то, что получается.

```python
def kth_stat(iterable_obj, k):
    """Compute k-order stat in iterable
    >>> kth_stat([4, 1, 0], 1)
    0
    >>> kth_stat(renge(100), 10)
    10
    """
    return sorted(iterable_obj[k-1])
```

***

* Кратко о CI/CD:

Непрерывная интеграция (**Continuous Integration, CI**) и непрерывная поставка (**Continuous Delivery, CD**) представляют собой культуру, набор принципов и практик, которые позволяют разработчикам чаще и надежнее развертывать изменения программного обеспечения.

CI/CD — это одна из DevOps-практик. Она также относится и к agile-практикам: автоматизация развертывания позволяет разработчикам сосредоточиться на реализации бизнес-требований, на качестве кода и безопасности.

С технической точки зрения, **цель CI** — обеспечить последовательный и автоматизированный способ сборки, упаковки и тестирования приложений. При налаженном процессе непрерывной интеграции разработчики с большей вероятностью будут делать частые коммиты, что, в свою очередь, будет способствовать улучшению коммуникации и повышению качества программного обеспечения.

Непрерывная поставка начинается там, где заканчивается непрерывная интеграция. Она автоматизирует развертывание приложений в различные окружения: большинство разработчиков работают как с продакшн-окружением, так и со средами разработки и тестирования.

Многие команды, использующие CI/CD-конвейеры в облаках используют контейнеры, такие как Docker, и системы оркестрации, такие как Kubernetes. Контейнеры позволяют стандартизировать упаковку, поставку и упростить масштабирование и уничтожение окружений с непостоянной нагрузкой.

***
