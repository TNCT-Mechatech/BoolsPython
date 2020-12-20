import os
import Bools
if __name__ == "__main__":
    print("start program...")
    bits = [True,True,False,True,False,True,False,False,True]
    b = Bools.Bools(len(bits),bits)
    byte = b._get_bytes()
    print(bin(byte))
    b._set_bytes(byte)
    byte = b._get_bytes()
    print(bin(byte))
