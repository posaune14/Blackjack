import pygame, sys, random
from pygame.locals import QUIT

pygame.init()
deck = [2]
images = []


class Card(pygame.sprite.Sprite):

    def __init__(self, fileName, cardType):
        pygame.sprite.Sprite.__init__(self)
        self.state = "null"
        self.image = pygame.image.load(fileName)
        self.image = pygame.transform.scale(self.image, (75, 100))
        self.fileName = fileName
        self.cardType = cardType
        self.rect = self.image.get_rect()
        self.rect.x = 700
        self.rect.y = 0
        self.distance = 375

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self):
        if self.cardType == "player" and self.rect.y > self.distance:
            self.speed = [0, 0]
        if self.cardType == "dealer" and self.rect.y >30:
            self.speed = [0, 0]
        self.rect = self.rect.move(self.speed)

    def update(self):
        #self.move()
        if self.state == "move":
            self.move()


class gameState():

  def __init__(self):
      self.scene = "main_menu"

  def state_manager(self):
      #if statement that depending on scene calls main menu or main game
      if self.scene == "main_menu":
          self.main_menu()
      if self.scene == "main_game":
          self.main_game()
      #if self.scene == "end_game":
          #self.end_game()

  def main_menu(self):
      for event in pygame.event.get():
          if event.type == QUIT:
              pygame.quit()
              sys.exit()
          #button code
          if event.type == pygame.MOUSEBUTTONDOWN:
              if buttonrect.collidepoint(event.pos):
                  self.scene = "main_game"
      screen.fill("#333333")
      screen.blit(button, buttonrect)
      screen.blit(blackjack, blackjackrect)
      screen.blit(butheresascreen, butheresascreenrect)
      pygame.display.update()
      pygame.time.delay(100)

  def main_game(self):
    global x
    global y
    global active
    global inputText
    global color
    global textSurface
    global wager
    global cardValuePlayer
    global repeat
    global tokens
    global currencyText
    global negative
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
      #repeating to add two cards to each hand 
      if event.type == pygame.MOUSEBUTTONDOWN:
        if textbox.collidepoint(event.pos):
          active = True
          color=colorActive
          textSurface = text.render(inputText, True, (color))
        else:
          active = False
          color=colorPassive
          textSurface = text.render(inputText, True, (color))
        if hitButtonrect.collidepoint(event.pos) and cardValuePlayer<21 and inputText != 'no. 1-100':
          if tokens-int(inputText) > -1 or negative==2:
            if tokens == 100:
              tokens -= int(inputText)
              negative+=1
              currencyText = text.render(str(tokens) + " Tokens", True, (0, 0, 0))
            playerCardDraw()
        if hitButtonrect.collidepoint(event.pos) or standButtonrect.collidepoint(event.pos):
          if inputText != 'no. 1-100' and tokens < int(inputText) and len(playerCards) == 2:
            inputText = ' Not enough tokens'
            textSurface = text.render(inputText, True, (color))
        if standButtonrect.collidepoint(event.pos) and inputText != 'no. 1-100' and inputText != " Not enough tokens":
          if tokens == 100:
            tokens -= int(inputText)
            currencyText = text.render(str(tokens) + " Tokens", True, (0, 0, 0))
          finalDealerCardDraw()
      if event.type == pygame.KEYDOWN:
        if active:
          if event.key == pygame.K_RETURN:
            active = False
            color=colorPassive
            textSurface = text.render(inputText, True, (color))
          elif event.key == pygame.K_TAB:
            inputText = ' '
            textbox.x=370
            textSurface = text.render(inputText, True, (color))
          elif event.key == pygame.K_BACKSPACE:
            inputText = inputText[:-1]
            textSurface = text.render(inputText, True, (color))
          else:
            inputText += event.unicode
            textSurface = text.render(inputText, True, (color))
      if end==2:
        self.scene = "end_game"
    if repeat == 0:
      firstDealerCardDraw()
      playerCardDraw()
    if repeat == 1:
      secondDealerCardDraw()
      playerCardDraw()
    #if button.collidepoint(event.pos):
    #collidepoint checks if moust pointer is at the button location
    screen.fill("#2D5A27")
    screen.blit(deck, deckrect)
    #screen.blit(wager, (325, 200))
    screen.blit(standButton, standButtonrect)
    screen.blit(hitButton, hitButtonrect)
    screen.blit(textSurface, (textbox.x+5, textbox.y+5))
    screen.blit(wagerLabel, wagerLabalRect)
    screen.blit(currencyText, currencyTextRect)
    cards.draw(screen)
    cards.update()
    pygame.display.update()
    pygame.time.delay(100)
  def end_game(self):
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
    screen.fill("#333333")
    pygame.display.update()
    pygame.time.delay(100)
