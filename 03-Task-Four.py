import csv


class Team:
    def __init__(self):
        self.wins = 0
        self.draws = 0
        self.losses = 0
        self.goals = {'for': 0, 'against': 0}


def process_match(row):
    [name_one, score_one, name_two, score_two] = row
    team_one, team_two = teams.get(name_one), teams.get(name_two)

    if score_one > score_two:
        team_one.wins, team_two.losses = team_one.wins + 1, team_two.losses + 1
    elif score_one < score_two:
        team_one.losses, team_two.wins = team_one.losses + 1, team_two.wins + 1
    else:
        team_one.draws, team_two.draws = team_one.draws + 1, team_two.draws + 1


def update_teams(row):
    for i in range(0, len(row), 2):
        if not teams.get(row[i]):
            teams[row[i]] = Team()
        teams.get(row[i]).goals['for'] += row[i + 1]
        teams.get(row[i]).goals['against'] += row[i - 1]

    process_match(row)


def parse_file(path):
    file_stream = open(path)
    file_contents = csv.reader(file_stream)
    for row in file_contents:
        row[1], row[3] = int(row[1]), int(row[3])
        update_teams(row)


def pad_text(text, desired_length):
    text = str(text)
    return text+(' '*abs(desired_length-len(text)))


def generate_line(team_name):
    stats = teams.get(team_name)
    played = stats.wins+stats.losses+stats.draws
    line = pad_text(team_name, 10)+pad_text(played, 3)+pad_text(stats.wins, 3)
    line += pad_text(stats.draws, 3)+pad_text(stats.losses, 3)
    line += pad_text(stats.goals['for'], 4)+pad_text(stats.goals['against'], 6)
    line += pad_text(stats.goals['for']-stats.goals['against'], 8)+str(stats.wins*3+stats.draws)
    return line


def sort_dict(unsorted_teams):
    criteria = lambda team: ((team[1].wins*3)+team[1].draws, team[1].goals['for'] - team[1].goals['against'], team[0])
    return dict(sorted(unsorted_teams.items(), key=criteria, reverse=True))


def create_table():
    print(pad_text('', 10)+pad_text('P  W  D  L', 14)+pad_text('F', 4)+pad_text('A', 4)+pad_text('Diff', 7)+'Pts')
    sorted_teams = sort_dict(teams)
    for i in sorted_teams:
        print(generate_line(i))


teams = {}

if __name__ == '__main__':
    parse_file('scores.csv')
    create_table()
