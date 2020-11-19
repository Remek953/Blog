# My Blog

## About

Blog application using Django with working tags and comments system. Using the Django admin I can create, update, edit, or delete the content. Posts have categories that can be used to sort them. Each posts have a creation date, author and number of comments. Finally, users are able to leave comments on posts. Added Bootstrap 4 for front end. You can hosted Django image files with amazon web services AWS - S3 but I disabled it in settings.py

## Project setup

Before start the project, you must install libraries for Python and Django. Open Windows Command Line, go to project directory and type:

```sh
pip install -r requirements.txt
```

Run server:
```sh
python manage.py runserver
```

The superuser login and password:
```sh
login: admin
password: admin
```

I have set ALLOWED_HOSTS as follows:
```sh
ALLOWED_HOSTS = ['127.0.0.1:8000',]
```

## Clone

To clone repository, open Windows Command Line and navigate to directory, where you would like to download and type:
```sh
$ git clone https://github.com/Remek953/Blog.git
```

## License

Distributed under the MIT License.