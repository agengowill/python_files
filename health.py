import random

health = 50
difficulty = 2
health_portion = random.randint(25, 50)
new_health = int((health + health_portion) / difficulty)
print(new_health)

