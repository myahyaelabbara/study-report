print("=== Study day report ===") 

name = input("What's your name? ").title()
block1 = float(input("Hours in deep work block 1: "))
block2 = float(input("Hours in deep work block 2: "))
block3 = float(input("Hours in deep work block 3: "))

light = float(input("Hours in light study: "))

total = block1 + block2 + block3 + light
valid = (0 <= block1 <= 12 and 0 <= block2 <= 12 and 0 <= block3 <= 12
         and 0 <= light <= 12 and total <= 24)
print(f"Valid: {valid}")
print()
print(f"Report for {name}")
print(f"Total today: {total:.1f} h")


