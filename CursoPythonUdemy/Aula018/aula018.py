txt = "Somo os chamados \"vikings\" do norte."
print(txt)

txt = "Ola\nMundo!" # \n quebra de linha
print(txt)

txt = "Ola\rMundo!" # \r Retorno
print(txt)

txt = "Olá\tMundo!" # \t tabulação = 4 espaços
print(txt)

txt = "Isso irá inserir um \\ (barra invertida)." # representa uma barra invertida
print(txt)

txt = "It\'s alright."  # \' substitui por uma aspas simples.
print(txt)

# Este exemplo apaga um caractere anterior(backspace):
txt = "Ola \bMundo!"
print(txt)

# A barra invertida seguida por um 'x' e um número hexadecimal representa um valor hexadecimal.
txt = "\x48\x65\x6c\x6c\x6f"
print(txt)

#Uma barra invertida seguida por três inteiros resultará em um valor octadecimal(octal).
txt = "\110\145\154\154\157"
print(txt)
