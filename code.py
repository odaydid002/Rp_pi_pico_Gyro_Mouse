import usb_hid
from adafruit_hid.mouse import Mouse
import busio
import board
import adafruit_mpu6050
from digitalio import DigitalInOut, Direction, Pull

i2c = busio.I2C(board.GP1, board.GP0)
mpu = adafruit_mpu6050.MPU6050(i2c)

mouse = Mouse(usb_hid.devices)

but1 = DigitalInOut(board.GP13)
but1.direction = Direction.INPUT
but1.pull = Pull.UP

but2 = DigitalInOut(board.GP12)
but2.direction = Direction.INPUT
but2.pull = Pull.UP

def map_interval(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

while True:
    
    
    x,y,z = mpu.gyro
    xm = int(map_interval(x, 1,- 1, -15, 15))
    zm = int(map_interval(z, 1, -1, -15, 15))
    
    mouse.move(zm, xm)
    
    if not but1.value:
        mouse.click(Mouse.RIGHT_BUTTON)
        while not but1.value:
            pass
        
    if not but2.value:
        mouse.click(Mouse.LEFT_BUTTON)
        while not but2.value:
            pass
    