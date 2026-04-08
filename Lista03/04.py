popA = 80000
txA = 0.03
popB = 200000
txB = 0.015
i = 0
while popA < popB :
    popA *= txA+1
    popB *= txB+1
    i += 1
print(f'Foram nescessario {i} anos para a População da cidade A igualar ou Ultrapassar a População da cidade B')