qtd_aluno = 0
media = 0
maior_media = 0
while qtd_aluno < 2:
    nome = input('Qual o seu nome? ')
    n1 = float(input('Qual a primeira nota?'))
    n2 = float(input('Qual a segunda nota?'))
    media_Aluno = (n1+n2)/2
    media += media_Aluno
    qtd_aluno= qtd_aluno + 1
    if media_Aluno>maior_media:
        maior_media = media_Aluno
        nome_aluno = nome
media_Turma = media / qtd_aluno 
print(f'A media da turma é {media_Turma:.2f} e a maior media foi do aluno {nome_aluno} e sua media foi: {maior_media:.2f}')