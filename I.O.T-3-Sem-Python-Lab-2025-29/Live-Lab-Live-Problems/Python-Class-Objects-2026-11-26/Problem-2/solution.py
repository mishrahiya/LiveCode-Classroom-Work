# LiveCode Classroom - Solution
# Batch: I.O.T 3 Sem Python Lab  2025-29
# Category: Live Lab Problems
# Question: Problem 2 (Create a Classs)
# Score: 1/1 (4/4 Test Cases Passed)
# Synced: Thursday, November 26, 2026 at 10:10 AM

# Write your Python solution below
class car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model= model
        self.year = year
car1 = car ("toyota","fortuner",2022)
car2 = car ("bmw","x5",2024)

print (car1.brand,car1.model,car1.year)
print (car2.brand,car2.model,car2.year)