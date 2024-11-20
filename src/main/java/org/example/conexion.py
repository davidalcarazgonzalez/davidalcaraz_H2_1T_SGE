import tkinter as tk
from tkinter import messagebox
import mysql.connector
from tkinter import ttk

# Conectar a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="curso",
    database="encuestas"
)

cursor = conexion.cursor()

# Función para guardar la encuesta
def guardar_encuesta():
    try:
        # Obtener los valores de los campos
        edad = edad_entry.get()
        sexo = sexo_entry.get()
        bebidas_semana = bebidas_entry.get()
        cervezas_semana = cervezas_entry.get()
        bebidas_finde = bebidas_finde_entry.get()
        bebidas_destiladas = bebidas_destiladas_entry.get()
        vinos = vinos_entry.get()
        perdidas_control = perdidas_control_entry.get()
        dependencia = dependencia_entry.get()
        digestivos = digestivos_entry.get()
        tension_alta = tension_alta_entry.get()
        dolor_cabeza = dolor_cabeza_entry.get()

        # Validar que todos los campos estén completos
        if not (edad and sexo and bebidas_semana and cervezas_semana and bebidas_finde and bebidas_destiladas and vinos
                and perdidas_control and dependencia and digestivos and tension_alta and dolor_cabeza):
            messagebox.showwarning("Campos incompletos", "Por favor, rellene todos los campos.")
            return

        # Obtener el último idEncuesta insertado
        cursor.execute("SELECT MAX(idEncuesta) FROM ENCUESTA")
        ultimo_id = cursor.fetchone()[0]

        # Si no hay registros, comenzamos con el id 1
        if ultimo_id is None:
            nuevo_id = 1
        else:
            nuevo_id = ultimo_id + 1  # Incrementar el último id

        # Insertar el nuevo registro en la base de datos
        cursor.execute(
            "INSERT INTO ENCUESTA (idEncuesta, edad, Sexo, BebidasSemana, CervezasSemana, BebidasFinSemana, BebidasDestiladasSemana, "
            "VinosSemana, PerdidasControl, DiversionDependenciaAlcohol, ProblemasDigestivos, TensionAlta, DolorCabeza) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (nuevo_id, edad, sexo, bebidas_semana, cervezas_semana, bebidas_finde, bebidas_destiladas, vinos, perdidas_control,
             dependencia, digestivos, tension_alta, dolor_cabeza)
        )
        conexion.commit()
        messagebox.showinfo("Éxito", "Encuesta agregada correctamente.")
        ventana_agregar.destroy()  # Cerrar la ventana de agregar encuesta
        mostrar_encuestas()  # Actualizar la vista de las encuestas

    except Exception as e:
        messagebox.showerror("Error", f"No se pudo agregar la encuesta: {e}")

