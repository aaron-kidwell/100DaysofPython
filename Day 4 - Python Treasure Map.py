#Welcome to my Python Treasure Map Game. Plant your treasure using list syntax e.g: 12. This would plant the treasure in the 2nd column last row.

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

column = int(position[0])
row = int(position[1])

if column >= 3 or row >= 3:
  print('Invalid Input Error.')
else:
  map[row][column] = 'X'
  print(f"{row1}\n{row2}\n{row3}")