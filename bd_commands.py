from bluedot import BlueDot
from gpiozero import LED
import json

bd = BlueDot()

def get_cmd(data, cmd_name, params):
  for i in data:
    if i["trigger"] == cmd_name:
      print("trigger: " + i["trigger"])
      print("command: " + i["command"] + " " + params) 
    
  return cmd_name

# Opening JSON file
f = open('/root/.TRIGGERcmdData/commands.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Closing file
f.close()

while True:
   bd.wait_for_press()
   # print(cmd + " on")
   cmd = get_cmd(data, "power", "on")
   
   bd.wait_for_release()
   # print(cmd + " off")
   cmd = get_cmd(data, "power", "off")
