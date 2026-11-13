from paciente import Paciente
from medico import Medico
from cita import Cita
from atencion import Atencion
from clinica import Clinica

# ---------- Crear la clínica ----------
clinica = Clinica()

# ---------- Datos de prueba ----------
paciente_01 = Paciente("P001", "Francisco", 20)
medico_01 = Medico("M001", "Oscar Torres", "Cardiologia")
cita_01 = Cita("C001", paciente_01, medico_01, "04/11/2026")

clinica.agregar_paciente(paciente_01)
clinica.agregar_medico(medico_01)
clinica.agregar_cita(cita_01)

print(paciente_01.resumen())
print(medico_01.resumen())
print(cita_01.resumen())

# ---------- Registrar atención ----------
print("\n--- Registrar atención ---")
atencion_01 = Atencion("A001", cita_01, "Hipertensión leve", "Dieta baja en sal y control en 15 días")
clinica.registrar_atencion(atencion_01)
print("Atención registrada en el historial.")

# ---------- Buscar paciente (for) ----------
print("\n--- Buscar paciente ---")
codigo = input("Ingrese el código del paciente: ").strip().upper()
paciente = clinica.buscar_paciente(codigo)

if paciente is not None:
    print("Paciente encontrado:", paciente.resumen())
    print("Sus atenciones:")
    atenciones = clinica.historial_por_paciente(codigo)   # usa filter()
    if len(atenciones) == 0:
        print("Ese paciente no tiene atenciones registradas.")
    else:
        for atencion in atenciones:
            print(atencion.resumen())
else:
    print("No existe un paciente con ese código.")

# ---------- Historial completo ----------
print("\n--- Historial de atenciones ---")
clinica.mostrar_historial()

# ---------- Citas de un médico (filter) ----------
print("\n--- Citas del médico M001 ---")
for cita in clinica.citas_por_medico("M001"):
    print(cita.resumen())

# ---------- Resumen de la clínica ----------
print("\n--- Resumen de la clínica ---")
print(clinica.resumen())