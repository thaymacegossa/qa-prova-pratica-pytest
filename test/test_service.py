import unittest
from io import StringIO
import sys
from src.service.dataframe_service import DataframeService


class TestDataframeService(unittest.TestCase):
    
    def setUp(self):
        self.service = DataframeService()
    
    def capture_output(self, func):
        captured_output = StringIO()
        sys.stdout = captured_output
        func()
        sys.stdout = sys.__stdout__
        return captured_output.getvalue()
    
    def test_init(self):
        self.assertIsNotNone(self.service.dataset_repository)
    
    def test_open_empty_dataset(self):
        self.service.open_empty_dataset()
        dataset = self.service.get_dataset()
        self.assertIsNotNone(dataset)
        self.assertEqual(len(dataset), 0)
    
    def test_insert_data(self):
        self.service.open_empty_dataset()
        self.service.insert_data("Notebook", 2500.00, 5)
        dataset = self.service.get_dataset()
        self.assertEqual(len(dataset), 1)
        self.assertEqual(dataset.iloc[0]['name'], "Notebook")
        self.assertEqual(dataset.iloc[0]['price'], 2500.00)
        self.assertEqual(dataset.iloc[0]['quantity'], 5)
    
    def test_insert_data_with_default_quantity(self):
        self.service.open_empty_dataset()
        self.service.insert_data("Mouse", 50.00)
        dataset = self.service.get_dataset()
        self.assertEqual(dataset.iloc[0]['quantity'], 0)
    
    def test_get_dataset(self):
        self.service.open_empty_dataset()
        self.service.insert_data("Teclado", 150.00, 3)
        dataset = self.service.get_dataset()
        self.assertEqual(len(dataset), 1)
    
    def test_clear_dataset(self):
        self.service.open_empty_dataset()
        self.service.insert_data("Notebook", 2500.00, 5)
        self.service.clear_dataset()
        dataset = self.service.get_dataset()
        self.assertIsNone(dataset)
    
    def test_update_product_quantity(self):
        self.service.open_empty_dataset()
        self.service.insert_data("Notebook", 2500.00, 5)
        self.service.update_product_quantity("Notebook", 10)
        dataset = self.service.get_dataset()
        self.assertEqual(dataset.iloc[0]['quantity'], 10)
    
    def test_update_product_quantity_not_found(self):
        self.service.open_empty_dataset()
        output = self.capture_output(
            lambda: self.service.update_product_quantity("Inexistente", 10)
        )
        self.assertIn("Erro", output)
    
    def test_remove_product(self):
        self.service.open_empty_dataset()
        self.service.insert_data("Notebook", 2500.00, 5)
        self.service.insert_data("Mouse", 50.00, 3)
        self.service.remove_product("Notebook")
        dataset = self.service.get_dataset()
        self.assertEqual(len(dataset), 1)
        self.assertEqual(dataset.iloc[0]['name'], "Mouse")
    
    def test_remove_product_not_found(self):
        self.service.open_empty_dataset()
        output = self.capture_output(
            lambda: self.service.remove_product("Inexistente")
        )
        self.assertIn("Erro", output)
    
    def test_print_dataset_empty(self):
        self.service.open_empty_dataset()
        output = self.capture_output(self.service.print_dataset)
        self.assertIn("empty", output.lower())
    
    def test_print_dataset_with_data(self):
        self.service.open_empty_dataset()
        self.service.insert_data("Notebook", 2500.00, 5)
        output = self.capture_output(self.service.print_dataset)
        self.assertIn("Notebook", output)


if __name__ == '__main__':
    unittest.main()
