"""
    Tercera tarea de APA - manejo de vectores

    Nombre y apellidos: Guillem Perez Sanchez
"""

class Vector:
    """
    Clase usada para trabajar con vectores sencillos.
    """
    def __init__(self, iterable):
        """
        Constructor de la clase Vector. Su único argumento es un iterable con las componentes del vector.
        """
        self.vector = list(iterable)  # Ahora siempre es una lista

    def __repr__(self):
        """
        Representación oficial del vector que permite construir uno nuevo idéntico mediante copia-pega.
        """
        return f"Vector({self.vector})"

    def __str__(self):
        """
        Representación bonita del vector.
        """
        return str(self.vector)

    def __getitem__(self, key):
        """Devuelve un elemento o una loncha del vector."""
        return self.vector[key]

    def __setitem__(self, key, value):
        """Fija el valor de una componente o loncha del vector."""
        self.vector[key] = value

    def __len__(self):
        """Devuelve la longitud del vector."""
        return len(self.vector)

    def __add__(self, other):
        """Suma al vector otro vector o una constante."""
        if isinstance(other, (int, float, complex)):
            return Vector(uno + other for uno in self.vector)
        else:
            return Vector(uno + otro for uno, otro in zip(self.vector, other.vector))

    __radd__ = __add__

    def __neg__(self):
        """Invierte el signo del vector."""
        return Vector([-1 * item for item in self.vector])

    def __sub__(self, other):
        """Resta al vector otro vector o una constante."""
        return -(-self + other)

    def __rsub__(self, other):
        """Método reflejado de la resta."""
        return -self + other

    def __mul__(self, other):
        """Producto de Hadamard o multiplicación por escalar."""
        if isinstance(other, Vector):  
            if len(self.vector) != len(other.vector):
                raise ValueError("Los vectores deben tener la misma dimensión para el producto de Hadamard")
            return Vector([a * b for a, b in zip(self.vector, other.vector)])
        elif isinstance(other, (int, float)):  
            return Vector([a * other for a in self.vector])
        else:
            return NotImplemented

    def __rmul__(self, other):
        """Multiplicación de un vector por un escalar."""
        return self * other  

    def __matmul__(self, other):
        """Producto escalar de dos vectores."""
        if isinstance(other, Vector):
            if len(self.vector) != len(other.vector):
                raise ValueError("Los vectores deben tener la misma dimensión para el producto escalar")
            return sum(a * b for a, b in zip(self.vector, other.vector))
        else:
            return NotImplemented

    def __rmatmul__(self, other):
        """Producto escalar cuando el vector está a la derecha del operador @."""
        return self @ other  

    def __floordiv__(self, other):
        """Componente paralela de self respecto a other (v1 // v2)."""
        if isinstance(other, Vector):
            norm_squared = other @ other  # |v2|²
            if norm_squared == 0:
                raise ValueError("No se puede proyectar sobre el vector cero")
            scalar_projection = (self @ other) / norm_squared  # (v1 • v2) / |v2|²
            return Vector([scalar_projection * x for x in other.vector])  # v1^||

    def __mod__(self, other):
        """Componente normal de self respecto a other (v1 % v2)."""
        if isinstance(other, Vector):
            return Vector([a - b for a, b in zip(self.vector, (self // other).vector)])  # v1^⊥ = v1 - v1^||
