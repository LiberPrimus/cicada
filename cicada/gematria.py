import math

class Gematria:
    def __init__(self):
        self.gematriaprimus = (
            (" ", " ", 0),
            (u"ᚠ", "f", 2),
            (u"ᚢ", "v", 3),
            (u"ᚢ", "u", 3),
            (u"ᚦ", "T", 5),  # th
            (u"ᚩ", "o", 7),
            (u"ᚱ", "r", 11),
            (u"ᚳ", "k", 13),
            (u"ᚳ", "c", 13),
            (u"ᚷ", "g", 17),
            (u"ᚹ", "w", 19),
            (u"ᚻ", "h", 23),
            (u"ᚾ", "n", 29),
            (u"ᛁ", "i", 31),
            (u"ᛄ", "j", 37),
            (u"ᛇ", "E", 41),  # eo
            (u"ᛈ", "p", 43),
            (u"ᛉ", "x", 47),
            (u"ᛋ", "z", 53),
            (u"ᛋ", "s", 53),
            (u"ᛏ", "t", 59),
            (u"ᛒ", "b", 61),
            (u"ᛖ", "e", 67),
            (u"ᛗ", "m", 71),
            (u"ᛚ", "l", 73),
            (u"ᛝ", "G", 79),  # ing
            (u"ᛝ", "G", 79),  # ng
            (u"ᛟ", "O", 83),  # oe
            (u"ᛞ", "d", 89),
            (u"ᚪ", "a", 97),
            (u"ᚫ", "A", 101),  # ae
            (u"ᚣ", "y", 103),
            (u"ᛡ", "I", 107),  # ia
            (u"ᛡ", "I", 107),  # io
            (u"ᛠ", "X", 109),  # ea
        )
        self.latsimple = (
            ("T", "th"),
            ("E", "eo"),
            ("G", "ing"),
            ("G", "ng"),
            ("O", "oe"),
            ("A", "ae"),
            ("I", "io"),
            ("I", "ia"),
            ("X", "ea"),
        )

        self.emirps = [13, 17, 31, 37, 71, 73, 79, 97, 107, 113, 149, 157, 167, 179, 199, 311, 337, 347, 359, 389, 701,
                       709, 733, 739, 743, 751, 761, 769, 907, 937, 941, 953, 967, 971, 983, 991, 1009, 1021, 1031,
                       1033, 1061, 1069, 1091, 1097, 1103, 1109, 1151, 1153, 1181, 1193, 1201, 1213, 1217, 1223, 1229,
                       1231, 1237, 1249, 1259, 1279, 1283, 1301, 1321, 1381, 1399, 1409, 1429, 1439, 1453, 1471, 1487,
                       1499, 1511, 1523, 1559, 1583, 1597, 1601, 1619, 1657, 1669, 1723, 1733, 1741, 1753, 1789, 1811,
                       1831, 1847, 1867, 1879, 1901, 1913, 1933, 1949, 1979, 3011, 3019, 3023, 3049, 3067, 3083, 3089,
                       3109, 3121, 3163, 3169, 3191, 3203, 3221, 3251, 3257, 3271, 3299, 3301, 3319, 3343, 3347, 3359,
                       3371, 3373, 3389, 3391, 3407, 3433, 3463, 3467, 3469, 3511, 3527, 3541, 3571, 3583, 3613, 3643,
                       3697, 3719, 3733, 3767, 3803, 3821, 3851, 3853, 3889, 3911, 3917, 3929, 7027, 7043, 7057, 7121,
                       7177, 7187, 7193, 7207, 7219, 7229, 7253, 7297, 7321, 7349, 7433, 7457, 7459, 7481, 7507, 7523,
                       7529, 7547, 7561, 7577, 7589, 7603, 7643, 7649, 7673, 7681, 7687, 7699, 7717, 7757, 7817, 7841,
                       7867, 7879, 7901, 7927, 7949, 7951, 7963, 9001, 9011, 9013, 9029, 9041, 9103, 9127, 9133, 9161,
                       9173, 9209, 9221, 9227, 9241, 9257, 9293, 9341, 9349, 9403, 9421, 9437, 9439, 9467, 9479, 9491,
                       9497, 9521, 9533, 9547, 9551, 9601, 9613, 9643, 9661, 9679, 9721, 9749, 9769, 9781, 9787, 9791,
                       9803, 9833, 9857, 9871, 9883, 9923, 9931, 9941, 9967, 10007, 10009, 10039, 10061, 10067, 10069,
                       10079, 10091, 10151, 10159, 10177, 10247, 10253, 10273, 10321, 10333, 10343, 10391, 10429, 10453,
                       10457, 10459, 10487, 10499, 10613, 10639, 10651, 10711, 10739, 10781, 10853, 10859, 10867, 10889,
                       10891, 10909, 10939, 10987, 10993, 11003, 11057, 11071, 11083, 11149, 11159, 11161, 11197, 11243,
                       11257, 11329, 11353, 11423, 11447, 11489, 11497, 11551, 11579, 11587, 11593, 11621, 11657, 11677,
                       11699, 11701, 11717, 11719, 11731, 11777, 11779, 11783, 11789, 11833, 11839, 11897, 11903, 11909,
                       11923, 11927, 11933, 11939, 11953, 11959, 11969, 11971, 11981, 12071, 12073, 12107, 12109, 12113,
                       12119, 12149, 12227, 12241, 12253, 12269, 12289, 12301, 12323, 12373, 12437, 12491, 12547, 12553,
                       12577, 12611, 12619, 12641, 12659, 12689, 12697, 12713, 12743, 12757, 12763, 12799, 12809, 12829,
                       12841, 12893, 12907, 12919, 12983, 13009, 13043, 13147, 13151, 13159, 13163, 13259, 13267, 13291,
                       13297, 13337, 13441, 13457, 13469, 13477, 13499, 13513, 13523, 13553, 13591, 13597, 13619, 13693,
                       13697, 13709, 13711, 13751, 13757, 13759, 13781, 13789, 13829, 13841, 13873, 13903, 13933, 13963,
                       14029, 14057, 14071, 14081, 14087, 14107, 14143, 14153, 14177, 14207, 14221, 14251, 14293, 14303,
                       14323, 14327, 14387, 14423, 14431, 14447, 14449, 14479, 14519, 14549, 14551, 14557, 14563, 14591,
                       14593, 14621, 14629, 14633, 14657, 14713, 14717, 14821, 14831, 14843, 14879, 14891, 14897, 14923,
                       14929, 14939, 14947, 14957, 15013, 15053, 15091, 15101, 15131, 15139, 15149, 15227, 15241, 15263,
                       15289, 15299, 15307, 15349, 15377, 15383, 15461, 15493, 15497, 15511, 15527, 15541, 15601, 15643,
                       15649, 15661, 15667, 15679, 15683, 15731, 15733, 15737, 15791, 15803, 15907, 15919, 15937, 15973,
                       16001, 16007, 16063, 16073, 16103, 16111, 16127, 16193, 16217, 16223, 16249, 16267, 16427, 16433,
                       16451, 16453, 16481, 16493, 16547, 16567, 16573, 16603, 16651, 16691, 16699, 16729, 16747, 16763,
                       16829, 16879, 16883, 16937, 16943, 16979, 17011, 17021, 17033, 17041, 17047, 17117, 17203, 17207,
                       17209, 17383, 17393, 17417, 17443, 17467, 17477, 17491, 17519, 17573, 17579, 17599, 17627, 17669,
                       17681, 17683, 17713, 17737, 17747, 17749, 17827, 17839, 17863, 17903, 17909, 17911, 17923, 17939,
                       17959, 18013, 18041, 18077, 18089, 18133, 18169, 18191, 18199, 18253, 18269, 18307, 18329, 18353,
                       18379, 18413, 18427, 18439, 18461, 18539, 18593, 18637, 18671, 18691, 18701, 18719, 18731, 18743,
                       18749, 18757, 18773, 18787, 18803, 18859, 18899, 18911, 18913, 19001, 19013, 19037, 19051, 19163,
                       19181, 19219, 19231, 19237, 19249, 19301, 19333, 19403, 19421, 19423, 19471, 19477, 19489, 19531,
                       19541, 19543, 19553, 19577, 19661, 19681, 19687, 19697, 19751, 19759, 19763, 19793, 19801, 19813,
                       19841, 19913, 19973, 30011, 30029, 30059, 30139, 30161, 30197, 30223, 30259, 30271, 30319, 30323,
                       30341, 30367, 30467, 30491, 30517, 30529, 30539, 30557, 30593, 30643, 30649, 30661, 30757, 30809,
                       30851, 30853, 30859, 30881, 30911, 30931, 30949, 30971, 30983, 31033, 31051, 31063, 31069, 31081,
                       31091, 31121, 31139, 31183, 31193, 31223, 31259, 31267, 31277, 31307, 31327, 31393, 31481, 31531,
                       31543, 31601, 31627, 31643, 31649, 31721, 31723, 31741, 31771, 31799, 31859, 31873, 31891, 31907,
                       31957, 31963, 31981, 31991, 32009, 32077, 32099, 32143, 32173, 32189, 32203, 32213, 32233, 32257,
                       32261, 32299, 32303, 32321, 32341, 32353, 32369, 32377, 32411, 32441, 32467, 32479, 32491, 32497,
                       32531, 32537, 32563, 32579, 32633, 32647, 32687, 32693, 32713, 32749, 32783, 32869, 32887, 32911,
                       32933, 32939, 32941, 32971, 32983, 32999, 33013, 33029, 33049, 33071, 33181, 33199, 33223, 33287,
                       33301, 33317, 33329, 33391, 33461, 33589, 33617, 33623, 33641, 33751, 33767, 33809, 33811, 33857,
                       33863, 33911, 33923, 33931, 34031, 34123, 34129, 34141, 34147, 34159, 34211, 34267, 34273, 34301,
                       34367, 34469, 34471, 34513, 34549, 34583, 34589, 34591, 34603, 34613, 34651, 34673, 34687, 34721,
                       34757, 34781, 34807, 34841, 34847, 34897, 34919, 34961, 34963, 35027, 35051, 35069, 35083, 35099,
                       35117, 35129, 35141, 35149, 35159, 35201, 35221, 35227, 35257, 35267, 35281, 35311, 35317, 35323,
                       35327, 35363, 35381, 35401, 35419, 35437, 35447, 35461, 35521, 35531, 35537, 35569, 35591, 35729,
                       35801, 35803, 35911, 35969, 35983, 35993, 36013, 36037, 36061, 36097, 36107, 36109, 36131, 36187,
                       36191, 36209, 36217, 36251, 36269, 36277, 36353, 36373, 36467, 36473, 36479, 36523, 36541, 36599,
                       36607, 36721, 36739, 36761, 36791, 36809, 36833, 36871, 36877, 36913, 36931, 36943, 36973, 37021,
                       37061, 37123, 37199, 37201, 37243, 37307, 37309, 37321, 37363, 37379, 37409, 37463, 37489, 37507,
                       37547, 37549, 37561, 37571, 37589, 37619, 37643, 37781, 37813, 37831, 37847, 37889, 37897, 37951,
                       37963, 37991, 37997, 38011, 38039, 38053, 38113, 38119, 38219, 38239, 38287, 38327, 38329, 38351,
                       38371, 38377, 38393, 38449, 38459, 38543, 38557, 38629, 38639, 38651, 38671, 38707, 38711, 38723,
                       38737, 38861, 38867, 38903, 38917, 38921, 38923, 38953, 38977, 38993, 39047, 39113, 39119, 39157,
                       39161, 39217, 39241, 39313, 39359, 39371, 39383, 39397, 39419, 39439, 39451, 39461, 39503, 39511,
                       39541, 39581, 39623, 39631, 39709, 39749, 39791, 39799, 39821, 39827, 39829, 39839, 39869, 39877,
                       39887, 39901, 39929, 39953, 39983, 39989, 70001, 70009, 70061, 70079, 70121, 70141, 70163, 70241,
                       70249, 70271, 70289, 70313, 70327, 70351, 70373, 70381, 70439, 70457, 70489, 70529]


    # algorithm taken from here: https://pastebin.com/6v1XC1kV
    def gem_map(self, x, src, dest):
        m = {p[src]: p[dest] for p in self.gematriaprimus}
        return [m[c] if c in m else c for c in x]

    def lat_to_sim(self, x):
        x = x.replace("q", "cw")
        for sim in self.latsimple:
            x = x.replace(sim[1], sim[0])
        return x

    def sim_to_lat(self, x):
        for sim in self.latsimple:
            x = x.replace(sim[0], sim[1])
        return x

    def run_to_lat(self, x):
        return self.sim_to_lat("".join(self.gem_map(x, 0, 1)))

    def run_to_num(self, x):
        return self.gem_map(x, 0, 2)

    def lat_to_run(self, x):
        x = x.lower().replace("qu", "q")
        return "".join(self.gem_map(self.lat_to_sim(x), 1, 0))

    def lat_to_num(self, x):
        # strip non alpha chars when converting to num
        x = "".join([c for c in x if c.isalpha() or c == " "])
        return self.gem_map(self.lat_to_sim(x.lower()), 1, 2)

    def num_to_run(self, x):
        return self.gem_map(x, 2, 0)

    def num_to_lat(self, x):
        return self.sim_to_lat("".join(self.gem_map(x, 2, 1)))

    def get_primes(self):
        return self.primes

    def get_emirps(self):
        return self.emirps


