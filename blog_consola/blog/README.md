# Mini Blog de Consola
Este proyecto es un blog simple creado con Python.
Permite:
- listar posts guardados;
- buscar posts por título y por tag;
- guardar la información en un archivo de texto.
- validar posteos

## Cómo ejecutar el proyecto
 1- Activar el entorno virtual
 2- Ubicarse en la carpeta "blog_consola"
 3- ejecutar el archivo principal:
    Bash
    python blog/main.py

## Organización del blog
"blog_consola": es la carpeta principal del proyecto
"main.py": es el archivo principal que activa la consola
"blog": es la carpeta que sirve como paquete para contener los modulos integrados al proyecto
"__init__": es un archivo que señala que la carpeta es un paquete
"menu": es el módulo que nuclea las funciones que mostraran las opciones principales del menú para elegir
"operaciones": es el módulo que nuclea las funciones que permiten buscar y filtrar
"validaciones": es el módulo que nuclea las funciones que permiten validar posts