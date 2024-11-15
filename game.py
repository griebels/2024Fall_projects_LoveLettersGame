from players import *

class Game:
    def __init__(self, players):
        self.players = players
        # game.players[2] --> a player object
        cards_drawn, cards = new_game()
        # print(len(cards))
        cards = current_deck(cards, cards_drawn)
        deal_cards()

    def deal_cards(self):
        """
        Deals cards randomly to each player prior to the first round
        :return:
        """
        for player in self.players:
            player.players_hand = []
            card_drawn = draw_a_card(cards_drawn, cards)
            player.players_hand.append(card_drawn)
def new_game():
    """
    Starts a new game by resetting cards to have the entire deck, and resets cards_drawn to empty since no cards have been drawn yet.
    :return: cards_drawn, cards
    """
    cards_drawn = []
    cards = [Princess(), 'Countess', 'King', 'Prince', 'Prince', 'Handmaid', 'Handmaid', 'Baron', 'Baron', 'Priest',
             'Priest', 'Guard', 'Guard', 'Guard', 'Guard', 'Guard']

    return cards_drawn, cards

def deal_cards():
    """
    Deals cards randomly to each player prior to the first round
    :return:
    """
    Player.players_hand = []
    card_drawn = draw_a_card(cards_drawn, cards)
    Player1.players_hand.append(card_drawn)

    # Player2.players_hand = []
    # card_drawn = draw_a_card(cards_drawn, cards)
    # Player2.players_hand.append(card_drawn)
    #
    # Player3.players_hand = []
    # card_drawn = draw_a_card(cards_drawn, cards)
    # Player3.players_hand.append(card_drawn)



def current_deck(cards, cards_drawn):
    """
    keep track of the current deck, removing cards_played (discard pile) and cards_drawn (currently in players hands)
    :param cards:
    :param cards_drawn:
    :return: cards that are in play
    """
    for card in cards:
        if card in cards_drawn:
            cards.remove(card)
    return cards

def players_hand(player):
    """
    keep track of the players current hand
    :param player:
    :return:
    """
    players_hand = []
    return players_hand

def draw_a_card(cards_drawn, cards, players_hand):
    """
    Draws a card randomly from the current deck
    :param cards_drawn:
    :param cards:
    :return: card that is drawn
    """
    i = random.randint(0, 15)
    card_drawn = cards[i]
    cards_drawn.append(card_drawn)
    players_hand.append(card_drawn)
    return card_drawn, cards_drawn, players_hand

# def play_card():
#     """
#
#     :return:
#     """


def player_is_out_of_the_round(player_out, players):
    """
    removes a player who is out of the round from the players list, and returns the players who are still in that round
    :return: players who are still in the round
    """
    players = players.remove(player_out)
    return players


def list_opponents(players, current_player):
    # TODO: check if opponent has handmaid card, then remove them from opponents list?

    opponents = players.remove(current_player)
    return opponents

def update_cards_played(card_played, cards_played):
    cards_played.append(card_played)
    return cards_played, cards_played

def clear_cards_in_play(cards_in_play):
    cards_in_play = []
    return cards_in_play

def player_turn(player, Player.strategy):
    card_drawn = draw_a_card(cards_drawn, cards)
    player.players_hand.append(card_drawn)
    move = player.strategy(self, opponents_hand)
    return move


def round():
    for player in players:
        player_turn(player, player.strategy)


def winner():
    if len(players) == 1:
        return players[0]

    elif len(current_deck) = 0:
        ending_hands = {}

        # players[0] > players [1]
        for player in players:
            ending_hands.append(player: player.players_hand.card_value)
            #TODO : find correct syntax for adding to dict, its not the above pseudo code
            current_max_value = 0
        for player in ending_hands:
            if player.players_hand.card_value > current_max_value
            current_max_value = player.players_hand.card_value
            #can we access who that player is from the class structure above
            winner = current_max_value
            return winner

#check if there is already a clear winner before implementing a round
def game_play_until_winner():
    if len(players) != 1 or len(cards) != 0: #if no winner yet
        round()
    #recursion of rounds until a winner is identified for that game
    else:
        winner = winner()
    return winner