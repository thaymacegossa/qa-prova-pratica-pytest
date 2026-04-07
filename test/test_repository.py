import unittest
from src.repository.dataframe_repository import DataframeRepository


class TestDataframeRepository(unittest.TestCase):
    
    def setUp(self):
        self.repo = DataframeRepository()
    
    def test_init(self):
        self.assertIsNone(self.repo.dataset)
    
    def test_open_empty_dataset(self):
        self.repo.open_empty_dataset()
        self.assertIsNotNone(self.repo.dataset)
        self.assertEqual(len(self.repo.dataset), 0)
    
    def test_get_dataset(self):
        self.repo.open_empty_dataset()
        dataset = self.repo.get_dataset()
        self.assertIsNotNone(dataset)
        self.assertEqual(len(dataset), 0)
    
    def test_insert_data(self):
        self.repo.open_empty_dataset()
        data = {"name": "Produto A", "price": 100.0, "quantity": 5}
        self.repo.insert_data(data)
        dataset = self.repo.get_dataset()
        self.assertEqual(len(dataset), 1)
        self.assertEqual(dataset.iloc[0]['name'], "Produto A")
    
    def test_insert_data_without_initialization(self):
        data = {"name": "Produto A", "price": 100.0, "quantity": 5}
        with self.assertRaises(ValueError):
            self.repo.insert_data(data)
    
    def test_clear_dataset(self):
        self.repo.open_empty_dataset()
        data = {"name": "Produto A", "price": 100.0, "quantity": 5}
        self.repo.insert_data(data)
        self.repo.clear_dataset()
        self.assertIsNone(self.repo.dataset)
    
    def test_update_quantity(self):
        self.repo.open_empty_dataset()
        data = {"name": "Produto A", "price": 100.0, "quantity": 5}
        self.repo.insert_data(data)
        self.repo.update_quantity("Produto A", 10)
        dataset = self.repo.get_dataset()
        self.assertEqual(dataset.iloc[0]['quantity'], 10)
    
    def test_update_quantity_not_found(self):
        self.repo.open_empty_dataset()
        with self.assertRaises(ValueError):
            self.repo.update_quantity("Produto Inexistente", 10)
    
    def test_remove_by_name(self):
        self.repo.open_empty_dataset()
        data1 = {"name": "Produto A", "price": 100.0, "quantity": 5}
        data2 = {"name": "Produto B", "price": 200.0, "quantity": 3}
        self.repo.insert_data(data1)
        self.repo.insert_data(data2)
        self.repo.remove_by_name("Produto A")
        dataset = self.repo.get_dataset()
        self.assertEqual(len(dataset), 1)
        self.assertEqual(dataset.iloc[0]['name'], "Produto B")
    
    def test_remove_by_name_not_found(self):
        self.repo.open_empty_dataset()
        with self.assertRaises(ValueError):
            self.repo.remove_by_name("Produto Inexistente")


if __name__ == '__main__':
    unittest.main()
