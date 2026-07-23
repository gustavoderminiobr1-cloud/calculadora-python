import tkinter as tk

BOTOES = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("C", 4, 0), ("0", 4, 1), ("=", 4, 2), ("+", 4, 3),
]


def montar_display(master, display_var):
    display = tk.Entry(
        master,
        textvariable=display_var,
        font=("Arial", 24),
        justify="right",
        state="readonly",
        readonlybackground="white",
    )
    display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)
    return display


def montar_botoes(master, ao_clicar):
    for texto, linha, coluna in BOTOES:
        comando = lambda t=texto: ao_clicar(t)
        tk.Button(master, text=texto, font=("Arial", 18), command=comando).grid(
            row=linha, column=coluna, sticky="nsew", padx=2, pady=2
        )


def configurar_grid(master):
    for i in range(5):
        master.rowconfigure(i, weight=1)
    for i in range(4):
        master.columnconfigure(i, weight=1)
