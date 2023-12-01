from flask import Flask, render_template,request,redirect,url_for
from db import db
from datos import datos


class programa:
    def __init__(self):
        
        self.app=Flask(__name__)
        self.app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///datos.sqlite3"
        
       
       #agregar nuestra db a la aplicacion
        db.init_app(self.app)    
    

        self.app.add_url_rule("/" , view_func=self.todoslosdatos)
        self.app.add_url_rule("/nuevo" , view_func=self.agregar, methods=["GET", "POST"])
        
        #Iniciar el servidor 
        with self.app.app_context():
            db.create_all()
        self.app.run(debug=True)
        
    def todoslosdatos(self):
        return "Busacar"
        
    def agregar(self):
        #verificar si debe enviar el formulario o procesar los datos
        if request.method=="POST":
            #crear un objeto de la clase Localizacion con los valores  del fotmulario
            coordenadas=request.form["coordenadas"]
            nombre=request.form["nombre"]
            direccion=request.form["direccion"]
            
            los_datos=datos(coordenadas,nombre,direccion)
            
            #guardar el objeto en la db
            
            db.session.add(los_datos)
            db.session.commit()
            return redirect(url_for("todoslosdatos"))
            
        
        
        return render_template("Visor.html")

miprograma=programa()

