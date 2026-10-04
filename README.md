# restaurante_app

**Alison Dayana Andrango Nieto**

## Semana 16 - Manejo de eventos en Tkinter

### Descripción

En la Semana 16 se continuó el desarrollo de `restaurante_app`, conservando las funcionalidades implementadas anteriormente y ampliando la sección de gestión de usuarios.

El objetivo principal fue aplicar el manejo de eventos en Tkinter mediante un formulario y una tabla `Treeview`, manteniendo la separación entre la interfaz, los modelos, los servicios y los archivos JSON.

### Evolución del proyecto

La aplicación parte de la versión desarrollada en semanas anteriores, por lo que se conservaron las funcionalidades de:

* Inicio de sesión.
* Navegación entre las diferentes secciones.
* Gestión de productos.
* Registro de ventas.
* Persistencia mediante archivos JSON.

Como parte de la evolución de esta semana, se incorporó la gestión de usuarios mediante un formulario y un `Treeview`, además del manejo de diferentes eventos para mejorar la interacción con la aplicación.

### Gestión de usuarios y roles

La gestión de usuarios permite realizar las operaciones básicas de:

* Registrar usuarios.
* Consultar usuarios mediante una tabla.
* Actualizar usuarios.
* Eliminar usuarios con confirmación.
* Limpiar el formulario.
* Seleccionar el rol del usuario.

Los roles disponibles son:

* Administrador
* Empleado
* Cliente

El usuario con rol **Administrador** puede acceder a la gestión administrativa de usuarios. Los usuarios con rol **Empleado** o **Cliente** no tienen acceso a esta sección.

Desde la pantalla de usuarios, el Administrador puede registrar únicamente usuarios de tipo Empleado o Cliente.

### Manejo de eventos

La aplicación utiliza eventos de Tkinter para responder a diferentes acciones del usuario.

#### `<<TreeviewSelect>>`

Se utiliza `bind()` para detectar cuando se selecciona una fila del `Treeview`.

Al seleccionar un usuario, se obtiene su identificación y se utiliza `RestauranteServicio` para buscar el objeto correspondiente. Luego, sus datos se cargan automáticamente en el formulario.

La tabla muestra:

* Identificación
* Nombre
* Usuario
* Rol

La contraseña no se muestra directamente en la tabla.

#### `<Return>`

Se utiliza como atajo de teclado para registrar un usuario desde el formulario.

El callback asociado al evento reutiliza el método `registrar_usuario()` existente, evitando duplicar la lógica de registro.

#### `<Escape>`

Permite limpiar el formulario y cancelar la selección actual, dejando la interfaz en un estado inicial para realizar una nueva operación.

#### `<<ComboboxSelected>>`

Se utiliza en el `Combobox` del rol para responder al cambio entre las opciones `Cliente` y `Empleado`.

#### `command=`

Los botones principales utilizan `command=` para ejecutar sus respectivas operaciones:

* Registrar
* Actualizar
* Eliminar
* Limpiar

De esta manera, se diferencia el uso de `command=` en los botones y `bind()` para eventos de teclado, selección del `Treeview` y cambios del `Combobox`.

### Callbacks

Los eventos asociados mediante `bind()` ejecutan callbacks que coordinan la respuesta de la interfaz.

Los callbacks reciben la interacción del usuario y reutilizan los métodos existentes, mientras que las validaciones, reglas de negocio y operaciones de persistencia permanecen en `RestauranteServicio`.

### Separación de responsabilidades

La interfaz se encarga de mostrar los componentes, recibir las interacciones del usuario y actualizar la información visual.

El modelo `Usuario` representa los datos del usuario e incorpora el atributo `rol`.

`RestauranteServicio` se encarga de las operaciones de usuarios, las validaciones, las reglas de negocio y la persistencia.

La interfaz no realiza directamente la lectura o escritura de los archivos JSON.

### Persistencia

Los usuarios se almacenan en:

```text
datos/usuarios.json
```

El atributo `rol` también se guarda en este archivo.

Las operaciones de registro, actualización y eliminación utilizan `RestauranteServicio` para guardar los cambios.

### Estructura del proyecto

```text
restaurante_app/
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
├── assets/
└── main.py
```

La carpeta `assets/` contiene los recursos visuales utilizados por la aplicación, como el logotipo y los íconos de los botones.

### Comprobaciones realizadas

Durante las pruebas de la Semana 16 se verificó que:

* La aplicación inicia correctamente.
* El inicio de sesión continúa funcionando.
* Productos y Ventas continúan funcionando.
* El Administrador puede acceder a Usuarios.
* Empleados y Clientes no tienen acceso a la gestión administrativa de usuarios.
* Se pueden registrar usuarios Cliente y Empleado.
* Los usuarios registrados aparecen en el `Treeview`.
* Al seleccionar un usuario, sus datos se cargan en el formulario.
* Se puede actualizar un usuario.
* Se puede eliminar un usuario mediante confirmación.
* La cuenta administrativa actualmente autenticada no puede eliminarse.
* `Enter` permite registrar un usuario.
* `Escape` permite limpiar el formulario y la selección.
* El `Combobox` permite seleccionar el rol.
* Los cambios de usuarios se gestionan mediante `RestauranteServicio`.

### Conclusiones

La implementación de la Semana 16 permitió ampliar `restaurante_app` sin modificar la estructura principal desarrollada en las semanas anteriores. La gestión de usuarios ahora permite realizar las operaciones básicas de registro, consulta, actualización y eliminación, diferenciando los roles de Administrador, Empleado y Cliente.

También se aplicaron eventos de Tkinter mediante `bind()`, como `<<TreeviewSelect>>`, `<Return>`, `<Escape>` y `<<ComboboxSelected>>`, mientras que los botones mantienen el uso de `command=`. De esta manera, la interfaz puede responder a diferentes acciones del usuario sin colocar las reglas de negocio directamente en ella.

Finalmente, las pruebas realizadas permitieron comprobar que las funcionalidades implementadas funcionan junto con el inicio de sesión, los productos y las ventas, manteniendo la persistencia de los usuarios mediante `RestauranteServicio` y `usuarios.json`.

### Ejecución

Para ejecutar la aplicación, se debe abrir el proyecto y ejecutar:

```text
main.py
```

La aplicación inicia mostrando la pantalla de inicio de sesión y, después de validar las credenciales, permite acceder a las opciones correspondientes según el rol del usuario.
