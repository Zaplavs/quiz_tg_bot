quest_dict_1 = [{
      "text": "Какой оператор используется для возведения в степень в Python?",
      "options": ["^", "**", "*", "/"],
      "correct_answer": "**"
    },
    {
      "text": "Какой метод используется для добавления элемента в конец списка?",
      "options": ["add()", "insert()", "append()", "extend()"],
      "correct_answer": "append()"
    },
    {
      "text": "Как создать пустой кортеж в Python?",
      "options": ["()", "[]", "{}", "tuple()"],
      "correct_answer": "()"
    },
    {
      "text": "Какой тип данных является изменяемым в Python?",
      "options": ["int", "str", "tuple", "list"],
      "correct_answer": "list"
    },
    {
      "text": "Какой оператор используется для проверки равенства значений в Python?",
      "options": ["=", "==", "!=", "<>"],
      "correct_answer": "=="
    },
    {
      "text": "Какое ключевое слово используется для определения функции в Python?",
      "options": ["function", "def", "fun", "define"],
      "correct_answer": "def"
    },
    {
      "text": "Какой метод используется для удаления элемента из словаря по ключу?",
      "options": ["remove()", "pop()", "delete()", "discard()"],
      "correct_answer": "pop()"
    },
    {
      "text": "Какой тип данных используется для хранения уникальных элементов?",
      "options": ["list", "tuple", "set", "dict"],
      "correct_answer": "set"
    },
    {
      "text": "Как получить длину строки 'hello' в Python?",
      "options": ["len('hello')", "length('hello')", "size('hello')", "count('hello')"],
      "correct_answer": "len('hello')"
    },
    {
      "text": "Какой оператор используется для логического 'И' в Python?",
      "options": ["&", "&&", "and", "||"],
      "correct_answer": "and"
    }
]

quest_dict_2 = [
    {
      "text": "Какой метод строк возвращает копию строки, в которой все символы приведены к верхнему регистру?",
      "options": ["upper()", "capitalize()", "title()", "swapcase()"],
      "correct_answer": "upper()"
    },
    {
      "text": "С помощью какого ключевого слова начинается блок обработки исключений?",
      "options": ["try", "except", "finally", "with"],
      "correct_answer": "try"
    },
    {
      "text": "Какой цикл используется для итерации по последовательности (например, списку или строке)?",
      "options": ["for", "while", "do-while", "repeat"],
      "correct_answer": "for"
    },
    {
      "text": "Как проверить, присутствует ли ключ 'name' в словаре 'd'?",
      "options": ["'name' in d", "'name' exists in d", "d.has_key('name')", "d.contains('name')"],
      "correct_answer": "'name' in d"
    },
    {
      "text": "Что вернет выражение '5 // 2' в Python 3?",
      "options": ["2.5", "2", "3", "2.0"],
      "correct_answer": "2"
    },
    {
      "text": "Какой из этих типов данных является неупорядоченной коллекцией?",
      "options": ["list", "tuple", "str", "set"],
      "correct_answer": "set"
    },
    {
      "text": "Какой оператор используется для объединения (конкатенации) строк?",
      "options": ["&", "+", "join", "."],
      "correct_answer": "+"
    },
    {
      "text": "Какое ключевое слово используется для выхода из цикла до его нормального завершения?",
      "options": ["break", "continue", "pass", "exit"],
      "correct_answer": "break"
    },
    {
      "text": "Какой метод используется для удаления последнего элемента из списка и его возврата?",
      "options": ["remove()", "pop()", "delete()", "discard()"],
      "correct_answer": "pop()"
    },
    {
      "text": "Как импортировать модуль 'math' в Python?",
      "options": ["import math", "include math", "require math", "using math"],
      "correct_answer": "import math"
    }
]

