import time

def VerificationToken():
        epoch = int(str(time.time()).replace(".", "")[:13])
        context = {"a":epoch,"b":0,"c":1,"d":2,"e":0}
        epoch_b16 = f"0{hex(epoch)[2:]}"
        o, u = '', 0
        for f in range(len(str(context).replace(" ", ""))):
            s = int(f"0x{epoch_b16[u:u+2]}", 16)
            u += 2
            if u >= len(epoch_b16): u=0
            i = str(hex(ord(str(context)[f]) ^ s)).replace("0x", "")
            if len(i) != 2: i = f"0{i}"
            o+=i
        return f"{epoch_b16}-{o}"