name = "aTools"

version = "2.03"

authors = [
    "Alan Camilo",
    "Michael Klimenko",
    "Jeremy Andriambolisoa",
]

description = \
    """
    aTools is the ultimate free utilities belt for Maya animators
    """


requires = [
    "python-3+",
    "maya-2025+"
]

uuid = "MKlimenko.aTools"

build_command = 'python {root}/build.py {install}'

def commands():
    env.PYTHONPATH.append("{root}/python")
