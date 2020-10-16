import re
from collections import defaultdict, deque

from flask import Flask, Markup, render_template, request
from qiskit import IBMQ, BasicAer
from qiskit.providers.ibmq import least_busy

from dnd import *

###############################################################################
# To run this on an actual quantum device, uncomment the following lines, and
# comment out `backend = BasicAer.get_backend("qasm_simulator")`. Then
# uncomment the lines in the `get class` section of the character generator
# as described further down.
###############################################################################

# IBMQ.save_account("ibmq-token-goes-here")
# provider = IBMQ.load_account()
# backend = least_busy(
#     provider.backends(
#         filters=lambda x: x.configuration().n_qubits >= 5
#         and not x.configuration().simulator
#         and x.status().operational == True
#     )
# )

backend = BasicAer.get_backend("qasm_simulator")


app = Flask(__name__)

# Dice
d4 = QuantumDice(4)
d6 = QuantumDice(6)
d8 = QuantumDice(8)
d10 = QuantumDice(10)
d12 = QuantumDice(12)
d20 = QuantumDice(20)

# Name Generator
ng = NameGenerator

# Race Generator
rg = QuantumRandomInt(0, len(RACES) - 1)

# Class Generator
optimized_params = [
    [1.5152966068304041, 1.5186556648643206, 1.5897032108958873, 1.5548881877792053],
    [1.5140511223814679, 1.5525252793751712, 1.5436261575253685, 1.531691495711558],
    [1.5208848465686453, -1.5591762572392858, 1.5407844523800633, 1.5313232523519738],
    [1.5744828123931423, 1.5299845623465544, 1.5838176568542992, 1.5961253930916945],
    [1.579295007117179, 1.5791026247724318, 1.619656245047392, 1.5814117923262674],
    [1.560252034691874, 1.5793652373905132, 1.5610876056311191, 1.5408873842531166],
    [1.5619034442228519, 1.5898848964174048, -1.625555178039331, 1.5876778474263558],
    [1.5671534101130173, 1.5984692977165749, 1.6231658940661673, 1.586303255554067],
    [1.5663561253156386, 1.5942352578417385, 1.615257310682868, 1.5992071329147994],
    [-1.5707949530624141, 1.5486410621699014, 1.5749954829986246, 1.5962243513635772],
    [-1.5881629546748068, 1.5531438652735101, 1.593658466365199, 1.5740210765637093],
    [1.5708378454015384, 1.5521537463839634, 1.5599211865205593, -1.5396072960245804],
    [1.5103576258283542, 1.5618815162318456, 1.550846150136395, -1.5704798290697968],
    [1.5729353102094399, 1.5523276667052224, 1.5440468497267712, 1.5801624642911067],
    [1.5742667240293402, 1.5731283355199297, -1.572299197520027, 1.5707461907532896],
    [1.5880583523256642, -1.537514350553075, 1.5928677958938111, -1.629508380536372],
]

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
        name = ng("name").generate(syllables, backend=backend)

        # get race
        idx = rg.generate(backend=backend)[0]
        race = RACES[idx]

        #### get clan name if dwarf
        clan_name = "NULL"
        
        if race == "Hill Dwarf" or "Mountain Dwarf":
            
            clan_name = ng("clan").generate_clan()
            #clan_name = generate_clan()

        # get class

        #######################################################################
        # To run this on a actual device, uncomment the following lines, and
        # comment out `thetas = optimized_params[idx]` and
        # `dnd_class = ClassGenerator.generate(race, thetas)[0]`
        #######################################################################

        # cg = ClassGenerator(race, backend=backend)
        # cg.optimize(maxiter=500)
        # dnd_class = ClassGenerator.generate(race, cg.get_minima())[0]

        thetas = optimized_params[idx]
        dnd_class = ClassGenerator.generate(race, thetas)[0]

        return render_template(
            "character_generator.html",
            name=name,
            race=race,
            clan_name = clan_name,
            dnd_class=dnd_class,
            backstory=Markup(story),
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
            roll = d20.roll(times, modifier, backend=backend)
        elif dice == "D4":
            roll = d4.roll(times, modifier, backend=backend)
        elif dice == "D6":
            roll = d6.roll(times, modifier, backend=backend)
        elif dice == "D8":
            roll = d8.roll(times, modifier, backend=backend)
        elif dice == "D10":
            roll = d10.roll(times, modifier, backend=backend)
        elif dice == "D12":
            roll = d12.roll(times, modifier, backend=backend)
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
    lines = SCENE.split("\n")
    scene = " ".join(["<p>" + line + "</p>" for line in lines])
    categories = [
        "an animal",
        "a noun (singular)",
        "an adjective describing appearance or smell",
        "a name",
        "an instrument",
        "an adjective",
        "a drink",
        "a food",
        "another name",
        "a noun (plural)",
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
        user_categories = []
        for user_category in user.findall(scene):
            if user_category not in user_categories:
                user_categories.append(user_category)
        user_replies = deque([request.form.get(category) for category in categories])

        for user_category in user_categories:
            reply = user_replies.popleft()
            category = user_category.partition("_")[2].lower()
            capitalized = {"name", "another_name", "animal", "noun"}
            if category in capitalized:
                word = reply.capitalize()
            else:
                word = reply.lower()
            word = '<span style="color: #ff8c00">' + word + "</span>"
            scene = scene.replace(user_category, word)

        qc = re.compile("QC_\w+")
        category_idx = defaultdict(int)
        for qc_category in qc.findall(scene):
            category = qc_category.partition("_")[2].lower()
            word_chooser = QuantumRandomInt(0, len(WORD_BANK[category]) - 1)
            idx = word_chooser.generate(backend=backend)[0]
            if len(WORD_BANK[category]) > 1:
                while idx == category_idx[category]:
                    idx = word_chooser.generate()[0]
            category_idx[category] = idx
            word = WORD_BANK[category][idx].lower()
            word = '<span style="color: #1e90ff">' + word + "</span>"
            scene = scene.replace(qc_category, word, 1)

        return render_template(
            "scene_generator.html", scene=Markup(scene), answered=True
        )


if __name__ == "__main__":
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
