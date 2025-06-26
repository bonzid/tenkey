tenkey_dict={
    "2": "a",
    "22": "b",
    "222": "c",
    "3": "d",
    "33": "e",
    "333": "f",
    "4": "g",
    "44": "h",
    "444": "i",
    "5": "j",
    "55": "k",
    "555": "l",
    "6": "m",
    "66": "n",
    "666": "o",
    "7": "p",
    "77": "q",
    "777": "r",
    "7777": "s",
    "8": "t",
    "88": "u",
    "888": "v",
    "9": "w",
    "99": "x",
    "999": "y",
    "9999": "z",
    "0": " "
}

reverse_tenkey_dict={v: k for k, v in tenkey_dict.items()}

#---------------------------------------------------------#

import unicodedata

def remove_accents(text):
    return ''.join(
        c for c in unicodedata.normalize('NFD',text)
        if unicodedata.category(c)!='Mn'
    )

def tenkey_to_text(s):
    #minuscule et sans accents
    s=s.lower()
    s=remove_accents(s)
    codes=s.split() #séparer par les espaces
    lettres=[tenkey_dict.get(code,code) for code in codes]
    return ''.join(lettres)


def txt_to_tenkey(s):
    s=s.lower()
    s=remove_accents(s)
    codes=[reverse_tenkey_dict.get(char,char) for char in s]
    return ' '.join(codes)


#---------------------------------------------------------#

#Round-trip test
txt="Qui me reflète sinon toi-même"
encoded=txt_to_tenkey(txt)
decoded=tenkey_to_text(encoded)
print(f"Original: {txt}")
print(f"Encoded : {encoded}")
print(f"Decoded : {decoded}")
