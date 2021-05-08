from string import ascii_uppercase
alphas = [x for x in ascii_uppercase]

def next_alpha(ap=''):
    if ap.isalpha():
        l = len(ap)
        for i in range(0,l):
            if ap[i] != 'Z':
                itx = alphas.index(ap[i])
                ap = ap[:i] + alphas[itx+1]
                return ap
        return ap + 'A'
    else:
        return alphas[0]

def generate_num(num):
    st = str(num)
    l1 = len(st)
    for i in range(len(st)):
        if st[i].isdigit():
            break
    alpha = st[:i]
    nummm = st[i:]
    l = len(nummm)
    nummm = str(int(nummm) + 1)
    if l < len(nummm):
        alp = next_alpha(alpha)
        return alp + nummm[-(l1-len(alp)):]
    else:
        return alpha + nummm

print(generate_num(99999))
print(generate_num('ZZ999'))
print(generate_num('Z9999'))
