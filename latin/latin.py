#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import collections
import pprint
pprint = pprint.PrettyPrinter(indent=4).pprint
import grammar_table

class LatinError(Exception): pass
class InvalidFormError(LatinError): pass

translation_table = ("aeiouAEIOU", "āēīōūĀĒĪŌŪ")
translation_table = {i + ":": j for i, j in zip(*translation_table)}

class Word:
    def __init__(self, text):
        while "\b" in text:
            text1 = text[:text.find("\b")]

            if text1.endswith(":"): text1 = text1[:-2]
            else: text1 = text1[:-1]

            text2 = text[text.find("\b") + 1:]
            text = text1 + text2
        for i in translation_table:
            if i in text:
                text = text.replace(i, translation_table[i])

        self.text = text

    def __str__(self):
        return self.text

    def __repr__(self):
        return str(self)

class Verb(Word):
    stem_type = collections.namedtuple("Stem", ("present", "perfect", "supine", "subjunctive"))
    dictionary = {}
    grammar_table = grammar_table.grammar_table

    def __init__(self, conjugation, pres_stem, perf_stem, sup_stem, subj_stem):
        self.conjugation = conjugation
        self.stems = Verb.stem_type(pres_stem, perf_stem, sup_stem, subj_stem)

    def __str__(self):
        return str(self.form())

    def form(self, *args, **kwargs):
        return self._form_misc(table=Verb.grammar_table[self.conjugation - 1], *args, **kwargs)

    def _form_misc(self, *args, ending="", table=[], **kwargs):
        passive = False
        subjunctive = False
        perfect = False
        tense = 0
        plural = False
        person = 1

        if "perfect" in args:
            perfect = True
        if "pluperfect" in args:
            perfect = True
            tense = -1
        if "future" in args:
            tense = 1
        if "past" in args:
            tense = -1
        if "imperfect" in args:
            tense = -1
        if "conjunctive" in args or "subjunctive" in args:
            subjunctive = True
        if "passive" in args:
            passive = True

        if "2nd person" in args:
            person = 2
        elif "3rd person" in args:
            person = 3

        if "plural" in args:
            plural = True

        if "imperative" in args:
            if tense == 0:
                return [Word(self.stems[0] + table[2][6][int(plural)])]
            elif tense == 1:
                return [Word(self.stems[0] + table[2][7][int(plural)][max(0, person - 2)])]
        elif "participle" in args:
            if perfect:
                return [Word(self.stems[0] + table[2][3] + ending)]
            else:
                return [Word(self.stems[0] + table[2][2][int(plural)] + ending if plural else "")]
        elif "infinitive" in args:
            return [Word(self.stems[0] + table[2][int(passive)])]
        elif "gerund" in args:
            return [Word(self.stems[0] + table[2][4] + ending)]
        elif "gerundive" in args:
            return [Word(self.stems[0] + table[2][5] + ending)]

        return self._form_raw(passive, subjunctive, perfect, tense, plural, person, ending, table)

    def _form_raw(self, passive=False, subjunctive=False, perfect=False, tense=0, plural=False, person=1, ending="", table=[]):
        tense = int(tense/abs(tense)) if tense else 0

        if subjunctive and tense == 1:
            raise InvalidFormError("Subjunctives cannot be future tense")
        elif passive and perfect: # Supine

            flags = []
            if subjunctive: flags.append("subjunctive")
            if tense: flags.append(["past", "present", "future"][tense + 1])
            if plural: flags.append("plural")
            if person: flags.append(["1st", "2nd", "3rd"][person - 1] + " person")

            return [Word(self.stems[2] + ending), Verb.from_dict("esse").form(*flags)[0]]
        else:
            if perfect:
                stemp = 1
            elif subjunctive and tense == 0:
                stemp = 3
            else:
                stemp = 0

            ending = table
            ending = ending[int(passive)]
            ending = ending[int(subjunctive)]
            ending = ending[int(perfect)]
            ending = ending[tense + 1]
            ending = ending[int(plural)]
            ending = ending[person - 1]

            return [Word(self.stems[stemp] + ending)]

    @classmethod
    def from_dict(cls, infinitive):
        #translation_table = ("aeiouAEIOU", "āēīōūĀĒĪŌŪ")
        if infinitive in cls.dictionary:
            return cls.dictionary[infinitive]
        else:
            raise KeyError("%s not in dictionary" % infinitive)

    @classmethod
    def remember(cls, verb):
        cls.dictionary[str(verb.form("infinitive")[0])] = verb

