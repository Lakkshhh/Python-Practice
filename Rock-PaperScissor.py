import random
options = ['Rock','Paper','Scissor']
comp_ch = random.choice(options)
wins = 0
loss = 0
tie = 0

play_game = True
while play_game:
  user_ch = input('''Enter your choice:
1) Rock 
2) Scissor 
3) Paper 

''')
  print()
  print('User choice = ',user_ch)
  print('Computer choice = ',comp_ch)
  print()
  if user_ch=='Rock':
      if comp_ch=='Paper':
          print('Paper covers Rock. You lose!')
          loss += 1
      elif comp_ch == 'Scissor':
          print('Rock smashes Scissors.You win!')
          wins += 1
      else:
          print('Tie!')
          tie += 1
  elif user_ch == 'Scissor':
      if comp_ch=='Paper':
          print('Scissors cut papers. You win!')
          wins +=1
      elif comp_ch == 'Rock':
          print('Rock smashes Scissors.You lose!')
          loss += 1
      else:
          print('Tie!')
          tie += 1
  elif user_ch == 'Paper':
      if comp_ch=='Rock':
          print('Paper cover rock. You win!')
          wins += 1
      elif comp_ch == 'Scissor':
          print('Scissors cut papers. You lose!')
          loss += 1
      else:
          print('Tie!')
          tie += 1
  else:
      print('Invalid option chosen')
  print()

  usr_ch = True
  while usr_ch:
    usr = input('''Do you wish to play again? 
1) Yes
2) No

''')
    print()
    if usr == 'Yes':
      usr_ch = False
      print('-'*80)
      continue
    elif usr == 'No':
      play_game = False
      print('-'*80)
      break
    else:
      print("Inavlid option chosen!")

print('Total number of wins = ', wins)
print('Total number of losses = ', loss)
print('Total number of ties = ', tie)