class Cipher:

    def __repr__(self):
        return "<Cipher %s>" % (self.text)

    def __str__(self):
        return self.text

    def __init__(self, text, alpha):
        self.text = text
        self.alpha = alpha
        self.primes = lambda: (
            n
            for n, _ in enumerate(iter(int, 1))
            if all(n % p != 0 for p in range(2, int(math.sqrt(n)) + 1))
               and n not in [0, 1]
        )
        self.PI = "31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989380952572010654858632788659361533818279682303019520353018529689957736225994138912497217752834791315155748572424541506959508295"
        self.gm = Gematria()

    def to_runes(self):
        return Runes(self.gm.lat_to_run(self.text))

    def to_latin(self):
        return Latin(self.gm.run_to_lat(self.text))

    def to_numbers(self):
        return self.gm.run_to_num(self.gm.lat_to_run(self.text))

    def sub(self, plain, cipher):
        self.text = self.text.upper()
        return Cipher(self.text.translate(str.maketrans(plain, cipher)), self.alpha)

    def shift(self, n):
        return self.sub(self.alpha, self.alpha[n:] + self.alpha[:n])

    def atbash(self):
        return self.sub(self.alpha, self.alpha[::-1])

    def gematria_sum(self):
        return sum([n for n in self.to_numbers() if type(n) is int])

    def gematria_sum_words(self):
        return [Runes(w).gematria_sum() for w in self.text.split()]

    def gematria_sum_sentences(self):
        return [Runes(w).gematria_sum() for w in self.text.split('.')]

    def gematria_sum_lines(self):
        return [Runes(w).gematria_sum() for w in self.text.splitlines()]

    def to_index(self):
        return [self.alpha.index(i.upper()) for i in self.text.upper()]

    def AES(self, key):
        from Crypto.Cipher import AES

        cipher = AES.new(key, AES.MODE_EAX)
        plaintext = cipher.decrypt(str.encode(self.text))

        try:
            cipher.verify(str.encode(self.text))
            print("The message is authentic:", plaintext)
        except ValueError:
            print("Key incorrect or message corrupted")

    def running_shift(self, key, interrupts="", skip_indices=[], decrypt=False):
        if not key:
            return self.text

        # handles modulo
        def key_generator(key):
            while True:
                for k in key:
                    yield k

        key = key_generator(key)
        if type(interrupts) == list:
            interrupts = "".join(interrupts)
        o = ""
        i = 0

        for c in self.text:
            if c not in self.alpha or c in interrupts.upper():
                o += c
                i += 1
                continue
            if i in skip_indices:
                o += c
                i += 1
                continue
            c_index = self.alpha.index(c)
            # grab next key value
            shift = next(key)
            if decrypt:
                # invert the shift to decrypt
                shift = -shift
            # shift c by shift, wrap around if shift is longer than alpha
            o += self.alpha[(c_index + shift) % len(self.alpha)]
            i += 1

        return Cipher(o, self.alpha)

    def vigenere(self, key, interrupts=[], decrypt=False):
        key = [self.alpha.index(k) for k in key.upper() if k in self.alpha]
        return self.running_shift(key, interrupts="", skip_indices=[], decrypt=decrypt)

    def totient_stream(self, interrupts="", skip_indices=[]):
        return self.running_shift(
            (-p + 1 for p in self.primes()),
            interrupts=interrupts,
            skip_indices=skip_indices,
        )

    # new rune = sum of the two previous runes % 29
    def fib_stream(self, with_primes=False, gemsum=False, XOR=False):
        o = ''
        j = 0
        t = self.text
        primes = Gematria().get_primes()
        for c in t:
            if c not in self.alpha or j < 2:
                o += c
            else:
                try:
                    curr_index = self.alpha.index(c)
                    concat_cipher = t[0:j].replace('.', '').replace(' ', '').replace('\n', '')
                    prev_index = self.alpha.index(concat_cipher[-1:])
                    prev_index2 = self.alpha.index(concat_cipher[-2:][0])
                    if with_primes:
                        new_rune = self.alpha[(primes[prev_index] + primes[prev_index2]) % 29]
                    elif gemsum:
                        prevgem = Runes(f'{self.alpha[prev_index]}{self.alpha[prev_index2]}').gematria_sum()
                        new_rune = self.alpha[prevgem % 29]
                    elif XOR:
                        new_rune = "".join(
                            [chr(ord(a) ^ ord(b)) for a, b in zip(self.alpha[prev_index], self.alpha[prev_index2])])
                    else:
                        new_rune = self.alpha[(prev_index + prev_index2) % 29]
                    o += new_rune
                except:
                    o += c

            j += 1
        return Cipher(o, self.alpha)

    def fib_prime_stream(self):
        self.fib_stream(True)

    def fib_sum_stream(self):
        self.fib_stream(False, True)

    def xor_repeating_key(self, key):
        output = b''
        index = 0
        for byte in str.encode(self.text):
            output += bytes([byte ^ key[index]])
            if index + 1 == len(key):
                index = 0
            else:
                index += 1
        return Cipher(output.decode(), self.alpha)

    def mod60(self):
        o = ''
        j = 0
        t = self.text
        for c in t:
            if c not in self.alpha:
                o += c
            else:
                index = self.alpha.index(c)
                new_rune = self.alpha[((index + 3301) % 60) % 29]
                o += new_rune
            j += 1
        return Cipher(o, self.alpha)

    def arbitrary(self, func):
        o = ''
        j = 0
        for c in self.text:
            if c not in self.alpha:
                o += c
            else:
                index = self.alpha.index(c)
                o += self.alpha[func(index, Gematria().get_primes(), Gematria().get_emirps(), j)]
                j += 1
        return Cipher(o, self.alpha)


