# DONT SPEAK
CLI personal assisten(will soon be)

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

**IDEAS**
- button with name like "view my brain"
  - mind-map-like view: button

## Done:
- `add/create <type> <name>` : add entity to database and add link to current, if it exists
- `add/create <type <name> to/in <parent_name>`: add entity to database and add link to parent
