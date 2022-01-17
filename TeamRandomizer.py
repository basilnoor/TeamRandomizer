#   Team randomizer will take a players name and rank and store it in a class.
#   The main function will take a list of players and place them in balabnced teams based on their given ranks.

import random

NUMBER_OF_TRIES = 0


class Person:
    """Takes a persons name and initializes it."""

    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name


class Player(Person):
    """
    Takes a players name and rank, in that order, and initializes it.
    Inhirits from Person.
    """

    def __init__(self, name, rank):
        # Uses Person superclass to initialize players name with their rank.
        # Only used to practice inheritance. Otherwise unneccesary.
        self._name = name
        self._rank = rank

    def get_rank(self):
        return self._rank

    def set_rank(self, new_rank):
        self._rank = new_rank


def randomizer(list_of_players):
    """
    This function takes a list of player objects and organizes them randomly into two teams.
    Team balance will be based on the players ranks.
    """

    team_1 = []
    team_2 = []

    counter = 0

    random.shuffle(list_of_players)

    for player in list_of_players:
        if player.get_rank() > 8:
            if counter == 0:
                team_1.append(player)
                counter = 1
            elif counter == 1:
                team_2.append(player)
                counter = 0
            list_of_players.remove(player)

    for player in list_of_players:
        if 4 <= player.get_rank():
            if counter == 0:
                team_1.append(player)
                counter = 1
            elif counter == 1:
                team_2.append(player)
                counter = 0
            list_of_players.remove(player)

    for player in list_of_players:
        if 0 < player.get_rank():
            if counter == 0:
                team_1.append(player)
                counter = 1
            elif counter == 1:
                team_2.append(player)
                counter = 0

    balance_checker(team_1, team_2)


def team_power(team_1, team_2):
    team_1_total = 0
    team_2_total = 0

    for player in team_1:
        team_1_total += player.get_rank()

    for player in team_2:
        team_2_total += player.get_rank()

    compare_total = team_1_total - team_2_total

    return compare_total


def balance_checker(team_1, team_2):

    global NUMBER_OF_TRIES
    combine_teams = team_1 + team_2

    if 4 > team_power(team_1, team_2) > -4:  # Add exception for when teams can never be balanced
        finalize(team_1, team_2)
    else:
        NUMBER_OF_TRIES += 1
        if NUMBER_OF_TRIES < 10:
            randomizer(combine_teams)
        else:
            print("Teams cannot be balanced.")
            exit()


def finalize(team_1, team_2):

    team_1_final = []
    team_2_final = []
    combine_teams = team_1 + team_2

    for player in team_1:
        team_1_final.append(player.get_name())

    for player in team_2:
        team_2_final.append(player.get_name())

    print(team_1_final)
    print(team_2_final)

    print()
    redo = input("Would you like to re-balance teams? (y/n): ")
    if redo == "y" or redo == "Y":
        randomizer(combine_teams)
    elif redo == "n" or redo == "N":
        print("Goodluck bois!")

    print()

    restart = input("Would you like to change players? (y/n): ")
    if restart == "y" or restart == "Y":
        start()
    elif restart == "n" or restart == "N":
        print("Peace later boi!")
        exit()


def add_more():
    add = input("Would you like to add a player? (y/n): ")
    if add == "y" or add == "Y":
        return True
    elif add == "n" or add == "N":
        return False


def start():
    """
    Initialize players with their ranks beforehand.
    Create a list of players that will be playing and pass it to randomizer() to get balanced teams.
    """

    # List of players
    # First picks
    basil = Player("basil", 10)
    nab = Player("nab", 10)
    chris = Player("chris", 10)
    garret = Player("garret", 10)

    # Second picks
    ervin = Player("ervin", 8)
    sw8r = Player("sw8r", 8)

    # Third Picks
    teetee = Player("teetee", 6)
    brad = Player("brad", 6)
    baran = Player("baran", 6)

    # Forth Picks
    taha = Player("taha", 4)
    koala = Player("koala", 4)
    meek = Player("meek", 4)

    # Last Picks :(
    tiff = Player("tiff", 2)
    joey = Player("joey", 2)
    juan = Player("juan", 2)

    list_of_all_players = [basil, nab, chris, garret, ervin, brad, sw8r, teetee, baran, taha, koala, meek, tiff, joey,
                           juan]

    players_playing = []

    print("#note# add player names as shown above with a single space between players")
    add_players = input("Choose players to add: ")
    list_of_players_string = add_players.split()
    for player_string in list_of_players_string:
        for player in list_of_all_players:
            if player_string == player.get_name():  # Add exception if name doesnt exist
                players_playing.append(player)

    print()
    if len(players_playing) == 1:
        print("Need more than 1 person playing!")
    elif len(players_playing) == 0:
        print("Nice you have no friends!")
    else:
        print("Balanced Teams: ")
        randomizer(players_playing)


def main():
    print("Welcome to TeamRandomizer!")
    print()
    print("List of current players in database include:")
    print("basil, nab, chris, garret, ervin, brad, sw8r")
    print("teetee, baran, taha, koala, meek, tiff, joey and juan.")
    print()
    print("!DISCLAIMER!")
    print("Please choose players from this list. If they are not on the list")
    print("they must be added to the database for TeamRandomizer to work...ask Basil")
    print()

    start()


if __name__ == "__main__":
    main()
