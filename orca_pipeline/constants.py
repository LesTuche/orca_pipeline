SSUBO = ["ssubo"]
CHECK_STATES = ["COMPLETED", "FAILED", "CANCELLED", "TIMEOUT"]
DEFAULT_STEPS = ["OPT", "NEB_CI", "TS", "IRC", "SP"]


MAX_TRIALS = 1
FREQ_THRESHOLD = -50
RETRY_DELAY = 60


HIGH_MEM_THRESHOLD = 100


SLURM_PARAMS_BIG_HIGH_MEM = {"nprocs": 24, "maxcore": 10000}

SLURM_PARAMS_BIG_LOW_MEM = {"nprocs": 24, "maxcore": 2524}


SLURM_PARAMS_SMALL_LOW_MEM = {"nprocs": 24, "maxcore": 1000}

SLURM_PARAMS_SMALL_HIGH_MEM = {"nprocs": 24, "maxcore": 3500}


SLURM_PARAMS_XTB = {"nprocs": 12, "maxcore": 1500}


LOW_MEM_ELEMENTS = {
    "H",
    "He",
    "Li",
    "Be",
    "B",
    "C",
    "N",
    "O",
    "F",
    "Ne",
    "Na",
    "Mg",
    "Al",
    "Si",
    "P",
    "S",
    "Cl",
    "Ar",
    "K",
    "Ca",
}

HARTREE_TO_KCAL_MOL = 627.509
kb = 1.380648 * 10**-23  # J/K
