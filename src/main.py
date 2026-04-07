from src.application.application import App


def main():
    print("Iniciando o sistema...")
    app = App()
    app.run()
    print("Finalizando o sistema...")

if __name__ == "__main__":
    main()