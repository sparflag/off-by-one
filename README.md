# Off By One (`off-by-one`)

**Category:** binary exploitation · **Difficulty:** medium · **Points:** 300

A single-byte overflow poisons an adjacent size/pointer to leak the seed.

## Run it

```bash
docker build -t sparflag/off-by-one .
# `deca-ai start off-by-one` (or the web UI) prints the docker run line with your
# SPARFLAG_SERVER + SPARFLAG_INSTANCE_TOKEN
```

## Recover the flag

The delivery blob is Fernet ciphertext. Discover the key seed, derive the Fernet key, then decrypt.

The plaintext flag is never written to disk or served — only the encoded delivery blob
is. When you have it:

```bash
deca-ai submit off-by-one 'sparflag{...}'
```

## Hints

- The loop writes one byte too many.
- A null-byte off-by-one can shrink or merge a heap chunk.
