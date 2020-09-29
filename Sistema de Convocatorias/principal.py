from flask import Flask, render_template, request
from flask import make_response
from flask import send_file
from flask import jsonify

# Instancia de Flask. Aplicación
app = Flask(__name__)

# Creamos nuestro primer route. '/login'
@app.route('/')
def template():
 # Renderizamos la plantilla. Formulario HTML.
 # templates/form.html
 return render_template("gentelella-master/production/index.html")

@app.route('/contratistasactuales')
def contratistasactuales():
 db=cx_Oracle.makedsn('200.69.103.17',1521, 'xe')
 conn = cx_Oracle.connect(user=r'RITA', password='IDEXUD2020', dsn=db)
 c = conn.cursor()
 p = """SELECT * FROM IDXPROY.CONTRATO WHERE SITUACION=14""" #Situación 14 EN EJECUCIÓN
 c.execute(p)
 contratistas_ejecucion=0 
 cedulas=[]
 for result in c:
     #print(result)
     cedulas.append(result[8])
     contratistas_ejecucion=contratistas_ejecucion+1

 print(cedulas)
 print(contratistas_ejecucion)
 return jsonify(cedulas=cedulas)

if __name__ == '__main__':
 # Iniciamos la apicación en modo debug
 
 #app.run(debug=True)
 app.run(host='0.0.0.0')