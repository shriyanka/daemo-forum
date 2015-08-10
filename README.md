Daemo Forum : Forum for open governance operations of Daemo : the crowdsourcing platform (https://daemo.stanford.edu)
Installation :    
    $ cd daemo-forum
    $ git checkout daemo_v0.1
    $ virtualenv venv
    $ source ./venv/bin/activate
    $ pip install -r requirements.txt
    $ python manage.py runserver
    or 
    $ gunicorn forum.wsgi -b :8002

You should then be able to open your browser on http://127.0.0.1:8000

This Project is based on Spirit project (https://github.com/nitely/Spirit)
