#!/usr/bin/python3

import sys
import argon2

secret      = sys.argv[1].encode(sys.stdout.encoding)
salt        = sys.argv[2].encode(sys.stdout.encoding)
time_cost   = int(sys.argv[3])
mem_cost    = int(sys.argv[4])
parallelism = int(sys.argv[5])
hash_len    = int(sys.argv[6])

encoded_hash = argon2.low_level.hash_secret(
    secret,
    salt,
    time_cost=time_cost,
    memory_cost=2**mem_cost,
    parallelism=parallelism,
    hash_len=hash_len,
    type=argon2.low_level.Type.I)

print (encoded_hash.decode(sys.stdout.encoding))
