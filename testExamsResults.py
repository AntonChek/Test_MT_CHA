from main import *
from classes.institute import Institute
import unittest

class TestAddExamResult(unittest.TestCase):
    stud = Student("Луковцев Алексей Владимирович", 185775)
    spec = Specialization('Фундаментальная информатика и информационные технологии')
    subject = Subject("Б1.Б.22", "Основы программирования", 1, 144, spec)
    group = Group("Б-ФИИТ-21", 2021, spec)
    data = date(2021, 1, 10)

    def test_one(self): #correct
        inst = Institute()
        inst.add_exam_points(ExamPoints(self.stud, 59.9, 25.4, self.data, self.group.name, self.subject))
        self.assertEqual(len(inst.exam_points), 1)

    def test_three(self):
        inst = Institute()
        with self.assertRaises(Exception):
            result = ExamPoints(self.stud, 80.0, 10, self.data, self.group.name, self.subject)
            inst.add_exam_points(result)
        self.assertEqual(len(inst.exam_points), 0)

    def test_four(self):
        inst = Institute()
        with self.assertRaises(Exception):
            result = ExamPoints(self.stud, 60.0, 40, self.data, self.group.name, self.subject)
            inst.add_exam_points(result)
        self.assertEqual(len(inst.exam_points), 0)

    def test_five(self):
        inst = Institute()
        with self.assertRaises(Exception):
            result = ExamPoints(self.stud, -60.0, 40, self.data, self.group.name, self.subject)
            inst.add_exam_points(result)
        self.assertEqual(len(inst.exam_points), 0)

    def test_six(self):
        inst = Institute()
        with self.assertRaises(Exception):
            result = ExamPoints(12, 60.0, 25, self.data, self.group.name, self.subject)
            inst.add_exam_points(result)
        self.assertEqual(len(inst.exam_points), 0)

    def test_seven(self):
        inst = Institute()
        with self.assertRaises(Exception):
            result = ExamPoints(self.stud, 60.0, 24, self.data, self.group.name, self.subject)
            inst.add_exam_points(result)
        self.assertEqual(len(inst.exam_points), 0)

    def test_eight(self):
        inst = Institute()
        with self.assertRaises(Exception):
            inst.add_exam_points(123)
        self.assertEqual(len(inst.exam_points), 0)

    def test_nine(self):
        inst = Institute()
        with self.assertRaises(Exception):
            result = ExamPoints(self.stud, 60.0, -25, self.data, self.group.name, self.subject)
            inst.add_exam_points(result)
        self.assertEqual(len(inst.exam_points), 0)

    def test_ten(self):
        inst = Institute()
        with self.assertRaises(Exception):
            result = ExamPoints(self.stud, 60, 25, self.data, self.group.name, self.subject)
            inst.add_exam_points(result)
        self.assertEqual(len(inst.exam_points), 0)


class TestGetExamResult(unittest.TestCase):
    student = Student("Луковцев Алексей Владимирович", 185775)
    spec = Specialization('Фундаментальная информатика и информационные технологии')
    subject = Subject("Б1.Б.22", "Основы программирования", 1, 144, spec)
    group = Group("Б-ФИИТ-21", 2021, spec)
    data = date(2021, 1, 10)

    def test_1(self):  # Корректный тест
        ep = ExamPoints(self.student, 55.4, 30.0, self.data , self.group.name, self.subject)
        inst = Institute()
        inst.add_exam_points(ep)
        self.assertEqual(len(inst.get_exam_points(self.group.name,self.subject.name,self.data)), 1)

    def test_2(self):
        inst = Institute()
        with self.assertRaises(Exception):
            g_examres = inst.get_exam_result(None, None)
            inst.get_exam_result(g_examres)

if __name__ == "__main__":
    unittest.main()