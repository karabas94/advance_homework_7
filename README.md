##  Library django project

--------
* Done:
  * created project
  * created the library app
  * created models
  * installed django gedug toolbar
  * database setup
  * created admin models
  * created management command create_users
  * created management command create_library
  * created fixtures in db.json
  * create views and templates
  * used aggregate, annotate, prefetch_related and select_related
--------
**How to start project**
* install all from requirements.txt
* for start project write in terminal:
```
    
    $ python manage.py runserver
    
```
* for creating 100 users write in terminal:
```
    
    $ ./manage.py create_users
    
```
* for create 1000 books, 100 authors, 10 publisher and 10 store:
```
    
    $ ./manage.py create_library
    
```
* for loading fixtures:
  * clear table:
```
    
    $ ./manage.py flush
    
```
  * load fixtures
```
    
    $ ./manage.py loaddata db.json
    
```
* for check apps:
```
    
    http://127.0.0.1:8000/library/
    
```
* Quit the server with CONTROL-C.
--------
Project checked by flake8