import tkinter as tk
from tkinter import ttk, messagebox
from crud import agregar_encuesta, obtener_encuestas, actualizar_encuesta, eliminar_encuesta
from exportacion import exportar_a_excel, exportar_a_excel_con_filtros
from graficos import grafico_consumo_promedio_por_edad, grafico_problemas_salud, grafico_consumo_edad

class AplicacionEncuestas:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Gestión de Encuestas")
        self.ventana.geometry("1400x600")

        self.frame = tk.Frame(self.ventana)
        self.frame.pack()

        # Entradas para agregar encuesta
        tk.Label(self.frame, text="Edad").grid(row=0, column=0)
        self.entrada_edad = tk.Entry(self.frame)
        self.entrada_edad.grid(row=0, column=1)

        tk.Label(self.frame, text="Sexo").grid(row=1, column=0)
        self.entrada_sexo = tk.Entry(self.frame)
        self.entrada_sexo.grid(row=1, column=1)

        tk.Label(self.frame, text="Consumo Semanal").grid(row=2, column=0)
        self.entrada_consumo = tk.Entry(self.frame)
        self.entrada_consumo.grid(row=2, column=1)

        tk.Label(self.frame, text="Problemas de Salud").grid(row=3, column=0)
        self.entrada_problemas = tk.Entry(self.frame)
        self.entrada_problemas.grid(row=3, column=1)

        # Filtros
        tk.Label(self.frame, text="Filtrar por Edad").grid(row=4, column=0)
        self.filtro_edad = tk.Entry(self.frame)
        self.filtro_edad.grid(row=4, column=1)

        tk.Label(self.frame, text="Filtrar por Sexo").grid(row=5, column=0)
        self.filtro_sexo = tk.Entry(self.frame)
        self.filtro_sexo.grid(row=5, column=1)

        # Botones
        self.frame_botones = tk.Frame(self.ventana)
        self.frame_botones.pack()

        self.btn_agregar = tk.Button(self.frame_botones, text="Agregar", command=self.agregar)
        self.btn_agregar.pack(side=tk.LEFT, padx=10)

        self.btn_exportar = tk.Button(self.frame_botones, text="Exportar a Excel", command=self.exportar)
        self.btn_exportar.pack(side=tk.LEFT, padx=10)

        self.btn_exportar_con_filtros = tk.Button(self.frame_botones, text="Exportar Filtrado", command=self.exportar_con_filtros)
        self.btn_exportar_con_filtros.pack(side=tk.LEFT, padx=10)

        self.btn_grafico = tk.Button(self.frame_botones, text="Mostrar Gráfico", command=self.mostrar_grafico)
        self.btn_grafico.pack(side=tk.LEFT, padx=10)

        # Tabla de encuestas
        self.tabla = ttk.Treeview(self.ventana, columns=("ID", "Edad", "Sexo", "Consumo", "Problemas"), show="headings")
        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Edad", text="Edad")
        self.tabla.heading("Sexo", text="Sexo")
        self.tabla.heading("Consumo", text="Consumo Semanal")
        self.tabla.heading("Problemas", text="Problemas de Salud")
        self.tabla.pack(fill="both", expand=True)

        # Cargar los datos
        self.cargar_datos()

    def agregar(self):
        edad = self.entrada_edad.get()
        sexo = self.entrada_sexo.get()
        consumo = self.entrada_consumo.get()
        problemas = self.entrada_problemas.get()
        mensaje = agregar_encuesta(edad, sexo, consumo, problemas)
        messagebox.showinfo("Resultado", mensaje)
        self.cargar_datos()

    def cargar_datos(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)
        encuestas = obtener_encuestas()
        for encuesta in encuestas:
            self.tabla.insert('', 'end', values=(encuesta['idencuesta'], encuesta['edad'], encuesta['sexo'], encuesta['consumo_semanal'], encuesta['problemas_salud']))

    def exportar(self):
        encuestas = obtener_encuestas()
        mensaje = exportar_a_excel(encuestas)
        messagebox.showinfo("Resultado", mensaje)

    def exportar_con_filtros(self):
        # Obtener los filtros
        edad_filtro = self.filtro_edad.get()
        sexo_filtro = self.filtro_sexo.get()

        # Filtrar las encuestas
        encuestas = obtener_encuestas()
        encuestas_filtradas = [encuesta for encuesta in encuestas if
                               (edad_filtro == "" or str(encuesta['edad']) == edad_filtro) and
                               (sexo_filtro == "" or encuesta['sexo'].lower() == sexo_filtro.lower())]

        if encuestas_filtradas:
            mensaje = exportar_a_excel_con_filtros(encuestas_filtradas)
            messagebox.showinfo("Resultado", mensaje)
        else:
            messagebox.showerror("Error", "No se encontraron encuestas que coincidan con los filtros.")

    def mostrar_grafico(self):
        encuestas = obtener_encuestas()

        if encuestas:
            grafico_consumo_promedio_por_edad(encuestas)
            # o elegir otro gráfico, por ejemplo:
            # grafico_problemas_salud(encuestas)
            # grafico_consumo_edad(encuestas)
        else:
            messagebox.showerror("Error", "No hay datos disponibles para graficar.")

# Ejecutar la aplicación
if __name__ == "__main__":
    ventana = tk.Tk()
    app = AplicacionEncuestas(ventana)
    ventana.mainloop()
