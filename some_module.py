from my_library.some_eletronics import SBC

class Car(object):
    """Uma tentativa simples de implementar um carro"""

    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year = year
        self.__odometer_reading=0
    
    def get_descritive_name(self):
        """Devolve um nome descritivo, formatado de modo elegante"""
        long_name=str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def ride(self, milhas):
        """simula o deslocamento do carro"""
        self.__update_odometer(milhas)
        print("\nvruuuuuum")
        
    
    def read_odometer(self):
        """Exibe uma frase que mostra a milhagem do carro"""
        print("Este carro possui "+ str(self.__odometer_reading) + " milhas.")
        
    def __update_odometer(self, milhas):
        """Aualiza o valor do odometro"""
        self.__odometer_reading = self.__odometer_reading + milhas
        
class EletricCar(Car):
    """Uma naiva de modelar um carro elérico"""
    def __init__(self, make, model, year, battery_size):
        """Inicializa os aributos da classe pai"""
        super().__init__(make, model, year)
            
        """Inicializar os aribuos da classe filha"""
        self.battery_size = battery_size
        self.pc=SBC("Ana")
    def describe_battery(self):
        """Exibe uma frase elegante que descreve a capacidade da baeria"""
        print("Este carro possui uma bateria com "\
              + str(self.battery_size) + "kwh de capacidade.")
    def ride(self,milhas):
        """Somula o deslocameno do carro elétrico"""
        print("\nHello world, i'm here!")