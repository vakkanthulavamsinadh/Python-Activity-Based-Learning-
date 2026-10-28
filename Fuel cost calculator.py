Problem Statement:
Calculate the fuel required and cost of a journey using distance, vehicle mileage, and fuel price.

Objectives:
Use input, arithmetic operators, and conditional statements to estimate journey expenses.

Assumptions:
Distance is in kilometres, mileage is kilometres per litre, and fuel price is rupees per litre. Inputs must be positive.

Algorithm:
Read distance, mileage, and fuel price.
Validate that all values are positive.
Fuel required = distance / mileage.
Total cost = fuel required × price per litre.
Display fuel and cost.

Pseudocode:
START
READ distance, mileage, price
IF any value ≤ 0: DISPLAY invalid input
ELSE fuel ← distance / mileage
cost ← fuel × price
DISPLAY fuel and cost
END

Flowchart:
Start → Read distance, mileage, price → Validate inputs → Calculate litres and cost → Display result → End

python code:
distance = int(input("Enter distance in km: "))
mileage = int(input("Enter mileage in km per litre: "))
price = int(input("Enter fuel price per litre: "))

fuel = distance / mileage
cost = fuel * price

print("Fuel required:", fuel, "litres")
print("Total fuel cost:", cost, "rupees")

Test Cases:
Distance 150 km, mileage 15 km/L, price ₹100/L → fuel 10 L; cost ₹1,000. Mileage 0 → invalid input.

Conclusion:
The program estimates fuel consumption and journey cost from basic vehicle and fuel information.