quest_dict_3 = [
    {
      "text": "Какой тип данных имеет `args` в определении функции `def func(*args):`?",
      "options": ["list", "tuple", "set", "dict"],
      "correct_answer": "tuple"
    },
    {
      "text": "Какой срез `s[...]` вернет строку `s` в обратном порядке?",
      "options": ["[:-1]", "[1:]", "[::-1]", "[-1:]"],
      "correct_answer": "[::-1]"
    },
    {
      "text": "Какой 'магический' метод является конструктором объекта класса?",
      "options": ["__new__", "__init__", "__del__", "__create__"],
      "correct_answer": "__init__"
    },
    {
      "text": "Что создает выражение `(x*x for x in range(5))`?",
      "options": ["Список", "Кортеж", "Множество", "Генератор"],
      "correct_answer": "Генератор"
    },
    {
      "text": "Какой тип данных имеет `kwargs` в определении функции `def func(**kwargs):`?",
      "options": ["list", "tuple", "set", "dict"],
      "correct_answer": "dict"
    },
    {
      "text": "Что возвращает функция `map()` в Python 3?",
      "options": ["list", "tuple", "Итератор", "set"],
      "correct_answer": "Итератор"
    },
    {
      "text": "Какой оператор используется для проверки идентичности объектов (сравнения ID в памяти)?",
      "options": ["==", "is", "eq", "id"],
      "correct_answer": "is"
    },
    {
      "text": "Какое ключевое слово используется в функции для создания генератора?",
      "options": ["return", "generate", "yield", "next"],
      "correct_answer": "yield"
    },
    {
      "text": "Что гарантирует использование `with open(...)` при работе с файлом?",
      "options": ["Скорость", "Авто-закрытие", "Защиту от записи", "Кодировку"],
      "correct_answer": "Авто-закрытие"
    },
    {
      "text": "Каким будет результат `set([1, 2, 2, 3, 1])`?",
      "options": ["{1, 2, 2, 3, 1}", "[1, 2, 3]", "{1, 2, 3}", "(1, 2, 3)"],
      "correct_answer": "{1, 2, 3}"
    }
]

quest_dict_4 = [
    {
      "text": "Что является метаклассом по умолчанию в Python 3?",
      "options": ["object", "type", "class", "metaclass"],
      "correct_answer": "type"
    },
    {
      "text": "Какой из этих 'магических' методов будет вызван только при обращении к несуществующему атрибуту объекта?",
      "options": ["__getattr__", "__get__", "__getattribute__", "__getitem__"],
      "correct_answer": "__getattr__"
    },
    {
    "text": "Какой 'магический' метод используется для получения итератора из объекта?",
    "options": ["__next__", "__iter__", "__getitem__", "__len__"],
    "correct_answer": "__iter__"
    },
    {
      "text": "Какой алгоритм используется для MRO (Method Resolution Order) в Python 3?",
      "options": ["DFS (поиск в глубину)", "BFS (поиск в ширину)", "C3 линеаризация", "Алгоритм Дейкстры"],
      "correct_answer": "C3 линеаризация"
    },
    {
      "text": "Какую пару методов должен реализовать класс для поддержки протокола менеджера контекста (оператора `with`)?",
      "options": ["__enter__ и __exit__", "__open__ и __close__", "__start__ и __stop__", "__init__ и __del__"],
      "correct_answer": "__enter__ и __exit__"
    },
    {
      "text": "Что в многопоточном Python предотвращает одновременное выполнение байт-кода несколькими потоками в CPython?",
      "options": ["Mutex", "Semaphore", "GIL (Global Interpreter Lock)", "Tornado Lock"],
      "correct_answer": "GIL (Global Interpreter Lock)"
    },
    {
      "text": "Какой декоратор из модуля `functools` реализует паттерн 'мемоизация'?",
      "options": ["@lru_cache", "@wraps", "@total_ordering", "@singledispatch"],
      "correct_answer": "@lru_cache"
    },
    {
      "text": "Какая операция является наиболее эффективной для `collections.deque` по сравнению со стандартным `list`?",
      "options": ["Доступ к элементу по индексу", "Сортировка на месте", "Получение среза", "Добавление/удаление с обоих концов"],
      "correct_answer": "Добавление/удаление с обоих концов"
    },
    {
      "text": "Класс, реализующий хотя бы метод `__get__`, является представителем какого паттерна?",
      "options": ["Адаптер", "Прокси", "Дескриптор", "Итератор"],
      "correct_answer": "Дескриптор"
    },
    {
      "text": "Для чего используется синтаксическая конструкция `yield from` в генераторах?",
      "options": ["Для возврата значения", "Для делегирования подгенератору", "Для завершения генератора", "Для обработки исключений"],
      "correct_answer": "Для делегирования подгенератору"
    }
]