# Función para abrir la ventana de agregar encuesta
def abrir_agregar_encuesta():
    global ventana_agregar, edad_entry, sexo_entry, bebidas_entry, cervezas_entry, bebidas_finde_entry
    global bebidas_destiladas_entry, vinos_entry, perdidas_control_entry, dependencia_entry, digestivos_entry
    global tension_alta_entry, dolor_cabeza_entry

    ventana_agregar = tk.Toplevel(ventana)
    ventana_agregar.title("Agregar Encuesta")

    # Crear los labels y entries
    tk.Label(ventana_agregar, text="Edad").grid(row=0, column=0)
    edad_entry = tk.Entry(ventana_agregar)
    edad_entry.grid(row=0, column=1)

    tk.Label(ventana_agregar, text="Sexo").grid(row=1, column=0)
    sexo_entry = tk.Entry(ventana_agregar)
    sexo_entry.grid(row=1, column=1)

    tk.Label(ventana_agregar, text="Bebidas por semana").grid(row=2, column=0)
    bebidas_entry = tk.Entry(ventana_agregar)
    bebidas_entry.grid(row=2, column=1)

    tk.Label(ventana_agregar, text="Cervezas por semana").grid(row=3, column=0)
    cervezas_entry = tk.Entry(ventana_agregar)
    cervezas_entry.grid(row=3, column=1)

    tk.Label(ventana_agregar, text="Bebidas fin de semana").grid(row=4, column=0)
    bebidas_finde_entry = tk.Entry(ventana_agregar)
    bebidas_finde_entry.grid(row=4, column=1)

    tk.Label(ventana_agregar, text="Bebidas destiladas por semana").grid(row=5, column=0)
    bebidas_destiladas_entry = tk.Entry(ventana_agregar)
    bebidas_destiladas_entry.grid(row=5, column=1)

    tk.Label(ventana_agregar, text="Vinos por semana").grid(row=6, column=0)
    vinos_entry = tk.Entry(ventana_agregar)
    vinos_entry.grid(row=6, column=1)

    tk.Label(ventana_agregar, text="Pérdida de control").grid(row=7, column=0)
    perdidas_control_entry = tk.Entry(ventana_agregar)
    perdidas_control_entry.grid(row=7, column=1)

    tk.Label(ventana_agregar, text="Dependencia alcohol").grid(row=8, column=0)
    dependencia_entry = tk.Entry(ventana_agregar)
    dependencia_entry.grid(row=8, column=1)

    tk.Label(ventana_agregar, text="Problemas digestivos").grid(row=9, column=0)
    digestivos_entry = tk.Entry(ventana_agregar)
    digestivos_entry.grid(row=9, column=1)

    tk.Label(ventana_agregar, text="Tensión alta").grid(row=10, column=0)
    tension_alta_entry = tk.Entry(ventana_agregar)
    tension_alta_entry.grid(row=10, column=1)

    tk.Label(ventana_agregar, text="Dolor de cabeza").grid(row=11, column=0)
    dolor_cabeza_entry = tk.Entry(ventana_agregar)
    dolor_cabeza_entry.grid(row=11, column=1)

    # Botón para guardar la encuesta
    tk.Button(ventana_agregar, text="Guardar Encuesta", command=guardar_encuesta).grid(row=12, column=0, columnspan=2)

# Función para mostrar las encuestas en una tabla
def mostrar_encuestas():
    # Limpiar la tabla antes de mostrar las nuevas encuestas
    for item in treeview.get_children():
        treeview.delete(item)

    try:
        cursor.execute("SELECT * FROM ENCUESTA")
        encuestas = cursor.fetchall()

        # Mostrar las encuestas en el treeview
        for encuesta in encuestas:
            treeview.insert("", "end", values=encuesta)

    except Exception as e:
        messagebox.showerror("Error", f"No se pudieron cargar las encuestas: {e}")

