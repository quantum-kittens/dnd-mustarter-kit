from .qrandom import QuantumRandomInt

# Name generation

CONSONANTS = "bcdfghjklmnpqrstvwxyz"
VOWELS = "aeiou"

## Letter synergy dict
LETTER_SYNERGY_DICT = {
    "b": "lrwy",
    "c": "hklrwy",
    "d": "hrwy",
    "f": "fhlry",
    "g": "hy",
    "h": "my",
    "j": "hjrwy",
    "k": "hy",
    "l": "ly",
    "m": "hy",
    "n": "nwy",
    "p": "phlrwy",
    "q": "kwy",
    "r": "hry",
    "s": "hlprstvwy",
    "t": "hrtvwyz",
    "v": "hlvy",
    "w": "hw",
    "x": "lrwxy",
    "y": "bcdfghjklmnpqrstvwxz",
    "z": "hlryz",
}

CONS_OR_VOW = "cv"

# dwarf clan names (clan name = first part + second part)
CLAN_FIRST = ["iron", 
              "steel",
              "fist", 
              "willow",
              "stone", 
              "giants",
              "amber", 
              "thorn",
              "birch", 
              "ashen", 
              "frost", 
              "battle", 
              "crag", 
              "elder",
              "oaken",
              "axe",
              "sky",
              "gold"]

CLAN_SECOND = ["beard", 
               "fist", 
               "thorn", 
               "forge", 
               "hammer", 
               "helm",
               "shield",
               "stone",
               "peak",
               "born",
               "bane"]


class NameGenerator:
    def __init__(self, nametype): #nametype can be 'name' or 'clan'
        self.coin = QuantumRandomInt(0, 1)
        self.nametype = nametype
        if self.nametype == "name":
            self.vowel_chooser = QuantumRandomInt(0, len(VOWELS) - 1)
            self.consonant_chooser = QuantumRandomInt(0, len(CONSONANTS) - 1)
        else:
            self.first_chooser = QuantumRandomInt(0, len(CLAN_FIRST) - 1)
            self.second_chooser = QuantumRandomInt(0, len(CLAN_SECOND) - 1)

    def generate(self, syllables, **kwargs):
        name = ""
        # Generate the first part of the name
        letter_type = CONS_OR_VOW[self.coin.generate(**kwargs)[0]]
        name = name + self._get_letters(
            letter_type, self.coin.generate(**kwargs)[0] + 1, **kwargs
        )
        # Generate the remaining name
        while syllables > 0:
            # Toggle consonants and vowels: c -> v and v -> c
            letter_type = CONS_OR_VOW[CONS_OR_VOW.index(letter_type) ^ 1]
            name = name + self._get_letters(
                letter_type, self.coin.generate(**kwargs)[0] + 1, **kwargs
            )
            syllables -= 1

        return name.capitalize()

    def _get_letters(self, letter_type, num_letters, **kwargs):
        if not 1 <= num_letters <= 2:
            raise ValueError("num_letters must be 1 or 2")

        if num_letters == 1:
            if letter_type == "c":
                return self._get_consonant(**kwargs)
            else:
                return self._get_vowel(**kwargs)
        else:
            if letter_type == "c":
                letter1 = self._get_consonant(**kwargs)
                letter2 = self._get_consonant(**kwargs)
                synergy_list = max(
                    LETTER_SYNERGY_DICT[letter1], LETTER_SYNERGY_DICT[letter2], key=len
                )
                if synergy_list is LETTER_SYNERGY_DICT[letter1]:
                    while letter2 not in synergy_list:
                        letter2 = self._get_consonant(**kwargs)
                else:
                    letter1, letter2 = letter2, letter1
                    while letter2 not in synergy_list:
                        letter2 = self._get_consonant(**kwargs)
                return letter1 + letter2
            else:
                letter1 = self._get_vowel(**kwargs)
                letter2 = self._get_vowel(**kwargs)
                return letter1 + letter2

    def _get_consonant(self, **kwargs):
        idx = self.consonant_chooser.generate(1, **kwargs)[0]
        return CONSONANTS[idx]

    def _get_vowel(self, **kwargs):
        idx = self.vowel_chooser.generate(1, **kwargs)[0]
        return VOWELS[idx]
    
    def generate_clan(self,**kwargs):
            idxf = self.first_chooser.generate(1, **kwargs)[0]
            idxs = self.second_chooser.generate(1, **kwargs)[0]
            first = CLAN_FIRST[idxf]
            second = CLAN_SECOND[idxs]

            while second == first:
                idxs = self.second_chooser.generate(1, **kwargs)[0]
                second = CLAN_SECOND[idxs]
    
            clan = first + second
            return clan.capitalize()

