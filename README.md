django-project-template
=======================

My reusable django project template

Creating a project
------------------

```bash
$ mkdir myproject.com && cd myproject.com/
$ django-admin.py startproject --template=https://github.com/h3/django-project-template/archive/v1.0.0.zip --extension=wsgi,py,md myproject
```

With django-duke-client
-----------------------

Edit the `buildout.cfg` file:


```ini
[django]
template=https://github.com/h3/django-project-template/archive/v1.0.0.zip
```

Then:

```bash
$ buildout
```