# Función para abrir la ventana de actualización
def abrir_actualizar_encuesta():
    seleccion = treeview.selection()
    if seleccion:
        id_encuesta = treeview.item(seleccion)["values"][0]  # Asumimos que la primera columna es el ID

        # Obtener los datos de la encuesta seleccionada
        cursor.execute("SELECT * FROM ENCUESTA WHERE idEncuesta = %s", (id_encuesta,))
        encuesta = cursor.fetchone()

        if encuesta:
            global ventana_actualizar, edad_entry, sexo_entry, bebidas_entry, cervezas_entry, bebidas_finde_entry
            global bebidas_destiladas_entry, vinos_entry, perdidas_control_entry, dependencia_entry, digestivos_entry
            global tension_alta_entry, dolor_cabeza_entry

            ventana_actualizar = tk.Toplevel(ventana)
            ventana_actualizar.title("Actualizar Encuesta")

            # Crear los labels y entries con los valores de la encuesta seleccionada
            tk.Label(ventana_actualizar, text="Edad").grid(row=0, column=0)
            edad_entry = tk.Entry(ventana_actualizar)
            edad_entry.insert(0, encuesta[1])  # Rellenar con el valor de la encuesta
            edad_entry.grid(row=0, column=1)

            tk.Label(ventana_actualizar, text="Sexo").grid(row=1, column=0)
            sexo_entry = tk.Entry(ventana_actualizar)
            sexo_entry.insert(0, encuesta[2])  # Rellenar con el valor de la encuesta
            sexo_entry.grid(row=1, column=1)

            tk.Label(ventana_actualizar, text="Bebidas por semana").grid(row=2, column=0)
            bebidas_entry = tk.Entry(ventana_actualizar)
            bebidas_entry.insert(0, encuesta[3])  # Rellenar con el valor de la encuesta
            bebidas_entry.grid(row=2, column=1)

            tk.Label(ventana_actualizar, text="Cervezas por semana").grid(row=3, column=0)
            cervezas_entry = tk.Entry(ventana_actualizar)
            cervezas_entry.insert(0, encuesta[4])  # Rellenar con el valor de la encuesta
            cervezas_entry.grid(row=3, column=1)

            tk.Label(ventana_actualizar, text="Bebidas fin de semana").grid(row=4, column=0)
            bebidas_finde_entry = tk.Entry(ventana_actualizar)
            bebidas_finde_entry.insert(0, encuesta[5])  # Rellenar con el valor de la encuesta
            bebidas_finde_entry.grid(row=4, column=1)

            tk.Label(ventana_actualizar, text="Bebidas destiladas por semana").grid(row=5, column=0)
            bebidas_destiladas_entry = tk.Entry(ventana_actualizar)
            bebidas_destiladas_entry.insert(0, encuesta[6])  # Rellenar con el valor de la encuesta
            bebidas_destiladas_entry.grid(row=5, column=1)

            tk.Label(ventana_actualizar, text="Vinos por semana").grid(row=6, column=0)
            vinos_entry = tk.Entry(ventana_actualizar)
            vinos_entry.insert(0, encuesta[7])  # Rellenar con el valor de la encuesta
            vinos_entry.grid(row=6, column=1)

            tk.Label(ventana_actualizar, text="Pérdida de control").grid(row=7, column=0)
            perdidas_control_entry = tk.Entry(ventana_actualizar)
            perdidas_control_entry.insert(0, encuesta[8])  # Rellenar con el valor de la encuesta
            perdidas_control_entry.grid(row=7, column=1)

            tk.Label(ventana_actualizar, text="Dependencia alcohol").grid(row=8, column=0)
            dependencia_entry = tk.Entry(ventana_actualizar)
            dependencia_entry.insert(0, encuesta[9])  # Rellenar con el valor de la encuesta
            dependencia_entry.grid(row=8, column=1)

            tk.Label(ventana_actualizar, text="Problemas digestivos").grid(row=9, column=0)
            digestivos_entry = tk.Entry(ventana_actualizar)
            digestivos_entry.insert(0, encuesta[10])  # Rellenar con el valor de la encuesta
            digestivos_entry.grid(row=9, column=1)

            tk.Label(ventana_actualizar, text="Tensión alta").grid(row=10, column=0)
            tension_alta_entry = tk.Entry(ventana_actualizar)
            tension_alta_entry.insert(0, encuesta[11])  # Rellenar con el valor de la encuesta
            tension_alta_entry.grid(row=10, column=1)

            tk.Label(ventana_actualizar, text="Dolor de cabeza").grid(row=11, column=0)
            dolor_cabeza_entry = tk.Entry(ventana_actualizar)
            dolor_cabeza_entry.insert(0, encuesta[12])  # Rellenar con el valor de la encuesta
            dolor_cabeza_entry.grid(row=11, column=1)

            # Botón para guardar la encuesta actualizada
            tk.Button(ventana_actualizar, text="Actualizar Encuesta", command=lambda: actualizar_encuesta(id_encuesta)).grid(row=12, column=0, columnspan=2)

