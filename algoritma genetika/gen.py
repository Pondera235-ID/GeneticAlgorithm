import random
import string

#https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits
def id_generator(size=1, chars=string.ascii_letters):
    return ''.join(random.choice(chars) for _ in range(size))