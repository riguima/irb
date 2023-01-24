import PySimpleGUI as sg
from pathlib import Path

from main import get_votes_from_post, generate_df


if __name__ == '__main__':
    sg.theme('DarkAmber')
    layout = [
        [sg.Text('Código do post'), sg.InputText(key='post_code', size=(50, 50))],
        [sg.Text('Pasta para download'), sg.Input(key='folder', size=(30, 30)),
         sg.FolderBrowse('Selecionar', target='folder')],
        [sg.Button('Gerar Planilha')],
    ]
    window = sg.Window('Bot Instagram', layout, resizable=False, element_justification='c')
    while True:
        event, values = window.read()
        if event == 'Gerar Planilha':
            df = generate_df(get_votes_from_post(values['post_code']))
            df.to_excel(Path(values['folder']) / 'result.xlsx', index=False)
        elif event == sg.WIN_CLOSED:
            break
