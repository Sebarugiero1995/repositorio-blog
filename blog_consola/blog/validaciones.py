from . import datos

def validar_post(post):
                errores = []

                if not isinstance(post,dict):
                        return False, "- ERROR: El post no es un diccionario"
                claves_necesarias = ["titulo", "contenido", "autor", "tags","estado"]
                for clave in claves_necesarias:
                        if clave not in post:
                                errores.append(f"- ERROR: {clave} errónea o faltante")
                if "titulo" in post:
                        if not isinstance(post["titulo"], str) or post["titulo"].strip() == "":
                                errores.append("- ERROR: El título no puede estar vacío")
                if "contenido" in post:
                        if not isinstance(post["contenido"], str) or post["contenido"].strip() == "":
                                errores.append("- ERROR: El contenido no puede estar vacío")
                if "autor" not in post:
                        errores.append("- ERROR: Falta el autor")
                else:
                        if not isinstance(post["autor"], dict):
                                errores.append("- ERROR: El autor no es un diccionario")
                        else:
                                if "nombre" not in post["autor"]:
                                        errores.append("- ERROR: El diccionario 'autor' no tiene 'nombre' definido")               
                if "tags" in post and not isinstance(post["tags"], list):
                        errores.append("- ERROR: El tag no es una lista")
                if "estado" in post and post["estado"] not in datos.estados_post:
                        errores.append("- ERROR: El estado asignado es erróneo")
                if len(errores) > 0:
                        mensaje_error = "\n".join(errores)
                        return False, f"\n{mensaje_error}"
                
                return True, "El post es válido"

def opcion_validar_posts(opcion):
        if opcion == 4:
                for i, un_post in enumerate(datos.posts):
                        es_valido, mensaje = validar_post(un_post)
                        print(f"Post {i + 1}: {mensaje}")