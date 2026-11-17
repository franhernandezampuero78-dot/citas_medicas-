import contextlib
import io
import unittest
from unittest.mock import patch

from atencion import Atencion
from cita import Cita
from medico import Medico
from paciente import Paciente
from main import crear_clinica_demo, ejecutar_menu, leer_edad_valida, medicos_por_especialidad


class PruebasKawsay(unittest.TestCase):
    def setUp(self):
        self.clinica = crear_clinica_demo()
        self.salida = io.StringIO()
        self.redirect = contextlib.redirect_stdout(self.salida)
        self.redirect.__enter__()
        self.addCleanup(self.redirect.__exit__, None, None, None)

    def test_edades_limite_y_reintentos(self):
        for limite in (0, 120):
            with self.subTest(limite=limite):
                with patch('builtins.input', side_effect=['abc', '-5', '150', str(limite)]):
                    self.assertEqual(leer_edad_valida(), limite)
        self.assertIn('número entero', self.salida.getvalue())
        self.assertIn('entre 0 y 120', self.salida.getvalue())

    def test_edad_invalida_no_se_registra(self):
        for edad in (-1, 121, 'abc', True, 1.5):
            self.assertFalse(self.clinica.agregar_paciente(Paciente('P003', 'Ficticio', edad)))
        self.assertEqual(len(self.clinica.pacientes), 2)

    def test_duplicados_en_las_cuatro_colecciones(self):
        c = self.clinica
        casos = [
            (c.agregar_paciente, Paciente(' p001 ', 'Ficticio', 0), c.pacientes),
            (c.agregar_medico, Medico(' m001 ', 'Ficticio', 'Otra'), c.medicos),
            (c.agregar_cita, Cita(' c001 ', c.pacientes[0], c.medicos[0], '01/01/2027'), c.citas),
            (c.registrar_atencion, Atencion(' a001 ', c.citas[0], 'Ficticio', 'Ficticio'), c.historial_atenciones),
        ]
        for registrar, objeto, registros in casos:
            cantidad = len(registros)
            self.assertFalse(registrar(objeto))
            self.assertEqual(len(registros), cantidad)

    def test_referencias_invalidas(self):
        c = self.clinica
        cita = Cita('C002', Paciente('P999', 'Ficticio', 20), c.medicos[0], '01/01/2027')
        self.assertFalse(c.agregar_cita(cita))
        cita = Cita('C002', c.pacientes[0], Medico('M999', 'Ficticio', 'Otra'), '01/01/2027')
        self.assertFalse(c.agregar_cita(cita))
        self.assertFalse(c.registrar_atencion(Atencion('A002', cita, 'Ficticio', 'Ficticio')))
        self.assertEqual(len(c.citas), 1)
        self.assertEqual(len(c.historial_atenciones), 1)

    def test_campos_obligatorios(self):
        self.assertFalse(self.clinica.agregar_paciente(Paciente(' ', 'Ficticio', 20)))
        self.assertFalse(self.clinica.agregar_medico(Medico('M002', 'Ficticio', ' ')))

    def test_consultas_y_listas_vacias(self):
        c = self.clinica
        originales = c.medicos.copy()
        self.assertEqual(medicos_por_especialidad(c, ' CARDIOLOGIA '), originales)
        self.assertEqual(medicos_por_especialidad(c, 'Pediatria'), [])
        self.assertEqual(c.medicos, originales)
        self.assertEqual(len(c.historial_por_paciente('P001')), 1)
        self.assertEqual(c.historial_por_paciente('P002'), [])
        self.assertIsNone(c.buscar_paciente('P999'))
        self.assertEqual(len(c.citas_por_medico('M001')), 1)

    def test_flujo_completo_del_menu(self):
        entradas = [
            '1', 'P003', 'Paciente ficticio 3', 'abc', '150', '0',
            '2', 'M002', 'Médico ficticio 2', 'Pediatria',
            '4', 'C002', 'P003', 'M002', '10/12/2026',
            '5', 'A002', 'C002', 'Diagnóstico ficticio', 'Tratamiento ficticio',
            '3', 'P003', '6', 'Pediatria', '7', 'M002', '8', '9', '0',
        ]
        with patch('builtins.input', side_effect=entradas):
            ejecutar_menu(self.clinica)
        self.assertEqual(len(self.clinica.historial_por_paciente('P003')), 1)
        self.assertIn('Paciente registrado:', self.salida.getvalue())
        self.assertIn('Cita registrada:', self.salida.getvalue())
        self.assertIn('Atención registrada:', self.salida.getvalue())

    def test_menu_referencias_inexistentes_y_sin_resultados(self):
        entradas = ['4', 'C002', 'P999', '4', 'C002', 'P001', 'M999',
                    '5', 'A002', 'C999', '3', 'P999', '3', 'P002',
                    '6', 'Pediatria', '7', 'M999', 'x', '0']
        with patch('builtins.input', side_effect=entradas):
            ejecutar_menu(self.clinica)
        self.assertIn('No existe un paciente', self.salida.getvalue())
        self.assertIn('No existe un médico', self.salida.getvalue())
        self.assertIn('No existe una cita', self.salida.getvalue())
        self.assertIn('no tiene atenciones', self.salida.getvalue())
        self.assertIn('No hay médicos', self.salida.getvalue())
        self.assertEqual(len(self.clinica.citas), 1)


if __name__ == '__main__':
    unittest.main()
