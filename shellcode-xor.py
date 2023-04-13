import sys
        
data = open(sys.argv[1], 'rb').read()

key  = b"\x48\x6f\x37\x73\x41\x4d\x33\x45\x68\x30\x42\x41\x35\x6c\x50\x51\x77\x32\x7a\x58\x77\x33\x4e" # Put here your key as byte like for example (0x90 or 0x40 or 0x30) and more...

data = bytearray(data)
ctr = 0 
for i in range(0, len(data)):
 ctr = 0 if ctr == len(key) else ctr
 data[i] = data[i] ^ key[ctr]
 ctr+=1

data.reverse()
data = bytes(data)
 
print("{ " + ", ".join([hex(i) for i in data]) + " };")
