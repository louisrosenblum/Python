def process_season(season, games_played, points_earned):
    print("Season: " + str(season) + ", Games Played: " + str(games_played) +
          ", Points earned: " + str(points_earned))
    print("Possible Win-Tie-Loss Records")
    print("-----------------------------")
    if (points_earned % 3) == 0 and points_earned != 0:
        for i in range(games_played):
            a = points_earned / 3
            b = i
            c = a-b
            d = 3 *b
            if a-b >=0 and a-b + 3*b <= games_played:
                print(str(int(c)) + "-" + str(d) + "-" + str(int(games_played - c - d)))
    if (points_earned % 3) == 1:
        for i in range(games_played):
            a = points_earned // 3
            b = i
            c = a - b
            d= 3 * b
            if a-b >=0 and a-b + 3*b <= games_played:
                print(str(int(c)) + "-" + str(d+1) + "-" + str(int(games_played - c - d-1)))
    if (points_earned % 3) == 2:
        for i in range(games_played):
            a = points_earned // 3
            b = i
            c = a - b
            d= 3 * b
            if a-b >=0 and a-b + 3*b <= games_played:
                print(str(int(c)) + "-" + str(d+2) + "-" + str(int(games_played - c - d-2)))
    if points_earned == 0:
            print(str(0) + "-" + str(0) + "-" + str(int(games_played)))
    if points_earned == 1:
        print(str(0) + "-" + str(1) + "-" + str(int(games_played-1)))
    if points_earned == 2:
        print(str(0) + "-" + str(1) + "-" + str(int(games_played-2)))

x = int(input(": "))
y = int(input(": "))
z = int(input(": "))

process_season(x,y,z)
