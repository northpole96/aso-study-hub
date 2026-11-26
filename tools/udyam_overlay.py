"""Corrections to the PYQ Bank from the Udyam IAS GA and English books (udyam pyq/*.pdf), checked 26 Nov 2026.
Keys are the publisher's, not OPSC's. Applied by build_pyq_bank.py after the questions are built.
Key (paper, year, question number in the paper): FILL = options and/or key we did not have; ADOPT = our old key was wrong or a
guess, the book's is better (old key kept in the note); CHECK = the two keys disagree, ours stays and the card says so."""
BOOK = "Key from the Udyam IAS book."
FILL = {
    ("ga", 2025, 3): dict(a="A", w="Palamu district, Jharkhand. " + BOOK),
    ("ga", 2025, 66): dict(o=["a-1, b-2, c-3, d-4", "a-1, b-2, c-4, d-3", "a-1, b-3, c-2, d-4", "a-2, b-1, c-3, d-4"], a="A",
        w="Match: a-1 (West Antarctic ice edge, 400 feet a year), b-2 (Andes of Peru, 1978-95), c-3 (Tien Shan, 25 percent in 60 years), d-4 (Russian Caucasus, four decades). The figures are quoted from the question and are not checked. " + BOOK),
    ("ga", 2025, 67): dict(o=["a-1, b-2, c-3, d-4", "a-2, b-1, c-4, d-3", "a-3, b-4, c-1, d-2", "a-4, b-3, c-2, d-1"], a="D",
        w="Gujarat 4 (Pakistan), Himachal Pradesh 3 (China), Uttarakhand 2 (China and Nepal), West Bengal 1 (Bhutan and Bangladesh; Nepal is also a neighbour but is not in the option). " + BOOK),
    ("ga", 2025, 85): dict(o=["a-1, b-2, c-3, d-4", "a-2, b-3, c-1, d-4", "a-2, b-3, c-4, d-1", "a-4, b-1, c-3, d-2"], a="C",
        w="Oxygen 21 percent (2), nitrogen 78 percent (3), ozone a trace gas, unevenly spread (4), water vapour the most variable gas (1). " + BOOK),
    ("ga", 2025, 93): dict(o=["a-1, b-2, c-3, d-4", "a-2, b-1, c-4, d-3", "a-2, b-4, c-3, d-1", "a-1, b-4, c-3, d-2"], a="B",
        w="Trans-Himalayan 2 (sparse vegetation, wild sheep and goats), Himalayan 1 (high mountains), Semi-arid 4 (next to the desert), Western Ghats 3 (dense forests). " + BOOK),
    ("en", 2025, 72): dict(a="C", w="QRPS: Reading romantic novels and going to sleep has been her habit. " + BOOK),
    ("en", 2018, 46): dict(c=True, a="C", o=[
        "\u201cAre we going to the mall?\u201d \u201cIf we are we'd better be prepared they don't take cash.\u201d We to need to pay by card or Paytm in any case we are not making any big purchases. Are we?\u201d",
        "\u201cAre we going to the mall if we are wed better be prepared they don't take cash.\u201d We to need to pay by card or Paytm in any case we are not making any big purchases.\u201d Are we?\u201d",
        "\u201cAre we going to the mall? If we are, we'd better be prepared. They don't take cash. We need to pay by card, or Paytm. In any case, we are not making any big purchases, are we?\u201d",
        "\u201cAre we going to the mall? If we are we'd better be prepared. They don't take cash. We need to pay by card or Paytm. In any case we are not making any big purchases, are we?\u201d"],
        w="Our key C: the fully punctuated version, with commas after 'If we are', 'card' and 'In any case'. Udyam book key: D (the same without those commas). CHECK. Options are from the Udyam IAS book."),
}
ADOPT = {
    ("ga", 2021, 7): ("C", "Microsoft. CBSE announced Data Science (classes 8 to 12) with Microsoft in June 2021. Our old key was Intel (the option was misprinted 'Inter'). " + BOOK),
    ("ga", 2021, 19): ("A", "John Hopfield. Deepak Dhar and John Hopfield shared the 2022 Boltzmann Medal. Our old key was Daan Frenkel. " + BOOK),
    ("ga", 2021, 53): ("D", "Kazakhstan chaired the SCO Council of Heads of Government that met by video on 25 Nov 2021. Our old key was India. " + BOOK),
}
CHECK = {   # our key stays; the card says what the book says
    ("en", 2018, 37): "Udyam book: D (until). Our key A (till). Both mean the same here.",
    ("en", 2018, 68): "Udyam book: C (detaining the poor up to 10 years). Our key A. Re-read the passage.",
    ("en", 2021, 62): "Udyam book: C (at). Our key A (about).",
    ("en", 2021, 83): "Udyam book: D (have, as in 'have been fed'). Our key B (are).",
    ("en", 2021, 89): "Udyam book: C (has been). Our key A (are). Collective noun: both are argued.",
    ("en", 2025, 56): "Udyam book: B (subterraneously). Our key A (subterranean).",
    ("en", 2025, 70): "Udyam book: D (in the slope). Our key A (does). 'on the slope' is the better English, so D is likely.",
    ("ga", 2018, 11): "Udyam book: D (V. K. Saraswat). Our key A.",
    ("ga", 2018, 13): "Udyam book: C (Plankton and Nekton). Our key A (Plankton).",
    ("ga", 2018, 34): "Udyam book: C and D are both wrong statements, so no unique key. Our key D.",
    ("ga", 2018, 56): "Udyam book: D (Vijayanta, first built in India). Our key B (Arjun, first designed in India). Depends on what 'indigenous' means.",
    ("ga", 2018, 70): "Udyam book: B (Rhinos). Our key C (Elephants).",
    ("ga", 2021, 42): "Udyam book: B (Central Vigilance Commission). Our key C (Santhanam Committee).",
    ("ga", 2021, 44): "Udyam book: A (Public opinion). Our key B (Election).",
    ("ga", 2021, 46): "Udyam book: B (Masterman Committee). Our key D (Northcote-Trevelyan).",
    ("ga", 2021, 65): "Udyam book: A (Alaska). Our key B (Aleutian Islands).",
    ("ga", 2021, 78): "Udyam book: B (Laterite soil). Our key D (Yellow earth).",
    ("ga", 2021, 100): "Udyam book: C (Predatory spiders). Our key A (Secondary carnivores).",
    ("ga", 2021, 27): "Udyam book: disputed, B is the commonly supplied key. Our key A.",
    ("ga", 2025, 34): "Udyam book: A (Only 1 and 4). Our key B (Only 1, 3 and 4). Re-read statement 3.",
}