repeat=0
negative=1
#speed modifier for new cards


#save first card file name
firstCard = ''
#card list
totalCards = []


x = 0
y = 0
#hit card values, 
cardValueDealer = 0
cardValuePlayer = 0
dealerCards = []
playerCards = []
def cardComputation(card):
  word = card.fileName
  for i in range(2, 11):
    if word.find(str(i)) == 7:
      return i
    if word.find('king') == 7:
      return 10
    if word.find('queen') == 7:
      return 10
    if word.find('jack') == 7:
      return 10
    if word.find('ace') == 7:
      return 11
def checkAce():
  if 11 in playerCards and cardValuePlayer >21:
    playerCards.remove(11)
    playerCards.append(1)
  if 11 in dealerCards and cardValueDealer >21:
    dealerCards.remove(11)
    dealerCards.append(1)
      #check both player and dealer cards to see if ace is in them and then we can change the ace value depending on the total
def firstDealerCardDraw():
  global deckImages
  global y
  global repeat
  global cardValueDealer
  global firstCard
  global totalCards
  filename = deckImages.pop()
  card = Card(filename, 'dealer')
  dealerCards.append(cardComputation(card))
  cardValueDealer = sum(dealerCards)
  card.image = pygame.image.load("playingCardBack.png")
  card.image = pygame.transform.scale(card.image, (75, 100))
  card.fileName = filename
  firstCard = filename
  card.state = 'move'
  card.speed = [-25+y, 2]
  y+=2
  totalCards.append(card)
  cards.add(card)
def secondDealerCardDraw():
  global deckImages
  global y
  global cardValueDealer
  filename = deckImages.pop()
  card = Card(filename, 'dealer')
  card.state = 'move'
  card.speed = [-25+y, 2]
  y+=2
  dealerCards.append(cardComputation(card))
  checkAce()
  cardValueDealer = sum(dealerCards)
  cards.add(card)
def finalDealerCardDraw():
  global deckImages
  global y
  global cardValueDealer
  global firstCard
  global totalCards
  flipCard()
  for i in range(3):
    if cardValueDealer < 17:
      filename = deckImages.pop()
      card = Card(filename, 'dealer')
      card.state = 'move'
      card.speed = [-25+y, 2]
      y+=2
      dealerCards.append(cardComputation(card))
      cardValueDealer = sum(dealerCards)
      checkAce()
      cardValueDealer = sum(dealerCards)
      cards.add(card)
    else:
      pass
  checkResult()
def flipCard():
  global deckImages
  global firstCard
  global totalCards
  cardImage = pygame.image.load(firstCard)
  cardImage = pygame.transform.scale(cardImage, (75, 100))
  totalCards[0].image = cardImage
def playerCardDraw():
  global deckImages
  global x
  global cardValuePlayer
  global repeat
  card = Card(deckImages.pop(), 'player')
  playerCards.append(cardComputation(card))
  cardValuePlayer = sum(playerCards) 
  checkAce()
  cardValuePlayer = sum(playerCards) 
  card.state = 'move'
  card.speed = [-12 + x, 12]
  x+=1
  cards.add(card)
  repeat+=1
end = 1
def checkResult():
  global tokens
  global currencyText
  global end
  if cardValueDealer>21 and cardValuePlayer<22: #win 
    tokens += ((int(inputText))*2)
  if cardValueDealer<cardValuePlayer and cardValuePlayer<22: #win
    tokens += ((int(inputText))*2)
  if cardValuePlayer>21 and cardValueDealer>21: #draw
    tokens += (int(inputText))
  if cardValuePlayer==cardValueDealer and cardValuePlayer<22: #draw
    tokens += (int(inputText))
  if cardValuePlayer<cardValueDealer and cardValueDealer<22: #lost
    pass
  if cardValueDealer<22 and cardValuePlayer>21: #lost
    pass
  print(tokens)
  currencyText = text.render(str(tokens) + " Tokens", True, (0, 0, 0))
  end+=1
  #need to animate
    
