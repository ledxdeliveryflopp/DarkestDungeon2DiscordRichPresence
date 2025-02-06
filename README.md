# Discord Rich Presence for Darkest Dungeon 2


**Интеграция Discord rich presence для игры Darkest Dungeon 2.**
Совместим с DLC - The Binding Blade и режимом Kingdoms

![plot](/static/md/kingdoms_inn.png)

## Требования
Работа проверена Windows 10

## Варианты приложения
1. **dd2DRP_with_console** - приложение в котором видно консоль
2. **dd2DRP_no_console.** - приложение в котором не видно консоль(работает полностью в фоне)

## Как скачать и использовать Exe?
1. Скачайте нужный exe
2. Запустите exe до игры или во время игры в Darkest Dungeon 2
3. Приложение будет обновлять активность каждые 8 секунд
4. При запуске приложения оно будет каждую минуту искать процесс игры и если найдет начнет устанавливать активность через 30 секунд
5. При закрытии Darkest Dungeon 2, приложение закроется через 10 секунд

## Настройки приложения(необязательно)
1. создайте файл settings.json рядом с exe
2. добавьте туда ключ "path" с значение пути к лог файлу Darkest Dungeon 2
```json
{
  "path": "C:\\Users\\<username>\\AppData\\LocalLow\\RedHook\\Darkest Dungeon II\\Player.log"
}
```
>Если не создать файл настроек, то приложение попробует получить имя текущего пользователя и построить путь к логу

## Особенности
1. Главное изображение в Discord ставится в зависимости от режима игры(обычное исповедание или Kingdoms)

**Изображение в режиме исповедания**
![plot](/static/md/main_menu.png)

**Изображение в режиме Kingdoms**
![plot](/static/md/kingdoms_inn.png)

2. При битвах отображается название "расы"(не знаю как правильно назвать) противников(с определенном нюансом) и мини изображение

![plot](/static/md/beastman_kingdoms.png)

![plot](/static/md/kingdoms_kultist.png)

![plot](/static/md/military_battle.png)

3. При передвиженни по локации  отображается название локации и устанавливается мини изображение локации(не для всех локаций)

![plot](/static/md/tundra.png)

## Не баги, а фичи
1. Изображения есть не для всех локаций и врагов
2. Название расы врага изменяется только после убийства врага этой расы(до убийства оно ставится на "В бою с неизвестным врагом" или на предыдущую "расу")
3. Нет названия локаций и врагов из DLC - Inhuman Bondage

## TODO
1. Добавить иконки для врагов и локаций
2. Добавить врагов