import tkinter as tk
from tkinter import messagebox
import re

class Alumno:
    def __init__(self, ci, apellidos, nombre, nota):
        self.ci = ci
        self.apellidos = apellidos
        self.nombre = nombre
        self.nota = nota
        self.calificacion = self.calcular_calificacion()

    def calcular_calificacion(self):
        if self.nota < 5:
            return "SS"
        elif 5 <= self.nota < 7:
            return "AP"
        elif 7 <= self.nota < 9:
            return "NT"
        else:
            return "SB"

    def __str__(self):
        return f"{self.ci} {self.apellidos}, {self.nombre} {self.nota} {self.calificacion}"

class GestionCalificaciones:
    def __init__(self):
        self.alumnos = []

    def mostrar_alumnos(self):
        self.alumnos_text.delete(1.0, tk.END)
        for alumno in self.alumnos:
            self.alumnos_text.insert(tk.END, f"{alumno}\n")

    def introducir_alumno(self):
        ci = self.ci_entry.get()
        apellidos = self.apellidos_entry.get()
        nombre = self.nombre_entry.get()
        try:
            nota = float(self.nota_entry.get())
        except ValueError:
            messagebox.showerror("Error", "La nota debe ser un número.")
            return

        # Validación del CI (solo números)
        if not ci.isdigit():
            messagebox.showerror("Error", "El CI debe contener solo números.")
            return

        # Validación de apellidos y nombre (solo letras)
        if not apellidos.isalpha():
            messagebox.showerror("Error", "Los apellidos deben contener solo letras.")
            return

        if not nombre.isalpha():
            messagebox.showerror("Error", "El nombre debe contener solo letras.")
            return

        # Validación de la nota (debe ser un número en el rango adecuado)
        if nota < 0 or nota > 10:
            messagebox.showerror("Error", "La nota debe ser un número entre 0 y 10.")
            return

        if any(alumno.ci == ci for alumno in self.alumnos):
            messagebox.showerror("Error", f"Ya existe un alumno con CI {ci}.")
        else:
            nuevo_alumno = Alumno(ci, apellidos, nombre, nota)
            self.alumnos.append(nuevo_alumno)
            messagebox.showinfo("Éxito", "Alumno introducido correctamente.")
            self.mostrar_alumnos()
            self.borrar_campos()  # Limpiar los campos de entrada después de agregar el alumno

    def eliminar_alumno(self):
        ci = self.ci_entry.get()
        self.alumnos = [alumno for alumno in self.alumnos if alumno.ci != ci]
        messagebox.showinfo("Éxito", f"Alumno con CI {ci} eliminado correctamente.")
        self.mostrar_alumnos()

    def consultar_nota_y_calificacion(self):
        ci = self.ci_entry.get()
        for alumno in self.alumnos:
            if alumno.ci == ci:
                messagebox.showinfo("Resultado", f"Nota: {alumno.nota}, Calificación: {alumno.calificacion}")
                return
        messagebox.showerror("Error", f"No se encontró el alumno con CI {ci}.")

    def modificar_nota(self):
        ci = self.ci_entry.get()
        try:
            nueva_nota = float(self.nota_entry.get())
        except ValueError:
            messagebox.showerror("Error", "La nota debe ser un número.")
            return

        if nueva_nota < 0 or nueva_nota > 10:
            messagebox.showerror("Error", "La nota debe estar entre 0 y 10.")
            return

        for alumno in self.alumnos:
            if alumno.ci == ci:
                alumno.nota = nueva_nota
                alumno.calificacion = alumno.calcular_calificacion()
                messagebox.showinfo("Éxito", f"Nota del alumno con CI {ci} modificada correctamente.")
                self.mostrar_alumnos()
                return
        messagebox.showerror("Error", f"No se encontró el alumno con CI {ci}.")

    def mostrar_suspensos(self):
        suspensos = [alumno for alumno in self.alumnos if alumno.calificacion == "SS"]
        if suspensos:
            self.alumnos_text.delete(1.0, tk.END)
            for alumno in suspensos:
                self.alumnos_text.insert(tk.END, f"{alumno}\n")
        else:
            messagebox.showinfo("Resultado", "No hay alumnos suspensos.")

    def mostrar_aprobados(self):
        aprobados = [alumno for alumno in self.alumnos if alumno.calificacion != "SS"]
        if aprobados:
            self.alumnos_text.delete(1.0, tk.END)
            for alumno in aprobados:
                self.alumnos_text.insert(tk.END, f"{alumno}\n")
        else:
            messagebox.showinfo("Resultado", "No hay alumnos aprobados.")

    def mostrar_matricula_de_honor(self):
        mh = [alumno for alumno in self.alumnos if alumno.nota == 10]
        if mh:
            self.alumnos_text.delete(1.0, tk.END)
            for alumno in mh:
                self.alumnos_text.insert(tk.END, f"{alumno}\n")
        else:
            messagebox.showinfo("Resultado", "No hay alumnos con matrícula de honor.")

    def borrar_campos(self):
        """Limpia los campos de entrada después de agregar un alumno."""
        self.ci_entry.delete(0, tk.END)
        self.apellidos_entry.delete(0, tk.END)
        self.nombre_entry.delete(0, tk.END)
        self.nota_entry.delete(0, tk.END)

