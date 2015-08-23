Daemo Forum : Forum for open governance operations of Daemo : the crowdsourcing platform (https://daemo.stanford.edu)

Installation :
 ```
    $ cd daemo-forum
    $ virtualenv venv
    $ source ./venv/bin/activate
    $ pip install -r requirements.txt
    $ python manage.py runserver
    $ gunicorn csp.wsgi (not working currently)
```

You should then be able to open your browser on http://127.0.0.1:8000

Heroku app : https://quiet-dawn-3697.herokuapp.com


This Project is based on Spirit project (https://github.com/nitely/Spirit)
