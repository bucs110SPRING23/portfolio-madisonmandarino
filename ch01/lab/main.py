#part a
weeks = 16
print("Number of weeks:", weeks)
classes = 5
print("Number of classes:", classes)
tuition = 6000
print("Total Tuition:", tuition)
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)

classes_per_week = 10
print("Classes per week:", classes_per_week)
cost_per_class = (cost_per_week / classes_per_week)
print("Cost per class:", cost_per_class)

#part b

import random 
pets =['dog','cat','bird','fish','snake','mouse', 'hamster']
random_pet = random.choice(pets)
print(random_pet)
