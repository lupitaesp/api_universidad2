import web
import json
import csv

class Alumnos:
    def GET(self):
        try:
            datos=web.input()     #Los datos introducidos por el usuario se almacenaran en datoS
            if datos['token']=="1234":#Si el usuario ingresa bien el token se declarara lo siguiente
                result=[]           #Un arreglo
                result2={}          #Un diccionario
                if datos['action']=="get":        #Si accion es get va a hacer lo siguiente
                    with open('static/csv/alumnos.csv','r') as csvfile:   #Ruta del archivo csv que va a leer, r es de lectura, csvfile es una variable cualquiera
                        reader = csv.DictReader(csvfile)         #Lector del archivo, DictReader te almacena los datos como en diccionario en este caso en la variable reader
                        for row in reader:              #Lee la primer fila y la manda la arreglo
                            result.append(row)          #Lo manda al arreglo result
                            result2['Version']="0.1.0"
                            result2['status']="200 OK"
                            result2['alumnos']=result      #Result2 en la posicion alumnos, sera lo que va a almacenar en result
                    return json.dumps(result2)          #Va a regresar un json del result2 que es lo que va almacenando el arreglo
                elif datos['action']=="search":
                    consulta={}
                    consulta['version']="0.2.0"
                    consulta['status']="200 ok"
                    result="matricula,nombre,primer_apellido,segundo_apellido,carrera\n"
                    with open('static/csv/alumnos.csv','r') as csvfile:
                        reader = csv.DictReader(csvfile)
                        result = []
                        for row in reader:
                            if str(row['matricula'])==datos['matricula']:
                                result.append(row)
                    return json.dumps(result)
                elif datos["action"] == "put":
                    consulta={}
                    consulta['version']="0.3.0"
                    consulta['status']="200 ok"
                    dato1 = datos["matricula"]
                    dato2 = datos["nombre"]
                    dato3 = datos["primer_apellido"]
                    dato4 = datos["segundo_apellido"]
                    dato5 = datos["carrera"]
                    result = []
                    result.append(dato1)
                    result.append(dato2)
                    result.append(dato3)
                    result.append(dato4)
                    result.append(dato5)
                    with open ('static/csv/alumnos.csv','a+', newline = '') as csvfiles:
                        writer = csv.writer(csvfiles)
                        writer.writerow(result)
                    return("SE HAN INGRESADO UN NUEVO REGISTRO")
                elif datos['action'] == "update":
                    consulta={}
                    consulta['version']="0.4.0"
                    consulta['status']="200 ok"
                    with open ('static/csv/alumnos.csv','r') as csvfiles:
                        reader =csv.DictReader(csvfiles)
                        l = []
                        val = 0
                        for row in reader:
                            result = []
                            if  str(row['matricula']) == datos['matricula']:
                 
                                with open ('static/csv/alumnos.csv','w') as csvfile:
                                    writer = csv.writer(csvfile)
                                    writer.writerow(row)
                                    va1 = datos["matricula"]
                                    va2 = datos["nombre"]
                                    va3 = datos["primer_apellido"]
                                    va4 = datos["segundo_apellido"]
                                    va5 = datos["carrera"]
                                    result.append(va1)
                                    result.append(va2)
                                    result.append(va3)
                                    result.append(va4)
                                    result.append(va5)
                                    l.append(result)
                            else:
                                fila1 = row['matricula'] 
                                fila2 = row['nombre']
                                fila3 = row['primer_apellido']
                                fila4 = row['segundo_apellido']
                                fila5 = row['carrera']
                                result.append(fila1)
                                result.append(fila2)
                                result.append(fila3)
                                result.append(fila4)
                                result.append(fila5)
                                l.append(result)
                        with open ('static/csv/alumnos.csv','a+', newline = '') as csvfiles:
                            writer = csv.writer(csvfiles)
                            for x in l:
                                writer.writerow(x)
                        if val == 0:
                            result.append("NO SE ENCONTRO EL DATO")
                    return json.dumps("SE HA ACTUALIZADO UN REGISTRO")
                elif datos['action'] == "delete":
                    consulta={}
                    consulta['version']="0.4.0"
                    consulta['status']="200 ok"
                    with open ('static/csv/alumnos.csv','r') as csvfiles:
                        reader =csv.DictReader(csvfiles)
                        m = []
                        val = 0
                        for row in reader:
                            result = []
                            if  str(row['matricula']) == datos['matricula']:
                                with open ('static/csv/alumnos.csv','w') as csvfile:
                                    writer = csv.writer(csvfile)
                                    writer.writerow(row)
                                    print("OKEY")
                            else:
                                fil1 = row['matricula'] 
                                fil2 = row['nombre']
                                fil3 = row['primer_apellido']
                                fil4 = row['segundo_apellido']
                                fil5 = row['carrera']
                                result.append(fil1)
                                result.append(fil2)
                                result.append(fil3)
                                result.append(fil4)
                                result.append(fil5)
                                m.append(result)
                            with open ('static/csv/alumnos.csv','a+', newline = '') as csvfiles:
                                writer = csv.writer(csvfiles)
                                writer.writerow(result)
                            if val == 0:
                                result.append("NO EXISTE NIGUN VALOR")
                        return json.dumps("SE HA ELIMINADO UN REGISTRO")
                else:                   
                    result2={}
                    result2['Version']="0.5.0"
                    result2['status']="Command not found"
                    return json.dumps(result2)
            else:
                result={}
                result['Version']="0.5.0"
                result['status']="Los datos insertados son incorrectos"
                return json.dumps(result)
        except Exception as e:
            result={}
            text= "Algo salio mal{}".format(e.args)
            result  ['status'] = text 
            return json.dumps(result)