quest_dict_5 = [
    {
      "text": "Какой символ используется для однострочных комментариев в Python?",
      "options": ["//", "/* */", "#", "---"],
      "correct_answer": "#"
    },
    {
      "text": "Какой тип данных используется для хранения истинных или ложных значений (True/False)?",
      "options": ["str", "boolean", "int", "bool"],
      "correct_answer": "bool"
    },
    {
      "text": "Какой метод строк преобразует все символы строки в нижний регистр?",
      "options": ["lower()", "casefold()", "lowercase()", "islower()"],
      "correct_answer": "lower()"
    },
    {
      "text": "С помощью какого цикла можно выполнять блок кода до тех пор, пока условие истинно?",
      "options": ["for", "while", "if", "repeat"],
      "correct_answer": "while"
    },
    {
      "text": "Какой оператор используется для получения остатка от деления?",
      "options": ["/", "//", "*", "%"],
      "correct_answer": "%"
    },
    {
      "text": "Какой метод используется для получения количества элементов в списке?",
      "options": ["count()", "size()", "len()", "length()"],
      "correct_answer": "len()"
    },
    {
      "text": "Как правильно создать пустое множество (set)?",
      "options": ["{}", "[]", "set()", "()"],
      "correct_answer": "set()"
    },
    {
      "text": "Какое ключевое слово используется для проверки дополнительных условий после `if`?",
      "options": ["else if", "elseif", "elif", "another"],
      "correct_answer": "elif"
    },
    {
      "text": "Какой метод словаря возвращает список всех его ключей?",
      "options": ["values()", "items()", "keys()", "getkeys()"],
      "correct_answer": "keys()"
    },
    {
      "text": "Какой из этих типов данных является неизменяемым?",
      "options": ["list", "dict", "set", "tuple"],
      "correct_answer": "tuple"
    }
]

quest_dict_6 = [
    {
      "text": "Какой тип данных используется для хранения текста, например 'Hello World'?",
      "options": ["char", "string", "text", "str"],
      "correct_answer": "str"
    },
    {
      "text": "Какой оператор используется для проверки на неравенство?",
      "options": ["<>", "!==", "is not", "!="],
      "correct_answer": "!="
    },
    {
      "text": "Как получить доступ к первому элементу списка `my_list`?",
      "options": ["my_list(1)", "my_list[0]", "my_list.first()", "my_list[1]"],
      "correct_answer": "my_list[0]"
    },
    {
      "text": "Какое ключевое слово используется для выполнения кода, если условие в `if` ложно?",
      "options": ["except", "otherwise", "else", "then"],
      "correct_answer": "else"
    },
    {
      "text": "Какое ключевое слово используется для возврата значения из функции?",
      "options": ["give", "return", "yield", "send"],
      "correct_answer": "return"
    },
    {
      "text": "Какой метод строки удаляет пробелы с начала и конца строки?",
      "options": ["trim()", "cut()", "strip()", "clean()"],
      "correct_answer": "strip()"
    },
    {
      "text": "Что создаст `list(range(4))`?",
      "options": ["[1, 2, 3, 4]", "[0, 1, 2, 3]", "[0, 1, 2, 3, 4]", "4"],
      "correct_answer": "[0, 1, 2, 3]"
    },
    {
      "text": "Какой оператор используется для логического 'ИЛИ'?",
      "options": ["||", "|", "or", "either"],
      "correct_answer": "or"
    },
    {
      "text": "Какой метод используется, чтобы узнать, заканчивается ли строка определенным суффиксом?",
      "options": ["finishwith()", "endswith()", "suffix()", "hastail()"],
      "correct_answer": "endswith()"
    },
    {
      "text": "Как получить значение, связанное с ключом 'age', из словаря `person`?",
      "options": ["person.get('age')", "person.age", "person('age')", "person['age']"],
      "correct_answer": "person['age']"
    }
]

