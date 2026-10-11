print("=== Study day report ===") 

name = input("What's your name? ").title()
block1 = float(input("Hours in deep work block 1: "))
block2 = float(input("Hours in deep work block 2: "))
block3 = float(input("Hours in deep work block 3: "))

light = float(input("Hours in light study: "))

total = block1 + block2 + block3 + light

print()
print(f"Report for {name}")
print(f"Total today: {total:.1f} h")


