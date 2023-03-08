from bluedot import BlueDot
from gpiozero import LED

bd = BlueDot()
while True:
   bd.wait_for_press()
   print("on")
   bd.wait_for_release()
   print("off")
