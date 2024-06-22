import pyfirmata2 as pyfirmata
import time

board = pyfirmata.Arduino("COM5")

phrase = input("Enter a phrase: ")
loop = input("Repeat code (y/n): ").lower()
if loop == "y":
    loop = True
elif loop == "n":
    loop = False
else:
    raise Exception("Only y/n accepted!")
morseCode = {
  "0": "-----",
  "1": ".----",
  "2": "..---",
  "3": "...--",
  "4": "....-",
  "5": ".....",
  "6": "-....",
  "7": "--...",
  "8": "---..",
  "9": "----.",
  "A": ".-",
  "B": "-...",
  "C": "-.-.",
  "D": "-..",
  "E": ".",
  "F": "..-.",
  "G": "--.",
  "H": "....",
  "I": "..",
  "J": ".---",
  "K": "-.-",
  "L": ".-..",
  "M": "--",
  "N": "-.",
  "O": "---",
  "P": ".--.",
  "Q": "--.-",
  "R": ".-.",
  "S": "...",
  "T": "-",
  "U": "..-",
  "V": "...-",
  "W": ".--",
  "X": "-..-",
  "Y": "-.--",
  "Z": "--..",
  ".": ".-.-.-",
  ",": "--..--",
  "?": "..--..",
  "!": "-.-.--",
  "/": "-..-.",
  "&": ".-...",
  "@": ".--.-.",
  "'": ".----.",
  "(": "-.--.-",
  ")": "-.--.",
  ":": "---...",
  "=": "-...-",
  "+": ".-.-.",
  "-": "-....-",
  "\"": ".-..-.",
  ";": "-.-.-.",
  "_": "..--.-",
  "$": "...-..-"
}


def flash(char: str):
    if char == " ":
        board.digital[13].write(0)
        time.sleep(7)
    else:
        board.digital[13].write(0)
        code = morseCode[char]
        for part in code:
            board.digital[13].write(1)
            if part == ".":
                time.sleep(1)
            else:
                time.sleep(3)
            board.digital[13].write(0)
            time.sleep(3)


while True:
    for c in phrase:
        board.digital[13].write(0)
        if c in "abcdefghijklmnopqrstuvwxyz":
            flash(c.upper())
        else:
            flash(c)
    if not loop:
        break
