"""Simple test for RGB character LCD on Raspberry Pi"""
import time
import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd

# Modify this if you have a different sized character LCD
lcd_columns = 16
lcd_rows = 2

# Raspberry Pi Pin Config:
lcd_rs = digitalio.DigitalInOut(board.D26)  # LCD pin 4
lcd_en = digitalio.DigitalInOut(board.D19)  # LCD pin 6
lcd_d7 = digitalio.DigitalInOut(board.D5)  # LCD pin 14
lcd_d6 = digitalio.DigitalInOut(board.D6)   # LCD pin 13
lcd_d5 = digitalio.DigitalInOut(board.D20)   # LCD pin 12
lcd_d4 = digitalio.DigitalInOut(board.D21)  # LCD pin 11

lcd = characterlcd.Character_LCD_Mono(
    lcd_rs, 
    lcd_en, 
    lcd_d4, 
    lcd_d5, 
    lcd_d6, 
    lcd_d7, 
    lcd_columns, 
    lcd_rows
)

lcd.clear()

lcd.message = "Hello\nCircuitPython!"

