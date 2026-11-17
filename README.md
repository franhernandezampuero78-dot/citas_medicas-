# Sistema Kawsay — Equipo 8

Prototipo académico de consola para registrar pacientes, médicos, citas y
atenciones con datos ficticios. Combina programación estructurada, orientación
a objetos y consultas funcionales. No es un sistema clínico de uso real.

## Ejecutar

Requiere Python 3. Se verificó con Python 3.13.9 y no necesita paquetes externos.
Desde la carpeta del repositorio:

```powershell
python main.py
```

El menú permite registrar pacientes y médicos, buscar un paciente y su historial,
programar citas, registrar atenciones, buscar médicos por especialidad, consultar
citas por médico y mostrar el historial y el resumen general. La opción `0` sale.

Cada ejecución carga datos ficticios para facilitar la demostración:

| Código | Registro |
| --- | --- |
| P001 | Paciente ficticio con una atención |
| P002 | Paciente ficticio sin atenciones |
| M001 | Médico ficticio de Cardiologia |
| C001 | Cita de P001 con M001 |
| A001 | Atención ficticia de C001 |

## Organización y paradigmas

- `paciente.py`, `medico.py`, `cita.py` y `atencion.py`: clases con atributos,
  propiedades y métodos de resumen; representan las entidades y sus relaciones.
- `clinica.py`: administra las listas, valida los registros y consulta citas e
  historial. Los métodos de registro devuelven `True` al agregar y `False` al
  rechazar, mostrando el motivo.
- `main.py`: funciones, validación de entradas, diccionario de opciones y bucle
  del menú. Importarlo no inicia la interacción.
- `tests/test_kawsay.py`: comprobaciones con `unittest`, incluido el menú completo.

La búsqueda por código de paciente usa `for`. La búsqueda por especialidad y las
consultas de citas e historial usan `filter()` con `lambda`: la función anónima
indica qué objetos conservar; `filter()` produce un iterador y `list()` reúne
los resultados en una lista nueva, sin modificar la colección original.

## Validaciones

- Edad entera entre 0 y 120, incluidos ambos límites. El menú captura
  `ValueError` y vuelve a preguntar ante texto no numérico o valores fuera del rango.
- Códigos obligatorios y únicos dentro de cada tipo de registro. Se eliminan los
  espacios exteriores y se convierten a mayúsculas antes de guardarlos.
- Campos de texto obligatorios en el menú y especialidad obligatoria al registrar
  un médico en la clínica.
- Una cita requiere objetos de paciente y médico ya registrados; una atención
  requiere una cita registrada.
- Las consultas sin coincidencias muestran un mensaje y permiten continuar.
- La especialidad se compara sin distinguir mayúsculas ni espacios exteriores;
  sí distingue tildes: `Cardiologia` y `Cardiología` no son equivalentes.

## Pruebas

Desde la raíz del repositorio:

```powershell
python -B -m unittest discover -s tests -v
```

Las pruebas cubren edades límite e inválidas, duplicados de los cuatro tipos,
referencias inexistentes, campos obligatorios, búsquedas con y sin resultados y
registro completo mediante el menú. No requieren `pytest`.

Para comprobarlo manualmente:

1. Opción `1`: registrar P003 con nombre ficticio; introducir `abc`, `-5`, `150`
   y finalmente `0` como edad. Repetir P003 para comprobar el rechazo de duplicados.
   Registrar otro paciente con edad `120` para comprobar el límite superior.
2. Opción `4`: intentar C002 con P999; luego repetir con P001, M001 y una fecha
   no vacía para crearla. Repetir C002 para comprobar el rechazo.
3. Opción `5`: intentar una atención con C999; después registrar A002 con C002,
   diagnóstico ficticio y tratamiento ficticio.
4. Opción `3`: consultar P001, P002 y P999 para ver historial, lista vacía y
   paciente inexistente.
5. Opción `6`: buscar `Cardiologia` y `Pediatria` para ver coincidencia y lista vacía.
6. Opción `9`: revisar cantidades; opción `0`: salir.

## Limitaciones y trabajo futuro

Los datos se guardan solo en listas en memoria y se pierden al cerrar el programa.
La fecha se solicita como texto no vacío: aún no se valida el calendario ni los
cruces de horarios. No hay autenticación ni almacenamiento clínico seguro; usar
únicamente información ficticia. Las propiedades y listas siguen siendo mutables,
por lo que las validaciones de registro no protegen contra modificaciones directas
posteriores. Se permiten varias atenciones con códigos distintos para una cita.

Como trabajo futuro se propone integrar una base de datos, por ejemplo SQLite,
para conservar los registros e historiales, validar fechas y horarios y desarrollar
una interfaz gráfica.
