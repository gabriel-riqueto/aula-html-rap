cont=1
quant=0
while cont <=10:
    nums= int(input('Numeros: '))
    if nums<=200 and nums>=100:
        quant +=1     
    cont +=1
print(f'A quantidade de numeros que estão entre 100 e 200 é {quant}')