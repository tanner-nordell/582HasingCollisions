import hashlib
import os

def hash_collision(k):
    if not isinstance(k, int):
        print( "hash_collision expects an integer" )
        return( b'\x00',b'\x00' )
    if k < 0:
        print( "Specify a positive number of bits" )
        return( b'\x00',b'\x00' )

    mask = (1<<k)-1

    size = 16
    x = os.urandom(size)
    print("x in binary: ", x)
    print("x in hex: " + x.hex())
    x_hashed = hashlib.sha256(x)
    x_last_k_bits = int(x_hashed.hexdigest(), 16) & mask
    print("h(x) = ", x_hashed.hexdigest(), "  h(x) last", k ,"bits in hex:", hex(x_last_k_bits))
    #print("h(x) last", k ,"bits in hex:", hex(x_last_k_bits))

    while(1):
        y = os.urandom(size) #create a string of random bytes
        y_hashed = hashlib.sha256(y)
        y_last_k_bits = int(y_hashed.hexdigest(), 16) & mask

        #check to see if last k bits match
        if(x_last_k_bits == y_last_k_bits):
            break
    print("y in binary: ", y)
    print("y in hex: " + y.hex())
    print("h(y) = ", y_hashed.hexdigest(), "  h(y) last", k ,"bits in hex: ", hex(y_last_k_bits))
    #print("h(y) last bits in hex: ", hex(y_last_k_bits))
    return( x, y )

