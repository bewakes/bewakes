def xor_encrypt(string, password):
    """
    Encrypt the string with password
    """
    passlen = len(password)
    chunks = [string[x:x+passlen] for x in range(0,len(string), passlen)]
    xored = [xor_strings(password, x) for x in chunks]
    return "".join(xored)

def xor_strings(s1, s2):
    """
    xor two strings
    """
    zipped = zip(s1, s2)
    xored = [chr(ord(x)^ord(y)) for (x, y) in zipped]
    return "".join(xored)
