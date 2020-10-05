WORD_BANK = {
    # Personality adjectives
    "pos_adj": [
        "friendly",
        "cheerful",
        "gregarious",
        "bubbly",
        "charming",
        "charismatic",
        "benevolent",
        "sprightly",
        "buoyant",
        "brave",
        "courageous",
        "faithful",
        "delightful",
        "faithful",
        "clever",
        "courteous",
        "honest",
        "chirpy",
    ],
    "neg_adj": [
        "frivolous",
        "conceited",
        "frustrating",
        "dishonorable",
        "depraved",
        "fiendish",
        "diabolic",
        "wicked",
        "malicious",
        "malevolent",
        "serpentine",
        "cynical",
        "pompous",
        "frigid",
        "nasty",
    ],
    # Appearance/smell adjectives
    "app_neg_adj": [
        "dank",
        "grimy",
        "sour",
        "putrid",
        "scraggy",
        "gaunt",
        "dour",
        "grotty",
        "sordid",
        "manky",
        "stained",
        "malodorous",
        "fetid",
        "vile",
    ],
    "app_pos_adj": [
        "beautiful",
        "sparkly",
        "radiant",
        "pleasant",
        "colorful",
        "divine",
        "dazzling",
        "clean",
        "starry",
        "sun-kissed",
    ],
    "colors": [
        "blue",
        "mauve",
        "beige",
        "burgundy",
        "white",
        "brown",
        "carrot orange",
        "yellow",
        "plum",
        "green",
        "pink",
        "purple",
        "turquoise",
        "gold",
        "copper",
        "silver",
    ],
    # others
    "races": [
        "elf",
        "dwarf",
        "tiefling",
        "half-orc",
        "dragonborn",
        "gnome",
        "human",
        "halfling",
        "half-elf",
    ],
    "races_plural": [
        "elves",
        "dwarves",
        "tieflings",
        "half-orcs",
        "dragonborn",
        "gnomes",
        "humans",
        "halflings",
        "half elves",
    ],
    "objects": [
        "toothbrush",
        "lotion",
        "drumstick",
        "maple leaf",
        "book",
        "notebook",
        "tooth",
        "bracelet",
        "stick",
        "bookmark",
        "feather",
        "map",
        "poultice",
        "slipper",
        "lemon",
        "paperclip",
        "biscuit",
        "towel",
    ],
    "nouns": [
        "sunset",
        "slap",
        "tortoise",
        "cough",
        "book",
        "library",
        "bubble",
        "jar",
        "feud",
        "thief",
        "plumber",
        "pimple",
        "fan",
        "coffee pot",
        "stomach ache",
        "difficulty",
        "map",
        "nose hair",
        "curse",
        "wart",
        "fence",
        "horn",
        "matriarch",
        "cloak",
        "mouse",
        "spider",
        "ale",
        "vial",
        "sugar",
    ],
    "nouns_plural": [
        "fights",
        "warts",
        "stampedes",
        "oils",
        "combs",
        "coasters",
        "battles",
        "betrayals",
        "chamber pots",
        "vehicles",
        "slippers",
        "clogs",
        "formalities",
        "warts",
        "lemons",
        "tarts",
        "frowns",
        "bedrooms",
        "demons",
        "sundresses",
        "cats",
        "dogs",
        "clouds",
    ],
    "places": [
        "monastery",
        "town",
        "citadel",
        "school",
        "castle",
        "island",
        "mountain",
        "valley",
        "forest",
        "island",
        "library",
        "temple",
        "museum",
    ],
    "spices": [
        "cardamom",
        "cloves",
        "cinnamon",
        "nutmeg",
        "saffron",
        "vanilla",
        "chamomile",
        "spearmint",
        "coriander",
        "lavender",
    ],
    "condiments": [
        "ketchup",
        "mustard",
        "maple syrup",
        "soy sauce",
        "fish sauce",
        "wasabi",
        "tartar sauce",
        "relish",
    ],
    "conflicts": [
        "rampage of marauding monsters",
        "clash between rival tribes",
        "family feud",
        "war",
        "curse by an irritable wizard",
        "clash of clans",
        "government coup",
    ],
}


STORIES_DB = [
    "You ate a cursed USER_FRUIT and now you can't see the color QC_COLORS.",
    "A QC_NEG_ADJ picksie stole your USER_COLOR USER_OBJECT, and now you search high and low to recover it.",
    "When you were an infant, a QC_RACES wizard bestowed upon you an amulet with the symbol of a QC_NEG_ADJ USER_ANIMAL.",
    "You had a weird dream about a QC_COLORS USER_ANIMAL drinking USER_BEVERAGE, which you took as a sign to go on adventures.",
    "Your childhood was torn apart by a USER_ADJECTIVE QC_CONFLICTS.",
    "You were banished from QC_PLACES because you served USER_FOOD topped with QC_CONDIMENTS to QC_RACES_PLURAL.",
    "You are from a QC_PLACES that perished in a USER_NATURAL_DISASTER that you suspect wasn’t natural.",
    "Your family was killed by a group of QC_RACES warriors, and now you’ve sworn to USER_VERB with any you see.",
    "You once ate a delicious USER_FOOD in a distant QC_PLACES and now you can’t stop craving it--you must find it again!",
    "You’ve been on the run from a QC_NEG_ADJ QC_RACES who is stalking you because of his obsession with your USER_BODY_PART.",
    "You very lovingly call your QC_APP_POS_ADJ weapon your 'little USER_NOUN.'",
    "You jumped through a portal on a dare and found yourself in a QC_PLACES with USER_PLURAL_NOUN.",
    "You lost your USER_BODY_PART in a QC_CONFLICTS.",
    "A QC_NEG_ADJ sorcerer cursed you: you now turn into a USER_ANIMAL whenever you get the hiccups.",
    "You woke up in a QC_PLACES with no memory or clothes, just a USER_OBJECT.",
    "An enchanted USER_OBJECT once told you a captivating story about a QC_CONFLICTS.",
    "On a campaign you stumble across a magic USER_WEAPON that when wielded makes you think QC_NEG_ADJ thoughts.",
    "A QC_CONFLICTS drove you from your homeland, and all you have left is a bag of USER_PLURAL_OBJECT.",
]


