#Task 1
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
tracks = ['Track 1', 'Track 2', 'Track 3', 'Track 4']
#for (a,b) in zip(genres, tracks):
#    print(a,b)

#Task 2
#Need to get some help on this before submitting
g = 0
while g <2:
    g +=1
    for i in range(len(genres)):
         print(genres[g],tracks[i])
         if g == 2:
              break

#Task 3
genres.pop(-1)
for i in range(len(genres)):
        print("Now playing " + tracks[i] + ", " + genres[i] +".")

