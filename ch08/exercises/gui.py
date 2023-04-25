class Player:
  def __init__(self, pnum=1):
    """
    Initialize the player object
    args: pnum [int] the player's id number
    """
    self.player_num = pnum
    self.lives = 4 # players always start with 4 lives
    self.is_large = False # player always starts small

class Enemy:
    def __init__(self):
        self.position = [0, 0]  
        self.velocity = [0, 0]  
        self.damage = 3

class Powerup:
    def __init__(self):
        self.position = [0, 0] 
        self.effect = "heal" 
        self.duration = 15