import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        layout = [
            [sg.Text('Nome', size=(5,0)), sg.Input(size=(15,0), key="nome")],
            [sg.Text('Idade', size=(5,0)),sg.Input(size=(15,0), key="idade")],
            [sg.Text('Quais provedores de email são aceitos?')],
            [sg.Checkbox("Gmail", key="gmail"), sg.Checkbox("Outlook", key="outlook")],
            [sg.Button('Enviar dados')],
            [sg.Output(size=(30,20))]
        ]
        
        self.janela = sg.Window("Dados do usuário").layout(layout)
        
        
    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()           
            nome = self.values['nome']
            idade = self.values['idade']
            aceita_gmail = self.values['gmail']
            aceita_outlook = self.values['outlook']
            
            print(f'Nome: {nome}')
            print(f'Idade: {idade}')
            print(f'Gmail: {aceita_gmail}')
            print(f'Outlook: {aceita_outlook}')
        
            
tela = TelaPython()
tela.Iniciar()