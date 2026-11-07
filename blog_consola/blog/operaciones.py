from blog import datos

def ver_posts(opcion):
     if opcion == 1:
            print("")
            print("Posts disponibles: ")
            print("")
            for post in datos.posts:
                                         print(f"- {post["titulo"]} | Autor: {post["autor"]["nombre"]}")

def buscar_titulo(opcion):
        if opcion == 2:
                busqueda_titulo = input("Escribe un título: ").lower().strip()
                encontrados = 0
                for post in datos.posts:
                              titulo = post["titulo"].lower()
                
                              if busqueda_titulo in titulo:
                                   print("")
                                   print("Resultados encontrados:")                                   
                                   print(f"- {post["titulo"]} | Autor: {post["autor"]["nombre"]}")
                                   encontrados = encontrados + 1
                                   
                if encontrados == 0:
                             print("No hay resultados disponibles con ese titulo")

def filtrar_tag(opcion):
        if opcion == 3:
                busqueda_tags = input("Escribe un tag: ").lower().strip()
                encontrados = 0                
                for post in datos.posts:
                              for tag in post["tags"]: 
                                   if busqueda_tags == tag.lower():
                                                      print("")
                                                      print("Resultados encontrados:")                                                      
                                                      print(f"- {post["titulo"]} | Autor: {post["autor"]["nombre"]} | Tags: {post["tags"]}")
                                                      encontrados = encontrados + 1                           
                if encontrados == 0:
                               print("No hay resultados disponibles con ese tag")

def salir_sistema(opcion):
        if opcion == 5:
                print("Gracias por visitar nuestro blog. Saludos!")