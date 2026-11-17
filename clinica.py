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
        codigo = paciente.codigo.strip().upper()
        if not codigo:
            print("El código es obligatorio.")
            return False
        for registrado in self._pacientes:
            if registrado.codigo.strip().upper() == codigo:
                print("Ya existe un registro de paciente con ese código.")
                return False
        if type(paciente.edad) is not int or not 0 <= paciente.edad <= 120:
            print("La edad debe ser un entero entre 0 y 120.")
            return False
        paciente.codigo = codigo
        self._pacientes.append(paciente)
        return True

    def agregar_medico(self, medico):
        codigo = medico.codigo.strip().upper()
        if not codigo:
            print("El código es obligatorio.")
            return False
        for registrado in self._medicos:
            if registrado.codigo.strip().upper() == codigo:
                print("Ya existe un registro de médico con ese código.")
                return False
        if not medico.especialidad.strip():
            print("La especialidad es obligatoria.")
            return False
        medico.codigo = codigo
        self._medicos.append(medico)
        return True

    def agregar_cita(self, cita):
        codigo = cita.codigo.strip().upper()
        if not codigo:
            print("El código es obligatorio.")
            return False
        for registrado in self._citas:
            if registrado.codigo.strip().upper() == codigo:
                print("Ya existe un registro de cita con ese código.")
                return False
        if cita.paciente not in self._pacientes or cita.medico not in self._medicos:
            print("El paciente y el médico deben estar registrados.")
            return False
        cita.codigo = codigo
        self._citas.append(cita)
        return True

    def registrar_atencion(self, atencion):
        codigo = atencion.codigo.strip().upper()
        if not codigo:
            print("El código es obligatorio.")
            return False
        for registrado in self._historial_atenciones:
            if registrado.codigo.strip().upper() == codigo:
                print("Ya existe un registro de atención con ese código.")
                return False
        if atencion.cita not in self._citas:
            print("La cita debe estar registrada.")
            return False
        atencion.codigo = codigo
        self._historial_atenciones.append(atencion)
        return True

    # ---------- Búsquedas ----------
    def buscar_paciente(self, codigo):
        """Busca un paciente por código usando un for."""
        codigo = codigo.strip().upper()
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