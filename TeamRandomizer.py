#   Team randomizer will take a players name and rank and store it in a class.
#   The main function will take a list of players and place them in balabnced teams based on their given ranks.

import random

NUMBER_OF_TRIES = 0  # To limit recursion attempts for randomization


class NotEnoughPlayers(Exception):
    """Exception raised if user doesn't add atleast 2 players."""
    pass


class Person:
    """
    Takes a persons name and initializes it.
    All data members are private.
    """

    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name


class Player(Person):
    """
    Takes a players name and rank, in that order, and initializes it.
    Inhirits from Person class.
    All data members are private.
    """

    # Uses Person superclass to initialize players name with their rank.
    # Only using superclass to practice inheritance. Otherwise unneccesary.

    def __init__(self, name, rank):
        super().__init__(name)
        self._rank = rank

    def get_rank(self):
        return self._rank

    def set_rank(self, new_rank):
        self._rank = new_rank


def randomizer(list_of_players):
    """
    Takes a list of player objects and organizes them randomly into two teams.
    Team balance is based on the players ranks.
    Function separates players of equal rank on opposite teams; starts with the most valuable players.
    """

    team_1 = []
    team_2 = []

    counter = 0  # Keeps track of which team player is put in next

    random.shuffle(list_of_players)

    for player in list_of_players:  # Separation begins
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

    balance_checker(team_1, team_2)  # Calls function to check if teams are balanced


def balance_checker(team_1, team_2):
    """
     Takes 2 lists of player objects and checks for team balance.
     If the total ranks of both teams are within 4 points of eachother then finalizes teams.
     If difference of total ranks is >4 points than calls randomizer function.
    """

    global NUMBER_OF_TRIES
    combine_teams = team_1 + team_2

    if 4 > team_power(team_1, team_2) > -4:
        finalize(team_1, team_2)
    else:
        NUMBER_OF_TRIES += 1
        if NUMBER_OF_TRIES < 10:
            randomizer(combine_teams)
        else:
            print("Teams cannot be balanced.")
            exit()


def team_power(team_1, team_2):
    """
    Adds the total ranks of both teams separately then compares the values to see the difference.
    Returns the difference.
    """

    team_1_total = 0
    team_2_total = 0

    for player in team_1:
        team_1_total += player.get_rank()

    for player in team_2:
        team_2_total += player.get_rank()

    compare_total = team_1_total - team_2_total

    return compare_total


def finalize(team_1, team_2):
    """
    Takes the 2 balanced, randomized teams from balance_checker and outputs the names
    of the player objects in a new list.
    Allows user to rebalance teams via recursion by calling randomizer().
    Allows user to change players playing and restarts program by calling start().
    """

    team_1_final = []
    team_2_final = []
    combine_teams = team_1 + team_2

    for player in team_1:
        team_1_final.append(player.get_name())

    for player in team_2:
        team_2_final.append(player.get_name())

    # Final balanced teams outputted
    print(team_1_final)
    print(team_2_final)

    print()
    redo = input("Would you like to re-balance teams? (y/n): ")  # Rebalances teams
    if redo == "y" or redo == "Y":
        print("New Balanced Teams: ")
        randomizer(combine_teams)
    elif redo == "n" or redo == "N":
        print("Goodluck bois!")

    print()

    restart = input("Would you like to restart? (y/n): ")        # Resets program
    if restart == "y" or restart == "Y":
        start()
    elif restart == "n" or restart == "N":
        print("Peace later boi!")
        exit()


def start():
    """
    Initializes playerbase with their ranks beforehand.
    To add more players in playerbase do so here before running program or exception is thrown.
    User inputs string list of all players they want to play.
    """

    # List of players (Add new players here and to the list_of_all_players)
    # First picks
    basil = Player("basil", 10)
    nab = Player("nab", 10)
    chris = Player("chris", 10)
    garrett = Player("garrett", 10)

    # Second picks
    ervin = Player("ervin", 8)
    sw8r = Player("sw8r", 8)
    brad = Player("brad", 8)

    # Third Picks
    teetee = Player("teetee", 6)
    baran = Player("baran", 6)

    # Forth Picks
    taha = Player("taha", 4)
    koala = Player("koala", 4)
    meek = Player("meek", 4)
    ntry = Player("ntry", 4)

    # Last Picks :(
    tiff = Player("tiff", 2)
    joey = Player("joey", 2)
    juan = Player("juan", 2)

    # Used to compare with user string input
    list_of_all_players = [basil, nab, chris, garrett, ervin, brad, sw8r, teetee, baran, taha, koala, meek, tiff, joey,
                           juan, ntry]

    players_playing = []

    add_players = input("Choose players to add: ")
    list_of_players_string = add_players.split()
    for player_string in list_of_players_string:
        for player in list_of_all_players:
            if player_string == player.get_name():
                players_playing.append(player)

    print()
    try:
        if len(players_playing) >= 2:               # Requires atleast 2 people playing or raises exception
            print("Balanced Teams: ")
            randomizer(players_playing)
        else:
            raise NotEnoughPlayers
    except NotEnoughPlayers:
        print("You need to add atleast 2 players!")


def main():
    """
    Outlines use of program and calls start()
    """

    print("Welcome to TeamRandomizer! by Basil")
    print()
    print("!DISCLAIMER!")
    print("Please choose players from the list below.")
    print("If someone is not on the list they must be added piror to running program...ask Basil")
    print("Add player names as shown below with a single space between players. Pressing enter when finished.")
    print()
    print("!Team balance in the current version is based on VALORANT!")
    print()
    print()
    print("List of current players in database:")
    print("     ###########################################################")
    print("     |   basil       nab         chris       garrett     ervin |")
    print("     |   teetee      koala       tiff        baran       taha  |")
    print("     |   brad        sw8r        meek        joey        juan  |")
    print("     |   ntry                                                  |")
    print("     ###########################################################")
    print()
    start()


if __name__ == "__main__":
    main()
