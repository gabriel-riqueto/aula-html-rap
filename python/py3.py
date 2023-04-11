cont=1
quant=0
while cont <=15:
    idade= int(input('Sua idade: '))
    if idade<18:
        quant +=1     
    cont +=1
print(f'A quantidade de peessoas com menos de 18 são: {quant}')