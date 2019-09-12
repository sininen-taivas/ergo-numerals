import sys



def zigzag(i):
    return (i >> 31) ^ (i << 1)


def zigzag64(n):
    # a = n << 1
    a = n[1:64] + '0'
    # b = n >> 63
    b = n[0]*64
    return ''.join([{'0': ai, '1': {'0':'1','1':'0'}[ai]}[bi] for ai, bi in zip(a, b)])


def tobits(n, _group=8, _sep='_', _pad=False):
    'Express n as binary bits with separator'
    bits = '{0:b}'.format(n)[::-1]
    if _pad:
        bits = '{0:0{1}b}'.format(n,
                                  ((_group+len(bits)-1)//_group)*_group)[::-1]
        answer = _sep.join(bits[i:i+_group]
                                 for i in range(0, len(bits), _group))[::-1]
        answer = '0'*(len(_sep)-1) + answer
    else:
        answer = _sep.join(bits[i:i+_group]
                           for i in range(0, len(bits), _group))[::-1]
    return answer

def tovlq(n):
    return tobits(n, _group=7, _sep='1_', _pad=True)

def toint(vlq):
    return int(''.join(vlq.split('_1')), 2)

def vlqsend(vlq):
    for i, byte in enumerate(vlq.split('_')[::-1]):
        print('Sent byte {0:3}: {1:#04x}'.format(i, int(byte,2)))


def tobase16(vlq):
    r = ''
    for i, byte in enumerate(vlq.split('_')[::-1]):
        r += '{:02x}'.format(int(byte,2))
    return r



# потом массив байт преобразуется в Base16


# 100000 => 05c09a0c
# 500 => 05e807
# -666 => 05



def int64tobits(n):
    if n < 0:
        n += 2**64
    return '{0:064b}'.format(n)


def coder(n):
    z = zigzag(n)
    v = tovlq(z)
    r = '05' + tobase16(v)
    return r


def coder64(n):
    bits = int64tobits(n)
    print(bits)
    z = zigzag64(bits)
    print(z, int(z,2))
    v = tovlq(int(z,2))
    print(v)
    r = '05' + tobase16(v)
    return r



