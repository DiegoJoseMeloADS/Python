from pytube import YouTube
from PySimpleGUI import PySimpleGUI as sg

sg.theme('reddit') #tema
layout = [[sg.Text('Digite um link'),sg.InputText()],[sg.Button('Pesquisar')]]

janela = sg.Window('Música',icon = 'imagens/icone.ico').Layout(layout)

def download_audio(video_url):
	yt = YouTube(video_url)
	audio = yt.streams.filter(only_audio=True)[0]
	audio.download()


def titulo(video_url):
	yt = YouTube(video_url)
	return yt.title

def duracao(video_url):
	yt = YouTube(video_url)
	tempo = yt.length / 60
	return round(tempo,2)

while True:
	valor,video_url = janela.Read()

	if valor == sg.WINDOW_CLOSED:
	   break
	if valor == 'Pesquisar':

		janela.close()
		download_audio(video_url[0])
		sg.popup(f'Nome: {titulo(video_url[0])}\n Duração: {duracao(video_url[0])} \n Download Feito', title='Música',icon = 'imagens/icone.ico')

