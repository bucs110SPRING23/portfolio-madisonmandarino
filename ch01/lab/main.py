#part a
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)

classes_per_week = int(input("How many times per week does your class meet?"))
cost_per_class = (cost_per_week / classes_per_week)
print("Cost per class:", cost_per_class)

#part b

import random 
pets =['dog','cat','bird','fish','snake','mouse', 'hamster']
random_pet = random.choice(pets)
print(random_pet)
