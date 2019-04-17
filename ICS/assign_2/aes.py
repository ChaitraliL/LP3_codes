sbox = [[0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76],
        [0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0],
        [0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15],
        [0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75],
        [0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84],
        [0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF],
        [0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8],
        [0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2],
        [0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73],
        [0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB],
        [0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79],
        [0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08],
        [0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A],
        [0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E],
        [0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF],
        [0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16]]

rcon = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36]

fix_mat = [[2,3,1,1],[1,2,3,1],[1,1,2,3],[3,1,1,2]]

key = "Thats my Kung Fu"
plain_txt = "Two One Nine Two"

hex_key = [ hex(ord(char)) for char in key ]
txt = [ hex(ord(char)) for char in plain_txt ]

key = []
plain_txt = []
for i in range(4):
    word1 = []
    word2 = []
    for j in range(4):
        word1.append(hex_key.pop(0))
        word2.append(txt.pop(0))
    key.append(word1)
    plain_txt.append(word2)

def lcs(vec,offset):
    v = []
    for i in range(len(vec)):
        v.append(vec[(i+offset)%len(vec)])
    return v

def substitute(byte):
     if(len(byte) == 3):
         row = 0
         col = int(byte[2],16)
     else:
         row = int(byte[2],16)
         col = int(byte[3],16)
     return hex(sbox[row][col])

def xor_word(v1,v2):
    v3 = []
    for i in range(4):
        v3.append(hex(int(v1[i],16) ^ int(v2[i],16)))
    return v3

def sub_mat(mat):
    m = []
    for word in mat:
        w = [ substitute(byte) for byte in word ]
        m.append(w)
    return m

def lcs_mat(mat):
    r = [[mat[a][b] for a in range(4)] for b in range(4)]
    m = []
    for j in range(4):
        w = []
        for k in range(4):
            w.append(r[j][(k+j)%4])
        m.append(w)
    #r = [[m[a][b] for a in range(4)] for b in range(4)]
    return m

def mul_by_2(b):
    ls = (int(b,16) << 1) & 255
    if(len(b)==4):
        left_half = b[2]
        if(int(left_half,16) > 8):
            ls = ls ^ 0x1b
    return ls

def mul(b1,b2):
    if b1 == 1:
        return int(b2,16)
    elif b1 == 2:
        return mul_by_2(b2)
    elif b1 == 3:
        return (mul_by_2(b2) ^ int(b2,16))

def col_mat(mat):
    m = []
    for i in range(4):
        w = []
        for j in range(4):
            c = 0
            for k in range(4):
                    val = mul(fix_mat[j][k],mat[k][i])
                    c = c ^ val
            w.append(hex(c))
        m.append(w)
    return m

keys = []
keys.append(key)
for i in range(10):
    w = keys[i][3]
    w = lcs(w,1)
    w = [ substitute(byte) for byte in w ]
    const = rcon[i]
    w[0] = hex(int(w[0],16) ^ const)
    w1 = xor_word(w,keys[i][0])
    w2 = xor_word(w1,keys[i][1])
    w3 = xor_word(w2,keys[i][2])
    w4 = xor_word(w3,keys[i][3])
    keys.append([w1,w2,w3,w4])

state_mat_r0 = [ xor_word(w1,w2) for w1,w2 in zip(plain_txt,keys[0])  ]
matrices = []
matrices.append(state_mat_r0)

for i in range(1,10):
      mat = sub_mat(matrices[i-1])
      mat = lcs_mat(mat)
      mat = col_mat(mat)
      mat = [ xor_word(w1,w2) for w1,w2 in zip(mat,keys[i])  ]
      matrices.append(mat)

mat = sub_mat(matrices[9])
mat = lcs_mat(mat)
mat = [ xor_word(w1,w2) for w1,w2 in zip(mat,keys[10])  ]
print('Original msg:',plain_txt)
print('\n')
print('Encrpted msg:',mat)
