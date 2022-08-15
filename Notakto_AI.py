BoardA=[0,1,2,3,4,5,6,7,8]
BoardB=[0,1,2,3,4,5,6,7,8]
BoardC=[0,1,2,3,4,5,6,7,8]
Numbers=['0','1','2','3','4','5','6','7','8']
Alpha=['A','B','C']
MBoard = [BoardA, BoardB, BoardC]


dead=0 # Tells you how many boards are dead
FixC=0# Comes into play when alpha=[A,C] so that C takes the index of 1.
move=0 #Move starts with 0, basically move of every player is location+position
firstmove=0 # first move of AI determined by it
location=0
position=0
value=65
count=0 
trip=True
mylocation=0


def game():
  board()
  while dead<3:#Main game play. Game continues as long as oneboard is alive
    index()
    player()

def index():# Modifies value in such a way so that the game works
  global value

  if Alpha==['B','C']:
    value=66
  elif Alpha==['C']:
    value=67
  elif Alpha==['B']:
    value=66
  
def board():#Only displays if threeboards are alive
  print('A      B      C')
  print(*BoardA[:3],'',*BoardB[:3],'',*BoardC[:3])
  print(*BoardA[3:6],'',*BoardB[3:6],'',*BoardC[3:6],)
  print(*BoardA[6:],'',*BoardB[6:],'',*BoardC[6:])

def two(X,Y):#Only displays if only twoboards are alive
  print(X,'    ',Y)
  print(*MBoard[0][:3],'',*MBoard[1][:3])
  print(*MBoard[0][3:6],'',*MBoard[1][3:6])
  print(*MBoard[0][6:],'',*MBoard[1][6:])

def one(Y):#Only displays if only one board is alive.
  print(Y)
  print(*MBoard[0][:3])
  print(*MBoard[0][3:6])
  print(*MBoard[0][6:])

def player():# Takes input from the player. Checks if its valid.
  global count #Player 1 makes move only when count is 0
  global value
  global FixC
  global move
  global location
  global position

  while True:
    if count==0:
      move=player1()
      print('Player 1:',move)
      move_given_by='Player 1'
      winner='Player 2'
    else:
      move=input('Player 2: ')#[A,B,C]
      move_given_by='Player 2'#[0,1,2]
      winner='Player 1'       #[B,C]

    if len(move)!=2:
      print('Invalid move, please input again')
    else:
      location,position=move 
      if Alpha==['A','C'] and location=='C':
        FixC=1
      if Alpha==['A','C'] and location=='A':
        FixC=0
      if count==0:
        break
      else:
        if (position in Numbers) and (location in Alpha) and (MBoard[ord(location)-value-FixC][int(position)])!='X':
          break
        else:
          print('Invalid move, please input again')
  MBoard[ord(location)-value-FixC][int(position)]='X'

  if move_given_by=='Player 1':
    count=1
  else:
    count=0
  checkboard(ord(location)-value-FixC,location,winner)

def checkboard(z,L,p):# Determines which board is dead
   global dead
   global value

   if MBoard[z][:3].count('X')==3 or MBoard[z][3:6].count('X')==3 or MBoard[z][6:].count('X')==3:
     dead+=1
     del MBoard[z]
     Alpha.remove(L)

   elif MBoard[z][:7:3].count('X')==3 or MBoard[z][1:8:3].count('X')==3 or MBoard[z][2:9:3].count('X')==3:
     dead+=1
     del MBoard[z]
     Alpha.remove(L)

   elif MBoard[z][:9:4].count('X')==3 or MBoard[z][2:7:2].count('X')==3:
     dead+=1
     del MBoard[z]
     Alpha.remove(L)

   if dead!=3:
     display()
   if dead==3:
     print(p,'wins game')

def display():# Displays only if there is atleast one remaining board
  global dead
  if dead==0:
    BoardA, BoardB, BoardC=MBoard
    board()
  elif dead==1:
    two(Alpha[0],Alpha[1])
  elif dead==2:
    one(Alpha[0])


