import random
import math

# TO DO List
# Look up more on dictionaries
# Get Help from Brother Nelson
# Meet with a tutor


TEAM_NAME_INDEX = 0
TEAM_RANK_INDEX = 1
BRACKET_SEED_INDEX = 2
TEAM_RECORD_INDEX = 3
TEAM_WINS_INDEX = 4
TEAM_LOSSES_INDEX = 5
TOTAL_GAMES_PLAYED_INDEX = 6
WIN_PERCENTAGE_INDEX = 7
REGION_INDEX = 8
POINTS_PER_GAME_INDEX = 9
POINTS_ALLOWED_PER_GAME_INDEX = 10
TEAM_FIELD_GOAL_PERCENTAGE = 11
THREE_POINT_PERCENTAGE_INDEX = 12
REBOUNDS_PER_GAME_INDEX = 13
POINT_DIFFERENTIAL_INDEX = 14
TURNOVERS_PER_GAME_INDEX = 15
TURNOVERS_FORCED_PER_GAME_INDEX = 16


def main():

    march_madness_dict = read_dictionary('march_madness-2023.csv', TEAM_NAME_INDEX)

    round_of_32_dict = generate_round_of_64(march_madness_dict)

    sweet_16_dict = generate_round_of_32(round_of_32_dict)

    elite_8_dict = generate_sweet_16(sweet_16_dict)

    final_four_dict = generate_elite_8(elite_8_dict)

    championship_dict = generate_final_four(final_four_dict)

    champion_dict = generate_championship(championship_dict)

    champion = generate_champion(champion_dict)

    print(f'The National Champion is {champion}!')

    # Could I make a function here in the main that would allow me to determine the metric for winning and then run the whole system again? It could become one of the parameters
    # To each of the fucntions!! I do not want to have to go and change each function each time! 


def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary."""

    dictionary = {}

    with open(filename, 'rt') as csv_file:

        reader = csv.reader(csv_file)

        next(reader)


        for row_list in reader:
            if len(row_list) != 0:
                key = row_list [key_column_index]
                dictionary[key] = row_list

    return dictionary

# def bracket():

def generate_round_of_64(dictionary):

    round_of_32_dict = {}
    # Because I will be submitting each of them in order, I could set up the next matches just by how they are flowing into the dictionary in that order. 

    for team in dictionary.items():

        # I want to check and make sure that I am using the dictionary correctly! 

        team_name = team[0]
        team_seed = team[2]
        team_win_percentage = team[7]
        team_region = team[8]

        field_goal_percentage = team[11]


        # I need to get the seed and then make the 1 and 16 seed play from the specific region. 
        # It needs to show the team names 
        # needs to determine which team would win and then add them to the next list in the bracket 
        # Print the match up in bracket format. 
        # the next funtion will match and then do the same for the matchups in the next round.


        game_1 =  # teams, seed, win %, and region
                # the if statement to determine the winner 
                # round_of_32_dict.append

        game_2 =

        game_3 = 

        game_4 = 
        
        game_5 =

        game_6 =

        game_7 =

        game_8 = 

        game_9 =

        game_10 =

        game_11 =

        game_12 =

        game_13 =

        game_14 =

        game_15 =

        game_16 =

        game_17 =

        game_18 =

        game_19 =

        game_20 =

        game_21 =

        game_22 =

        game_23 =

        game_24 =

        game_25 =

        game_26 =

        game_27 =

        game_28 =

        game_29 =

        game_30 =

        game_31 =

        game_32 =


    round_of_64_matchups = (f'''
    {game_1} 
    {game_2} 
    {game_3}  
    {game_4} 
    {game_5}
    {game_6}
    {game_7} 
    {game_8} 
    {game_9}
    {game_10} 
    {game_11} 
    {game_12} 
    {game_13} 
    {game_14} 
    {game_15}
    {game_16} 
    {game_17} 
    {game_18} 
    {game_19} 
    {game_20} 
    {game_21} 
    {game_22}
    {game_23} 
    {game_24}
    {game_25} 
    {game_26} 
    {game_27} 
    {game_28} 
    {game_29} 
    {game_30} 
    {game_31} 
    {game_32} ''')

    print(round_of_64_matchups)

    return round_of_32_dict


def generate_round_of_32(dictionary):

    sweet_16_dict = {}

    for team in dictionary.items():

        team_name = team[0]
        team_seed = team[2]
        team_region = team[8]

        game_1 = 

        game_2 =

        game_3 = 

        game_4 = 
        
        game_5 =

        game_6 =

        game_7 =

        game_8 = 

        game_9 =

        game_10 =

        game_11 =

        game_12 =

        game_13 =

        game_14 =

        game_15 =

        game_16 =

    round_of_32_matchups =(f'''
    {game_1} 
    {game_2} 
    {game_3}  
    {game_4} 
    {game_5}
    {game_6}
    {game_7} 
    {game_8} 
    {game_9}
    {game_10} 
    {game_11} 
    {game_12} 
    {game_13} 
    {game_14} 
    {game_15}
    {game_16}''')

    print(round_of_32_matchups)

    return sweet_16_dict


def generate_sweet_16(dictionary):

    elite_8_dict = {}

    for team in dictionary.items():

        team_name = team[0]
        team_seed = team[2]
        team_region = team[8]

        game_1 = 

        game_2 =

        game_3 = 

        game_4 = 
        
        game_5 =

        game_6 =

        game_7 =

        game_8 = 

    sweet_16_matchups = (f'''
    {game_1} 
    {game_2} 
    {game_3}  
    {game_4} 
    {game_5}
    {game_6}
    {game_7} 
    {game_8} ''')

    print(sweet_16_matchups)

    return elite_8_dict


def generate_elite_8(dictionary):

    final_four_dict = {}

    for team in dictionary.items():

        team_name = team[0]
        team_seed = team[2]
        team_region = team[8]

        game_1 = 

        game_2 =

        game_3 = 

        game_4 = 

    elite_8_matchups =(f'''
    {game_1} 
    {game_2} 
    {game_3}  
    {game_4} ''')

    print(elite_8_matchups)

    return final_four_dict


def generate_final_four(dictionary):

    championship_dict = {}

    for team in dictionary.items():

        team_name = team[0]
        team_seed = team[2]
        team_region = team[8]

        game_1 = 

        game_2 =

    final_four_matchups =(f'''
    {game_1} 
    {game_2} ''')

    print(final_four_matchups)

    return championship_dict


def generate_championship(dictionary):

    champion_dict = {}

    for team in dictionary.items():

        team_name = team[0]
        team_seed = team[2]
        team_region = team[8]

        game_1 = 

    championship_matchup =(f'''
    {game_1} ''')

    return champion_dict

def generate_champion(dictionary):

    for team in dictionary.items():

        team_name = team[0]
        team_seed = team[2]

    champion = (f'Number {team_seed} seed {team_name}')

    return champion


if __name__ == "__main__":
    main()
