import hashlib
import os

def hash_collision(k):
    if not isinstance(k, int):
        print( "hash_collision expects an integer" )
        return( b'\x00',b'\x00' )
    if k < 0:
        print( "Specify a positive number of bits" )
        return( b'\x00',b'\x00' )

    mask = 2**k - 1


    size = 16
    x = os.urandom(size)
    print("str(x)" + str(x))
    print("str(x) in hex "+ str(x.hex()))
    x_hashed = hashlib.sha256(x)
    #print("x_hashed:  " + x_hashed)
    x_last_k_bits = int(x_hashed.hexdigest(),16) & mask
    while(1): #fix this
        y = os.urandom(size) #create a string of random bytes
        y_hashed = hashlib.sha256(y)
        y_last_k_bits = int(y_hashed.hexdigest(),16) & mask


        #check to see if last k bits match
        if(x_last_k_bits == y_last_k_bits):
            break

    #Collision finding code goes here



    x = b'\x00'
    y = b'\x00'
    
    return( x, y )

