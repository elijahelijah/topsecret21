
def scramble(text):
     result = ''
     for letter in text:
         if ord(letter) > 32 and ord(letter) < 80:
             letter = chr(ord(letter) + 47)
         elif ord(letter) >= 80 and ord(letter) < 127:
             letter = chr(ord(letter)- 47)
         result += letter
     return result
