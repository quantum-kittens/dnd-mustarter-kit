import re

from bank import ADJECTIVES
from qrandom import QuantumRandomInt


class StoryGenerator:
    def __init__(self, stories):
        self.stories = stories

    def generate(self, backend=None):
        story_chooser = QuantumRandomInt(0, len(self.stories) - 1)
        idx = story_chooser.generate(1, backend)[0]
        story = self.stories[idx]

        user = re.compile("USER_\w+")
        qc = re.compile("QC_\w+")

        for user_category in user.findall(story):
            category = user_category.partition("_")[2].lower()
            word = str(input(f"Choose a {category}: "))
            story = story.replace(user_category, word, 1)

        for qc_category in qc.findall(story):
            category = qc_category.partition("_")[2].lower()
            word_chooser = QuantumRandomInt(0, len(ADJECTIVES[category]) - 1)
            idx = word_chooser.generate(1, backend)[0]
            word = ADJECTIVES[category][idx]
            story = story.replace(qc_category, word, 1)

        return story
