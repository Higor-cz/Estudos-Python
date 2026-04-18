area=float(input('Digite a area que vai ser pintada em m²: '))
litros=area/3
latas= (litros//18)+1
precototal=latas*80
print(f'Para a area de {area}m², será nescessario {latas:.0f} latas e isso vai custar: {precototal:.2f}R$ ')