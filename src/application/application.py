import inquirer # type: ignore
from src.service.dataframe_service import DataframeService


class App:
    def __init__(self):
        self.operation = True
        self.dataset_service = DataframeService()

    def run(self):
        self.dataset_service.open_empty_dataset()

        while self.operation:
            questions = [
                inquirer.List(
                    'choice',
                    message='Escolha uma opção',
                    choices=[
                        'Inserir dados',
                        'Exibir dataset',
                        'Atualizar quantidade',
                        'Remover produto',
                        'Limpar dataset',
                        'Sair'
                    ]
                )
            ]
            
            answers = inquirer.prompt(questions)
            choice = answers['choice']

            if choice == 'Inserir dados':
                nome = input("Digite o nome do produto: ")
                preco = float(input("Digite o preço do produto: "))
                quantidade = int(input("Digite a quantidade do produto: "))
                self.dataset_service.insert_data(nome, preco, quantidade)
                print("Dados inseridos no dataset.")
            
            elif choice == 'Exibir dataset':
                self.dataset_service.print_dataset()
            
            elif choice == 'Atualizar quantidade':
                nome = input("Digite o nome do produto: ")
                quantidade = int(input("Digite a nova quantidade: "))
                self.dataset_service.update_product_quantity(nome, quantidade)
            
            elif choice == 'Remover produto':
                nome = input("Digite o nome do produto a remover: ")
                self.dataset_service.remove_product(nome)
            
            elif choice == 'Limpar dataset':
                self.dataset_service.clear_dataset()
                print("Dataset limpo.")
            
            elif choice == 'Sair':
                self.operation = False
                self.dataset_service.clear_dataset()
                print("Saindo do sistema...")