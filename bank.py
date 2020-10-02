WORD_BANK= {
    # Personality adjectives
    "pos_adj": ['friendly','cheerful','Gregarious', 'bubbly', 'charming', 'charismatic', 'benevolent', 'sprightly', 'buoyant', 'brave', 'courageous', 'faithful', 'delightful', 'faithful','clever', 'courteous','honest', 'chirpy'],
    "neg_adj": ['frivolous','Conceited', 'exasperating', 'dishonorable', 'depraved', 'fiendish', 'diabolic', 'wicked', 'malicious', 'malevolent', 'serpentine', 'cynical', 'pompous','frigid','offensive'],
    # Appearance/smell adjectives
    "app_neg_adj": ['dank', 'grimy', 'sour', 'putrid', 'emaciated', 'gaunt', 'dour', 'grotty', 'sordid', 'manky', 'stained', 'malodorous', 'fetid', 'vile'],
    "app_pos_adj": ['beautiful','sparkly','radiant', 'pleasant', 'colorful','divine','dazzling', 'clean', 'starry', 'sun-kissed'],
    "colors": ['blue', 'mauve', 'olive', 'burgundy', 'white', 'brown',  'orange', 'yellow',  'plum', 'green', 'pink', 'purple', 'turquoise', 'gold','copper', 'silver'],
    #others
    "races" : ['elf', 'dwarf', 'tiefling', 'half-orc', 'dragonborn', 'gnome', 'human', 'halfling', 'half-elf'],
    "races_plural" : ['elves', 'dwarves', 'tieflings', 'half-orcs', 'dragonborn', 'gnomes', 'humans', 'halflings', 'half elves'],
    "objects" : ['toothbrush', 'lotion', 'drumstick', 'maple leaf', 'book', 'notebook', 'tooth','bracelet', 'stick', 'bookmark', 'feather', 'map', 'poultice','slipper', 'lemon','paperclip', 'biscuit', 'towel'],
    "nouns" : ['sunset','slap', 'tortoise', 'cough', 'book', 'library', 'bubble', 'jar','feud', 'thief', 'plumber', 'pimple', 'fan', 'coffee pot', 'stomach ache', 'difficulty', 'map', 'nose hair', 'curse', 'wart','fence', 'horn', 'matriarch', 'cloak', 'mouse', 'spider', 'ale','vial', 'sugar'],
    "nouns_plural" : ['fights', 'warts', 'stampedes', 'oils', 'combs', 'coasters', 'battles', 'betrayals', 'chamber pots', 'vehicles', 'slippers','clogs','formalities', 'warts', 'lemons', 'tarts','frowns','bedrooms', 'demons', 'sundresses', 'cats', 'dogs','clouds'],
    "places" : ['Monastery', 'town', 'citadel', 'school', 'castle', 'island', 'mountain', 'valley', 'forest', 'island', 'library', 'temple','museum'],
    "spices" : ['cardamom', 'cloves', 'cinnamon', 'nutmeg', 'saffron', 'vanilla', 'chamomile', 'spearmint', 'coriander', 'lavender'],
    "condiments" : ['ketchup' ,'mustard', 'maple syrup', 'soy sauce','fish sauce', 'wasabi', 'tartar sauce','relish'],
    "conflicts" : ['rampage of marauding monsters', 'clash between rival tribes','family feud', 'war', 'curse by an irritable wizard', 'clash of clans', 'government coup']
}

STORIES_DB = [
    "You ate a cursed USER_FRUIT and now you can't see the color QC_COLORS.",
    "A QC_NEG_ADJ picksie stole your USER_COLOR USER_OBJECT, and now you search high and low to recover it.",
    "When you were an infant, a QC_RACES wizard bestowed upon you an amulet with a symbol of a QC_NEG_ADJ USER_ANIMAL.",
    "You had a weird dream about a QC_COLORS USER_ANIMAL drinking USER_BEVERAGE, which you took as a sign to go on adventures.",
    "Your childhood was torn apart by a USER_ADJECTIVE QC_CONFLICTS.",
    "You were banished from QC_PLACES because you served USER_FOOD topped with QC_CONDIMENTS to QC_RACES_PLURAL.",
    "You are from a QC_PLACES that perished in a USER_NATURAL_DISASTER that you suspect wasn’t natural.",
    "Your family was killed by a group of QC_RACES warriors, and now you’ve sworn to USER_VERB with any you see.",
    "You once ate a delicious USER_FOOD in a distant QC_PLACES and now you can’t stop craving it--you must find it again!",
    "You’ve been on the run from a QC_NEG_ADJ QC_RACES who is stalking you because of his obsession with your USER_BODY_PART.",
    "You very lovingly call your QC_APP_POS_ADJ weapon your \'little USER_NOUN.\'",
    "You jumped through a portal on a dare and found yourself in a QC_PLACES with USER_PLURAL_NOUN.",
    "You lost your USER_BODY_PART in a QC_CONFLICTS.",
    "A QC_NEG_ADJ sorcerer cursed you: you now turn into a USER_ANIMAL whenever you get the hiccups.",
    "You woke up in a QC_PLACES with no memory or clothes, just a USER_OBJECT.",
    "An enchanted USER_OBJECT once told you a captivating story about a QC_CONFLICTS.",
    "On a campaign you stumble across a magic USER_WEAPON that when wielded makes you think QC_NEG_ADJ thoughts.",
    "A QC_CONFLICTS drove you from your homeland, and all you have left is a bag of USER_OBJECT_PLURAL."
]
