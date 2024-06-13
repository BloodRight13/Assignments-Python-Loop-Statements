#Task 1
import random
moods = ["Happy", "Sad", "Energetic", "Calm", "Angry", "Depressed", "Stressed"]
days =["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday", "Saturday"]
for i in range(len(days)):
    print("On " + (days[i]) +", you were feeling " + random.choice(moods) + ".")

