## Develop Environment

### requeriments.txt

Para generar nuestro archivo de dependencias, empleamos el siguiente comando:

```sh
pipenv lock -r > requirements.txt
```

## Stage Environment

La posibilidad de contar con un entorno de pruebas o stage es de gran utilidad antes de realizar cambios a un entorno de producción. En este caso, emplearemos Heroku como SaaS para poder probar nuestra applicación

### Redirect SSL

En la seccion _Help_ de Heroku podemos encontrar una referencia al protocolo SSL y como podemos forzar la redirección por el protocolo seguro a la hora de interactuar con nuestra applicación.

[Can Heroku force an application to use SSL/TLS?](https://help.heroku.com/J2R1S4T8/can-heroku-force-an-application-to-use-ssl-tls)

### Pre-commit

**pre-commit** es un framework para gestion y mantenimiento de hooks de pre-commit multilenguaje, es decir, nos permite ejecutar herramientas para controlar ciertas reglas de complice a nuestro código al realizar un commit. Si nuestro código cumple con estas reglas de complice, el commit será ejecutado exitosamente; caso contrario, nuestro commit fallará.

Algunas referencias útiles a la hora de su configuración:

- [Tool Your Django Project: Pre-Commit Hooks](https://codeburst.io/tool-your-django-project-pre-commit-hooks-e1799d84551f)
- [Raise the Bar of Code Quality in Python Projects](https://levelup.gitconnected.com/raise-the-bar-of-code-quality-in-python-projects-7c49743f004f)

#### isort

**isort** es una herramienta que nos permite ordenar nuestras importaciones, la cual añadimos a la consifuración de pre-commit para hacerlo automaticamente.

Algunas referencias útiles a la hora de su configuración:

- [isort and pre-commit - a friendship with obstacles](https://jugmac00.github.io/blog/isort-and-pre-commit-a-friendship-with-obstacles/)
- [isort home](https://pycqa.github.io/isort/)

#### bandit

**bandit** es una herramienta diseñada para encontrar problemas de seguridad comunes en código Python, generando un reporte de los problemas encontrados.

La documentación oficial puede encontrarse en:

- [bandit docs](https://bandit.readthedocs.io/en/latest/)

#### pylint

#### black

#### flake8
