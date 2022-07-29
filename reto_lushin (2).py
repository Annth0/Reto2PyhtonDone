cliente = {
    "id":1,
    "nombre":"uwu",
    "edad": 20,
    # "atraccion": "x",
    # "apto":True,
    "primer_ingreso":False,
    # "total_boleta":"19000.0"
    
    # "agujas": 150000000.0,
    # "escolares": 300000000.0,
    # "hogar": 200000000.0
}

def prueba(cliente:dict)->dict:
    n=bool(cliente["primer_ingreso"])
    a=int(cliente["edad"])
    
    x={'nombre':cliente["nombre"],
    'edad': cliente["edad"],
    'atraccion': "",
    'apto': bool,
    'primer_ingreso':cliente["primer_ingreso"],
    'total_boleta':0.0
    } 
    if n == True:
        if a > 18:
            x["atraccion"]="X-Treme"
            x["total_boleta"]=20000 #como es la formula?
        
        if a >=15 and a <= 18:
            x["atraccion"]="Carros Chocones"
            x["total_boleta"]=5000#como es?
            
        if a >=7 and a <15:
            x["atraccion"]="Sillas voladoras"
            x["total_boleta"]=10000#como es?
        if a <7:
            x["atraccion"]="N/A"
            x["total_boleta"]="N/A"
        
    else:
        if a > 18:
            x["atraccion"]="X-Treme"
            x["total_boleta"]=20000
        
        if a >=15 and a <= 18:
            x["atraccion"]="Carros Chocones"
            x["total_boleta"]=5000
            
        if a >=7 and a <15:
            x["atraccion"]="Sillas voladoras"
            x["total_boleta"]=10000
        if a <7:
            x["atraccion"]="N/A"
            x["total_boleta"]="N/A"

        # if x["atraccion"]=="X-Treme":
        #     x["total_boleta"]=20000
        # elif x["atraccion"]=="Carros Chocones":
        #     x["total_boleta"]=5000
        # elif x["atraccion"]=="Sillas Voladoras":
        #     x["total_boleta"]=10000
    
    
    return x



cliente1={"id":1, "nombre":"Johana Fernandez", "edad":"20", "primer_ingreso":True}
cliente2={"id":1, "nombre":"Johana Fernandez", "edad":"20", "primer_ingreso":False}
cliente3={"id":2, "nombre":"Gloria Suarez", "edad":"20", "primer_ingreso":True}
cliente4={"id":3, "nombre":"Tatiana Suarez", "edad":"17", "primer_ingreso":True}
cliente5={"id":3, "nombre":"Tatiana Suarez", "edad":"17", "primer_ingreso":False}
cliente6={"id":4, "nombre":"Tatiana Ruiz", "edad":"8", "primer_ingreso":True}
cliente8={"id":4, "nombre":"Tatiana Ruiz", "edad":"8", "primer_ingreso":False}

print(prueba(cliente1))
print(prueba(cliente2))
print(prueba(cliente3))
print(prueba(cliente4))
print(prueba(cliente5)) 