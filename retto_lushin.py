# cliente = {
#     'id_cliente':1,
#     'nombre':'',
#     'edad': 20,
#     'primer_ingreso':False,
# }

def cliente (informacion:dict)-> dict:
    edad=int(informacion['edad'])
    primer_ingreso=bool(informacion['primer_ingreso'])
    

    if primer_ingreso == True:
        
        if edad > 18:
            informacion['atraccion']='X-Treme'
            informacion['apto']=True
            informacion['total_boleta']=19000.0
            
        
        if edad >=15 and edad <= 18:
            informacion['atraccion']='Carros chocones'
            informacion['apto']=True
            informacion['total_boleta']=4650.0
            
        if edad >=7 and edad <15:
            informacion['atraccion']='Sillas voladoras'
            informacion['apto']=True
            informacion['total_boleta']=9500.0
        if edad <7:
            informacion['atraccion']='N/A'
            informacion['apto']=False
            informacion['total_boleta']='N/A'
        
    else:
        
        
        if edad > 18:
            informacion['atraccion']='X-Treme'
            informacion['apto']=True
            informacion['total_boleta']=20000
        
        if edad >=15 and edad <= 18:
            informacion['atraccion']='Carros chocones'
            informacion['apto']=True
            informacion['total_boleta']=5000.0
            
        if edad >=7 and edad <15:
            informacion['atraccion']='Sillas voladoras'
            informacion['apto']=True
            informacion['total_boleta']=10000.0
        if edad <7:
            informacion['atraccion']='N/A'
            informacion['apto']=True
            informacion['total_boleta']='N/A'
    
    
    return informacion


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
	
# informacion = {
#     'nombre': 'Johana Fernandez',
#     'edad': 20,
#     'primer_ingreso': True
# }

# print(cliente(informacion))

# informacion = {
#     'nombre': 'Johana Fernandez',
#     'edad': 20,
#     'primer_ingreso': False

# }
# print(cliente(informacion))


