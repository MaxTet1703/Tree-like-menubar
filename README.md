# Tree-like menubar. Test task for UpTrader
## Description: django app implementing tree-like menu
### Requirements
- Меню реализовано через template tag
-  Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под выделенным пунктом тоже развернут.
- Хранится в БД.
- Редактируется в стандартной админке Django
- Активный пункт меню определяется исходя из URL текущей страницы
- Меню на одной странице может быть несколько. Они определяются по названию.
- При клике на меню происходит переход по заданному в нем URL. URL может быть задан как явным образом, так и через named url.
- На отрисовку каждого меню требуется ровно 1 запрос к БД

### Running and test
Firstly, open terminal in project root directory and create vurtual enviroment
```bash
python -m venv venv
```
Then activate this <br>
on Linux enter
```
source venv/bin/activate
```
on Windows
```
.\venv\Scripts\activate
```
After that, install all dependencies from requrement.txt\

```
pip install -r requrements.txt
```
Do migrate database and back up test dataset
```
python manage.py migrate
python manage.py initialize
```
To check, there is one query to render one menu enter
```
python maange.py test cool_app
```
Note: this project can work correctly with English letters




