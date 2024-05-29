class Person:
  def move(self):
    print("Move 4 paces")
  def rest(self):
    print("Gain 4 health points")

class Doctor(Person):
  # pass ## used if we don't need anything else
  def heal(self):
    print("Heal ten health points")
    
class Fighter(Person):
  def fight(self):
    print("Fight")
  def move(self):
    print("Move 6 paces")
    
class Wizard(Doctor):
  def cast_spell(self):
    print("Turns invisible")
  def heal(self):
    print("Heal 15 points")
  
character_1 = Person()
character_1.move()
doctor_1 = Doctor()
doctor_1.move()
doctor_1.heal()
fighter_1 = Fighter()
fighter_1.fight()
fighter_1.move()
wizard = Wizard()
wizard.heal()