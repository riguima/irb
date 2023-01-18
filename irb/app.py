from tkinter import Tk, ttk
from tkinter.filedialog import askdirectory
from main import save_worksheet


if __name__ == '__main__':
    window = Tk()
    window.resizable(False, False)
    window.geometry('600x600')
    label_post_code = ttk.Label(window, text='Código do post')
    input_post_code = ttk.Entry(window)
    button_save_worksheet = ttk.Button(
            window, text='Salvar Planilha',
            command=lambda: save_worksheet(askdirectory()))
    label_post_code.grid(row=0, column=0, ipadx=5)
    input_post_code.grid(row=0, column=1)
    button_save_worksheet.grid(row=1, column=0, ipady=10)
    window.mainloop()
