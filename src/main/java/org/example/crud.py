# crud.py
from conexion import conectar
import mysql.connector

def conectar_base_de_datos():
    # Conectar a la base de datos MySQL
    try:
        conexion = mysql.connector.connect(
            host="localhost",  # Cambia si tu base de datos está en otro host
            user="root",  # Tu usuario de la base de datos
            password="curso",  # Tu contraseña de la base de datos
            database="nombre_de_tu_base_de_datos"  # El nombre de tu base de datos
        )
        if conexion.is_connected():
            print("Conexión exitosa a la base de datos")
        return conexion
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def agregar_encuesta(edad, sexo, consumo, problemas):
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        query = """INSERT INTO encuestas (edad, sexo, consumo_semanal, problemas_salud)
                   VALUES (%s, %s, %s, %s)"""
        datos = (edad, sexo, consumo, problemas)
        try:
            cursor.execute(query, datos)
            conexion.commit()
            return "Encuesta agregada exitosamente."
        except Exception as e:
            return f"Error al agregar encuesta: {e}"
        finally:
            cursor.close()
            conexion.close()
    else:
        return "No se pudo conectar a la base de datos."

def obtener_encuestas():
    conexion = conectar_base_de_datos()
    if conexion is None:
        return []  # Si no se pudo conectar, devolver lista vacía

    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM encuestas")  # Cambia 'encuestas' si el nombre de tu tabla es otro
    encuestas = cursor.fetchall()
    conexion.close()

    return [{
        'idencuesta': fila[0],
        'edad': fila[1],
        'sexo': fila[2],
        'BebidasSemana': fila[3],
        'CervezasSemana': fila[4],
        'BebidasFinSemana': fila[5],
        'BebidasDestiladasSemana': fila[6],
        'VinosSemana': fila[7],
        'PerdidasControl': fila[8],
        'DiversionDependenciaAlcohol': fila[9],
        'ProblemasDigestivos': fila[10],
        'TensionAlta': fila[11],
        'DolorCabeza': fila[12]
    } for fila in encuestas]



def actualizar_encuesta(idencuesta, edad, sexo, consumo, problemas):
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        query = """UPDATE encuestas 
                   SET edad=%s, sexo=%s, consumo_semanal=%s, problemas_salud=%s 
                   WHERE idencuesta=%s"""
        datos = (edad, sexo, consumo, problemas, idencuesta)
        try:
            cursor.execute(query, datos)
            conexion.commit()
            return "Encuesta actualizada exitosamente."
        except Exception as e:
            return f"Error al actualizar encuesta: {e}"
        finally:
            cursor.close()
            conexion.close()
    else:
        return "No se pudo conectar a la base de datos."

def eliminar_encuesta(idencuesta):
    conexion = conectar()
    if conexion:
        cursor = conexion.cursor()
        query = "DELETE FROM encuestas WHERE idencuesta=%s"
        try:
            cursor.execute(query, (idencuesta,))
            conexion.commit()
            return "Encuesta eliminada exitosamente."
        except Exception as e:
            return f"Error al eliminar encuesta: {e}"
        finally:
            cursor.close()
            conexion.close()
    else:
        return "No se pudo conectar a la base de datos."