# Función para actualizar la encuesta en la base de datos
def actualizar_encuesta(id_encuesta):
    try:
        # Obtener los valores de los campos
        edad = edad_entry.get()
        sexo = sexo_entry.get()
        bebidas_semana = bebidas_entry.get()
        cervezas_semana = cervezas_entry.get()
        bebidas_finde = bebidas_finde_entry.get()
        bebidas_destiladas = bebidas_destiladas_entry.get()
        vinos = vinos_entry.get()
        perdidas_control = perdidas_control_entry.get()
        dependencia = dependencia_entry.get()
        digestivos = digestivos_entry.get()
        tension_alta = tension_alta_entry.get()
        dolor_cabeza = dolor_cabeza_entry.get()

        # Validar que todos los campos estén completos
        if not (edad and sexo and bebidas_semana and cervezas_semana and bebidas_finde and bebidas_destiladas and vinos
                and perdidas_control and dependencia and digestivos and tension_alta and dolor_cabeza):
            messagebox.showwarning("Campos incompletos", "Por favor, rellene todos los campos.")
            return

        # Actualizar la encuesta en la base de datos
        cursor.execute(
            "UPDATE ENCUESTA SET edad=%s, Sexo=%s, BebidasSemana=%s, CervezasSemana=%s, BebidasFinSemana=%s, "
            "BebidasDestiladasSemana=%s, VinosSemana=%s, PerdidasControl=%s, DiversionDependenciaAlcohol=%s, "
            "ProblemasDigestivos=%s, TensionAlta=%s, DolorCabeza=%s WHERE idEncuesta=%s",
            (edad, sexo, bebidas_semana, cervezas_semana, bebidas_finde, bebidas_destiladas, vinos, perdidas_control,
             dependencia, digestivos, tension_alta, dolor_cabeza, id_encuesta)
        )
        conexion.commit()
        messagebox.showinfo("Éxito", "Encuesta actualizada correctamente.")
        ventana_actualizar.destroy()  # Cerrar la ventana de actualización
        mostrar_encuestas()  # Actualizar la vista de las encuestas

    except Exception as e:
        messagebox.showerror("Error", f"No se pudo actualizar la encuesta: {e}")

# Función para eliminar encuesta
def eliminar_encuesta():
    seleccion = treeview.selection()
    if seleccion:
        id_encuesta = treeview.item(seleccion)["values"][0]  # Asumimos que la primera columna es el ID

        # Eliminar la encuesta de la base de datos
        cursor.execute("DELETE FROM ENCUESTA WHERE idEncuesta = %s", (id_encuesta,))
        conexion.commit()
        messagebox.showinfo("Éxito", "Encuesta eliminada correctamente.")
        mostrar_encuestas()  # Actualizar la vista de las encuestas

# Función para mostrar encuestas filtradas y ordenadas
def mostrar_filtros_orden():
    try:
        filtro = filtro_entry.get()  # Obtiene el campo por el cual filtrar
        valor_filtro = valor_filtro_entry.get()  # Valor del filtro
        orden = orden_combo.get()  # Campo por el cual ordenar
        direccion = direccion_combo.get()  # Dirección del orden (ASC o DESC)

        # Construcción dinámica de la consulta
        consulta = "SELECT * FROM ENCUESTA"
        condiciones = []
        if filtro and valor_filtro:
            condiciones.append(f"{filtro} = %s")
        if condiciones:
            consulta += " WHERE " + " AND ".join(condiciones)
        if orden:
            consulta += f" ORDER BY {orden} {direccion}"

        # Ejecución de la consulta
        valores = [valor_filtro] if filtro and valor_filtro else []
        cursor.execute(consulta, valores)
        encuestas = cursor.fetchall()

        # Limpiar la tabla antes de mostrar los resultados
        for item in treeview.get_children():
            treeview.delete(item)

        # Mostrar los resultados en el Treeview
        for encuesta in encuestas:
            treeview.insert("", "end", values=encuesta)

    except Exception as e:
        messagebox.showerror("Error", f"No se pudieron aplicar los filtros y ordenación: {e}")

