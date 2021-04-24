import serial
import time

serialArduino=serial.Serial("COM2",9600)
time.sleep(1)


while True:
    cad=serialArduino.readline().decode('ascii')
   pos=cad.index(":")
   rot=cad[:pos]
   pot1=cad[pos+1]

   if rot=='pot_arduino':
       print("Datos del potenciometro: {}".format(pot1))
   
   
    print(+*+*+*+*+*+*+*+*+*+*+*+*+*)
    print(cad)
    print(+*+*+*+*+*+*+*+*+*+*+*+*+*)