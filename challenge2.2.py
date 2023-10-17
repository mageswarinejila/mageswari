class player:
  def paly(self):
     print("the player is playing cricket.")

class Batsman(player): 
       def play(self):
          print("the batsman is batting.")

class Bowler(player):
      def play(self):
         print("the bowler is bowlling.")


Batsman = Batsman()
Bowler = Bowler()

Batsman.play()
Bowler.play() 