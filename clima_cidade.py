import requests

chave_api = "sua_chave_api" #utilize sua chave API

cidade = input("Digite uma cidade: ")

cidade = cidade.lower()

link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}&lang=pt_br"

#fazendo uma requisição a API
requisicao = requests.get(link)
#recebendo um dicionario python em formato json
requisicao_dic = requisicao.json()
# atribuindo as informações a desçricao e temperatura do dicionario e selecionando oque das listas weather e temperature as informações que eu quero
descricao = requisicao_dic['weather'][0]['description']
temperatura = requisicao_dic['main']['temp'] - 273.15 #conversão fahrenheit para celsius
print(f'Está {descricao} com {temperatura:.2f}cº de temperatura')