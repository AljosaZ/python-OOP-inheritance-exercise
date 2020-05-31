class Player():
    def __init__(self, name, last_name, height_cm, weight_kg):
        self.name = name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

    def weight_to_lbs(self):
        pounds = self.weight_kg * 2.20462262
        return pounds


class BasketballPlayer(Player):
    def __init__(self, name, last_name, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(name=name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists

class FootballPlayer(Player):
    def __init__(self, name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super().__init__(name=name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards

print('This program will allow you to enter and save the information of athletes.')
f_name = input('Please enter first name: ')
l_name = input('Please enter last name: ')
height = input('Please enter height in cm: ')
weight = input('Please enter weight in kg: ')
sport = input('Please enter "goal" or "hoop" to enter football-player or basket-ball-player information: ')


if sport == "goal":
    print('You are about to enter the information for a football player!')
    goals = int(input('Please enter the number of goals: '))
    y_cards = int(input('Please enter the number of yellow cards: '))
    r_cards = int(input('Please enter the number of red cards: '))
    f_player = FootballPlayer(name=f_name, last_name=l_name, height_cm=height, weight_kg=weight, goals=goals, yellow_cards=y_cards, red_cards=r_cards)

    with open("f_players.txt", "a") as fball_players_file:
        fball_players_file.write(str(f_player.__dict__) + "\n")

    print('Information sucessfully entered!')
    print('Currently existing football player information: ')
    player_info_dictionaries = []
    with open("f_players.txt", "r") as fball_players_file:
        for line in fball_players_file:
            player_info_dictionaries.append(eval(line))
        for i in range(len(player_info_dictionaries)):
            print(f'{player_info_dictionaries[i].get("name")} {player_info_dictionaries[i].get("last_name")}')

else:
    print('You are about to enter the information for a basketball player!')
    points = int(input('Please enter points: '))
    rebounds = int(input('Please enter rebounds: '))
    assists = int(input('Please enter assists: '))
    b_player = BasketballPlayer(name=f_name, last_name=l_name, height_cm=height, weight_kg=weight, points=points, rebounds=rebounds, assists=assists)

    with open("b_players.txt", "a") as bball_players_file:
        bball_players_file.write(str(b_player.__dict__) + "\n")

    print('Information sucessfully entered!')
    print('Currently existing basketball player information: ')
    player_info_dictionaries = []
    with open("b_players.txt", "r") as bball_players_file:
        for line in bball_players_file:
            player_info_dictionaries.append(eval(line))
        for i in range(len(player_info_dictionaries)):
            print(f'{player_info_dictionaries[i].get("name")} {player_info_dictionaries[i].get("last_name")}')