area=float(input('Digite a area que vai ser pintada em m²: '))
litros=area/6
latas= (litros//18)+1
galoes= (litros//3.6)+1
precolatas=latas*80
precogaloes=galoes*25
areamista=(area+area*10/100)
litrosMisto=areamista/6
latassobra= (litrosMisto//18)
sobra=litrosMisto%18
galoessobra=(sobra//3.6)+1
precoMisto=(latassobra*80)+(galoessobra*25)
print(f'Para a area de{area}m², usando somente latões será nescessario {latas}, e custará R${precolatas}.')
print(f'Para a area de{area}m², usando somente galões será nescessario {galoes}, e custará R${precogaloes}.')
print(f'Para a area de{areamista}m², usando latões e galões será nescessario {latassobra} latões e {galoessobra} galões, e custará R${precoMisto}.')