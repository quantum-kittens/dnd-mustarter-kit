import re

from bank import WORD_BANK
from qrandom import QuantumRandomInt

class StoryGenerator:
    def __init__(self, stories):
        self.stories = stories

    def generate(self, backend=None):
        idx = 0 # takes care of when there's only one story
        if len(self.stories) > 1:
            story_chooser = QuantumRandomInt(0, len(self.stories) - 1)
            idx = story_chooser.generate(1, backend)[0]
        story = self.stories[idx]

        user = re.compile("USER_\w+")
        qc = re.compile("QC_\w+")

        for user_category in user.findall(story):
            category = user_category.partition("_")[2].lower()
            if category == 'name':
                word = str(input(f"Choose a {category}: ")).capitalize()
            else:
                word = str(input(f"Choose a {category}: ")).lower()
            red_word = '<red>' + word + '</red>' # user inputs are red
            story = story.replace(user_category, red_word, 1)

            
        for qc_category in qc.findall(story):
            category = qc_category.partition("_")[2].lower()
            word_chooser = QuantumRandomInt(0, len(WORD_BANK[category]) - 1)
            idx = word_chooser.generate(1, backend)[0]
            word = WORD_BANK[category][idx].lower()
            blue_word = '<blue>' + word + '</blue>' #qc inputs are blue
            story = story.replace(qc_category, blue_word, 1)
        
        return story
