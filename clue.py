suspects = ["Green", "Mustard", "Peacock", "Plum", "Scarlett", "White"]
weapons = ["Candlestick", "Dagger", "Lead Pipe", "Revolver", "Rope", "Wrench"]
rooms = ["Ballroom", "Billiard Room", "Conservatory", "Dining Room", "Hall", "Kitchen","Library", "Lounge", "Study"]
totalCards = 21
cardsAfterSol = 18

class player:
  """
  Player class that contains an initializer and 
  functions to add cards (max 3) and check if 
  the given player has a card.
  """
  def __init__(self, name, cards):
    self.name = name
    self.cards = cards

  def addCard(self, card):
    if len(self.cards) < 3:
      self.cards[len(self.cards - 1)] = card
    else:
      return False

  def checkCard(self, card):
    for x in self.cards:
      if x == card:
        return True
    return False


def initGame():
  players = []
  numPlayers = int(input("What is the number of players?"))
  cardsPer = cardsAfterSol // numPlayers
  for num in range(numPlayers):
    cards = []
    if num == 0:
      for x in range(cardsPer):
        card = input("input your card: ")
        cards.append(card)
      players.append(player("main", cards))
    else:
      players.append(player(input("What is the next player's name: "), cards))
  return players
  

if __name__ == "__main__":
  players = initGame()
