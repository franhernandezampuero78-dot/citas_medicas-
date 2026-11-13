class Clinica:
    def __init__(self):
        self._pacientes = []
        self._medicos = []
        self._citas = []
        self._historial_atenciones = []   # historial de atenciones

    #getters
    @property
    def pacientes(self):
        return self._pacientes

    @property
    def medicos(self):
        return self._medicos

    @property
    def citas(self):
        return self._citas

    @property
    def historial_atenciones(self):
        return self._historial_atenciones

    #setters
    @pacientes.setter
    def pacientes(self, valor):
        self._pacientes = valor

    @medicos.setter
    def medicos(self, valor):
        self._medicos = valor

    @citas.setter
    def citas(self, valor):
        self._citas = valor

    @historial_atenciones.setter
    def historial_atenciones(self, valor):
        self._historial_atenciones = valor

    # ---------- Agregar ----------
    def agregar_paciente(self, paciente):
        self._pacientes.append(paciente)

    def agregar_medico(self, medico):
        self._medicos.append(medico)

    def agregar_cita(self, cita):
        self._citas.append(cita)

    def registrar_atencion(self, atencion):
        self._historial_atenciones.append(atencion)

    # ---------- Búsquedas ----------
    def buscar_paciente(self, codigo):
        """Busca un paciente por código usando un for."""
        for paciente in self._pacientes:
            if paciente.codigo == codigo:
                return paciente
        return None

    def citas_por_medico(self, codigo_medico):
        """Devuelve las citas de un médico usando filter()."""
        return list(filter(lambda cita: cita.medico.codigo == codigo_medico,
                           self._citas))

    def historial_por_paciente(self, codigo_paciente):
        """Devuelve las atenciones de un paciente usando filter()."""
        return list(filter(lambda atencion: atencion.cita.paciente.codigo == codigo_paciente,
                           self._historial_atenciones))

    # ---------- Mostrar ----------
    def mostrar_historial(self):
        if len(self._historial_atenciones) == 0:
            print("Aún no hay atenciones registradas.")
        else:
            for atencion in self._historial_atenciones:
                print(atencion.resumen())

    def resumen(self):
        return (f"Pacientes: {len(self._pacientes)} | "
                f"Médicos: {len(self._medicos)} | Citas: {len(self._citas)} | "
                f"Atenciones: {len(self._historial_atenciones)}")