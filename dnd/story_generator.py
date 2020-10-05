import re
from collections import deque

from .bank import WORD_BANK
from .qrandom import QuantumRandomInt


class StoryGenerator:
    def __init__(self, stories):
        self.stories = stories
        self.story_chooser = QuantumRandomInt(0, len(self.stories) - 1)
        self.story = ""
        self.user_categories = []

    def select_story(self, **kwargs):
        idx = 0  # takes care of when there's only one story
        if len(self.stories) > 1:
            idx = self.story_chooser.generate(**kwargs)[0]
        self.story = self.stories[idx]

    def get_user_categories(self):
        user = re.compile("USER_\w+")
        self.user_categories = user.findall(self.story)
        out = []
        for user_category in self.user_categories:
            category = user_category.partition("_")[2].lower()
            category = category.replace("_", " ")
            out.append(category)
        return out

    def complete_story(self, user_replies, **kwargs):
        if len(user_replies) != len(self.user_categories):
            raise ValueError("Not all questions have been answered.")
        user_replies = deque(user_replies)

        for user_category in self.user_categories:
            reply = user_replies.popleft()
            category = user_category.partition("_")[2].lower()
            if category == "name":
                word = reply.capitalize()
            else:
                word = reply.lower()
            word = '<span style="color: #ff8c00">' + word + "</span>"
            self.story = self.story.replace(user_category, word, 1)

        qc = re.compile("QC_\w+")
        for qc_category in qc.findall(self.story):
            category = qc_category.partition("_")[2].lower()
            word_chooser = QuantumRandomInt(0, len(WORD_BANK[category]) - 1)
            idx = word_chooser.generate(**kwargs)[0]
            word = WORD_BANK[category][idx].lower()
            word = '<span style="color: #1e90ff">' + word + "</span>"
            self.story = self.story.replace(qc_category, word, 1)

        return self.story
