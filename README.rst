Catálogo de Láminas
===================

Cátalogo de Láminas Grupak

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django


Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Instalación
-----------

* Instalar Docker - https://www.docker.com/get-started

* Verificar que docker-compose está disponible - https://docs.docker.com/compose/install/

* En Windows desde cmd.exe::

    $ docker-compose --version

* Generar la plataforma de desarrollo local::

    $ docker-compose -f local.yml build

* Iniciar los contenedores de Django y Postgresql::

    $ docker-compose -f local.yml up -d

* Agregar super usuario de administración::

    $ docker-compose -f local.yml run --rm django python manage.py createsuperuser

* Navegar a http://localhost:8000/

* El administrador está en http://localhost:8000/admin

* Adicionalmente, se instaló MySQL 5.7, el cual se puede acceder desde Adminer en: http://127.0.0.1:8080/?server=mysql

Solución de Problemas
^^^^^^^^^^^^^^^^^^^^^

* Para re-generar el Stack de Django hay que hacer::

    $ docker-compose stop
    $ docker-compose down
    $ docker-compose -f local.yml build
    $ docker-compose -f local.yml up

* Ejecutar comandos de Django::

    $ docker-compose -f local.yml run --rm django python manage.py --help

* Acceder al contenedor de Django::

    $ docker-compose -f local.yml run --rm django sh

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Type checks
^^^^^^^^^^^

Running type checks with mypy:

::

  $ mypy catalogo_de_laminas

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ pytest

Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html





Sentry
^^^^^^

Sentry is an error logging aggregator service. You can sign up for a free account at  https://sentry.io/signup/?code=cookiecutter  or download and host it yourself.
The system is setup with reasonable defaults, including 404 logging and integration with the WSGI application.

You must set the DSN url in production.


Deployment
----------

The following details how to deploy this application.



Docker
^^^^^^

See detailed `cookiecutter-django Docker documentation`_.

.. _`cookiecutter-django Docker documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html



