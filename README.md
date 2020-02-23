# Proyecto-API
![FotoPortada](https://raw.githubusercontent.com/bersuan/Proyecto-API/master/input/foto-proyecto.jpg)

Deseamos analizar los mensajes de chat 'públicos' de mi equipo y crear métricas de opinión
de las diferentes personas en tu equipo. El objetivo de este proyecto es analizar las conversaciones de su equipo,
para asegurarse de que estén contentos 😃.

Practicará en este proyecto:

- API (Flask)
- Análisis de sentimiento TextBlob
- Sistemas de recomendación

Para ello crearemos una API con las siguientes caracteristicas:

### 1. Para creación de los usuarios:

  - Creamos una lista de usuarios que seran miembros de nuestros chats y los guardaremos en una coleccion de nuestra base de datos de MongoDB.
  - Creamos un sistema de recomendacion en el cual nos muestra cuales son los usuarios mas parecidos entre si.

### 2. Para la creación de chats y conversaciones:

  - Creamos una serie de chats en los cuales añadiremos a distintos usuarios y crearemos una conversación entre ellos que tambien cargaremos en nuestra base de datos de MongoDB
  
### 3. Comprobacion de resultado:

  - Para comprobar el resultado de nuestra API realicaremos una requests en la cual se podrán obtenes todos los mensajes escrito tanto en un grupo como por un usuario.
  - Por ultimo crearemos un json con todos los sentimientos de los mensajes en el chat de un grupo o de un usuario.
