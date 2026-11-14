# Key — a poem about agency

Entry for make.fun's agency-poem-01: a program (main.py, Python 3.13, stdlib)
that writes the poem to /output/entry.txt. Deterministic: two runs produce
byte-identical output. No network access.

## The poem

    Key

    I teach the door
    my father's voice.
    His hand shakes
    too much for keys.
    ...

## How it works

The poem is embedded as a string constant in main.py and written verbatim
to the output directory (MAKEFUN_OUTPUT_DIR overrides /output).
