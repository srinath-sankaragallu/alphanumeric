from string import ascii_uppercase
alphas = [x for x in ascii_uppercase]

def next_alpha(ap=''):
    if ap.isalpha():
        l = len(ap)
        for i in range(l - 1, -1, -1):
            if ap[i] != 'Z':
                itx = alphas.index(ap[i])
                if i == l:
                    ap = ap[:i] + alphas[itx+1]
                else:
                    ap = ap[:i] + alphas[itx+1] +ap[i+1:]
                return ap
            else:
                if i < l -1:
                    ap = ap[:i] + 'A' + ap[i+1:]
                else:
                    ap = ap[:i] + 'A'
        return ap
    else:
        return alphas[0]

def generate_num(num):
    st = str(num)
    for i in range(len(st)):
        if st[i].isdigit():
            break
    alpha = st[:i]
    nummm = st[i:]
    l = len(nummm)
    nummm = str(int(nummm) + 1)
    if l < len(nummm):
        return next_alpha(alpha) + nummm[-l:]
    else:
        return alpha + nummm

print(generate_num(99999))
print(generate_num('AB999'))
print(generate_num('A9999'))
