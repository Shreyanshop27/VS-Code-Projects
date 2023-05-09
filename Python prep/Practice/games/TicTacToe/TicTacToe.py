from random import choices

class TTT:
    def __init__(self):
      self.row1=[" "," "," "]
      self.row2=[" "," "," "]
      self.row3=[" "," "," "]
    
    def place(self,letter,player):
        """
        This Function take a letter qwe(r1)asd(r2)zxc(r3) to determine where to place Xs or Os
        player (variable) choose that the player is computer ot human
        """
        if letter == "q":
            if player == "h":
                self.row1[0]="O"
            elif player == "c":
                self.row1[0]="X"
        elif letter == "w":
            if player == "h":
                self.row1[1]="O"
            elif player == "c":
                self.row1[1]="X"
        elif letter == "e":
            if player == "h":
                self.row1[2]="O"
            elif player == "c":
                self.row1[2]="X"
        elif letter == "a":
            if player == "h":
                self.row2[0]="O"
            elif player == "c":
                self.row2[0]="X"    
        elif letter == "s":
            if player == "h":
                self.row2[1]="O"
            elif player == "c":
                self.row2[1]="X"
        elif letter == "d":
            if player == "h":
                self.row2[2]="O"
            elif player == "c":
                self.row2[2]="X"
        elif letter == "z":
            if player == "h":
                self.row3[0]="O"
            elif player == "c":
                self.row3[0]="X"
        elif letter == "x":
            if player == "h":
                self.row3[1]="O"
            elif player == "c":
                self.row3[1]="X"
        elif letter == "c":
            if player == "h":
                self.row3[2]="O"
            elif player == "c":
                self.row3[2]="X"

    
  
    def check(self):
        """
        This fuction check if any player has make 3 symbol in row
        and tell which player is winner
        or currently no one has won
        """
        if self.row1 == ["X","X","X"] :
            return 1
        elif self.row2 == ["X","X","X"] :
            return 1
        elif self.row3 == ["X","X","X"] :
            return 1
        elif self.row1[0]=="X" and self.row2[1]=="X" and self.row3[2]=="X":
            return 1
        elif self.row1[2]=="X" and self.row2[1]=="X" and self.row3[0]=="X":
            return 1
        elif self.row1 == ["O","O","O"] :
            return 0
        elif self.row2 == ["O","O","O"] :
            return 0
        elif self.row3 == ["O","O","O"] :
            return 0
        elif self.row1[0]=="O" and self.row2[1]=="O" and self.row3[2]=="O":
            return 0
        elif self.row1[2]=="O" and self.row2[1]=="O" and self.row3[0]=="O":
            return 0
        else:
            return 2
    def board(self):
        print(self.row1)
        print(self.row2)
        print(self.row3)
        
        
        