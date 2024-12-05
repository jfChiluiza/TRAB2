import tkinter as tk
import random

class PiedraPapelTijera:
    def __init__(self, root):
        self.root = root
        self.root.title("Piedra, Papel o Tijera")
        
        # Puntuación
        self.puntuacion_jugador = 0
        self.puntuacion_computadora = 0
        
        # Título del juego
        self.label_titulo = tk.Label(root, text="Juego Piedra, Papel o Tijera", font=("Arial", 16))
        self.label_titulo.pack(pady=10)

        # Botones para las opciones del jugador
        self.boton_piedra = tk.Button(root, text="Piedra", font=("Arial", 14), width=20, command=lambda: self.jugar("Piedra"))
        self.boton_piedra.pack(pady=5)
        
        self.boton_papel = tk.Button(root, text="Papel", font=("Arial", 14), width=20, command=lambda: self.jugar("Papel"))
        self.boton_papel.pack(pady=5)
        
        self.boton_tijera = tk.Button(root, text="Tijera", font=("Arial", 14), width=20, command=lambda: self.jugar("Tijera"))
        self.boton_tijera.pack(pady=5)

        # Resultado del juego
        self.label_resultado = tk.Label(root, text="¡Haz tu jugada!", font=("Arial", 14))
        self.label_resultado.pack(pady=10)

        # Selección de la computadora
        self.label_computadora = tk.Label(root, text="La computadora elige...", font=("Arial", 14))
        self.label_computadora.pack(pady=10)

        # Puntuación
        self.label_puntuacion = tk.Label(root, text=f"Jugador: {self.puntuacion_jugador} - Computadora: {self.puntuacion_computadora}", font=("Arial", 14))
        self.label_puntuacion.pack(pady=10)

    def jugar(self, eleccion_jugador):
        # Opciones posibles
        opciones = ["Piedra", "Papel", "Tijera"]
        
        # Elección de la computadora
        eleccion_computadora = random.choice(opciones)
        self.label_computadora.config(text=f"La computadora elige: {eleccion_computadora}")

        # Determinar el resultado
        if eleccion_jugador == eleccion_computadora:
            resultado = "Empate!"
        elif (eleccion_jugador == "Piedra" and eleccion_computadora == "Tijera") or \
             (eleccion_jugador == "Tijera" and eleccion_computadora == "Papel") or \
             (eleccion_jugador == "Papel" and eleccion_computadora == "Piedra"):
            resultado = "¡Ganaste!"
            self.puntuacion_jugador += 1
        else:
            resultado = "Perdiste"
            self.puntuacion_computadora += 1

        # Mostrar el resultado
        self.label_resultado.config(text=resultado)

        # Actualizar la puntuación
        self.label_puntuacion.config(text=f"Jugador: {self.puntuacion_jugador} - Computadora: {self.puntuacion_computadora}")

if __name__ == "__main__":
    root = tk.Tk()
    juego = PiedraPapelTijera(root)
    root.mainloop()
