def Media (nota1, nota2):
    media= (nota1 + nota2) / 2
    return media 

def verificar_aprovacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"