import PySimpleGUI as sg

from main import get_votes_from_post, generate_df


if __name__ == '__main__':
    sg.theme('DarkAmber')
    layout = [
        [sg.Text('Código do post'), sg.InputText(key='post_code')],
        [sg.Text('Pasta para download'), sg.Input(key='folder'),
         sg.FolderBrowse('Selecionar', target='folder')],
        [sg.Button('Salvar Planilha')],
    ]
    window = sg.Window('Bot Instagram', layout, resizable=False)
    while True:
        event, values = window.read()
        if event == 'Salvar Planilha':
            df = generate_df(get_votes_from_post(values['post_code']))
            df.to_excel(values['folder'])
