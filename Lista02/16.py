#16. A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.
na = 0
nf = 1
while nf < 500:
    nf += na
    na = nf - na
    print(nf,end=' ')