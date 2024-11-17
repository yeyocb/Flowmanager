import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from random import randint

class Proyecto:
    def __init__(self, codigo, nombre, descripcion, jefeProyecto):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__jefeProyecto = jefeProyecto
    def getCodigo(self): return self.__codigo
    def getNombre(self): return self.__nombre
    def getDescripcion(self): return self.__descripcion
    def getJefeProyecto(self): return self.__jefeProyecto
    def generateData(self): print('Generate')

class Miembro:
    def __init__(self, dni, nombre, rol):
        self.__dni = dni
        self.__nombre = nombre
        self.__rol = rol # jefeProyecto, desarollador, QA
    def getDni(self): return self.__dni
    def getNombre(self): return self.__nombre
    def getRol(self): return self.__rol
    def generateData(self): print('Generate')

class Incidencia:
    def __init__(self, numeroIncidenia, proyecto, fechaHora, tipoPrueba, tipoIncidencia,
                 miembroDesarrollador, miembroQA, descripcion, fechaHoraQA, fechaHoraDesa, fechaHoraCierre, desarrolladorSol):
        self.__numeroIncidenia = numeroIncidenia
        self.__proyecto = proyecto
        self.__fechaHora = fechaHora
        self.__tipoPrueba = tipoPrueba # Pruebas Funcionales, Pruebas de Integración, Pruebas de Validación, Pruebas de Regresión, Pruebas de Carga
        self.__tipoIncidencia = tipoIncidencia # Falla de sistema, performance, usabilidad
        self.__miembroDesarrollador = miembroDesarrollador
        self.__miembroQA = miembroQA
        self.__descripcion = descripcion
        self.__fechaHoraQA = fechaHoraQA
        self.__fechaHoraDesa = fechaHoraDesa
        self.__fechaHoraCierre = fechaHoraCierre
        self.__desarrolladorSol = desarrolladorSol
        self.__estado = 'Abierto'
    def getNumeroIncidencia(self): return self.__numeroIncidenia
    def getProyecto(self): return self.__proyecto
    def getFechaHora(self): return self.__fechaHora
    def getTipoPrueba(self): return self.__tipoPrueba
    def getTipoIncidencia(self): return self.__tipoIncidencia
    def getMiembroDesarrollador(self): return self.__miembroDesarrollador
    def getMiembroQA(self): return self.__miembroQA
    def getDescripcion(self): return self.__descripcion
    def getFechaHoraQA(self): return self.__fechaHoraQA
    def getFechaHoraDesa(self): return self.__fechaHoraDesa
    def getFechaHoraCierre(self): return self.__fechaHoraCierre
    def getDesarrolladorSol(self): return self.__desarrolladorSol
    def getEstado(self): return self.__estado
    def setEstado(self, estado): self.__estado = estado
    def generateData(self): print('Generate')

class FlowManagerApp:
    def __init__(self, nameCSV):
        self.data = pd.read_csv(nameCSV)

    def generarDatos(self):
        if st.button("Generar Indicencias"):
            cantidadInci = randint(1000, 2000)
            st.success(f"Se ha generado {cantidadInci} Incidencias.")

    def actualizarIncidencia(self):
        st.write("## Actualizar Incidencia")

        st.subheader("Lista de Incidencias")
        st.dataframe(self.data)
        idIncidencia = st.number_input("Introduce el Id de la Incidencia:", min_value=1, max_value=len(self.data), step=1)
        estados = ["Abierto", "En progreso", "Listo para QA", "Reasignado", "Cerrado"]

        nuevoEstado = st.selectbox("Selecciona el estado:", estados)

        if st.button("Guardar Cambios"):
            if idIncidencia in self.data["NumeroIncidencia"].values:
                self.data.loc[self.data["NumeroIncidencia"] == idIncidencia, "Estado"] = nuevoEstado
                st.success(f"Se ha actualizado la incidencia {idIncidencia} a {nuevoEstado}.")
            else:
                st.error("El numero de incidencia ingresado no existe en la lista de incidencias.")

        st.subheader("Lista de Incidencias Actualizada")
        st.dataframe(self.data)

    def verReportes(self):
        st.write("### Reporte por tipo de Prueba")
        prueba_counts = self.data['TipoPrueba'].value_counts()
        plt.figure(figsize=(11, 8))
        prueba_counts.plot(kind='bar')
        plt.title("Cantidad de Incidencias por Tipo de Prueba")
        plt.ylabel("Cantidad")
        plt.xlabel("Tipo de Prueba")
        plt.xticks(rotation=0)
        st.pyplot(plt)

        st.write("### Reporte por Tipo de Incidencia")
        incidencia_counts = self.data['TipoIncidencia'].value_counts()
        plt.figure(figsize=(8, 5))
        incidencia_counts.plot(kind='bar', color='orange')
        plt.title("Cantidad de Incidencias por Tipo de Incidencia")
        plt.ylabel("Cantidad")
        plt.xlabel("Tipo de Incidencia")
        plt.xticks(rotation=0)
        st.pyplot(plt)

        st.write("### Reporte por Desarrollador Responsable de la Incidencia")
        desarrollador_counts = self.data['MiembroDesarrollador'].value_counts()
        plt.figure(figsize=(8, 5))
        desarrollador_counts.plot(kind='bar', color='green')
        plt.title("Cantidad de Incidencias por Desarrollador Responsable")
        plt.ylabel("Cantidad")
        plt.xlabel("Desarrollador")
        plt.xticks(rotation=0)
        plt.tight_layout()
        st.pyplot(plt)

        st.write("### Reporte por QA Responsables de la Prueba ")
        qa_counts = self.data['MiembroQA'].value_counts()
        plt.figure(figsize=(8, 5))
        qa_counts.plot(kind='bar', color='purple')
        plt.title("Cantidad de Incidencias por QA Responsable")
        plt.ylabel("Cantidad")
        plt.xlabel("QA Responsable")
        plt.xticks(rotation=0)
        plt.tight_layout()
        st.pyplot(plt)

        st.write("### Reporte por Desarrollador Responsables de la Solución")
        desarrollador_sol_counts = self.data['DesarrolladorSol'].value_counts()
        plt.figure(figsize=(8, 5))
        desarrollador_sol_counts.plot(kind='bar', color='red')
        plt.title("Cantidad de Incidencias por Desarrollador Responsable de la Solución")
        plt.ylabel("Cantidad")
        plt.xlabel("Desarrollador de la Solución")
        plt.xticks(rotation=0)
        plt.tight_layout()
        st.pyplot(plt)

    def menu(self):
        st.title("Aseguramiento y Gestión de Calidad de Software")
        st.sidebar.title("Navegación")

        menuOpcion = st.sidebar.radio(
            "Navegación:",
            ("Generar", "Actualizar Incidencia", "Reportes")
        )

        if menuOpcion == "Generar":
            st.write("## Generar Datos")
            st.write("### Selecciona un boton para generar los datos.")
            self.generarDatos()
        elif menuOpcion == "Actualizar Incidencia":
            self.actualizarIncidencia()
        elif menuOpcion == "Reportes":
            self.verReportes()

def main():
    app = FlowManagerApp('incidencias.csv')
    app.menu()

if __name__ == "__main__":
    main()