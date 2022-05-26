from main import Student
from classes.institute import Institute
import unittest

class TestAddStudent(unittest.TestCase):
    def test_one(self): #correct
        stud = Student('Чекуров Антон Юрьевич', 1857750000)
        inst = Institute()
        inst.add_stud(stud)
        self.assertEqual(len(inst.students), 1)

    def test_two(self): #correct
        stud = Student('Чекуров Антон Юрьевич', 185775)
        stud1 = Student('Иванов Иван Иванович', 199995)
        inst = Institute()
        inst.add_stud(stud)
        inst.add_stud(stud1)
        self.assertEqual(len(inst.students), 2)

    def test_three(self):
        stud = Student('','')
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_stud(stud)
        self.assertEqual(len(inst.students), 0)

    def test_four(self):
        stud = Student('Чекуров Антон Юрьевич', '185775')
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_stud(stud)
        self.assertEqual(len(inst.students), 0)

    def test_five(self):
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_stud(123)
        self.assertEqual(len(inst.students), 0)

    def test_six(self):
        stud = Student('185775','Чекуров Антон Юрьевич')
        stud1 = Student('185775','Чекуров Антон Юрьевич')
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_stud(stud)
            inst.add_stud(stud1)
        self.assertEqual(len(inst.students), 0)

    def test_seven(self):
        stud = Student('185775','185775')
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_stud(stud)
        self.assertEqual(len(inst.students), 0)

    def test_eight(self):
        stud = Student('Чекуров Антон Юрьевич', '185775')
        stud1 = Student('Иванов Иван Иванович', '185775')
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_stud(stud)
            inst.add_stud(stud1)
        self.assertEqual(len(inst.students), 0)

    def test_nine(self):
        stud = Student('Чекуров Антон Юрьевич', '185775')
        stud1 = Student('Чекуров Антон Юрьевич', '199995')
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_stud(stud)
            inst.add_stud(stud1)
        self.assertEqual(len(inst.students), 0)

class TestGetStudent(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        self.institute = Institute()
        self.institute.students = [
            Student("Антон Юрьевич Чекуров", 185775),
            Student("Иван Иванович Иванов", 548724)
        ]
        super(TestGetStudent, self).__init__(*args, **kwargs)

    def test_1(self): #correct
        g_student = self.institute.get_student(185775)
        self.assertEqual("Антон Юрьевич Чекуров", g_student.fio)
        self.assertEqual(185775, g_student.code)

    def test_2(self):
        with self.assertRaises(Exception):
            self.institute.get_student(-154512)

    def test_3(self):
        with self.assertRaises(Exception):
            self.institute.get_student(99999)

    def test_4(self):
        with self.assertRaises(Exception):
            self.institute.get_student(1000000)

    def test_5(self):
        with self.assertRaises(Exception):
            self.institute.get_student(152.451)

    def test_6(self):
        with self.assertRaises(Exception):
            self.institute.get_student("lol")

    def test_7(self):
        with self.assertRaises(Exception):
            self.institute.get_student(None)


if __name__ == "__main__":
    unittest.main()