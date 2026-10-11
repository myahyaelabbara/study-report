print("=== Study day report ===") 

name = input("What's your name? ").title()
block1 = float(input("Hours in deep work block 1: "))
block2 = float(input("Hours in deep work block 2: "))
block3 = float(input("Hours in deep work block 3: "))
light = float(input("Hours in light study: "))
rest_day = input("Was today a rest day? (yes/no) ").lower() == "yes"
hour = int(input("What hour did you stop studying? (0-23) ")) 
total = block1 + block2 + block3 + light
valid = (0 <= block1 <= 12 and 0 <= block2 <= 12 and 0 <= block3 <= 12
         and 0 <= light <= 12 and total <= 24)
print(f"Valid: {valid}")
print()
print(f"Report for {name}")
if valid:
    percent = (total / 8) * 100
    print(f"Total today: {total:.1f} h ({percent:.0f}% of your 8 h target)")

if not valid:
    print("Some hours are impossible: each block must be 0 to 12 h, and a day at most 24 h.")
elif total >= 12:
    print("Tier: Summit day")
elif total >= 10:
    print("Tier: Deep diver")
elif total >= 8:
    print("Tier: Full-timer")
elif total >= 4:
    print("Tier: Building up")
elif total > 0:
    print("Tier: Warming up")
else:
    print("No study logged today.")

if valid and total < 8:
    print(f"{8 - total:.1f} h more makes it a full-timer day.")

if rest_day:
    print("Rest day: your streak is safe.")

if not 0 <= hour <= 23:
    print(f"{hour} isn't a real hour: hours go from 0 to 23.")
elif hour >= 23 or hour < 5:
    print("Late night! Sleep is when your brain turns today's study into memory.")

