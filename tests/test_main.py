import unittest
import main


class TestPeopledocs(unittest.TestCase):
    def setUp(self):
        self.test_parameters = '1', "passport", "4507 498533", "Василий Кентозавров"

    # Тест вывода
    def test_info(self):
        for el in self.test_parameters:
            self.assertIn(main.list(main.documents), el)

    # Тест добавления
    def test_add_list(self):
        main.add_list('1', "passport", "4507 498533", "Василий Кентозавров")
        self.assertIn("4507 498533", main.directories['1'])
        self.assertIn({"type": "passport", "number": "4507 498533", "name": "Василий Кентозавров"}, main.documents)

    # Тест удаления
    def test_del(self):
        main.remove_doc('1', "4507 498533", "Василий Кентозавров")
        self.assertNotIn(self.test_parameters, main.documents)
        self.assertNotIn("4507 498533", main.directories.values())
