from .bank import WORD_BANK
from .qrandom import QuantumRandomInt

qc = re.compile("QC_\w+")
backend = None
for qc_category in qc.findall(SCENE):
    category = qc_category.partition("_")[2].lower()
    word_chooser = QuantumRandomInt(0, len(WORD_BANK[category]) - 1)
    idx = word_chooser.generate(1, backend)[0]
    word = WORD_BANK[category][idx].lower()
    SCENE = SCENE.replace(qc_category, word, 1)
