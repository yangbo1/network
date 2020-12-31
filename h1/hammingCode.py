# 原码上添加码
def hamming(code, addCode):
    print(code, addCode)
    codelist = list(code)
    for i in range(len(addCode)):
        codelist.insert(2**i-1, addCode[i])
    return ''.join(codelist)

# 奇偶校验覆盖率
def parityCheck(code, i):
    pi = None
    for j in range(2 ** i - 1, len(code), 2 ** (i + 1)):
        for k in code[j:j + 2 ** i]:
            if k == '.':
                continue
            if pi is None:
                pi = k
            else:
                pi = bin(int(pi, 2) ^ int(k, 2))[2:]
    return pi
def check(hammingCode):
    i = 0
    p = ''
    while 2 ** i - 1 < len(hammingCode):
        p += parityCheck(hammingCode, i)
        i += 1
    print('检错位=', p[::-1])
    return p[::-1]
# 解码
def decode(hammingCode):
    c1 = check(hammingCode)
    eindex = int(c1, 2) - 1
    hammingCodeList = list(hammingCode)
    if eindex >= 0:
        hammingCodeList[eindex] = str(int(hammingCodeList[eindex]) ^ 1)
    r = 0
    while 2**r-1 < len(hammingCodeList):
        hammingCodeList[2**r-1] = '.'
        r += 1
    print(''.join(hammingCodeList).replace('.', ''))
    return ''.join(hammingCodeList).replace('.', '')
# 计算要添加的码
def P(code):
    r = cr(len(code))
    tmpcode = hamming(code, ''.join(['.' for i in range(r)]))
    print(tmpcode)
    p = ''
    for i in range(r):
        p += parityCheck(tmpcode, i)
    print('要添加的码=', p)
    return p

# 计算校验码位数zL
def cr(n):
    # 2**r - 2r >= 5
    r = 0
    while 2**r - r < n+1:
        r += 1
    print('添加的码位数=', r)
    return r
if __name__ == '__main__':
    code = '10010001010100010010001000101001010000101101110100101010010100100100100101001010101001001010101010'
    addcode= P(code)
    hammingCode = hamming(code, addcode)
    print('hammingCode=', hammingCode)
    # decode('01110010000')
    decode('011100110001010010001001000100011010010100001011011101001010100110100100100100101001010101001001010101010')