import tkinter as tk
janela = tk.Tk()
mensagem_para_usuario = "Esta é uma mensagem.\n(Pode ser bastante útil para o usuário)"
msg = tk.Message(janela, text = mensagem_para_usuario)
msg.config(bg='red', font=('verdana', 24, 'bold'))
msg.pack()
janela.mainloop()