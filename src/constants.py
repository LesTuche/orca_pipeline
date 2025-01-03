SSUBO = ["ssubo", "-m", "No"]
CHECK_STATES = ['COMPLETED', 'FAILED', 'CANCELLED', 'TIMEOUT']
DEFAULT_STEPS = ["OPT", "NEB_TS", "TS", "IRC","SP"]


MAX_TRIALS = 10
FREQ_THRESHOLD = -50
RETRY_DELAY = 60

SLURM_PARAMS_HIGH_MEM = {
    'nprocs': 24,
    'maxcore': 9000
}

SLURM_PARAMS_LOW_MEM = {
    'nprocs': 24,
    'maxcore': 2524
}

SLURM_PARAMS_XTB = {
    'nprocs': 12,
    'maxcore': 2000
}
