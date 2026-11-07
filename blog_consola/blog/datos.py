perfil_autor = {
    "nombre": "Carl Johnson",
    "bio": "Periodista y diseñador de videojuegos",
    "especialidad": "Videojuegos",
    "redes sociales": ["@cj_gstreet", "@c.johnson"]
}

estados_post = ("borrador", "publicado", "archivado")

etiquetas_blog = {"Videojuegos", "Nintendo", "Sony", "RPG", "Sony", "Shooter"}
posts = [
    {
        "id" : 1,
        "titulo" : "The Legend of Zelda: Ocarina of Time Remake, ¿que cambios planea Nintendo?",
        "autor" : perfil_autor,
        "tags" : ["Videojuegos", "Nintendo", "RPG"],
        "contenido" : "En el siguiente post se detallan los cambios planeados por Nintendo",
        "estado" : "publicado"

    },
    {
        "id" : 2,
        "titulo" : "Doctrine, el neo-vampiro de Overwatch",
        "autor" : perfil_autor,
        "tags" : ["Videojuegos", "Shooter", "Blizzard"],
        "contenido" : "Una de las sorpresas que nos dieron en la BlizzCon 2026 es la revelación de un nuevo personaje",
        "estado" : "borrador"
    },
    {
        "id" : 3,
        "titulo" : "GOTY 2026: GTA VI se suma a la competencia sobre la hora",
        "autor" : perfil_autor,
        "tags" : ["Videojuegos", "Sony", "GOTY","RPG"],
        "contenido" : "Se anunciaron los participantes del proximo evento que celebra los Game of The Year, con la sorpresa de que el GTA VI estará presente",
        "estado" : "archivado"
    },
    {
            "id" : 4,
            "titulo" : " ",
            "autor" : perfil_autor,
            "tags" : ["@"],
            "contenido" : "",
            "estado" : "en creacion"
        },

]