distance = int(input("Enter distance in km: "))
mileage = int(input("Enter mileage in km per litre: "))
price = int(input("Enter fuel price per litre: "))

fuel = distance / mileage
cost = fuel * price

print("Fuel required:", fuel, "litres")
print("Total fuel cost:", cost, "rupees")
