popA = 80000
popB = 200000
txA = 0.03
txB = 0.015
anos = 0
while popA > popB:
    popA = popA * 1.03
    popB = popB *1.015
    anos += 1
print(f'A quantidade de anos para A superar B foi de {anos}')