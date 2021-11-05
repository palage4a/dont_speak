# VERY WIP "DONT SPEAK"
Командный интерфейс для персонального помощника  
~~CLI personal assisten(will soon be)

## Как будет работать
--

## Сущности
See `entities.py` for more.
- `Calendar` - календарь с датами и временем.
- `Tasks` - задачи, могут быть вложенные (иметь подзадачи)
  Задачи имеют:
  - Название
  - Описание
  - Время создание
  - Список напоминание
  - Список заметок
- `Reminders` - напоминания
- `Notes` - заметки

## Возможные команды
- `выбрать задачу "ключевые слова для поиска"`: скрытая команда, не должна использоваться явно
- `создать задачу "название задачи"`: создается задача в общем списке и выбрать ее
- `добавить заметку "текст заметки":` в последнюю задачу с которой было взаимодействие добавляется заметка. Если было указаны ключевые слова для поиска: то в задачу, которая нашлась по ключевым словам. 
- `создать подзадачу "название подзадачи"`: создает подзадачу


# TODO:
- DSL
  - examples:
    ```bash
    > `create task`
    1) With name?
    2) With description?
    3) With deadline?
    ...) With <property-name>?
    > 1
    Input name: test
    1) With description?
    2) With deadline?
    ...) With <property-name>?
    ... and so on
    ```
