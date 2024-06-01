import unittest
from src.logica.gestor_tareas import GestorTareas

class TestGestorTareas(unittest.TestCase):
    pass


class TestGestorTareas(unittest.TestCase):
    def test_obtener_tareas(self):
        gestor = GestorTareas()
        tarea1 = Tarea("Tarea 1", "Descripción de la tarea 1")
        tarea2 = Tarea("Tarea 2", "Descripción de la tarea 2")
        gestor.agregar_tarea(tarea1)
        gestor.agregar_tarea(tarea2)
        self.assertEqual(gestor.obtener_tareas(), [tarea1, tarea2])


class GestorTareas:
    def marcar_completada(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice].completada = True
        else:
            raise IndexError("Índice fuera de rango")


class TestGestorTareas(unittest.TestCase):
    def test_marcar_completada(self):
        gestor = GestorTareas()
        tarea = Tarea("Tarea 1", "Descripción de la tarea 1")
        gestor.agregar_tarea(tarea)
        gestor.marcar_completada(0)
        self.assertTrue(gestor.tareas[0].completada)


class TestGestorTareas(unittest.TestCase):
    def test_eliminar_tarea(self):
        gestor = GestorTareas()
        tarea1 = Tarea("Tarea 1", "Descripción de la tarea 1")
        tarea2 = Tarea("Tarea 2", "Descripción de la tarea 2")
        gestor.agregar_tarea(tarea1)
        gestor.agregar_tarea(tarea2)
        gestor.eliminar_tarea(0)
        self.assertEqual(gestor.obtener_tareas(), [tarea2])
