"""
    changes done:
        1. calculation of decryption key using modinverse(ek,phi)
        2. simplification of two_prime_no func (now it doesn't generate same numbers)
        3. checking correct output is simplified
    certain exception in RSA Algorithm itself:
        1. doesn't work for very small prime no.s like [2,7] [3,5] [2,11]
        2. doesn't work for same prime no.s
"""
import random
from fractions import gcd

def check_prime(no):
    for i in range(2,no):
        if(no%i == 0):
            return False
    return True;

def two_prime_no():
    p = []
    while(len(p) != 2):
        no = random.randint(2,50)
        while(check_prime(no) == False):
            no = random.randint(2,50)
        if no not in p:
            p.append(no)
    return(p[0],p[1])

class rsa_algo:

    def __init__(self,p,q):
        self.ek_set = []
        self.dk_set = []
        self.em_set = []
        self.dm_set = []
        self.p = p
        self.q = q
        self.phi = (p-1)*(q-1)
        self.n = p*q

    def modinv(self,a, m): # calculates modulo inverse of a for mod m
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        return None

    def find_ek(self):
        for i in range(2,self.phi):
            if(gcd(i,self.phi) == 1):
                self.ek_set.append(i)

    def find_dk(self):
        p = self.phi
        for val in self.ek_set:
            n = self.modinv(val,p)
            self.dk_set.append(n)

    def encrypt(self,m):
        for ek in self.ek_set:
            self.em_set.append((m**ek)%self.n)

    def decrypt(self):
        for dk,em in zip(self.dk_set,self.em_set):
            self.dm_set.append((em**dk)%self.n)
        print("if at the eol you see only the msg to be encrpted in bracs then sb changa hai {}\n".format(set(self.dm_set)))

    def printvalues(self):
        x = zip(self.ek_set,self.dk_set,self.em_set,self.dm_set)
        for ek,dk,em,dm in x:
            print(ek,dk,em,dm)

def main():
    n1,n2 = two_prime_no()
    print(n1,n2)
    user = rsa_algo(n1,n2)
    user.find_ek()
    user.find_dk()
    print('\n')
    print("msg to be encrpted: 25\n")
    user.encrypt(25)
    user.decrypt()
    print('printing various keys and their results......')
    print('\n')
    print('encryption key, decryption key, encrpted msg, decrypted msg')
    # uncomment below line to see all the keys and msgs
    #user.printvalues()

if __name__ == '__main__':
    main()