quest_dict_7 = [
    {
      "text": "Какое ключевое слово используется для объявления класса?",
      "options": ["def", "class", "object", "struct"],
      "correct_answer": "class"
    },
    {
      "text": "Как называется процесс создания объекта из класса?",
      "options": ["Определение", "Инициализация", "Создание экземпляра", "Наследование"],
      "correct_answer": "Создание экземпляра"
    },
    {
      "text": "Какой специальный метод используется для инициализации состояния объекта при его создании?",
      "options": ["__main__()", "__start__()", "__init__()", "__new__()"],
      "correct_answer": "__init__()"
    },
    {
      "text": "Что традиционно используется в качестве имени первого параметра в методах экземпляра класса?",
      "options": ["this", "object", "instance", "self"],
      "correct_answer": "self"
    },
    {
      "text": "Как называется функция, которая определена внутри класса?",
      "options": ["Процедура", "Метод", "Подпрограмма", "Атрибут"],
      "correct_answer": "Метод"
    },
    {
      "text": "Как называется переменная, связанная с конкретным экземпляром класса?",
      "options": ["Глобальная переменная", "Атрибут экземпляра", "Статическая переменная", "Классовая переменная"],
      "correct_answer": "Атрибут экземпляра"
    },
    {
      "text": "Какой принцип ООП позволяет классу-потомку перенимать свойства и методы класса-родителя?",
      "options": ["Инкапсуляция", "Полиморфизм", "Абстракция", "Наследование"],
      "correct_answer": "Наследование"
    },
    {
      "text": "Как правильно создать объект `my_car` класса `Car`?",
      "options": ["my_car = new Car", "my_car = Car", "my_car = Car()", "create my_car from Car"],
      "correct_answer": "my_car = Car()"
    },
    {
      "text": "Если у объекта `cat` есть метод `meow()`, как его вызвать?",
      "options": ["cat.meow()", "meow(cat)", "cat->meow()", "call cat.meow"],
      "correct_answer": "cat.meow()"
    },
    {
      "text": "Какой принцип ООП объединяет данные (атрибуты) и методы, которые с ними работают, в одном объекте?",
      "options": ["Наследование", "Инкапсуляция", "Полиморфизм", "Декомпозиция"],
      "correct_answer": "Инкапсуляция"
    }
]

quest_dict_8 = [
    {
      "text": "Как создать пустой словарь в Python?",
      "options": ["[]", "()", "dict[]", "{}"],
      "correct_answer": "{}"
    },
    {
      "text": "Какой оператор используется для умножения?",
      "options": ["x", "**", "*", "^"],
      "correct_answer": "*"
    },
    {
      "text": "Какой метод используется для удаления элемента из списка по его значению?",
      "options": ["pop()", "del", "remove()", "discard()"],
      "correct_answer": "remove()"
    },
    {
      "text": "Какой из этих типов данных является упорядоченной и изменяемой коллекцией?",
      "options": ["tuple", "set", "list", "str"],
      "correct_answer": "list"
    },
    {
      "text": "Какой результат будет у `bool(0)`?",
      "options": ["True", "False", "0", "Ошибка"],
      "correct_answer": "False"
    },
    {
      "text": "Какая функция используется для вывода информации в консоль?",
      "options": ["display()", "log()", "print()", "output()"],
      "correct_answer": "print()"
    },
    {
      "text": "Как получить доступ к последнему элементу списка `my_list`?",
      "options": ["my_list[-1]", "my_list[last]", "my_list[len(my_list)]", "my_list[end]"],
      "correct_answer": "my_list[-1]"
    },
    {
      "text": "Какой оператор используется для проверки, содержится ли значение в списке?",
      "options": ["is in", "contains", "in", "has"],
      "correct_answer": "in"
    },
    {
      "text": "Какой метод строки разбивает ее на список по указанному разделителю?",
      "options": ["split()", "join()", "divide()", "separate()"],
      "correct_answer": "split()"
    },
    {
      "text": "Как преобразовать строку '123' в целое число?",
      "options": ["int('123')", "integer('123')", "str_to_int('123')", "to_int('123')"],
      "correct_answer": "int('123')"
    }
]

