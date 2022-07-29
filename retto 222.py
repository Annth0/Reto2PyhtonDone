def cliente (informacion:dict)-> dict:
   
    
    nombre= informacion['nombre']
    edad=int(informacion['edad'])
    primer_ingreso= informacion['primer_ingreso']
    
    #    el orden aqui va adentro porque la respuesta va despues
    if edad > 18: #aqui no hay otro diccionario sobre ese, ya está incluido
        atraccion='X-Treme'
        apto=True
        if primer_ingreso == True:
            total_boleta= 20000 - (20000*0.05)
        else:
            total_boleta=20000
        
    elif edad >=15 and edad <= 18:
        atraccion='Carros chocones'
        apto=True
        if primer_ingreso == True:
            total_boleta= 4650.0
        else:
            total_boleta= 5000
        
    elif edad >=7 and edad <15:
        atraccion='Sillas voladoras'
        apto=True
        if primer_ingreso == True:
            total_boleta= 100000 - (10000*0.05)
        else:
            total_boleta= 10000
    else:
        atraccion='N/A'
        apto=False
        total_boleta='N/A'
#y el orden que tenemos es otro, solo era ordenarlo
# es decir meter el ingreso adentro de lo que piden
    respuesta = {
        'nombre':nombre,
        'edad':edad,
        'atraccion':atraccion,
        'apto':apto,
        'primer_ingreso':primer_ingreso,
        'total_boleta':total_boleta
    }

    return respuesta #unico

informacion={'nombre':'Johana Fernandez', 'edad':20, 'primer_ingreso':True}
print(cliente(informacion))

informacion={'nombre':'Johana Fernandez', 'edad':20, 'primer_ingreso':False}
print(cliente(informacion))
informacion={'nombre':'Gloria Suarez', 'edad':3, 'primer_ingreso':True}
print(cliente(informacion))
informacion={'nombre':'Tatiana Suarez', 'edad':17, 'primer_ingreso':True}
print(cliente(informacion))
informacion={'nombre':'Tatiana Suarez', 'edad':17, 'primer_ingreso':False}
print(cliente(informacion))
informacion={'nombre':'Tatiana Ruiz', 'edad':8, 'primer_ingreso':True}
print(cliente(informacion))
informacion={'nombre':'Tatiana Ruiz', 'edad':8, 'primer_ingreso':False}
print(cliente(informacion))
