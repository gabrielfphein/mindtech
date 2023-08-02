import PySimpleGUI as sg

def criar_janela_inicial():
    sg.theme('DarkBlue4')
    linha = [
        [sg.Checkbox(''), sg.InputText('')]
    ]
    layout = [
        [sg.Frame('Tarefas', layout=linha, key='container'),
         sg.Button('Nova Tarefa'), sg.Button('Resetar')]
    ]
    return sg.Window('Todo List', layout=layout, finalize=True)


janela = criar_janela_inicial()

while True:
    event, values = janela.Read()

    if event == sg.WIN_CLOSED:
        break
    elif 'Nova tarefa':
        janela.extend_layout(janela['container'], [
            [sg.Checkbox(''), sg.Input('')]])
