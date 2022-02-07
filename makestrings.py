#! /usr/bin/python

# make a string of n length with n characters
# to simulate a unix directory
# https://unix.stackexchange.com/questions/367008/why-is-socket-path-length-limited-to-a-hundred-chars
# bash:
#    tr -dc 'A-Za-z0-9/' </dev/urandom | head -c 104  ; echo
#   LHbKeOXWwaUht5r3z55MMdSBAVf63/c8p7DgnElU1DkrAa7JD4k7oiukzIgU1827UG0UVMEPopj2NFOXsJk0hHgA8ece6NwEK3VB8KKC
# macOS:
#   cat /dev/urandom | env LC_ALL=C tr -dc 'a-zA-Z0-9/' | fold -w 104 | head -n 1
#   TfM4sYpINNP9Nt8aYyDIGZTUl772rpakCsBPj6WjUtuakBYJfU3UoL7WM/1BvMBSrzaaV/rQBqck6VBtzwS97rK8Wj/2Drh4dg3BuwqF

from random import choice
from string import ascii_lowercase

def makestring(n):
    string_val = "".join(choice(ascii_lowercase) for i in range(n))
    dir_val = "/".join(string_val[i:i+5] for i in range(0, len(string_val),5))
    return dir_val

print(makestring(104))
print(makestring(105))

# python makestrings.py
# otazu/xrvhg/usrnc/yaibc/nxota/cglxb/wmnyn/zpvqj/bvnkq/oneqb/fgtuu/xkrja/gedbo/uzzwn/izhia/qjfti/fgdqx/zonmw/vyevn/qcpay/mvje
# rjals/hiuvi/arskj/winym/vxado/nfbwr/ohpsj/wfxkb/iyryk/elhca/spvxi/yyxqf/jygix/jyqen/bqyan/umtae/kdipj/twaaj/xddat/oqbbv/vdbzf