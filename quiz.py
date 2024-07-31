print("Seja bem vindo oa quiz do Lucas!")
comecar = input("Quer começar ? (S/N) ")

if comecar != "S":
    quit()
    
pontos = 0
    
print("Começando...")
print("Quem desenvolveu o jogo Grand Theft Auto (GTA) ? \n (A) Rockstar Games \n (B) Ubisoft \n (C) Activision \n (D) Ea \n")
resposta_1 = input("Resposta : ")

if resposta_1 == "A":
    print("Certo!")
    pontos = pontos + 1
else:
    print("Incorreto!")
    
print("Qual o nome do protagonista do jogo GTA San Andreas ? \n (A) Carlos John \n (B) Carl Jonhson \n (C) Carl Jaqueline \n (D) Carlos Jonhson \n")
resposta_2 = input("Resposta : ")

if resposta_2 == "B":
    print("Certo!")
    pontos = pontos + 1
else:
    print("Incorreto!")
    
print(f"Quiz acabou... Pontuação: {pontos}/2")