from ensurepip import version
from unicodedata import name
from setuptools import setup

setup(
    name = "paquetecalculos",
    version = "1.0",
    description = "Paquete de redondeo y potencia",
    author = "Monjardin",
    author_email = "robertomonjardin95@gmail.com",
    url = "github.com/MONYARDIN",
    packages = ["calculos", "calculos.redondeo_potencia"]
)

#Para crear un paquete distribuible debemos de ingresar en la consola el siguiente comando: python setup.py sdist