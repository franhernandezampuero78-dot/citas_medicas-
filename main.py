from paciente import Paciente
from medico import Medico
from cita import Cita
from atencion import Atencion
from clinica import Clinica


def leer_texto(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("El campo es obligatorio.")


def leer_edad_valida():
    while True:
        try:
            edad = int(input("Edad (0 a 120): "))
        except ValueError:
            print("La edad debe ser un número entero.")
            continue
        if 0 <= edad <= 120:
            return edad
        print("La edad debe estar entre 0 y 120.")


def buscar_medico_codigo(clinica, codigo):
    for medico in clinica.medicos:
        if medico.codigo == codigo.strip().upper():
            return medico
    return None


def buscar_cita_codigo(clinica, codigo):
    for cita in clinica.citas:
        if cita.codigo == codigo.strip().upper():
            return cita
    return None


def medicos_por_especialidad(clinica, especialidad):
    return list(filter(
        lambda medico: medico.especialidad.strip().casefold() == especialidad.strip().casefold(),
        clinica.medicos,
    ))


def mostrar_resultados(registros, mensaje_vacio):
    if not registros:
        print(mensaje_vacio)
    for registro in registros:
        print(registro.resumen())


def crear_clinica_demo():
    clinica = Clinica()
    paciente = Paciente("P001", "Paciente ficticio 1", 20)
    medico = Medico("M001", "Médico ficticio 1", "Cardiologia")
    cita = Cita("C001", paciente, medico, "04/11/2026")
    clinica.agregar_paciente(paciente)
    clinica.agregar_paciente(Paciente("P002", "Paciente ficticio 2", 30))
    clinica.agregar_medico(medico)
    clinica.agregar_cita(cita)
    clinica.registrar_atencion(Atencion(
        "A001", cita, "Diagnóstico ficticio", "Tratamiento ficticio",
    ))
    return clinica


def ejecutar_menu(clinica):
    opciones_menu = {
        "1": "Registrar paciente",
        "2": "Registrar médico",
        "3": "Buscar paciente e historial",
        "4": "Programar cita",
        "5": "Registrar atención",
        "6": "Buscar médicos por especialidad",
        "7": "Consultar citas de un médico",
        "8": "Mostrar historial completo",
        "9": "Mostrar resumen",
        "0": "Salir",
    }
    while True:
        print("\n--- Sistema Kawsay | Solo datos ficticios ---")
        for codigo, descripcion in opciones_menu.items():
            print(f"{codigo}. {descripcion}")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "0":
            print("Fin del programa. Los datos de esta sesión no se conservan.")
            return
        elif opcion == "1":
            codigo = leer_texto("Código del paciente: ").upper()
            nombre = leer_texto("Nombre ficticio: ")
            paciente = Paciente(codigo, nombre, leer_edad_valida())
            if clinica.agregar_paciente(paciente):
                print("Paciente registrado:", paciente.resumen())
        elif opcion == "2":
            codigo = leer_texto("Código del médico: ").upper()
            nombre = leer_texto("Nombre ficticio: ")
            especialidad = leer_texto("Especialidad: ")
            medico = Medico(codigo, nombre, especialidad)
            if clinica.agregar_medico(medico):
                print("Médico registrado:", medico.resumen())
        elif opcion == "3":
            codigo = leer_texto("Código del paciente: ").upper()
            paciente = clinica.buscar_paciente(codigo)
            if paciente is None:
                print("No existe un paciente con ese código.")
                continue
            print("Paciente encontrado:", paciente.resumen())
            mostrar_resultados(clinica.historial_por_paciente(codigo),
                               "Ese paciente no tiene atenciones registradas.")
        elif opcion == "4":
            codigo = leer_texto("Código de la cita: ").upper()
            paciente = clinica.buscar_paciente(leer_texto("Código del paciente: "))
            if paciente is None:
                print("No existe un paciente con ese código.")
                continue
            medico = buscar_medico_codigo(clinica, leer_texto("Código del médico: "))
            if medico is None:
                print("No existe un médico con ese código.")
                continue
            fecha = leer_texto("Fecha (DD/MM/AAAA): ")
            cita = Cita(codigo, paciente, medico, fecha)
            if clinica.agregar_cita(cita):
                print("Cita registrada:", cita.resumen())
        elif opcion == "5":
            codigo = leer_texto("Código de atención: ").upper()
            cita = buscar_cita_codigo(clinica, leer_texto("Código de la cita: "))
            if cita is None:
                print("No existe una cita con ese código.")
                continue
            diagnostico = leer_texto("Diagnóstico ficticio: ")
            tratamiento = leer_texto("Tratamiento ficticio: ")
            atencion = Atencion(codigo, cita, diagnostico, tratamiento)
            if clinica.registrar_atencion(atencion):
                print("Atención registrada:", atencion.resumen())
        elif opcion == "6":
            especialidad = leer_texto("Especialidad: ")
            mostrar_resultados(medicos_por_especialidad(clinica, especialidad),
                               "No hay médicos con esa especialidad.")
        elif opcion == "7":
            codigo = leer_texto("Código del médico: ").upper()
            if buscar_medico_codigo(clinica, codigo) is None:
                print("No existe un médico con ese código.")
                continue
            mostrar_resultados(clinica.citas_por_medico(codigo),
                               "Ese médico no tiene citas registradas.")
        elif opcion == "8":
            clinica.mostrar_historial()
        elif opcion == "9":
            print(clinica.resumen())
        else:
            print("Opción inválida. Seleccione una opción del menú.")


if __name__ == "__main__":
    ejecutar_menu(crear_clinica_demo())
