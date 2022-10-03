from serial.tools import list_ports
import pydobot
import math

from PIL import Image


ports = [p.device for p in list_ports.comports()]


for i,port in enumerate(ports):
    print(f"{i}: {port}")

port = ports[int(input("Vælg en port: "))]

try:
    dobot = pydobot.Dobot(port=port)
except:
    print("Fejl, kunne ikke forbinde til robotten")
print("Forbindelse oprettet")



def home():
    mode=pydobot.enums.PTPMode.MOVJ_XYZ
    dobot._set_ptp_cmd(250, 0, 150, 90, mode=mode, wait=True)

def firkant(x, y, w, h):
	dobot.move_to(x, y, -30, 0, wait = True)
	dobot.move_to(x, (y+h), -30, 0, wait = True)
	dobot.move_to((x+w), (y+h), -30, 0, wait = True)
	dobot.move_to((x+w), y, -30, 0, wait = True)
	dobot.move_to(x, y, -30, 0, wait = True)


done = False

while done == False:
    cmd = input("Vælg kommando: ")

    if cmd.startswith("q"):
        dobot.close()
        done = True
    elif cmd == "Firkant":
        firkant(250, 0, 20, 20)

    elif cmd == "Sekskant":
    	dobot.move_to(250, 0, -30, 0, wait = True)
    	dobot.move_to(260, 10, -30, 0, wait = True)
    	dobot.move_to(260, 20, -30, 0, wait = True)
    	dobot.move_to(250, 30, -30, 0, wait = True)
    	dobot.move_to(240, 20, -30, 0, wait = True)
    	dobot.move_to(240, 10, -30, 0, wait = True)
    	dobot.move_to(250, 0, -30, 0, wait = True)

    elif cmd == "pos":
    	print(dobot.pose())

    elif cmd == "billede":
        p = "image-asset.jpeg"
        with Image.open(p) as im:
            im = im.resize((80, 80))
            pix = im.load()

        for y in range(0, im.width):
            pixel = pix[y, x]
            if pixel == (0, 0, 0):
                firkant(x+250, y, 2, 2)

    #elif cmd == "cirkel":
    #	for v in range(0,360,5):
    #		r = 20
    #		dobot.move_to(r*math.cos(v)+250,r*math.sin(v),-30, 0, wait=True)
