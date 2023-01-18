import PySimpleGUI as sg

from main import get_comments_from_post, generate_df


if __name__ == '__main__':
    layout = [
        [sg.Text('Código do post'), sg.InputText()],
        [sg.Button('Salvar Planilha')],
    ]
    window = sg.Window('Bot Instagram', layout)
    while True:
        event, values = window.read()
        if event == 'Salvar Planilha':
            df = generate_df(get_comments_from_post(values[0]))
            df.to_excel()
