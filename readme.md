# Proyecto final: Castro, Jeremias

Esta Web es un Blog en el cual se pueden cargar imágenes y diferentes atributos, está personalizada para difundir la música Reggae y los diferentes generos asociados.

La misma contiene los requisitos pautados para la entrega del trabajo final:

- Un CRUD completo.
- Una página de inicio, una página con el listado de todas las publicaciones y otra con las publicaciones que realizó el usuario  que está logueado.
- Envío y administración de mensajes.
- NavBar/pages/profile management.
- Buscador por un atributo (intermprete)

Para poder correr este proyecto es necesario tener instalado python 3.11 o superior. 

## Paquetes necesarios para la instalación
Desde la terminal correr el siguiente comando
```bash
pip3 install django
```

## Para poder correr el servidor 
Desde la terminal correr el siguiente comando

```bash
python3 manage.py runserver
```

## Navegacion de la página

El nombre del Blog es Roots Club. 

- Home/ : 
El link de acceso al Home/ se encuentra en el boton "Roots Club", en la barra de navegación, de color amarillo. Tambien desde el boton "Back to main" que se encuentra en el Footer.

- Todas las publicaciones:
Para acceder a todas las publicaciones, pulsar el botón "Eventos" en la barra de navegación o en "listado de eventos" ubicado en el artículo, sobre la parte inferior derecha. No es necesario estar logueado para ver todas las publicaciones de la página.

- Usuario desconocido:
Si el usuario no ha accedido con su contraseña, el menú de opciones está reducido. Solo podrá enviar mensajes a algún usuario registrado, ver todos las publicaciones, visitar el Home/ y la página de About/, realizar una busqueda (por interprete) y acceder o registrarse según corresponda.

- Acceso/Registro:
Para acceder o registrarse se debe ingresar por los botones ubicados en la barra de navegacion.
Una vez que se registró puede acceder a la página con su nombre de usuario y clave. El menú de opciones permitirá realizar más acciones, como crear publicaciones y modificar solo aquellas que publicó, acceder a un listado solamente con las publicaciones que realizó ese usuario, y administrar los mensajes recibidos.
Tambien puede administrar su perfil, agregandole o cambiandole una foto, que se verá en la barra de navegación una vez logueado.
