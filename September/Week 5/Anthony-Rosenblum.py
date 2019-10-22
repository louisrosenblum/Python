# --------------------------------------
# CSCI 127, Lab 4
# September 26, 2017
# Anthony Louis Rosenblum
# --------------------------------------
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
            if a-b >=0 and a-b + 3*b <= games_played and(games_played - c - d) >=0 :
                print(str(int(c)) + "-" + str(d) + "-" + str(int(games_played - c - d)))
    if (points_earned % 3) == 1 and points_earned != 1:
        for i in range(games_played):
            a = points_earned // 3
            b = i
            c = a - b
            d= 3 * b
            if a-b >=0 and a-b + 3*b <= games_played and (games_played - c - d-1) >=0:
                print(str(int(c)) + "-" + str(d+1) + "-" + str(int(games_played - c - d-1)))
    if (points_earned % 3) == 2 and points_earned != 2:
        for i in range(games_played):
            a = points_earned // 3
            b = i
            c = a - b
            d= 3 * b
            if a-b >=0 and a-b + 3*b <= games_played and games_played - c - d-2 >= 0:
                print(str(int(c)) + "-" + str(d+2) + "-" + str(int(games_played - c - d-2)))
    if points_earned == 0:
            print(str(0) + "-" + str(0) + "-" + str(int(games_played)))
    if points_earned == 1:
        print(str(0) + "-" + str(1) + "-" + str(int(games_played-1)))
    if points_earned == 2:
        print(str(0) + "-" + str(2) + "-" + str(int(games_played-2)))
    

# --------------------------------------

def process_seasons(seasons):
    for i in range(len(seasons)):
        process_season(i+1,seasons[i][0], seasons[i][1])
        print("")

## --------------------------------------

## format of list: [[season-1-games, season-1-points], [season-2-games, season-2-points], etc.]
soccer_seasons = [[1, 3], [1, 1], [1, 0], [999999, 999999]]

process_seasons(soccer_seasons)
