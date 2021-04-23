import random
import string
import numpy
import struct

target = 'a'
panjang_target = len(target);

#https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits
def id_generator(size=1, chars=string.ascii_letters):
    return ''.join(random.choice(chars) for _ in range(size))
an = [ord(c) for c in id_generator(panjang_target)]
tg = [ord(c) for c in target]
pr = numpy.equal(an,tg);

#print('Target :',tg)
#print('Gen    :',an)
#print('logical :', pr)

def fitness():
	fitnes = (sum(pr)/panjang_target)*100
	return fitnes


packed = struct.pack(tg,an,fitness())
print(packed)
'''
#Python string to ascii code https://stackoverflow.com/questions/8452961/convert-string-to-ascii-value-python
a = 'aaaa'
b = 'aaac'
an = [ord(c) for c in a] # atau begini >> list(bytes(b'aaaa'))
tg = [ord(c) for c in b] # atau begini >> list(bytes(b'aaac'))

pr = numpy.equal(an,tg);
print('Target :',tg)
print('Gen :',an)
print('logical :', pr)


Actual = [1, 1, 2, 3, 1]
Predicted = [1, 1, 1, 3, 3]
output = [a == p for a,p in zip(Actual,Predicted) if p==1]
print(output)

an = 'aaaa'
tg = 'aaab'

pr = numpy.array(an == tg , dtype=int);
print('Target :',tg)
print('Gen :',an)
print('logical :', pr)


def random_char(y):
       return ''.join(random.choice(string.ascii_letters) for x in range(y))

a = 'asu'
i=0
while True :
	rand = (random_char(len(a)))
	i= i+1
	print(rand)
	if a == rand :
		print(' Selesai iterasi ke ' ,i)
		break
	else:
		print('iterasi ke' ,i)

a = 'a'
i=0
while True :
	rand = random.choice(string.ascii_letters)
	print(rand)
	i = i+1
	if a == rand:
		print('Selesai' , i)
		break
	else :
		print('lanjooot' , i)

#https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits
def id_generator(size=1, chars=string.ascii_letters):
    return ''.join(random.choice(chars) for _ in range(size))

def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))

'''