class IrregularVerb(Verb):
    def __init__(self, *args, **kwargs):
        if "table" in kwargs:
            self.table = kwargs["table"]
            del kwargs["table"]
        else:
            self.table = []

        Verb.__init__(self, *args, **kwargs)

    def form(self, *args, **kwargs):
        try:
            return self._form_misc(table=self.table, *args, **kwargs)
        except IndexError:
            return self._form_misc(table=Verb.grammar_table[self.conjugation - 1], *args, **kwargs)

# Summary of table format:
# + Active
#   + Indicative
#     + Imperfect
#       + Past (single, multiple)
#       + Present (single, multiple)
#       + Future (single, multiple)
#     + Perfect (same structure)
#   + Subjunctive (same structure)
# + Passive (same structure)
# + Miscellaneous
#   + Infinitive
#   + Passive Infinitive
#   + Participle (single, multiple)
#   + Perfect Participle
#   + Gerund
#   + Gerundive
#   + Imperative (single, multiple)
#   + Future Imperative (2nd person, 3rd person)

est_table = [
    [ # Active
        [ # Indicative
            [ # Non-perfect
                [["ram", "ra:s", "rat"], ["ra:mus", "ra:tis", "rant"]],
                [["\bsum", "s", "st"], ["\bsumus", "stis", "\bsunt"]],
                [["ro:", "ris", "rit"], ["rimus", "ritis", "runt"]]
            ], [ # Perfect
                [["eram", "era:s", "erat"], ["era:mus", "era:tis", "erant"]],
                [["i:", "isti:", "it"], ["imus", "istis", "e:runt"]],
                [["ero:", "eris", "erit"], ["erimus", "eritis", "erint"]]
            ]
        ], [ # Subjunctive
            [ # Non-perfect
                [["ssem", "sse:s", "sset"], ["sse:mus", "sse:tis", "ssent"]],
                [["\bim", "s", "\bit"], ["mus", "tis", "\bint"]],
                # None
            ], [ # Perfect
                [["issem", "isse:s", "isset"], ["isse:mus", "isse:tis", "issent"]],
                [["erim", "eris", "erit"], ["erimus", "eritis", "erint"]]
            ]
        ]
    ], [ # Passive
        [ # Indicative
            [ # Non-perfect
                [["rar", "ra:ris", "ra:tur"], ["ra:mur", "ra:mini", "rantur"]],
                [["sor", "ser", "estur", "sumur", "simini:", "suntur"]],
                [["ror", "reris", "ritur"], ["rimur", "ritis", "runt"]]
            ], [] # Perfect omitted; same as in Verb.grammar_table
        ], [ # Subjunctive
            [ # Non-perfect
                [["sser", "sse:ris", "sse:tur"], ["sse:mur", "sse:mini", "sse:ntur"]],
                [["\bir", "s", "\bit"], ["mur", "mini:", "\bint"]],
                # No future
            ], [] # Perfect same as grammar table
        ]
    ], [ # Miscellaneous
        "sse", # Infinitive
        "ri", # Passive Infinitive
        ["\bse:ns", "\bsent"], # Present Participle
        "s", # Perfect Participle
        "\bend", # Gerund
        "\bend", # Gerundive
        ["s", "ste"], # Present imperative
        [["sto:", "sto:"], ["sto:te", "\bunto:"]] # Future Imperative
    ]
]

est = IrregularVerb(1, "e", "fu", "es", "si:", table=est_table)
Verb.remember(est)

if __name__ == "__main__":
    vocare = Verb(1, "voca:", "voca:v", "voca:t", "voce:")
    print("Pluperfect third person singular of habere: ", habere.form("pluperfect", "3rd person", "singular"))

    habere = Verb(2, "habe:", "habu", "habit", "habea:")
    print("Pluperfect third person singular of habere: ", habere.form("pluperfect", "3rd person", "singular"))

    ducere = Verb(3, "duce:", "dux", "duct", "duca:")
    print("Pluperfect third person singular of habere: ", habere.form("pluperfect", "3rd person", "singular"))

    audire = Verb(4, "audi", "audi:v", "audi:t", "audia:")
    print("Pluperfect third person singular of audire: ", audire.form("pluperfect", "3rd person", "singular"))