class Runes(Cipher):
    def __init__(self, text):
        super().__init__(text, "ᚠᚢᚦᚩᚱᚳᚷᚹᚻᚾᛁᛄᛇᛈᛉᛋᛏᛒᛖᛗᛚᛝᛟᛞᚪᚫᚣᛡᛠ")


class Latin(Cipher):
    def __init__(self, text):
        super().__init__(text.upper(), "ABCDEFGHIJKLMNOPQRSTUVWXYZ")


class Hex(Cipher):
    def __init__(self, text):
        super().__init__(text.upper(), "0123456789ABCDEF")


if __name__ == "__main__":
    r = Runes("ᚱ ᛝᚱᚪᛗᚹ ᛄᛁᚻᛖᛁᛡᛁ ᛗᚫᚣᚹ ᛠᚪᚫᚾ")
    print(r)
    print(r.to_latin())
    print(r.sub("ᚠᚢᚦᚩᚱᚳᚷᚹᚻᚾᛁᛄᛇᛈᛉᛋᛏᛒᛖᛗᛚᛝᛟᛞᚪᚫᚣᛡᛠ", "ABCDEFGHIJKLMNOPQRSTUVWXYZ123").text)
    print(r.atbash().text)
    print(r.to_numbers())
    print(r.gematria_sum())
    print(r.to_latin().gematria_sum())
    print(r.gematria_sum_words())
    print(r.gematria_sum_lines())
    # ᚻᛖᛚᛚᚩ
    h = Latin("Hello").to_runes()
    print(h.text)
    for i in range(4):
        print(h.shift(i).text)
        print(Hex("afe81723").shift(i))
