from tkinter import simpledialog, Tk


def botao ():
    root = Tk()


    temp_window = Tk()
    temp_window.withdraw()


    temp_window.tk_setPalette(background="white", foreground="black", activeBackground="black", activeForeground="white")
    temp_window.option_add('*Dialog.msg.font', 'Helvetica 12')
    temp_window.option_add('*Dialog.msg.wrapLength', '4i')
    temp_window.option_add('*Dialog.msg.width', 30)
    temp_window.option_add('*Dialog.msg.anchor', 'center')


    temp_window.tk_setPalette(background="white", foreground="black", activeBackground="black", activeForeground="white")
    temp_window.option_add('*Dialog.msg.font', 'Helvetica 12')
    temp_window.option_add('*Dialog.msg.wrapLength', '4i')
    temp_window.option_add('*Dialog.msg.width', 30)
    temp_window.option_add('*Dialog.msg.anchor', 'center')


    temp_window.option_add('*Dialog.msg.font', 'Helvetica 12')
    temp_window.option_add('*Dialog.msg.wrapLength', '4i')
    temp_window.option_add('*Dialog.msg.width', 30)
    temp_window.option_add('*Dialog.msg.anchor', 'center')

    simpledialog.setokcancel('Caixa de Diálogo', 'Texto do corpo da caixa de diálogo')


    temp_window.deiconify()
    temp_window.lift(root)
    temp_window.mainloop()

    root.mainloop()