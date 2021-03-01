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
