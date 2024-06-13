#Task 1
import random
moods = ["Happy", "Sad", "Energetic", "Calm", "Angry", "Depressed", "Stressed"]
days =["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday", "Saturday"]
times = ["morning", "afternoon", "evening"]
for day in days:
    for time in times:
        print("On "+ day + " " + time + " you were " + random.choice(moods)+".")