#!/usr/bin/ipython
# very sleepy

eo_to_en = dict()
for line in open('EO_full.txt', 'rU'):
    if '#' in line:
        continue
    eo = ''
    en = ''
    line = bytes(line, 'utf-8') #Python 3 compat
    words = line.decode('utf-8').strip('\n').split(' ')
    pre_eo = True
    in_eo = False
    space = False
    for ww in words:
        if pre_eo:
            if not ww == '':
                pre_eo = False
                in_eo = True
                eo += ww
            continue
        if in_eo:
            if ww == '':
                if space:
                    in_eo = False
                else:
                    space = True
                    eo += ' '
            else:
                eo += ' ' + ww
                space = False
            continue
        else:
            en += ' ' + ww
    eo = eo.rstrip(' ')
    en = en.lstrip(' ')
    eo_to_en[eo] = en
