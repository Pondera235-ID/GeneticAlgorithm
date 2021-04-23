import numpy
from fitness import fitness
from gen import id_generator

def main():
    target = 'ab'
    panjang_target = len(target);

    an = [ord(c) for c in id_generator(panjang_target)]
    tg = [ord(c) for c in target]
    pr = numpy.equal(an,tg);


    print('Target :',tg)
    print('Gen    :',an)
    print('logical :', pr)
    print(fitness(panjang_target, pr))

main()