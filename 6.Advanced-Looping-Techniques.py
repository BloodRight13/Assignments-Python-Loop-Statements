#Task 1
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
popular_genres = genres[1:4]
print(popular_genres) 

#Task 2
string = ' Music'
genres2 = [i+ string for i in genres]
print(genres2)

#Task 3
i = 11
while i > 0:
    i-=1
    print(i)
    if i == 0:
        print("The beat drops now!")

