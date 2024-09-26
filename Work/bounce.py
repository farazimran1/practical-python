# bounce.py
#
# Exercise 1.5

initial_height = 100
current_height = initial_height
bounce_factor = 3 / 5
num_bounces = 0

while num_bounces < 10:
    num_bounces += 1
    current_height *= bounce_factor
    print(f"{num_bounces} {round(current_height, 4)}")
