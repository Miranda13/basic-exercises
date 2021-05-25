pacientes = int(input())
i = 0
hBaja = 0
hAlta = 0
hNormal = 0
mBaja = 0
mNormal = 0
mAlta = 0
while (i < pacientes):
    hemoglobina= float(input())
    genero = int(input())
    while(genero != 1 and genero != 2):
        genero = int(input())
    if (genero == 1):
        if (hemoglobina < 12.2):
            hBaja += 1
        elif (hemoglobina <= 16.6):
            hNormal += 1
        elif (hemoglobina > 16.6):
            hAlta += 1
    elif (genero == 2):
        if (hemoglobina < 12.6):
            mBaja += 1
        elif (hemoglobina <= 15):
            mNormal += 1
        elif (hemoglobina > 15):
            mAlta += 1    
    i += 1
print(hBaja, hAlta, hNormal, mBaja, mAlta, mNormal)   
    
    