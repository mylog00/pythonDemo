def inc_map(key, src_map):
    if key in src_map:
        src_map[key] += 1
    else:
        src_map[key] = 1


n = int(input())
gamesMap = {}
winMap = {}
defeatMap = {}
drawMap = {}
teams = set()
while n > 0:
    str = input().split(';')
    team1 = str[0]
    res1 = str[1]
    team2 = str[2]
    res2 = str[3]
    teams.add(team1)
    teams.add(team2)
    inc_map(team1, gamesMap)
    inc_map(team2, gamesMap)
    if res1 == res2:
        inc_map(team1, drawMap)
        inc_map(team2, drawMap)
    elif res1 > res2:
        inc_map(team1, winMap)
        inc_map(team2, defeatMap)
    else:
        inc_map(team2, winMap)
        inc_map(team1, defeatMap)
    n -= 1


def get_value(team, src_map):
    if team in src_map:
        return src_map.get(team)
    else:
        return 0

def get_score(team):
    wins = get_value(team, winMap) * 3
    draws = get_value(team, drawMap)
    return wins + draws


for team in teams:
    print(team, gamesMap.get(team), sep=':', end=' ')
    print(get_value(team, winMap), get_value(team, drawMap), get_value(team, defeatMap), get_score(team), sep=' ')
