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
  * created reminder form
  * created tasks
  * installed celery and rabbitmq-server
  * created scraping app, models, migrations, views, templates, tasks
  * created Book create, update, delete view and templates
  * updated Book deteil and list view and templates 
  * added cache_page
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
* for create 2000 books, 500 authors, 20 publisher and 20 store:
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
    
    $ ./manage.py loaddata fixtures/db.json
    
```
* for check apps:
```
    
    http://127.0.0.1:8000/library/
    http://127.0.0.1:8000/quote/
    
```
* for start celery:
```
    
    celery -A core worker --loglevel=info
    
```
* for starts the celery beat service:
```
    
    celery -A core beat -l info
    
```
* for start rabbitmq-server:
```
    
    sudo systemctl start rabbitmq-server
    
```
* Quit the server with CONTROL-C.
--------
Project checked by flake8