def player1():# Move given by my AI
  global firstmove
  global value
  global location
  global FixC
  global dead
  global trip
  global mylocation

  if firstmove==0:# First move given by AI
    tactic='A4'
    firstmove+=1
    return tactic
  else:
    if location=='B' and trip==True: #That is if player2 plays first move on B happens when NO X on board
      tactic='C4'
      trip= False
      mylocation='C'
      return tactic

    elif location=='C'and trip==True: #That is if player2 plays first move on C happens when NO X on board
      tactic='B4'
      trip= False
      mylocation="B"
      return tactic

    if len(MBoard)==2 and MBoard[0][4]=='X' and MBoard[1][4]=='X':
      tactic=location+str(simplesacrifice1(ord(location)-value-FixC))
      return tactic
    
    elif dead==2 and MBoard[0][4]=='X':# That is if player2 plays first move on A
      tactic=location+str(boottrap(ord(location)-value-FixC))
      return tactic
    
    elif len(MBoard)==2 and MBoard[ord(location)-value-FixC][4]=='X' and MBoard[0][4]!=MBoard[1][4]:
      tactic=location+str(boottrap(ord(location)-value-FixC))
      return tactic

    elif dead==1 and MBoard[ord(location)-value-FixC][4]=='X' and (MBoard[0][4]!='X'or MBoard[1][4]!='X') and MBoard.count('X')>1:
      tactic=location+str(boottrap(ord(location)-value-FixC))
      return tactic


    elif dead==2 and mylocation in Alpha and MBoard[0][4]=='X' and MBoard[1][4]=='X':

      tactic=location+str(simplesacrifice1(ord(location)-value-FixC))
      return tactic

    elif location==mylocation and mylocation in Alpha and dead==1: # IF opponent plays in my board where I have a X at center, 2 board remaining
      tactic=location+str(boottrap(ord(location)-value-FixC))
      return tactic

    elif mylocation not in Alpha and dead==2: # If opponent killed my boottrap , 1 board remaining
      tactic=Alpha[0]+str(attacked(0))
      return tactic

    elif dead!=2 and MBoard[ord(location)-value-FixC].count('X')>1:# 3rd move by AI and an only happens if there is already an X on the board

      tactic=location+str(simplesacrifice1(ord(location)-value-FixC))
      if str(simplesacrifice1(ord(location)-value-FixC)) in Numbers: # if its possible to kill the board simply, otherwise it returns NONE
        return tactic

      else:
        tactic= location+str(complex2X(ord(location)-value-FixC)) # if the board can only be killed by setting up 2X
        return tactic
    


def simplesacrifice1(z):# if they played in the board with an x already. 
  score=0
  for i in range(9):
    if MBoard[z][i]!='X':
      MBoard[z][i]='X'
      if MBoard[z][:3].count('X')==3 or MBoard[z][3:6].count('X')==3 or MBoard[z][6:].count('X')==3:
        break
      elif MBoard[z][:7:3].count('X')==3 or MBoard[z][1:8:3].count('X')==3 or MBoard[z][2:9:3].count('X')==3:
        break
      elif MBoard[z][:9:4].count('X')==3 or MBoard[z][2:7:2].count('X')==3:
        break
      else:
        MBoard[z][i]=i
        score+=1
  if score!=7:
    return i
  else:
    return complex2X(z)

def complex2X(z):# cant be killed simply so have to apply the 2X method
  global position
  combination=[[0,5,7],[1,5,6],[2,3,7],[3,1,8],[99],[5,1,6],[6,1,5],[7,0,5],[8,1,3]]
  for index in combination:
    if int(position) in index:
      record=[]
      for i in index:
        record.append(str(MBoard[z][i]))
      if record.count('X')==2:

        for i in record:
          if i in Numbers:
            MBoard[z][int(i)]='X'
            return i
            break

def boottrap(z): # Traps in the last board
  global position
  combination=[[5,7],[6,8],[7,3],[2,8],[9999],[0,6],[1,5],[0,2],[1,3]]
  for index in combination:
    if combination.index(index)==int(position) and combination.index(index)!=4:
      for i in index:
        if MBoard[z][i]!='X':
          MBoard[z][i]='X'
          status= boardstatus(ord(location)-value-FixC)
          if status=='alive':
            return i
            break
          else:
            MBoard[z][i]=i

def attacked(z):
  combination=[[0,8],[2,6],[3,5],[1,7]] # IF NO 2X trap in the last board
  combo2=[1,3,5,7] # IF THERE IS 2X TRAP IN LAST BOARD
  
  for index in combination:
    if MBoard[z][index[0]]=='X' and MBoard[z][index[1]]!='X':

      MBoard[z][index[1]]=='X'
      return index[1]
      break
    elif MBoard[z][index[1]]=='X' and MBoard[z][index[0]]!='X':
      MBoard[z][index[0]]=='X'
      return index[0]
      break
       
  if MBoard[z].count('X')==5:
    for i in combo2:
      if MBoard[z][i]!='X':
        MBoard[z][i]=='X'
        return i

def boardstatus(z):
  status='alive' # this means board won't be dead if next move made in it
  if MBoard[z][:3].count('X')==3 or MBoard[z][3:6].count('X')==3 or MBoard[z][6:].count('X')==3:
    status='dead'
  elif MBoard[z][:7:3].count('X')==3 or MBoard[z][1:8:3].count('X')==3 or MBoard[z][2:9:3].count('X')==3:
    status='dead'
  elif MBoard[z][:9:4].count('X')==3 or MBoard[z][2:7:2].count('X')==3:
    status='dead'
  return status

game()