- JS GUI for MVP
  - check [ D3 lib ](https://github.com/d3/d3) for mind-map UI
    - note: useless [ zoom ](https://observablehq.com/@d3/smooth-zooming) in D3

## ROADMAP:
**Soon**:
- update entities
- interactive adding entity: information about parent is displayed while updating ("editing message in chat"-like)
- entities name suggestions

**Not soon**:
- command suggestions
- persistent storage
- chatbot UI-like (buttons with commands name)
- Mobile App

**Ideas**
- button with name like "view my brain"
  - mind-map-like view: button

~~**Done**~~:  
- `add/create <type> <name>` : add entity to database and add link to current, if it exists
- `add/create <type <name> to/in <parent_name>`: add entity to database and add link to parent

# Какие проблемы я хочу решить для себя?
1. быстрый поиск заметок и задач
  - **Пример**: `read about bread` выдает список существующих заметок или задач в виде вырезок из текста отсортированных по количество встреч этого слова либо по "важности" места в котором встретилось слово.  
  Если у сущности название содержит слово "bread", то в результатах оно выше чем у сущностей, которые содержат это слово в других местах, то в результатах оно выше чем у сущностей, которые содержат это слово в других местах.
  ```bash
  $ > read about bread
  ---
  1) Task "Buy bread?" <info about task>
  ---
  2) Note "How about eat?"
    ...
    sfas fdasfa fasdf sf asdfa sfadsfafs
    sfas BREAD fasdf sf asdfa sfadsfafs
    sfas fdasfa fasdf sf asdfa sfadsfafs
    ...
    fdaf fdasf fdasfdaf
    asdf adsfad fdsfd BREAD dafa fdasfasd 
    fdaf fdasf fdasfdaf
    ---
  3) Note "Yeah!"
    ... sfas fdasfa fasdf sf asdfa sfadsfafs
    asdf adsfad fdsfd BREAD dafa fdasfasd 
    fdaf fdasf fdasfdaf ...
   ---
   Need more about ...?
  $ > 2
  Note "How about eat?"
    <full text of note>
  ```
2. быстрое создание заметок, задач и напоминания из любого состояния
 - **Пример**: `remind about bread at 16:30` предлагает список задач, которые содержат с себе слово "bread" c сортировкой:
   1. **задачи**, в название которых встречается слово
   2. **задачи**, в описание(первая заметка) которых встречается слово
   3. **задачи** , в остальных заметках которых встречается слово
   4. **заметки**, в название которых встречается слово
   5. **заметки**, в тексте которых встречается слово
   > количество "встреч" слова так же влияет на сортировку
   ```bash
   $ > remind about "bread" at "16:30"
   ---
   1) Task "buy bread":
        Desc: "fasdlkfj f fadsfd
              kalsdjf lk fdf asdf"
   ---
   2) Task "Buy all of this":
        Desc: "Bread Lemon Pen"
   ---
   3) Task "Be happy":
        Desc: "Very important task"
        Note at 10.10.21:
          ".... fdsalkfjalfkj lkjdsaf lkjadslkf jaslkdfj
          fdlakfjlka BREAD dfabfhafakjfdkl
          asdfadfalksfjdlj asdfjlsk fladsj fl... "
   $ > 1
   Remind you about "buy bread" at "16:30".
   ```

   ```bash
   $ > need buy bread
   Task "buy bread" created!
   ```

3. удобные напоминания (требует уточнения) - **???**
4. командный режим как `Ctrl-Shift-P` в **VScode**

## Функционал(хотелки)
- Состояние: прыгаем по задачам как по директориям:
  - создаем сущность, находясь в какой-то задаче: создается сущность внутри этой задачи;
  - принудительно можем указать задачу, в которой хотим создать сущность
- Нечеткий поиск и автокомплит:
  - предлагать варианты сущностей, если не удалось найти четкое совпадение
  - предлагать варианты пути: предложить добавить напоминание или допольнительно указать описание задачи
- Задание обязательных полей для задач или алгоритма создания задачи:
  - предлагать варианты добавления информации
- Коротко и ясно:
  - минимальное возможно количество взаимодействий, варианты:
    - голос
    - свайп-way (Drag-n-drop)

## Примеры интерфейса:
```bash
$ > need "buy bread"
Task "buy bread" created!
Need to be remind about "buy bread" at ...? [<datetime>/n]
$ > 16:30
Remind you about "buy bread" at "16:30".
$ Task "buy bread" >
```

```bash
$ > need "buy bread" at "16:30"
Task "buy bread" created!
Remind you at "16:30".
$ Task "buy bread" > _
```

```bash
$ > note about "bread": "need 2"
Found several suitable options:
1) Task "buy bread";
2) Task "buy all this things";
...
n) Task "be happy";
Do you want to see the options in more detail or have you decided?
<numbers of options> - for more
<one number of varian> - choose
$ > 1,2
---
1) Task "buy bread";
    Desc: <text of description>
    Notes:
    <datetime of note>: <text of note>
    ---
    <datetime of note>: <text of note>
    ---
    <datetime of note>: <text of note>
    <more notes>
---
2) Task "buy all this things";
    Desc: <text of description>
    Notes:
    <datetime of note>: <text of note>
    ---
    <datetime of note>: <text of note>
    ---
    <datetime of note>: <text of note>
    <more notes>
---
Give me a number or return to more options?
r - for return
<number> - choose
$ > 2
Note about "buy all this things" added!
$ Task "buy all this things" > _
```
```bash
$ > note about "bread"
Write your note:
$ > <text of note>
Got it! Found several suitable options:
1) Task "buy bread";
2) Task "buy all this things";
...
n) Task "be happy";
Do you want to see the options in more detail or have you decided?
<numbers of options> - for more
<one number of varian> - choose
$ > 2
Note about "buy all this things" added!
$ Task "buy all this things" > _
```
```bash
$ Task "buy all things" > note about "buy bread": "this different"
Note about "buy bread" added!
$ Task "buy bread" >
```

## Example of use:

> need buy bread at 16:30
create task "buy bread" with reminder with tag "deadline" at "16:30"

> need to buy bread tomorrow

create task "buy bread" with date "tommorrow"

> remind about bread at 16:15

if we have task with 'bread' word:
  - suggest variants notes/task with 'bread' word
  - add reminder to "buy bread" task with remind time "16:15"
else:
  - suggest add task about bread

> need buy pen at 16:13 and remind at 16:10

create task "buy pen" with reminder with tag "deadline" at "16:30" and with reminder with no tags at "16:10"

> note about buy pen what we need more power

add note to "buy pen" task with text "we need more power"
