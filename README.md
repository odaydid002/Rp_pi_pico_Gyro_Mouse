# Rp_pi_pico_Gyro_Mouse
Making gyro mouse using raspberry pi pico minicontroller + MPU6050 sensor

Setup:

![Screenshot 2024-03-06 200346](https://github.com/odaydid002/Rp_pi_pico_Gyro_Mouse/assets/88271352/6b561d8d-b931-4132-99e6-6c7ff05e234f)


MPU6050:
VCC  ------>   3.3v OUT (Pin 37)
GND  ------>   Any GND pin in board
SCL  ------>   I2C1 SCL GP1 (Pin 2)
SDA  ------>   I2C0 SDA GP0 (Pin 1)

Buttons: Use any GPIO pins for the buttons in our exemple we use GP12 for right click and GP13 for left click 
  Connect the button between GND and GPIO pin.


Raspberry pi pico
    Press and hold BOOTSEL button and plug the usb to the computer.
    It will apeare as storage device that has two files    INDEX.HTM  |  INFO_UF2.TXT
    Copy flash_nuke.uf2 And wait until reboot
    Copy adafruit-circuitpython-raspberry_pi_pico-en_US-8.0.0 The device will automaticly reboot with deferent name.
    Copy boot.py file and the lib folder to your raspberry pi pico device.
    
  If you want to edit the code:
    Open thonny. if you don't have thonny IDE, you can download it from link: https://thonny.org
    Connect GP15 (pin20) to GND and replug the device.
    Open Code.py from Thonny and start editing
    when you done save it to your Pico
