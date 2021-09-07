from pathlib import Path
from PIL import Image
from classes.listar_arquivos import ListarArquivos


caminho_placas     = 'assets/placas_originais'
caminho_caracteres = 'assets/placas_caracteres_separados'

lista_placas = ListarArquivos(caminho_placas).listar()
for placa in lista_placas:
    img_placa = Image.open(str(caminho_placas)+'/'+str(placa))
    img_placa_nome  = str(placa).replace('.png', '')

    # cria diretorio para salvar as imagens dos caracteres
    diretorio = str(caminho_caracteres)+'/'+str(img_placa_nome)
    Path(diretorio).mkdir(parents=True, exist_ok=True)

    # dimensoes imagem placa
    width_placa, height_placa = img_placa.size
    left_placa   = 45
    top_placa    = 50
    right_placa  = width_placa -45
    bottom_placa = height_placa-15

    # remove bordas da imagem da placa
    img_placa = img_placa.crop((left_placa, top_placa, right_placa, bottom_placa))

    # corte dos caracteres
    tamanho_caracter = 57.15
    altura   = img_placa.size[1]
    esquerda = 0
    direita  = tamanho_caracter
    for num_caracter_atual in range(7):
        img_caracter = img_placa.crop((esquerda, 0, direita, altura))

        direita  += tamanho_caracter
        esquerda += tamanho_caracter

        # img_caracter.show()
        img_caracter.save(
            str(caminho_caracteres)+'/'+
            str(img_placa_nome)+'/'+
            str(num_caracter_atual)+'.png' )