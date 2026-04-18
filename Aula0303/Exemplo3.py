hp=float(input('Qual seu HP total? '))
Dano=float(input('Quanto você tomou de dano?: '))
Danof=Dano
Danoextra=0
if Dano==hp/2:
    Danoextra=20
    Danof=Dano+Danoextra
hpf=hp-Danof
print(f'Seu Hp original era de {hp} você tomou {Dano} de dano e tomou {Danoextra} de dano extra, seu HP final é de: {hpf}HP')