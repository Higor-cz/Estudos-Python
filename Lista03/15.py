#A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.
na = 0
nf = 1
i = 0
while i < 100:
    i += 1
    nf += na
    na = nf - na
    print(nf,end=' ')