from aleatorio import *


game_still_going = True


class Soul(object):
    def __init__(self, name, hp, atk, defe, power, mana):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defe = defe
        self.power = power
        self.mana = mana
        
    def attack(self, obj):
        global game_still_going
        #si el ataque tiene exito
        if success():
                print(f'{self.name} attacked {obj.name} with {self.power}.')
                
                #el contrincante se defiende
                obj.defend(self)                  

                if obj.hp <= 0:
                    print(f'{obj.name} is dead.')
                    print(f"{self.name} won the battle.")
                    game_still_going = False
        #si el atacador no tiene exito
        else:
            print(f"{self.name} missed!")
        
        if game_still_going:
            self.man(obj)
    
    
        
    def man(self, obj):
        self.mana -=1
        
        if self.mana == 0:
              print(f"{self.name} ran out of mana and will loose the next turn.")
        else:
            print(f"{self.name}'s actual mana: {self.mana}")
                              
    def defend(self, obj):
        if success():
            self.defe = False
        else:
            self.defe = True
        #el contrincante se defendio
        if self.defe:
            print(f'{self.name} fought back.')  
        #el contrincante no se defendio   
        else:
            print(f"{self.name}'s defense was unsuccesful.")
            self.hp -= obj.atk
            print(f"{self.name}'s actual HP: {self.hp}.")
                              
          
        
    
    def say_name(self):
        print(f"Hi, my name is {self.name},")
        print(f"I'm a {self.__class__.__name__}.")