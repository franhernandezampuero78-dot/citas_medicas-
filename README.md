# Sistema Kawsay

Prototipo académico de consola para representar pacientes, médicos, citas y
atenciones médicas mediante programación estructurada, orientada a objetos y
funcional. Proyecto del Equipo 8 para el curso de Lenguajes de Programación de
la Universidad Privada del Norte (UPN).

Utiliza datos de ejemplo y no está destinado a la atención clínica real.

## Requisitos y ejecución

- Python 3.6 o posterior.
- No requiere instalar librerías externas.

Desde la carpeta del proyecto, ejecutar:

```bash
python main.py
```

## Qué hace el programa

La ejecución sigue una secuencia de demostración:

1. Crea una clínica y carga un paciente (`P001`), un médico (`M001`) y una cita
   (`C001`). Muestra sus resúmenes.
2. Registra una atención de ejemplo (`A001`) vinculada a la cita.
3. Solicita el código de un paciente. Si existe, muestra sus datos y sus
   atenciones; si no existe, informa que no se encontró.
4. Muestra el historial completo, las citas del médico `M001` y el resumen de
   cantidades de la clínica.

La entrada del código elimina espacios exteriores y convierte el texto a
mayúsculas. Por ejemplo, `p001` se interpreta como `P001`.

El resumen final con los datos precargados es:

```text
Pacientes: 1 | Médicos: 1 | Citas: 1 | Atenciones: 1
```

## Archivos del proyecto

| Archivo | Responsabilidad |
| --- | --- |
| `paciente.py` | Define `Paciente`, con código, nombre, edad y un resumen. |
| `medico.py` | Define `Medico`, con código, nombre, especialidad y un resumen. |
| `cita.py` | Define `Cita`, que relaciona un paciente y un médico con una fecha. |
| `atencion.py` | Define `Atencion`, vinculada a una cita, con diagnóstico y tratamiento. |
| `clinica.py` | Almacena los objetos en listas y ofrece registros, búsquedas, historial y resumen. |
| `main.py` | Crea los datos de ejemplo y ejecuta la demostración por consola. |

## Paradigmas aplicados

- **Estructurado:** secuencia de instrucciones, condicionales y ciclos `for` para
  buscar pacientes y mostrar resultados.
- **Orientado a objetos:** cinco clases con constructores, propiedades
  (`@property`), setters y métodos. Las citas y atenciones guardan referencias
  a otros objetos.
- **Funcional:** `filter()` y `lambda` seleccionan citas por código de médico y
  atenciones por código de paciente, devolviendo listas nuevas sin modificar
  las colecciones originales.

## Comprobación manual

Ejecutar el programa una vez por cada caso:

| Entrada al solicitar el paciente | Resultado |
| --- | --- |
| `P001` | Muestra el paciente y su atención `A001`. |
| `p001` | Encuentra el mismo paciente al convertir el código a mayúsculas. |
| `P999` | Muestra «No existe un paciente con ese código.». |

En los tres casos, el programa continúa mostrando el historial completo, las
citas de `M001` y el resumen de la clínica.

## Alcance y limitaciones actuales

- Los registros se precargan en el código. No hay menú para registrar nuevos
  pacientes, médicos, citas o atenciones desde la consola.
- Los métodos de registro agregan objetos a listas sin validar códigos
  duplicados, edades ni referencias previamente registradas.
- La especialidad se almacena como atributo; no hay búsqueda por especialidad.
- La fecha se conserva como texto, sin validación de calendario ni de horarios.
- Los atributos con guion bajo siguen una convención de uso interno; las
  propiedades y setters no incorporan validaciones.
- Los datos solo viven en memoria y se pierden al finalizar la ejecución.
- El repositorio no incluye pruebas automatizadas ni dependencias externas.
