
def scramble(text):
     result = ''
     for letter in text:
         if ord(letter) > 32 and ord(letter) < 80:
             letter = chr(ord(letter) + 46)
         elif ord(letter) >= 80 and ord(letter) < 127:
             letter = chr(ord(letter)- 46)
         result += letter
     return result