# Configuración de la ventana
root = tk.Tk()
root.title("Gestión de Calificaciones")

# Crear instancias de las clases
gestion = GestionCalificaciones()

# Crear widgets
ci_label = tk.Label(root, text="CI (Cédula):")
ci_label.grid(row=0, column=0)
ci_entry = tk.Entry(root)
ci_entry.grid(row=0, column=1)

apellidos_label = tk.Label(root, text="Apellidos:")
apellidos_label.grid(row=1, column=0)
apellidos_entry = tk.Entry(root)
apellidos_entry.grid(row=1, column=1)

nombre_label = tk.Label(root, text="Nombre:")
nombre_label.grid(row=2, column=0)
nombre_entry = tk.Entry(root)
nombre_entry.grid(row=2, column=1)

nota_label = tk.Label(root, text="Nota:")
nota_label.grid(row=3, column=0)
nota_entry = tk.Entry(root)
nota_entry.grid(row=3, column=1)

# Asignar las entradas a las instancias de las variables
gestion.ci_entry = ci_entry
gestion.apellidos_entry = apellidos_entry
gestion.nombre_entry = nombre_entry
gestion.nota_entry = nota_entry
gestion.alumnos_text = None  # Se asignará más tarde

# Botones
introducir_button = tk.Button(root, text="Introducir Alumno", command=gestion.introducir_alumno)
introducir_button.grid(row=4, column=0, columnspan=2)

eliminar_button = tk.Button(root, text="Eliminar Alumno", command=gestion.eliminar_alumno)
eliminar_button.grid(row=5, column=0, columnspan=2)

consultar_button = tk.Button(root, text="Consultar Nota y Calificación", command=gestion.consultar_nota_y_calificacion)
consultar_button.grid(row=6, column=0, columnspan=2)

modificar_button = tk.Button(root, text="Modificar Nota", command=gestion.modificar_nota)
modificar_button.grid(row=7, column=0, columnspan=2)

# Área de texto para mostrar alumnos
alumnos_label = tk.Label(root, text="Lista de Alumnos:")
alumnos_label.grid(row=8, column=0, columnspan=2)

alumnos_text = tk.Text(root, height=10, width=50)
alumnos_text.grid(row=9, column=0, columnspan=2)

# Asignar el área de texto para mostrar a la clase
gestion.alumnos_text = alumnos_text

# Botones de mostrar
suspensos_button = tk.Button(root, text="Mostrar Suspensos", command=gestion.mostrar_suspensos)
suspensos_button.grid(row=10, column=0, columnspan=2)

aprobados_button = tk.Button(root, text="Mostrar Aprobados", command=gestion.mostrar_aprobados)
aprobados_button.grid(row=11, column=0, columnspan=2)

mh_button = tk.Button(root, text="Mostrar Matrícula de Honor", command=gestion.mostrar_matricula_de_honor)
mh_button.grid(row=12, column=0, columnspan=2)

# Ejecutar la aplicación
root.mainloop()
