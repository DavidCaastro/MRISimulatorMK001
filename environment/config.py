import json


def cargar_configuracion(entorno):
    with open(f'config_{entorno}.json') as f:
        return json.load(f)


# Uso en entorno de desarrollo
config = cargar_configuracion('dev')

