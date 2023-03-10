from bluedot import BlueDot
from gpiozero import LED
from signal import pause
import json, subprocess

bd = BlueDot(cols=2, rows=1)

for button in bd.buttons:
  if button.col == 0 and button.row == 0:
    button.color = "green"
  if button.col == 1 and button.row == 0:
    button.color = "red"

def get_cmd(data, cmd_name, params):
  for i in data:
    if i["trigger"] == cmd_name:
      print("trigger: " + i["trigger"])
      print("command: " + i["command"] + " " + params)

  return cmd_name

def run_cmd(data, cmd_name, params):
  for i in data:
    if i["trigger"] == cmd_name:
      print("-------------------------------------- trigger: " + i["trigger"])
      command = i["command"] + " " + params
      print("-------------------------------------- command: " + command)
      output = subprocess.Popen(command.split())
      # print(output)

  return cmd_name

f = open('/root/.TRIGGERcmdData/commands.json')
data = json.load(f)

# Closing file
f.close()

def pressed(pos):
    print("button {}.{} pressed".format(pos.col, pos.row))
    button=str(pos.col) + "." + str(pos.row)
    if(pos.col == 0 and pos.row == 0):
      cmd = run_cmd(data, "power", "on")
    if(pos.col == 1 and pos.row == 0):
      cmd = run_cmd(data, "power", "off")

bd.when_pressed = pressed

pause()