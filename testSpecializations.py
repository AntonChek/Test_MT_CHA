from main import Specialization
from classes.institute import Institute
import unittest

class TestAddSpec(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        self.institute = Institute()
        self.institute.specs = []
        super(TestAddSpec, self).__init__(*args, **kwargs)

    def test_one(self): #correct
        sp = Specialization('Фундаментальная информатика и информационные технологии')
        self.institute.add_spec(sp)
        self.assertEqual(len(self.institute.specs), 1)

    def test_two(self): #correct
        sp = Specialization('Фундаментальная информатика и информационные технологии')
        sp1 = Specialization('Информатика и вычислительная техника')
        self.institute.add_spec(sp)
        self.institute.add_spec(sp1)
        self.assertEqual(len(self.institute.specs), 2)

    def test_three(self):
        with self.assertRaises(Exception):
            self.institute.add_spec('')
        self.assertEqual(len(self.institute.specs), 0)

    def test_four(self):
        sp = Specialization('Фундаментальная информатика и информационные технологии')
        sp1 = Specialization('Фундаментальная информатика и информационные технологии')
        with self.assertRaises(Exception):
            self.institute.add_spec(sp)
            self.institute.add_spec(sp1)
        self.assertEqual(len(self.institute.specs), 1)

    def test_five(self):
        with self.assertRaises(Exception):
            self.institute.add_spec('')
        self.assertEqual(len(self.institute.specs), 0)

class TestGetSpec(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        self.institute = Institute()
        self.institute.specs = [
            Specialization("Математика (Дифференциальные уравнения,оптимальное управление и аналитика)"),
            Specialization("Фундамельная информатика и информационные технологии")
        ]
        super(TestGetSpec, self).__init__(*args, **kwargs)

    def test_1(self): #correct
        g_spec = self.institute.get_spec("Математика (Дифференциальные уравнения,оптимальное управление и аналитика)")
        self.assertEqual("Математика (Дифференциальные уравнения,оптимальное управление и аналитика)", g_spec.name)

    def test_2(self):
        with self.assertRaises(Exception):
            self.institute.get_spec(None)

    def test_3(self):
        with self.assertRaises(Exception):
            self.institute.get_spec("")

    def test_4(self):
        with self.assertRaises(Exception):
            self.institute.get_spec(354652)

if __name__ == "__main__":
    unittest.main()