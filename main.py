from flask import Flask,request,render_template,redirect,url_for

app=Flask(__name__)

usuario=[]
id_contador=1

@app.route("/", methods=['GET', 'POST'])
def crud():
    global id_contador
    if request.method=='POST':
        nombre=request.form["nombre"]
        correo=request.form["correo"]
        usuario.append({"id": id_contador, "nombre": nombre, "correo": correo})
        id_contador+=1
        # print (usuario)
    eliminar_id=request.args.get("eliminar")
    if eliminar_id:
        for diccionario in usuario:
            if str(diccionario["id"])==eliminar_id:
                usuario.remove(diccionario)
                break
                

    return render_template("crud.html", usuario=usuario)
#ruta para editar la informacion de un usuario
@app.route("/update/<int:id>", methods=['GET' , 'POST'])
def update(id):
    usuario_a_editar=''
    
    for diccionario in usuario: # para cada diccionario dentro la lista evalue
        if diccionario['id']==id:# si el id convertido a str es igual al id que me pasan po parametr0
            usuario_a_editar=diccionario # hemos identificado todos los datos a editar
            break

    #todo: actualizar la informacion del usuario ingresado
    if request.method=="POST":
        usuario_a_editar["nombre"]=request.form.get("nombre") # el nombre nuevo sera el que llegue por correo
        usuario_a_editar["correo"]=request.form.get("correo")# el nombre nuevo sera el que llegue por correo

        return redirect(url_for("crud"))# redireccione la aplicacion a la ruta de funcion crud es decir de nuevo arriba
    
    if usuario_a_editar=='': # si no encuantra el id arroja esta informacion
        return f"el usuario con id {id} no se encuantra"
    

    return render_template('editar.html', usuario_a_editar=usuario_a_editar)



if __name__=="__main__": 
    app.run(debug=True)