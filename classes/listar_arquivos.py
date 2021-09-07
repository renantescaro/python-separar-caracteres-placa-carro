import os


class ListarArquivos:
    def __init__(self, caminho_pasta) -> None:
        self.arquivos  = []
        self.caminho_pasta = caminho_pasta


    def listar(self):
        for p, _, files in os.walk(os.path.abspath(self.caminho_pasta)):
            for file in files:
                self.arquivos.append(file)
        return self.arquivos