SCENE = """The USER_ANIMAL and USER_NOUN is an old tavern, QC_APP_NEG_ADJ and QC_APP_NEG_ADJ and USER_ADJ3, but welcoming nonetheless.

You and your QC_POS_ADJ stallion, USER_NAME, have slept under too many night skies to be very picky anyway.

A QC_POS_ADJ QC_RACES waitress at the door waves you in from the murky dark outside, and you step into a room lit by bright lanterns that cast a QC_COLORS aura on the QC_RACES_PLURAL and QC_RACES_PLURAL relaxing by the fireplace, playing cards, or sharing drinks.

A bard plays a USER_INSTRUMENT in the corner, he isn’t very good but he’s enthusiastic.

You make your way to the bar at the back, where the barkeep, a USER_ADJ5 QC_RACES, polishes an empty glass.

“What’ll ye have, then?” the barkeep asks.

“Give me a USER_DRINK. And USER_FOOD if you have any,” you say, easing your heavy pack onto the floor, settling on a barstool.

The barkeep raises an eyebrow before shrugging and calling out to the waitress who greeted you.

“Fetch that fresh bit o’ USER_DRINK from the back would ye, lass? And tell cook to get on some USER_FOOD.” The barkeep turns to you, still polishing the same glass. “The name’s USER_ANOTHER_NAME. I would no object to hearing yours, but some like to keep low. What’ll it be?”

You simply smile. Your recent campaign gave you a bit of a reputation and you’d like to enjoy your USER_DRINK in peace.

USER_ANOTHER_NAME grins with a quick nod, then turns away to polish a second glass.

It is not long before you clasp your USER_DRINK, and they’ve even provided USER_FOOD, though it’s oddly topped with QC_CONDIMENTS. But you’ve eaten stranger things, and you dig in anyway.

As you sip and snack, you scan the room, tuning in to the soft murmurs of the tavern crowd, the dusty paintings of USER_PLURAL_NOUN and QC_NOUNS_PLURAL on the walls, the smell of sweat and QC_SPICES riding on the air.

You suppress a smile when the bard fumbles some USER_INSTRUMENT notes.

At once, you catch a whiff of USER_FLOWER, a scent that briefly tickles something in your memory; someone is next to you but as you turn to look, their hand blocks you.

“Don’t,” says a soft voice, too temperate for you to decipher whether QC_NEG_ADJ. “Let’s avoid being conspicuous.”

You comply, if only out of curiosity—what other surprises did The USER_ANIMAL and USER_NOUN--a tavern that served USER_FOOD with a twist--have to offer?

The mysterious stranger slips something into your hands, pressing your fingers around it.

“Guard this with your life,” says the soft voice. “Please.” This time the tone harbors a splash of desperation. When the stranger lets go of your hand, you venture a quick glance at what you hold.

Your fingers are tightly wrapped around a USER_COLOR USER_OBJECT. Baffled, you look up, but the stranger is gone.

“Hey, USER_ANOTHER_NAME, who was that?” you ask, turning to the barkeep.

“Hmm?”

“That person who spoke to me. Right here.” You point.

USER_ANOTHER_NAME looks at you as though you’ve grown a second head. “There’s no one come to the bar since ye.”

You frown, look from the barkeep to the USER_OBJECT in your hand. And with a hint of a chuckle, you slip it into the deep pockets of your cloak.

After all, you’ve seen stranger things.

You’ve met a picksie who snuck into your room to distract you with a song about a QC_NOUNS while her companion stole your QC_OBJECTS.

You’ve faced a one-eyed giant who guarded a trove of USER_PLURAL_OBJECT in an enchanted QC_PLACES.

You’ve even escaped a sphinx who posed for you a riddle you couldn’t solve: Five QC_RACES_PLURAL walk into a room. Only one leaves, carrying a QC_APP_POS_ADJ QC_OBJECTS. Who was waiting for them in the room?

Yes, you’ve certainly seen stranger things. And you will continue to do so, you suspect—what on earth could this USER_OBJECT mean? And why did the stranger smell of USER_FLOWER?

You push a handful of coins the barkeep’s way, strap on your pack, and head out the door.

You whistle for USER_NAME and you ride off into the night, the USER_COLOR USER_OBJECT tucked safely inside your pocket.

The answers are out there somewhere.
"""
