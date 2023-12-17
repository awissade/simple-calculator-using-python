def Add(x, y):
    return int(x) + int(y)

def Sub(x, y): 
    return int(x) - int(y)

def Mul(x, y):
    return int(x) * int(y)

def Div(x, y):
    if y == 0:
        raise ValueError("Cannot divide bu zero !")
    return int(x) / int(y)

def Mod(x, y):
    return int(x) % int(y)

def Exp(x, y):
    return int(x) ** int(y)
