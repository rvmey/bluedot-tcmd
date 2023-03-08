from bluedot import BlueDot
from signal import pause

def pressed(pos):
    print("button {}.{} pressed".format(pos.col, pos.row))

bd = BlueDot(cols=3, rows=7)
bd.when_pressed = pressed

for button in bd.buttons:
  if button.col == 0 and button.row == 0:
    button.color = "red"
  if button.col == 1 and button.row == 0:
    button.color = "red"
  if button.col == 2 and button.row == 0:
    button.color = "red"
  if button.col == 0 and button.row == 1:
    button.color = "green"
  if button.col == 1 and button.row == 1:
    button.color = "green"
  if button.col == 2 and button.row == 1:
    button.color = "green"
  if button.col == 0 and button.row == 2:
    button.color = "blue"
  if button.col == 1 and button.row == 2:
    button.color = "blue"
  if button.col == 3 and button.row == 2:
    button.color = "purple"
  if button.col == 0 and button.row == 3:
    button.color = "black"
  if button.col == 1 and button.row == 3:
    button.color = "black"
  if button.col == 2 and button.row == 3:
    button.color = "black"
  if button.col == 0 and button.row == 4:
    button.color = "black"
  if button.col == 1 and button.row == 4:
    button.color = "black"
  if button.col == 2 and button.row == 4:
    button.color = "black"
  if button.col == 0 and button.row == 5:
    button.color = "black"
  if button.col == 1 and button.row == 5:
    button.color = "black"
  if button.col == 2 and button.row == 5:
    button.color = "black"
  if button.col == 0 and button.row == 6:
    button.color = "black"
  if button.col == 1 and button.row == 6:
    button.color = "black"
  if button.col == 2 and button.row == 6:
    button.color = "black"

pause()
