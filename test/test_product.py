import unittest
from src.entity.product import Product


class TestProduct(unittest.TestCase):
    
    def test_product_initialization(self):
        produto = Product("Notebook", 2500.00, 5)
        self.assertEqual(produto.name, "Notebook")
        self.assertEqual(produto.price, 2500.00)
        self.assertEqual(produto.quantity, 5)
    
    def test_product_default_quantity(self):
        produto = Product("Mouse", 50.00)
        self.assertEqual(produto.quantity, 0)
    
    def test_product_str_representation(self):
        produto = Product("Teclado", 150.00, 3)
        resultado = str(produto)
        self.assertIn("Teclado", resultado)
        self.assertIn("150", resultado)
        self.assertIn("3", resultado)


if __name__ == '__main__':
    unittest.main()
