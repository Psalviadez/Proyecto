from db import db

class datos(db.Model):
    
    #Nombre de tabla 
    __tablename__="datos"
    
    #Conjunto de atributos que van a hacer los campos de la tabla
    
    #llave primaria 
    id=db.Column(db.Integer , primary_key=True)
    coordenadas=db.Column(db.Float(100))
    nombre=db.Column(db.String(30))
    direccion=db.Column(db.String(30))
    
    #Metodo constructor para mapear datos alos campos definidos
    
    def __init__(self, coordenadas, nombre,direccion):
        self.coordenadas=coordenadas
        self.nombre=nombre
        self.direccion=direccion
    