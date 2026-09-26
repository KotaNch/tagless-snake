def _imul(a,b):
    return ((a & 0xFFFFFFFF) * (b & 0xFFFFFFFF)) & 0xFFFFFFFF

def make_rng(seed):
    a = seed & 0xFFFFFFFF
    
    def rng():
        nonlocal a
        a = (a + 0x6D2B79F5) & 0xFFFFFFFF
        t = _imul(a ^ (a >> 15), 1 | a)
        inner = _imul(t ^ (t >> 7), 61 | t)
        t = ((t + inner) & 0xFFFFFFFF) ^ t
        t = (t ^ (t>>14 ) ) & 0xFFFFFFFF
        return t/4294967296
    
    return rng

def rand_int(rng, lo, hi):
    return lo + int(rng() * (hi - lo +1))



def rand_choice(rng, seq):
    return seq [int(rng() * len(seq))]

def hash_seed(s):
    h = 2166136261
    for c in s:
        h^= ord(c)
        h = _imul(h, 16777619)
    return h & 0xFFFFFFFF