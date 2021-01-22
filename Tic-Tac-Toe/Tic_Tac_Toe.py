print("*" * 10, " Гра хрестики нолики для двох гравців ", "*" * 10)

board = list(range(1, 10))

def drawBoard(board):
    print("-" * 13)
    for i in range(3):
        print("|", board[i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
    print("-" * 13)

def takeInput(playerToken):
   valid = False
   while not valid:
      playerAnswer = input("Куди поставити " + playerToken + "? ")
      try:
         playerAnswer = int(playerAnswer)
      except:
         print("Некоректний ввід. Ви впевнені що ввели число?")
         continue
      if playerAnswer >= 1 and playerAnswer <= 9:
         if(str(board[playerAnswer-1]) not in "XO"):
            board[playerAnswer-1] = playerToken
            valid = True
         else:
            print("Ця клітинка уже зайнята!")
      else:
        print("Некоректний ввід. Введіть число від 1 до 9.")

def checkWin(board):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          return board[each[0]]

def main(board):
    counter = 0
    win = False
    while not win:
        drawBoard(board)
        if counter % 2 == 0:
           takeInput("X")
        else:
           takeInput("O")
        counter += 1
        if counter > 4:
           tmp = checkWin(board)
           if tmp:
              print(tmp, "виграв!")
              win = True
              break
        if counter == 9:
            print("Нічия!")
            break
    drawBoard(board)

main(board)

input("Нажміть Enter для виходу!")