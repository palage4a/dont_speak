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

## TODO:

**Soon**:
- update entities
- interactive adding entity: information about parent is displayed while updating ("editing message in chat"-like)
- entities name suggestions

**Not soon**:
- command suggestions
- persistent storage
- chatbot UI-like (buttons with commands name)

## Done:
- `add/create <type> <name>` : add entity to database and add link to current, if it exists
- `add/create <type <name> to/in <parent_name>`: add entity to database and add link to parent
