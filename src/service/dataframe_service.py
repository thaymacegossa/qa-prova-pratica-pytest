from src.repository.dataframe_repository import DataframeRepository
from src.entity.product import Product


class DataframeService:
    def __init__(self):
        self.dataset_repository = DataframeRepository()

    def open_empty_dataset(self):
        self.dataset_repository.open_empty_dataset()

    def insert_data(self, nome: str, preco: float, quantidade: int = 0):
        produto = Product(nome, preco, quantidade)
        self.dataset_repository.insert_data(produto.__dict__)

    def get_dataset(self):
        return self.dataset_repository.get_dataset()
    
    def print_dataset(self):
        dataset = self.get_dataset()
        if dataset is not None:
            print(dataset)
        else:
            print("Dataset is empty.")
    
    def clear_dataset(self):
        self.dataset_repository.clear_dataset()
    
    def update_product_quantity(self, nome: str, quantidade: int):
        try:
            self.dataset_repository.update_quantity(nome, quantidade)
            print(f"Quantidade do produto '{nome}' atualizada para {quantidade}.")
        except ValueError as e:
            print(f"Erro: {e}")
    
    def remove_product(self, nome: str):
        try:
            self.dataset_repository.remove_by_name(nome)
            print(f"Produto '{nome}' removido do dataset.")
        except ValueError as e:
            print(f"Erro: {e}")