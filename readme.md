Alumno: Fermin Aldaya
Proyecto final
app: TrabajoYa

superusuario:   user: admin
                password: 12345

todos los usuarios tienen de password: *Coderhouse

Mi proyecto consiste en una pagina web de contrataciones, tanto para empleados que quieren buscar trabajo como para empleadores en publicar su perfil y sus ofertas.

modelos:
    	empleos atributos: Cargo; detalles; ubicacion; sueldo.
    	empleados	"   : nombre; apellido; mail; presentacion; experiencia; estudios.    
        empleador	"   : nombre; apellido; mail; presentacion; profesion; edad; nombreEmpresa.
        avatar      "   : Imagen; id del usuario.
        mensaje     "   : remitente; destinatario; asunto; mensaje; fecha de envio.
        usuario     "   : id; username; password; email; first_name; last_name.

Objetivo funcional: Ser capaz de crear un medio para poder subir tanto curriculums como ofertas de trabajo, ademas de poder visualizar el perfil de los usuario y poder 
                    ponerse en contacto con estos mismos.


Funcionalidad: La apliacion permite cargar datos en la base de datos tanto de empleos como el curriculum de los empleados y las especificaciones de los empleadores, a travez
                de forms especificos para cada modelo. Tambien se puede buscar datos por filtrado en la lista de cada modelo y ampliar los datos en cada pagina. Ademas es posible visualisar el perfil de cada usuario, mostrando los datos de usuario como los formularios que han subido a la web. De esta forma poder recopilar en un perfil todos los datos de un usuario. A su vez cada seccion de tarjetas, cuenta con un boton de contactar para ponerse en contacto con el creador de ya sea trabajo, trabajador o empleado.