quest_dict_9 = [
    {
      "text": "Какой тип данных используется для чисел с плавающей точкой, например 3.14?",
      "options": ["int", "decimal", "float", "number"],
      "correct_answer": "float"
    },
    {
      "text": "Какой метод списка используется для сортировки элементов на месте?",
      "options": ["sort()", "sorted()", "order()", "arrange()"],
      "correct_answer": "sort()"
    },
    {
      "text": "Какой оператор используется для логического 'НЕ'?",
      "options": ["!", "not", "no", "is not"],
      "correct_answer": "not"
    },
    {
      "text": "Как получить количество пар 'ключ-значение' в словаре `d`?",
      "options": ["len(d)", "d.size()", "d.count()", "size(d)"],
      "correct_answer": "len(d)"
    },
    {
      "text": "Какой метод строки проверяет, состоит ли строка только из цифр?",
      "options": ["isnumeric()", "isdigit()", "isdecimal()", "Все варианты верны"],
      "correct_answer": "Все варианты верны"
    },
    {
      "text": "Какое ключевое слово используется для пропуска текущей итерации цикла и перехода к следующей?",
      "options": ["break", "skip", "pass", "continue"],
      "correct_answer": "continue"
    },
    {
      "text": "Что вернет `type([1, 2, 3])`?",
      "options": ["<class 'list'>", "<class 'tuple'>", "<class 'array'>", "<class 'int'>"],
      "correct_answer": "<class 'list'>"
    },
    {
      "text": "Как объединить два списка `a` и `b` в один?",
      "options": ["a.add(b)", "a + b", "a.merge(b)", "a.append(b)"],
      "correct_answer": "a + b"
    },
    {
      "text": "Какая функция используется для получения ввода от пользователя в консоли?",
      "options": ["get()", "input()", "read()", "prompt()"],
      "correct_answer": "input()"
    },
    {
      "text": "Какой метод словаря используется для удаления элемента с возвратом его значения?",
      "options": ["remove()", "delete()", "pop()", "extract()"],
      "correct_answer": "pop()"
    }
]

quest_dict_10 = [
    {
      "text": "Какой метод строки используется для замены одной подстроки на другую?",
      "options": ["change()", "substitute()", "modify()", "replace()"],
      "correct_answer": "replace()"
    },
    {
      "text": "Какой оператор используется для проверки 'больше чем'?",
      "options": [">", ">=", "=>", ">>"],
      "correct_answer": ">"
    },
    {
      "text": "Можно ли изменить элемент в кортеже после его создания?",
      "options": ["Да", "Нет", "Только если это число", "Только если это строка"],
      "correct_answer": "Нет"
    },
    {
      "text": "Какой результат будет у выражения `True or False`?",
      "options": ["True", "False", "None", "Ошибка"],
      "correct_answer": "True"
    },
    {
      "text": "Как добавить пару 'ключ:значение' в существующий словарь `d`?",
      "options": ["d.add('key', 'value')", "d['key'] = 'value'", "d.insert('key', 'value')", "add {'key': 'value'} to d"],
      "correct_answer": "d['key'] = 'value'"
    },
    {
      "text": "Какая функция возвращает абсолютное значение числа?",
      "options": ["absolute()", "abs()", "value()", "positive()"],
      "correct_answer": "abs()"
    },
    {
      "text": "Какое ключевое слово используется в качестве 'заглушки' и ничего не делает?",
      "options": ["continue", "break", "wait", "pass"],
      "correct_answer": "pass"
    },
    {
      "text": "Какой метод используется для объединения элементов списка в одну строку с разделителем?",
      "options": ["concat()", "merge()", "join()", "combine()"],
      "correct_answer": "join()"
    },
    {
    "text": "Что делает оператор `+=`?",
    "options": ["Сложение с присваиванием", "Простое сложение", "Строгое равенство", "Увеличение на 2"],
    "correct_answer": "Сложение с присваиванием"
    },
    {
      "text": "Какой метод строки проверяет, начинается ли она с указанной подстроки?",
      "options": ["startswith()", "beginwith()", "is_prefix()", "has_start()"],
      "correct_answer": "startswith()"
    }
]


QUESTIONS = [
    *quest_dict_1,
    *quest_dict_2,
    *quest_dict_3,
    *quest_dict_4,
    *quest_dict_5,
    *quest_dict_6,
    *quest_dict_7,
    *quest_dict_8,
    *quest_dict_9,
    *quest_dict_10
]