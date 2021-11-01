## План занятия:

- От Intellij Idea к Pycharm
- От Gradle к Poetry (+Pyenv) для общей настройки и сборки проекта.
- Базовая структура проекта на Python
- Основы синтаксиса в Python в сравнении с Java: пакеты, модули, импорты, публичность, классы, блоки кода, переменные, типизация, None, функции, лямбды и их ограничения, важность код-стайла в Python, `снейк_кейс`, декораторы, комментарии, условные выражения
- Конвенции Pytest для именования тестов
- От швейцарского ножа Selenide с его лаконизмом в API до Selene как к фреймворку более минималистичному но и заточенному под более высокоуровневый стиль и язык пользователя
- О «Явно лучше неявного» из «Дзен Python»
- Классы и об'єкты в Python. Конструкторы и инициализаторы.
- Введение в фикстуры Pytest для настройки независимости тестов


## Материалы:

Запись последней версии урока в высоком качестве: https://www.loom.com/share/e794d51706f8427eabb2a7ecfc20520e

Исходники:
- Ссылка на детальный «сценарий урока» (на английском): https://github.com/yashaka/from-java-to-python-for-web-ui-tests
- Ссылка на репозиторий изначального кода на Java
https://github.com/autotests-cloud/qa_guru_5_9_jenkins_owner/tree/refactored-by-commits-per-idea
- Ссылка на репозиторий-конспект финального кода первой части урока (конспект = комиты за 15 и 16 Июня 2021)
https://github.com/autotests-cloud/qa_guru_5_9_jenkins_owner/tree/switch-to-python-step-by-step
- Ссылка на репозиторий с кодом в одном комите:
  - код из первого прогона первой части урока https://github.com/autotests-cloud/qa_guru_5_9_jenkins_owner/tree/to-python-part1
  - код из второго прогона первой части урока https://github.com/autotests-cloud/qa_guru_5_9_jenkins_owner/tree/to-python-part1-mark-ii
  - код из второй части урока (на основе кода из первого прогона): https://github.com/autotests-cloud/qa_guru_5_9_jenkins_owner/tree/to-python-part2

Подборка материалов по изучению Python http://autotest.how/python-ru

Другие ссылки упомянутые в уроке:
- Дзен Python: https://www.python.org/dev/peps/pep-0020/
- Стиль Гайд: https://www.python.org/dev/peps/pep-0008/
- Почему синтаксис `new` в Java и других языках ограничивает, 
  а его отсуствие, например в Python – добавляет гибкости?
  - https://medium.com/javascript-scene/why-composition-is-harder-with-classes-c3e627dcd0aa
- Запись в высоком качестве урока по рефакторингу для qa.guru: https://www.loom.com/share/04c2767188714759a095965346a3bd94

Ответы на некоторые частые вопросы:
- Как быстро выучить еще один язык программирования: http://autotest.how/learn-one-more-language-ru
- Что учить что-бы быстро повысить свой уровень, например готовлясь к собеседованию?
  - Лучшие практики, многие из которых неплохо собраны в официально документации Cypress: https://docs.cypress.io/guides/references/best-practices
  - Типы тестов по всем уровням пирамиды: https://martinfowler.com/articles/practical-test-pyramid.html
  - Кодинг базовых алгоритмов: https://leetcode.com/, https://exercism.io, https://codewars.com, и т.д.
  - Основы шаблона PageObject https://martinfowler.com/bliki/PageObject.html
  - Построение фреймворков на примере Selenium Webdriver: https://leanpub.com/selenium-webdriver-book
  - Принципы юнит-тестирования: https://www.amazon.com/gp/product/1617296279
