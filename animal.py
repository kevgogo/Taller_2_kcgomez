from abc import ABC, abstractmethod

# Definir la interfaz Animal
class Animal(ABC):
    @abstractmethod
    def hacer_sonido(self):
        """Método para devolver el sonido del animal."""
        pass

    @abstractmethod
    def tipo(self):
        """Método para devolver el tipo de animal."""
        pass

# Clase Gato que implementa Animal
class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"
    
    def tipo(self):
        return "Gato"

# Clase Perro que implementa Animal
class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"
    
    def tipo(self):
        return "Perro"

# Clase Hurón que implementa Animal
class Huron(Animal):
    def hacer_sonido(self):
        return "Gruñido"
    
    def tipo(self):
        return "Hurón"

# Clase Boa que implementa Animal
class BoaConstrictor(Animal):
    def hacer_sonido(self):
        return "Silbido"
    
    def tipo(self):
        return "Boa Constrictor"
    