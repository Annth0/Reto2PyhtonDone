informacion = {
    'id_cliente':1,
    'nombre':'uwu',
    'edad': 20,
    # 'atraccion': 'x',
    # 'apto':True,
    'primer_ingreso':False,
    # 'total_boleta':'19000.0'

}
# yo le veo igual e.e  n comprendo
# tienes llamada de diccionario dentro de diccionario

def prueba(cliente:dict)->dict:
    primer_ingreso=bool(informacion['primer_ingreso'])
    edad=int(informacion['edad'])
    
    x={'nombre':cliente['nombre'],
    'edad': cliente['edad'],
    'atraccion': '',
    'apto': bool,
    'primer_ingreso':cliente['primer_ingreso'],
    'total_boleta':0.0
    }
    
    # iniciaste con el if que va deslpues 
    if primer_ingreso == True:
        if edad > 18:
            x['apto']=True
            x['atraccion']='X-Treme'
            x['total_boleta']=19000.0
        
        if edad >=15 and edad <= 18:
            x['apto']=True
            x['atraccion']='Carroschocones'
            x['total_boleta']=4650.0
            
        if edad >=7 and edad <15:
            x['apto']=True
            x['atraccion']='Sillas voladoras'
            x['total_boleta']=9500.0
        if edad <7:
            x['apto']=False
            x['atraccion']='N/A'
            x['total_boleta']='N/A'
        
    else:
        if edad > 18:
            x['apto']=True
            x['atraccion']='X-Treme'
            x['total_boleta']=20000
        
        if edad >=15 and edad <= 18:
            x['apto']=True
            x['atraccion']='Carroschocones'
            x['total_boleta']=5000
            
        if edad >=7 and edad <15:
            x['apto']=True
            x['atraccion']='Sillas voladoras'
            x['total_boleta']=10000
        if edad <7:
            x['apto']=True
            x['atraccion']='N/A'
            x['total_boleta']='N/A'

        # if x['atraccion']=='X-Treme':
        #     x['total_boleta']=20000
        # elif x['atraccion']=='Carroschocones':
        #     x['total_boleta']=5000
        # elif x['atraccion']=='Sillas Voladoras':
        #     x['total_boleta']=10000
    
    
    return x # amor 
#cuando ejecuté este en el bot, me dijo esto



cliente={'id_cliente':1, 'nombre':'Johana Fernandez', 'edad':20, 'primer_ingreso':True}
cliente={'id_cliente':1, 'nombre':'Johana Fernandez', 'edad':20, 'primer_ingreso':False}
cliente={'id_cliente':2, 'nombre':'Gloria Suarez', 'edad':3, 'primer_ingreso':True}
cliente={'id_cliente':3, 'nombre':'Tatiana Suarez', 'edad':17, 'primer_ingreso':True}
cliente={'id_cliente':3, 'nombre':'Tatiana Suarez', 'edad':17, 'primer_ingreso':False}
cliente={'id_cliente':4, 'nombre':'Tatiana Ruiz', 'edad':8, 'primer_ingreso':True}
cliente={'id_cliente':4, 'nombre':'Tatiana Ruiz', 'edad':8, 'primer_ingreso':False}
	
print(prueba(cliente))


#bueno, lo que me decia era: no se puede llamar dict sobre dict

