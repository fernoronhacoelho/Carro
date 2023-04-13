"""
Created on Tue Apr 11 12:19:13 2023

@author: Alunos
"""

from my_library.some_module import Car, EletricCar

def workspace():
    my_new_car = Car('audi','a4',2016)
    
    print(f'\n{my_new_car.get_descritive_name()}')
   
    my_new_car.read_odometer()
    my_new_car.ride(25)
    my_new_car.read_odometer()
    
    
    my_new_eletric_car= EletricCar('tesla', 'S', 2019, 80)
    print(f'\n{my_new_eletric_car.get_descritive_name()}')
    my_new_eletric_car.describe_battery()
    my_new_eletric_car.ride(20)
    my_new_eletric_car.pc.say_your_name()
    
    print("\successful exit")
    
if __name__ == "__main__":
    workspace()