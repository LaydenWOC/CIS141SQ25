#2. The headlights of a car should only automatically turn on when the daylight outside is below a certain threshold. If a sensor threshold is below the number 8, print "Headlights On"; otherwise, print "Headlights Off".
lightlevel = input()
if int(lightlevel) < 8:
    print("Headlights On")
else:
    print("Headlights Off")