# Función para abrir la ventana de filtros y ordenación
def abrir_filtros_orden():
    global ventana_filtros, filtro_entry, valor_filtro_entry, orden_combo, direccion_combo

    ventana_filtros = tk.Toplevel(ventana)
    ventana_filtros.title("Filtros y Ordenación")

    tk.Label(ventana_filtros, text="Campo para filtrar").grid(row=0, column=0)
    filtro_entry = ttk.Combobox(
        ventana_filtros, values=["edad", "Sexo", "BebidasSemana", "CervezasSemana", "BebidasFinSemana",
                                 "BebidasDestiladasSemana", "VinosSemana", "PerdidasControl",
                                 "DiversionDependenciaAlcohol", "ProblemasDigestivos", "TensionAlta", "DolorCabeza"])
    filtro_entry.grid(row=0, column=1)

    tk.Label(ventana_filtros, text="Valor del filtro").grid(row=1, column=0)
    valor_filtro_entry = tk.Entry(ventana_filtros)
    valor_filtro_entry.grid(row=1, column=1)

    tk.Label(ventana_filtros, text="Campo para ordenar").grid(row=2, column=0)
    orden_combo = ttk.Combobox(
        ventana_filtros, values=["edad", "Sexo", "BebidasSemana", "CervezasSemana", "BebidasFinSemana",
                                 "BebidasDestiladasSemana", "VinosSemana", "PerdidasControl",
                                 "DiversionDependenciaAlcohol", "ProblemasDigestivos", "TensionAlta", "DolorCabeza"])
    orden_combo.grid(row=2, column=1)

    tk.Label(ventana_filtros, text="Dirección del orden").grid(row=3, column=0)
    direccion_combo = ttk.Combobox(ventana_filtros, values=["ASC", "DESC"])
    direccion_combo.grid(row=3, column=1)

    tk.Button(ventana_filtros, text="Aplicar", command=mostrar_filtros_orden).grid(row=4, column=0, columnspan=2)

# Ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Encuestas")

# Treeview para mostrar las encuestas
treeview = ttk.Treeview(ventana, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13), show="headings")
treeview.pack(fill=tk.BOTH, expand=True)

# Encabezados del Treeview
headers = ["ID", "Edad", "Sexo", "Bebidas Semana", "Cervezas Semana", "Bebidas Fin Semana", "Bebidas Destiladas",
           "Vinos Semana", "Pérdidas Control", "Dependencia Alcohol", "Problemas Digestivos", "Tensión Alta", "Dolor Cabeza"]
for i, header in enumerate(headers, start=1):
    treeview.heading(i, text=header)

# Botones de control
tk.Button(ventana, text="Agregar Encuesta", command=abrir_agregar_encuesta).pack(side=tk.LEFT, padx=5, pady=5)
tk.Button(ventana, text="Actualizar Encuesta", command=abrir_actualizar_encuesta).pack(side=tk.LEFT, padx=5, pady=5)
tk.Button(ventana, text="Filtrar y Ordenar", command=abrir_filtros_orden).pack(side=tk.LEFT, padx=5, pady=5)


# Cargar encuestas al inicio
mostrar_encuestas()

# Ejecutar la aplicación
ventana.mainloop()


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Encuestas")

# Crear el treeview para mostrar las encuestas
treeview = ttk.Treeview(ventana, columns=("idEncuesta", "Edad", "Sexo", "BebidasSemana", "CervezasSemana", "BebidasFinSemana", "BebidasDestiladasSemana",
                                          "VinosSemana", "PerdidasControl", "DiversionDependenciaAlcohol", "ProblemasDigestivos", "TensionAlta", "DolorCabeza"),
                        show="headings",height=35)

# Definir las columnas
for col in treeview["columns"]:
    treeview.heading(col, text=col)
    treeview.column(col, width=130)


treeview.grid(row=0, column=0, columnspan=4)

# Botones para gestionar las encuestas
tk.Button(ventana, text="Agregar Encuesta", command=abrir_agregar_encuesta).grid(row=1, column=0)
tk.Button(ventana, text="Actualizar Encuesta", command=abrir_actualizar_encuesta).grid(row=1, column=1)
tk.Button(ventana, text="Eliminar Encuesta", command=eliminar_encuesta).grid(row=1, column=2)


# Cargar las encuestas al iniciar la ventana
mostrar_encuestas()

ventana.mainloop()
