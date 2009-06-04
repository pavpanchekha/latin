# -*- coding: utf-8 -*-
grammar_table = [
    [ # Conjugation 1
        [ # Active
            [ # Indicative
                [ # Non-perfect
                    [["bam", "ba:s", "bat"], ["ba:mus", "ba:tis", "bant"]],
                    [["\bo:", "s", "\bat"], ["mus", "tis", "\bant"]],
                    [["bo:", "bis", "bit"], ["bimus", "bitis", "bunt"]],
                ], [ # Perfect
                    [["eram", "era:s", "erat"], ["era:mus", "era:tis", "erant"]],
                    [["i:", "isti:", "it"], ["imus", "istis", "e:runt"]],
                    [["ero:", "eris", "erit"], ["erimus", "eritis", "erint"]],
                ]
            ], [ # Subjunctive
                [ # Non-perfect
                    [["rem", "re:s", "ret"], ["re:mus", "re:tis", "rent"]],
                    [["\bem", "\be:s", "\bet"], ["\be:mus", "\be:tis", "\bent"]]
                ], [ # Perfect
                    [["issem", "isse:s", "isset"], ["isse:mus", "isse:tis", "issent"]],
                    [["erim", "eris", "erit"], ["erimus", "eritis", "erint"]]
                ]
            ]
        ], [ # Passive
            [ # Indicative
                [ # Non-perfect
                    [["bar", "ba:ris", "ba:tur"], ["ba:mur", "ba:mini:", "bantur"]],
                    [["\bor", "ris", "tur"], ["mur", "mini:", "ntur"]],
                    [["bor", "beris", "bitur"], ["bimur", "bimini:", "bunture"]]
                ], [ # Perfect
                    # Nothing here, supine case handled separately
                ]
            ], [ # Subjunctive
                [ # Non-perfect
                    [["rer", "re:ris", "re:tur"], ["re:mur", "re:mini:", "re:ntur"]],
                    [["\ber", "ris", "tur"], ["mur", "mini:", "ntur"]],
                    # Nothing here, supine case handled separately
                ], []
            ]
        ], [ # Miscellaneous
            "re", # Infinitive
            "ri", # Passive Infinitive
            ["ns", "\bant"], # Present Participle
            "t", # Perfect Participle
            "\band", # Gerund
            "\band", # Gerundive
            ["", "te"], # Present imperative
            [["to:", "to:"], ["to:te", "\banto:"]] # Future Imperative
        ]


    ], [ # Conjugation 2
        [ # Active
            [ # Indicative
                [ # Non-perfect
                    [["bam", "ba:s", "bat"], ["ba:mus", "ba:tis", "bant"]],
                    [["\beo:", "s", "\bet"], ["mus", "tis", "\bent"]],
                    [["bo:", "bis", "bit"], ["bimus", "bitis", "bunt"]],
                ], [ # Perfect
                    [["eram", "era:s", "erat"], ["era:mus", "era:tis", "erant"]],
                    [["i:", "isti:", "\it"], ["imus", "istis", "e:runt"]],
                    [["ero:", "eris", "erit"], ["erimus", "eritis", "erint"]],
                ]
            ], [ # Subjunctive
                [ # Non-perfect
                    [["ram", "ra:s", "rat"], ["ra:mus", "ra:tis", "rant"]],
                    [["\bem", "\be:s", "\bet"], ["\be:mus", "\be:tis", "\bent"]]
                ], [ # Perfect
                    [["issem", "isse:s", "isset"], ["isse:mus", "isse:tis", "issent"]],
                    [["erim", "eris", "erit"], ["erimus", "eritis", "erint"]]
                ]
            ]
        ], [ # Passive
            [ # Indicative
                [ # Non-perfect
                    [["bar", "ba:ris", "ba:tur"], ["ba:mur", "ba:mini:", "bantur"]],
                    [["\bor", "ris", "tur"], ["mur", "mini:", "ntur"]],
                    [["bor", "beris", "bitur"], ["bimur", "bimini:", "bunture"]]
                ], [ # Perfect
                    # Nothing here, supine case handled separately
                ]
            ], [ # Subjunctive
                [ # Non-perfect
                    [["rer", "re:ris", "re:tur"], ["re:mur", "re:mini:", "re:ntur"]],
                    [["\ber", "ris", "tur"], ["mur", "mini:", "ntur"]],
                    # Nothing here, supine case handled separately
                ], []
            ]
        ], [ # Miscellaneous
            "re", # Infinitive
            "ri", # Passive Infinitive
            ["ns", "\bent"], # Present Participle
            "\bit", # Perfect Participle
            "\bend", # Gerund
            "\bend", # Gerundive
            ["", "te"], # Present imperative
            [["to:", "to:"], ["to:te", "\bento:"]] # Future Imperative
        ]


    ], [ # Conjugation 3
        [ # Active
            [ # Indicative
                [ # Non-perfect
                    [["bam", "ba:s", "bat"], ["ba:mus", "ba:tis", "bant"]],
                    [["\bo:", "\bis", "\bit"], ["\bimus", "\bitis", "\bunt"]],
                    [["\bam", "s", "\bet"], ["mus", "tis", "\bent"]],
                ], [ # Perfect
                    [["eram", "era:s", "erat"], ["era:mus", "era:tis", "erant"]],
                    [["i:", "isti:", "it"], ["imus", "istis", "e:runt"]],
                    [["ero:", "eris", "erit"], ["erimus", "eritis", "erint"]],
                ]
            ], [ # Subjunctive
                [ # Non-perfect
                    [["\berem", "\bere:s", "\beret"], ["\bere:mus", "\bere:tis", "\berent"]],
                    [["\bam", "a:s", "\bat"], ["a:mus", "a:tis", "ant"]]
                ], [ # Perfect
                    [["issem", "isse:s", "isset"], ["isse:mus", "isse:tis", "issent"]],
                    [["erim", "eris", "erit"], ["erimus", "eritis", "erint"]]
                ]
            ]
        ], [ # Passive
            [ # Indicative
                [ # Non-perfect
                    [["bar", "ba:ris", "ba:tur"], ["ba:mur", "ba:mini:", "bantur"]],
                    [["\bor", "\beris", "\bitur"], ["\bimur", "\bimini:", "\buntur"]],
                    [["\bar", "ris", "tur"], ["mur", "mini:", "ntur"]]
                ], [ # Perfect
                    # Nothing here, supine case handled separately
                ]
            ], [ # Subjunctive
                [ # Non-perfect
                    [["rer", "re:ris", "re:tur"], ["re:mur", "re:mini:", "re:ntur"]],
                    [["\bar", "ris", "tur"], ["mur", "mini:", "ntur"]],
                    # Nothing here, supine case handled separately
                ], []
            ]
        ], [ # Miscellaneous
            "\bere", # Infinitive
            "\beri", # Passive Infinitive
            ["ns", "\bent"], # Present Participle
            "\bt", # Perfect Participle
            "\bend", # Gerund
            "\bend", # Gerundive
            ["\be", "\bite"], # Present imperative
            [["\bito:", "\bito:"], ["\bito:te", "\bunto:"]] # Future Imperative
        ]


    ], [ # Conjugation 4
        [ # Active
            [ # Indicative
                [ # Non-perfect
                    [["e:bam", "e:ba:s", "e:bat"], ["e:ba:mus", "e:ba:tis", "e:bant"]],
                    [["o:", "\bi:s", "t"], ["\bi:mus", "\bi:tis", "unt"]],
                    [["am", "e:s", "et"], ["e:mus", "e:tis", "ent"]],
                ], [ # Perfect
                    [["eram", "era:s", "erat"], ["era:mus", "era:tis", "erant"]],
                    [["i:", "isti:", "it"], ["imus", "istis", "e:runt"]],
                    [["ero:", "eris", "erit"], ["erimus", "eritis", "erint"]],
                ]
            ], [ # Subjunctive
                [ # Non-perfect
                    [["\bi:rem", "\bi:re:s", "\bi:ret"], ["\bi:re:mus", "\bi:re:tis", "\bi:rent"]],
                    [["\bam", "s", "\bat"], ["mus", "tis", "\bant"]]
                ], [ # Perfect
                    [["issem", "isse:s", "isset"], ["isse:mus", "isse:tis", "issent"]],
                    [["erim", "eris", "erit"], ["erimus", "eritis", "erint"]]
                ]
            ]
        ], [ # Passive
            [ # Indicative
                [ # Non-perfect
                    [["e:bar", "e:ba:ris", "e:ba:tur"], ["e:ba:mur", "e:ba:mini:", "e:bantur"]],
                    [["\bior", "ris", "tur"], ["mur", "mini:", "\biuntur"]],
                    [["ar", "e:ris", "e:tur"], ["e:mur", "e:mini:", "e:nture"]]
                ], [ # Perfect
                    # Nothing here, supine case handled separately
                ]
            ], [ # Subjunctive
                [ # Non-perfect
                    [["rer", "re:ris", "re:tur"], ["re:mur", "re:mini:", "re:ntur"]],
                    [["\bar", "ris", "tur"], ["mur", "mini:", "ntur"]],
                    # Nothing here, supine case handled separately
                ], []
            ]
        ], [ # Miscellaneous
            "re", # Infinitive
            "ri", # Passive Infinitive
            ["e:ns", "ent"], # Present Participle
            "t", # Perfect Participle
            "end", # Gerund
            "end", # Gerundive
            ["\bi:", "\bi:te"], # Present imperative
            [["\bi:to:", "\bi:to:"], ["\bi:to:te", "unto:"]] # Future Imperative
        ]
    ]
]
