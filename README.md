django-project-template
=======================

My reusable django project template


Creating a project
------------------

```bash
$ django-admin.py startproject --template=https://github.com/h3/django-project-template/archive/v1.0.0.zip --extension=py,md myproject
```

With django-duke-client
-----------------------

Edit the `buildout.cfg` file:


```conf
[django]
template=https://github.com/h3/django-project-template/archive/v1.0.0.zip
```

Then:

```bash
$ buildout
```
