import pandas as pd # type: ignore

class DataframeRepository:
    def __init__(self):
        self.dataset = None
    
    def open_empty_dataset(self):
        self.dataset = pd.DataFrame()
    
    def insert_data(self, data):
        if self.dataset is not None:
            self.dataset = pd.concat([self.dataset, pd.DataFrame([data])], ignore_index=True)
        else:
            raise ValueError("Dataset is not initialized. Please open an empty dataset first.")
        
    def get_dataset(self):
        return self.dataset
    
    def clear_dataset(self):
        self.dataset = None
    
    def update_quantity(self, name: str, quantity: int):
        if self.dataset is not None:
            try:
                mask = self.dataset['name'] == name
            except Exception as e:
                raise ValueError(f"Error occurred while updating product '{name}': {e}")
            if mask.any():
                self.dataset.loc[mask, 'quantity'] = quantity
            else:
                raise ValueError(f"Product '{name}' not found in dataset.")
        else:
            raise ValueError("Dataset is not initialized.")
    
    def remove_by_name(self, name: str):
        if self.dataset is not None:
            initial_length = len(self.dataset)
            try:
                self.dataset = self.dataset[self.dataset['name'] != name]
            except Exception as e:
                raise ValueError(f"Error occurred while removing product '{name}': {e}")
            if len(self.dataset) == initial_length:
                raise ValueError(f"Product '{name}' not found in dataset.")
        else:
            raise ValueError("Dataset is not initialized.")