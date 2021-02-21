import string
from random import *
characters = string.ascii_letters + string.punctuation  + string.digits
password =  "".join(choice(characters) for x in range(randint(7, 14)))
print("Şifreniz Bu;")
print("Your password is here;")
print(password)