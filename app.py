import re
from collections import deque

from flask import Flask, render_template, request

from dnd import *

app = Flask(__name__)

# Dice
d4 = QuantumDice(4)
d6 = QuantumDice(6)
d8 = QuantumDice(8)
d10 = QuantumDice(10)
d12 = QuantumDice(12)
d20 = QuantumDice(20)

# Name Generator
ng = NameGenerator()

# Race Generator
rg = QuantumRandomInt(0, len(RACES) - 1)

# Backstory Generator
sg = StoryGenerator(STORIES_DB)
user_categories = []


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/character", methods=["GET", "POST"])
def character():
    if request.method != "POST":
        sg.select_story()
        user_categories = sg.get_user_categories()
        return render_template(
            "character_generator.html", categories=user_categories, answered=False,
        )
    else:
        # get backstory
        user_categories = sg.get_user_categories()
        user_replies = [request.form.get(category) for category in user_categories]
        story = sg.complete_story(user_replies)

        # get name
        syllables = d4.roll(1, 0)[0][0]
        name = ng.generate(syllables)

        # get race
        idx = rg.generate()[0]
        race = RACES[idx]

        # get class
        cg = ClassGenerator(race)
        dnd_class = cg.generate(maxiter=100)[0]

        return render_template(
            "character_generator.html",
            name=name,
            race=race,
            dnd_class=dnd_class,
            backstory=story,
            answered=True,
        )


@app.route("/dice", methods=["GET", "POST"])
def dice():
    if request.method == "POST":
        dice = request.form.get("dice")
        times = int(request.form.get("times"))
        modifier = int(request.form.get("modifier"))

        roll = None
        if dice == "D20":
            roll = d20.roll(times, modifier)
        elif dice == "D4":
            roll = d4.roll(times, modifier)
        elif dice == "D6":
            roll = d6.roll(times, modifier)
        elif dice == "D8":
            roll = d8.roll(times, modifier)
        elif dice == "D10":
            roll = d10.roll(times, modifier)
        elif dice == "D12":
            roll = d12.roll(times, modifier)
        else:
            return render_template("dice_roller.html")

        roll_str = " + ".join([str(r) for r in roll[0]])
        roll_str = roll_str + f" + {modifier}"
        roll_str = roll_str + f" = {roll[1]}"

        return render_template("dice_roller.html", roll=roll_str)
    else:
        return render_template("dice_roller.html")


@app.route("/scene", methods=["GET", "POST"])
def scene():
    scene = SCENE
    categories = [
        "an animal",
        "a singular noun",
        "an adjective describing appearance or smell",
        "a name",
        "an instrument",
        "an adjective",
        "a drink",
        "a food",
        "another name",
        "a plural noun",
        "a flower",
        "a color",
        "an object",
        "an object (plural)",
    ]

    if request.method != "POST":
        return render_template(
            "scene_generator.html", categories=categories, answered=False
        )
    else:
        user = re.compile("USER_\w+")
        user_categories = set(user.findall(scene))
        user_replies = deque([request.form.get(category) for category in categories])

        print(len(user_categories) == len(user_replies))

        for user_category in user_categories:
            reply = user_replies.popleft()
            category = user_category.partition("_")[2].lower()
            if category == "name":
                word = reply.capitalize()
            else:
                word = reply.lower()
            scene = scene.replace(user_category, word)

        qc = re.compile("QC_\w+")
        for qc_category in qc.findall(scene):
            category = qc_category.partition("_")[2].lower()
            word_chooser = QuantumRandomInt(0, len(WORD_BANK[category]) - 1)
            idx = word_chooser.generate()[0]
            word = WORD_BANK[category][idx].lower()
            scene = scene.replace(qc_category, word, 1)

        return render_template("scene_generator.html", scene=scene, answered=True)


if __name__ == "__main__":
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
