import re


senha = input("Digite sua senha: ")

def verificar(senha):
    requisitos = {
        "comprimento": len(senha) >= 8,
        "maiuscula": re.search(r'[A-Z]', senha) is not None,
        "minuscula": re.search(r'[a-z]', senha) is not None,
        "numero": re.search(r'[0-9]', senha) is not None,
        "caractere_especial": re.search(r'[!@#\$%\^&\*\(\)_\+\-=\[\]\{\}\|\\:;"\'<>,\.\?/]', senha) is not None
    }
    return requisitos

def requisitos_faltando(requisitos):
  faltando = [requisito for requisito, atendido in requisitos.items() if not atendido]
  return faltando

requisitos = verificar(senha)
faltando = requisitos_faltando(requisitos)

if all(requisitos.values()):
    print("A senha é segura.")
else:
    print("A senha não é segura.")
    print("Requisitos faltando:")
    if "comprimento" in faltando:
        print("- Pelo menos 8 caracteres")
    if "maiuscula" in faltando:
        print("- Pelo menos uma letra maiúscula")
    if "minuscula" in faltando:
        print("- Pelo menos uma letra minúscula")
    if "numero" in faltando:
        print("- Pelo menos um número")
    if "caractere_especial" in faltando:
        print("- Pelo menos um caractere especial (!, @, #, etc.)")