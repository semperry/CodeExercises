def bottle_song():
  bottles = reversed(range(1, 100))

  for bottle in bottles:
    if bottle == 2:
      print(f'{bottle} bottles of beer on the wall, {bottle} bottles of beer. You take one down, pass it around, {next_bottle} bottle of beer on the wall\n')
      
    elif bottle == 1:
      print(f'{bottle} bottle of beer on the wall, {bottle} bottle of beer. You take one down, pass it around, no more bottles of beer on the wall\n')
    else:
        next_bottle = bottle - 1 
        print(f'{bottle} bottles of beer on the wall, {bottle} bottles of beer. You take one down, pass it around, {next_bottle} bottles of beer on the wall\n')
        bottle -= 1
        next_bottle -= 1


bottle_song()