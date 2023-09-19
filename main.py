class Player:
  def play(self):
    print("the player is playing    cricket.")
class Batsman(Player):
  def play(self):
    print("the Batsman is batting.")
class Bowler (Player):
  def play(self):
    print("the Bowler is bowling.")
batsman=Batsman()
bowler=Bowler()
batsman.play()
bowler.play()