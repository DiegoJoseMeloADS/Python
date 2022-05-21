import requests
from PySimpleGUI import PySimpleGUI as sg

chave_api = "insira a chave da sua API aqui" #para pegar a chave da sua API acesse e se cadastre no https://openweathermap.org

#layout
sg.theme('reddit') #tema
layout = [[sg.Text('Digite uma cidade'),sg.InputText()],[sg.Button('Pesquisar',button_color= ('purple'))]]

#janela
janela = sg.Window('Clima',icon='imagens/clima.ico').Layout(layout)

#ler eventos
while True:
    eventos,cidade = janela.Read()


    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Pesquisar':
        if cidade[0].isdigit() == True:
            sg.popup('Digite apenas texto', title='Clima', icon='imagens/clima.ico')
        else:
             link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade[0]}&appid={chave_api}&lang=pt_br"

             # fazendo uma requisição a API
             requisicao = requests.get(link)
             # recebendo um dicionario python em formato json
             requisicao_dic = requisicao.json()
             # atribuindo as informações a desçricao e temperatura do dicionario e selecionando oque das listas weather e temperature as informações que eu quero
             descricao = requisicao_dic['weather'][0]['description']
             temperatura = requisicao_dic['main']['temp'] - 273.15  # conversão fahrenheit para celsius

             janela.close()


             sg.popup(f'A descrição é {descricao} e a temperatura é de: {temperatura:.2f} º', title='Clima',icon='imagens/clima.ico')



