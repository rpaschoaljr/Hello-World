j = 7
i = 1
a = 1
controle = 0
while a == 1:
    print (f"I={i} J={j}")
    j= j - 1
    controle = controle + 1
    if controle == 3:
      i = i + 2
      controle = 0
      j = 7
    if i > 9:
        a = 2