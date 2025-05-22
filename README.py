class Pelicula:
    def __init__(self, codigo=0, titulo="", duracion=0, director="", prestada=False):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__duracion = duracion
        self.__director = director
        self.__prestada = prestada

    # Getters
    def get_codigo(self):
        return self.__codigo

    def get_titulo(self):
        return self.__titulo

    def get_duracion(self):
        return self.__duracion

    def get_director(self):
        return self.__director

    def is_prestada(self):
        return self.__prestada

    # Setters
    def set_codigo(self, codigo):
        self.__codigo = codigo

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_duracion(self, duracion):
        self.__duracion = duracion

    def set_director(self, director):
        self.__director = director

    def set_prestada(self, prestada):
        self.__prestada = prestada

    # Métodos
    def prestar(self):
        if not self.__prestada:
            self.__prestada = True
            return "La película ha sido prestada."
        else:
            return "La película ya estaba prestada."

    def devolver(self):
        if self.__prestada:
            self.__prestada = False
            return "La película ha sido devuelta."
        else:
            return "La película no estaba prestada."

    def costo_reproduccion(self, tarifa_por_minuto):
        costo_total = self.__duracion * tarifa_por_minuto
        return f"El costo de reproducir la película es: ${costo_total:.2f}"

    def __str__(self):
        estado = "está prestada" if self.__prestada else "no está prestada"
        return (f'La película {self.__codigo} titulada "{self.__titulo}" dirigida por '
                f'{self.__director} dura {self.__duracion} minutos y {estado}.')

    def __eq__(self, otra_pelicula):
        if isinstance(otra_pelicula, Pelicula):
            return self.__codigo == otra_pelicula.get_codigo()
        return False


if __name__ == "__main__":
    pelicula1 = Pelicula(1001, "Avatar", 162, "James Cameron")
    pelicula2 = Pelicula(1002, "Titanic", 195, "James Cameron")
    pelicula3 = Pelicula(1001, "Avatar (Edición extendida)", 180, "James Cameron")

    print(pelicula1)
    print(pelicula2)
    print(pelicula3)

    print(pelicula1.prestar())
    print(pelicula1.prestar())
    print(pelicula1.devolver())

    print(pelicula2.costo_reproduccion(20))

    print("¿pelicula1 y pelicula3 tienen el mismo código?", pelicula1 == pelicula3)# parcial-programaci-n
