total_fuel = 0
curr_fuel = 0

f = open("input1", "r")

for x in f:
    curr_fuel = (int(x) // 3) - 2
    fuel_for_fuel = (curr_fuel //3) - 2
    while fuel_for_fuel > 0:
        curr_fuel+=fuel_for_fuel
        fuel_for_fuel = (fuel_for_fuel //3) - 2
    total_fuel += curr_fuel
print(total_fuel)