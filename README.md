### **README - Gestión de Encuestas sobre Consumo de Alcohol y Salud**

---

#### **Descripción del Proyecto**
La aplicación **Gestión de Encuestas sobre Consumo de Alcohol y Salud** es una herramienta interactiva desarrollada en Python con una interfaz gráfica basada en Tkinter y conexión a MySQL. Está diseñada para gestionar datos sobre encuestas relacionadas con el consumo de alcohol y su impacto en la salud, permitiendo realizar análisis detallados y exportar resultados para su evaluación externa.

---

#### **Características Principales**
1. **Interfaz de Usuario con Tkinter**  
   - Fácil de usar, con formularios para la entrada de datos y botones para realizar operaciones CRUD.  
   
2. **Conexión a Base de Datos MySQL**  
   - Almacenamiento eficiente y seguro de las encuestas.  
   
3. **Operaciones CRUD**  
   - Crear, Leer, Actualizar y Eliminar encuestas directamente desde la interfaz.  

4. **Consultas y Filtros Personalizados**  
   - Permite ordenar y filtrar los datos basándose en criterios como edad, sexo o consumo semanal.  

5. **Exportación a Excel**  
   - Genera archivos Excel con los datos seleccionados para análisis externo.  

6. **Visualización Gráfica de los Datos**  
   - Gráficos interactivos que muestran patrones y relaciones en los datos.

---

#### **Requisitos del Sistema**
- **Python** 3.8 o superior  
- **MySQL Server** (con base de datos configurada)  
- Librerías de Python requeridas:  
  - `tkinter`
  - `pymysql`
  - `matplotlib`
  - `pandas`
  - `openpyxl`

---

#### **Configuración del Proyecto**
1. **Clonar el repositorio**  
   ```bash
   git clone <URL-del-repositorio>
   cd gestion-encuestas
   ```

2. **Configurar la base de datos MySQL**  
   - Crear una base de datos llamada `encuestasDB`.  
   - Ejecutar el archivo SQL para crear la tabla necesaria:  

   ```sql
   CREATE TABLE encuestas (
       idencuesta INT AUTO_INCREMENT PRIMARY KEY,
       edad INT,
       sexo VARCHAR(10),
       consumo_semanal INT,
       problemas_salud VARCHAR(255)
   );
   ```

3. **Instalar las dependencias necesarias**  
   ```bash
   pip install pymysql pandas matplotlib openpyxl
   ```

4. **Ejecutar la aplicación**  
   ```bash
   python app_encuestas.py
   ```

---

#### **Uso de la Aplicación**
1. **Gestión de Datos**  
   - Ingrese datos de encuestas mediante el formulario y guárdelos con el botón "Agregar".  
   - Actualice registros existentes seleccionándolos y modificando los campos.  
   - Elimine encuestas no deseadas directamente desde la interfaz.  

2. **Consultas y Filtros**  
   - Filtre los datos por criterios específicos, como edades o problemas de salud.  
   - Ordene los resultados por campos como consumo semanal o edad.  

3. **Exportación a Excel**  
   - Guarde los resultados filtrados o completos en un archivo Excel haciendo clic en "Exportar".  

4. **Generación de Gráficos**  
   - Visualice patrones en el consumo de alcohol mediante gráficos de barras, líneas o dispersión.

---

#### **Estructura del Proyecto**
- **`app_encuestas.py`**: Archivo principal, contiene la lógica de la interfaz y las interacciones del usuario.  
- **`crud.py`**: Funciones para conectar con MySQL y realizar operaciones CRUD.  
- **`exportacion.py`**: Funciones para exportar datos a Excel.  
- **`graficos.py`**: Genera gráficos basados en los datos de las encuestas.  

---


1. Interfaz principal con formulario y tabla de datos.  
2. Gráficos representando el consumo de alcohol por edades.  
3. Ejemplo de archivo Excel exportado.


---

#### **Contribuciones**
Las contribuciones son bienvenidas. Si desea colaborar:  
1. Haga un fork del proyecto.  
2. Cree una rama nueva para su contribución.  
3. Realice un pull request describiendo los cambios realizados.

---

#### **Autor**
**David** - Proyecto desarrollado como parte del análisis de datos sobre consumo de alcohol y salud en el marco de un ejercicio académico.
