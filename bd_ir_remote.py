from bluedot import BlueDot
from gpiozero import LED
from signal import pause
import json, subprocess

f = open('buttons.json')
buttons_json = json.load(f)
f.close()

rows = len(buttons_json)
print(rows)

cols = len(buttons_json[0])
print(cols)

bd = BlueDot(cols=cols, rows=rows)

# Color the buttons
for button in bd.buttons:
  color = buttons_json[button.row][button.col]['color']
  print("Setting " + str(button.col) + "." + str(button.row) + " " + color)
  button.color = color
  
def run_cmd(cmd, params):
    command = cmd + " " + params
    print("-------------------------------------- running: " + command)
    output = subprocess.Popen(command.split())

    return cmd

def pressed(pos):
  print("button {}.{} pressed".format(pos.col, pos.row))
  panel_button = buttons_json[pos.row][pos.col]['panel_button']
  cmd = run_cmd("/root/press_panel_button.sh", panel_button)

bd.when_pressed = pressed

pause()