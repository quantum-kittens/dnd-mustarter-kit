import numpy as np
from qiskit import BasicAer, QuantumCircuit, execute
from qiskit.aqua.components.optimizers import SPSA
from qiskit.circuit import ParameterVector

# Ratings
d = 1.1
c = 1.2
b = 1.3
a = 1.4
ap = 1.5
s = 1.6
sp = 1.7
op = 1.8

# Synergy matrix
SYNERGY_MATRIX = np.array(
    [
        [s, ap, a, c, s, s, s, c, s, b, ap, c, b, ap, ap, c],
        [s, c, a, a, b, s, ap, b, s, c, s, c, c, c, c, c],
        [s, c, a, a, b, s, ap, b, s, c, s, c, c, c, c, c],
        [c, s, b, b, ap, c, a, ap, ap, ap, c, ap, ap, s, s, d],
        [d, a, c, c, s, c, s, a, c, ap, c, ap, s, c, c, s],
        [b, a, ap, ap, s, c, a, s, c, s, b, ap, ap, c, b, c],
        [c, c, c, c, b, c, s, b, c, b, c, a, s, c, c, s],
        [c, c, c, c, b, c, s, b, c, b, c, a, s, c, c, s],
        [c, c, c, c, c, c, ap, c, c, c, c, b, ap, c, c, s],
        [a, sp, a, a, a, a, a, a, sp, a, a, a, a, sp, sp, a],
        [a, s, a, a, s, c, b, s, c, ap, c, s, s, s, s, b],
        [s, ap, a, a, s, c, a, s, a, s, c, ap, ap, a, a, a],
        [s, b, b, a, a, s, s, c, s, a, s, a, a, c, s, c],
        [sp, sp, sp, sp, sp, sp, sp, sp, sp, sp, sp, sp, sp, sp, sp, sp],
        [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
        [c, s, c, c, c, c, b, c, ap, c, c, a, a, s, s, ap],
    ]
)

# Races
RACES = [
    "Dragonborn",
    "Hill Dwarf",
    "Mountain Dwarf",
    "Dark Elf",
    "High Elf",
    "Wood Elf",
    "Deep Gnome",
    "Forest Gnome",
    "Rock Gnome",
    "Half-Elf",
    "Lightfoot Halfling",
    "Stout Halfling",
    "Half-Orc",
    "Variant Human",
    "Human",
    "Tiefling",
]

# Classes
CLASSES = [
    "Barbarian",
    "Bard",
    "Cleric",
    "Druid",
    "Fighter (Dex)",
    "Fighter (Str)",
    "Fighter (Eldritch Knight)",
    "Monk",
    "Paladin",
    "Ranger (Dex)",
    "Ranger (Str)",
    "Rogue",
    "Rogue (Arcane Trickster)",
    "Sorcerer",
    "Warlock",
    "Wizard",
]


class ClassGenerator:
    def __init__(self, race, backend=None, shots=4096):
        if race not in RACES:
            raise ValueError("Input is not a valid 5E SRD race.")

        self.backend = backend
        if not self.backend:
            self.backend = BasicAer.get_backend("qasm_simulator")
        self.shots = shots

        class_ratings = SYNERGY_MATRIX[RACES.index(race), :]
        self.expected_probabilities = class_ratings / np.sum(class_ratings)

        self.num_qubits = int(np.log2(len(CLASSES)))
        self.params = ParameterVector("θ", length=self.num_qubits)
        thetas_iter = iter(self.params)

        self.circuit = QuantumCircuit(self.num_qubits)
        for q in self.circuit.qubits:
            self.circuit.ry(next(thetas_iter), q)
        self.circuit.measure_all()

    def _measure(self, thetas):
        bound_circuit = self.circuit.bind_parameters({self.params: thetas})
        jobs = execute(bound_circuit, backend=self.backend, shots=self.shots)
        counts = jobs.result().get_counts()
        return counts

    def _objective_fn(self, thetas):
        counts = self._measure(thetas)
        probabilities = np.zeros(shape=(2 ** self.num_qubits))
        for k, v in counts.items():
            probabilities[int(k, 2)] = v / self.shots
        cost = np.sum(np.square(probabilities - self.expected_probabilities))
        return cost

    def generate(self, maxiter=500):
        rng = np.random.default_rng()
        thetas = rng.uniform(0, 2 * np.pi, self.num_qubits)

        spsa = SPSA(maxiter=maxiter)
        minima, _, _ = spsa.optimize(
            self.num_qubits, self._objective_fn, initial_point=thetas
        )

        counts = self._measure(minima)
        classes = [CLASSES[int(i, 2)] for i in reversed(sorted(counts, key=counts.get))]
        return classes
