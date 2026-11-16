import random as rand

#caesar

class caesar:
	def __init__(self, text, shift):
		self.text = text
		self.shift = shift % 26
	def cipher(self):
		alp = "abcdefghijklmnopqrstuvwxyz"
		s_alp = alp[self.shift:] + alp[:self.shift]
		u_alp = alp.upper()
		su_alp = s_alp.upper()
		trans = str.maketrans(alp + u_alp, s_alp + su_alp)
		ciphered = self.text.translate(trans)
		return ciphered

# morse

class morse:
#     dict
    morse = {
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", 
    "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", 
    "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", 
    "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", 
    "y": "-.--", "z": "--..", " ": "/",
    "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
    "6": "-....", "7": "--...", "8": "---..", "9": "----.", "0": "-----",
    ".": ".-.-.-", ",": "--..--", "?": "..--..", "'": ".----.", "!": "-.-.--", 
    "/": "-..-.", "(": "-.--.", ")": "-.--.-", "&": ".-...", ":": "---...", 
    ";": "-.-.-.", "=": "-...-", "+": ".-.-.", "-": "-....-", "_": "..--.-", 
    '"': ".-..-.", "$": "...-..-", "@": ".--.-."}
    invertedmorse = {key: value for value, key in morse.items()}
    
    def __init__(self, text):
        self.text = text.lower()
#     cipher
    def cipher(self):
        splitted_morse = []
        for byte in self.text:
            if byte == " ":
                splitted_morse.append("/")
            elif byte in self.morse:
                splitted_morse.append(self.morse[byte])
        return " ".join(splitted_morse)
#     decipher
    def decipher(self):
        splitted_beeps = self.text.strip().split(' ')
        beeps_meaning = []
        for beeps in splitted_beeps:
            if beeps == "/":
                beeps_meaning.append(" ")
            elif beeps in self.invertedmorse:
                beeps_meaning.append(self.invertedmorse[beeps])
        return "".join(beeps_meaning)
    
        
        
#baconian
class bacon:
    bacont = {
    'A': 'aaaaa', 'B': 'aaaab', 'C': 'aaaba', 'D': 'aaabb', 'E': 'aabaa',
    'F': 'aabab', 'G': 'aabba', 'H': 'aabbb', 'I': 'abaaa', 'J': 'abaab',
    'K': 'ababa', 'L': 'ababb', 'M': 'abbaa', 'N': 'abbab', 'O': 'abbba',
    'P': 'abbbb', 'Q': 'baaaa', 'R': 'baaab', 'S': 'baaba', 'T': 'baabb',
    'U': 'babaa', 'V': 'babab', 'W': 'babba', 'X': 'babbb', 'Y': 'bbaaa',
    'Z': 'bbaab'}
    tnocab = {value: key for key, value in bacont.items()}
    abjad = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    def __init__(self, text):
        self.text = text.replace(" ", "")
        self.fordeci = [self.text[i:i+5] for i in range(0, len(self.text), 5)]
    def cipher(self):
        ranstring = []
        a7b = []
        for hurf in self.text.upper():
            if hurf in bacon.bacont:
                a7b.append(bacon.bacont[hurf])
        fuseda7b = "".join(a7b)
        for i in range(len(fuseda7b)):
            ranstring.append(rand.choice(bacon.abjad))
        fusedranstring = "".join(ranstring)
        final = []
        for i in range(len(fuseda7b)):
            ab = fuseda7b[i]
            yz = fusedranstring[i]
            if ab == 'a':
                final.append(yz.lower())
            elif ab == 'b':
                final.append(yz.upper())
        return "".join(final)
    def cipherraw(self):
        a7b = []
        for hurf in self.text.upper():
            if hurf in bacon.bacont:
                a7b.append(bacon.bacont[hurf])
        return "".join(a7b)
    def decipher(self):
        decoded = []
        for g in self.fordeci:
            mg = ""
            for r in g:
                if r.isupper():
                    mg += "b"
                elif r.islower():
                    mg += "a"
            if mg in bacon.tnocab:
                decoded.append(bacon.tnocab[mg])
        return ''.join(decoded)
#ROT
class rot:
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    def __init__(self, text, num):
        self.text = text
        self.num = num
    def cipher(self):
        tali = ""
        for karakter in self.text:
            if karakter in rot.alpha:
                ind = rot.alpha.index(karakter)
                indeks = (ind + self.num) % len(rot.alpha)
                tali += rot.alpha[indeks]
            elif karakter == " ":
                tali += " "
        return tali
    def decipher(self):
        tali = ""
        for karakter in self.text:
            if karakter in rot.alpha:
                ind = rot.alpha.index(karakter)
                indeks = (ind - self.num) % len(rot.alpha)
                tali += rot.alpha[indeks]
            elif karakter == " ":
                tali += " "
        return tali
#Vignere
class vigenere:
    alp = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    def __init__(self, text, key):
        self.text = text.upper()
        self.key = key.upper()
    def cipher(self):
        res = []
        ki = 0
        for i in range(0, len(self.text)):
            if self.text[i] in vigenere.alp:
                it = vigenere.alp.index(self.text[i])
                ik = vigenere.alp.index(self.key[ki % len(self.key)])
                res.append(vigenere.alp[(it + ik) % 26])
                ki += 1
            else:
                res.append(self.text[i])
        return "".join(res)
    def decipher(self):
        res = []
        ki = 0
        for i in range(0, len(self.text)):
            if self.text[i] in vigenere.alp:
                it = vigenere.alp.index(self.text[i])
                ik = vigenere.alp.index(self.key[ki % len(self.key)])
                res.append(vigenere.alp[(it - ik + 26) % 26])
                ki += 1
            else:
                res.append(self.text[i])
        return "".join(res)
        