#max number of cards is 11 that can be taken
#card filenames for creating new files
deckImages = [
    "assets/ace_of_clubs.png", "assets/ace_of_diamonds.png",
    "assets/ace_of_hearts.png", "assets/ace_of_spades.png",
    "assets/2_of_clubs.png", "assets/2_of_diamonds.png",
    "assets/2_of_hearts.png", "assets/2_of_spades.png",
    "assets/3_of_clubs.png", "assets/3_of_diamonds.png",
    "assets/3_of_hearts.png", "assets/3_of_spades.png",
    "assets/4_of_clubs.png", "assets/4_of_diamonds.png",
    "assets/4_of_hearts.png", "assets/4_of_spades.png",
    "assets/5_of_clubs.png", "assets/5_of_diamonds.png",
    "assets/5_of_hearts.png", "assets/5_of_spades.png",
    "assets/6_of_clubs.png", "assets/6_of_diamonds.png",
    "assets/6_of_hearts.png", "assets/6_of_spades.png",
    "assets/7_of_clubs.png", "assets/7_of_diamonds.png",
    "assets/7_of_hearts.png", "assets/7_of_spades.png",
    "assets/8_of_clubs.png", "assets/8_of_diamonds.png",
    "assets/8_of_hearts.png", "assets/8_of_spades.png",
    'assets/queen_of_spades.png', 'assets/queen_of_hearts.png',
    'assets/queen_of_diamonds.png', 'assets/queen_of_clubs.png',
    'assets/king_of_clubs.png', 'assets/king_of_diamonds.png',
    'assets/king_of_hearts.png', 'assets/king_of_spades.png',
    'assets/jack_of_clubs.png', 'assets/jack_of_diamonds.png',
    'assets/jack_of_hearts.png', 'assets/jack_of_spades.png',
    'assets/10_of_clubs.png', 'assets/10_of_diamonds.png',
    'assets/10_of_hearts.png', 'assets/10_of_spades.png',
    'assets/9_of_clubs.png', 'assets/9_of_diamonds.png',
    'assets/9_of_hearts.png', 'assets/9_of_spades.png'
]
random.shuffle(deckImages)
#'playingCardBack.png'
#wage variables
colorPassive = (0, 0, 0)
colorActive = (255, 255, 255)
color = colorPassive
active = False
#game variables
'''z=0
wage = z
#Display wage amount on screen
black = 0, 0, 0'''
text = pygame.font.SysFont('times new roman', 18)
#This creates a new Surface with the specified text rendered on it.
#wager = text.render('Wager: ' + str(wage) + ' Chips', True, black)
#Create a pygame sprite group to organize all the cards on the screen
cards = pygame.sprite.Group()
game_state = gameState()

#Create textbox input for wages
#Rect(left, top, width, height) -> Rect
textbox = pygame.Rect(380, 550, 100, 100)
defaultText = pygame.font.Font(None, 24)
inputText = 'no. 1-100'
textSurface = text.render(inputText, True, (color))
textbox.w = max(100, textSurface.get_width()+10)
#centerline text, delete text when clicked on, implement text given into wage variable

#currency
tokens = 100

#wage text
wagerLabalRect = pygame.Rect(310, 555, 100, 100)
wagerLabel = pygame.font.Font(None, 24)
wagerLabel = text.render('Wager:', True, (0, 0, 0))

#currency left
currencyTextRect = pygame.Rect(10, 10, 100, 100)
currencyText = pygame.font.Font(None, 24)
currencyText = text.render('100 Tokens', True, (0, 0, 0))

#Main menu images and buttons
button = pygame.image.load("green/normal.png")
button = pygame.transform.scale(button, (150, 100))
buttonrect = button.get_rect()
buttonrect.x = 325
buttonrect.y = 250

blackjack = pygame.image.load("blackjack.png")
blackjack = pygame.transform.scale(blackjack, (300, 200))
blackjackrect = blackjack.get_rect()
blackjackrect.x = 250
blackjackrect.y = 25

butheresascreen = pygame.image.load("butheresascreen.png")
butheresascreen = pygame.transform.scale(butheresascreen, (600, 200))
butheresascreenrect = butheresascreen.get_rect()
butheresascreenrect.x = 100
butheresascreenrect.y = 350

#Create main game buttons and set positions
hitButton = pygame.image.load("hit.png")
hitButton = pygame.transform.scale(hitButton, (75, 50))
hitButtonrect = hitButton.get_rect()
hitButtonrect.x = 200
hitButtonrect.y = 250

standButton = pygame.image.load("stand.png")
standButton = pygame.transform.scale(standButton, (125, 50))
standButtonrect = standButton.get_rect()
standButtonrect.x = 500
standButtonrect.y = 250

#Create game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Hello World!')



#Create deck image on screen and set position
deck = pygame.image.load('playingCardBack.png')
deck = pygame.transform.scale(deck, (75, 100))
deckrect = deck.get_rect()
deckrect.x = 700
deckrect.y = 0

while True:
    game_state.state_manager()


#https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite

#Things to do later:
#Reorganize code so we dont use so many global
#game functionality (ace value change, calculating results)
