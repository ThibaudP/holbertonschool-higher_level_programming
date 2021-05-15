#!/usr/bin/python3
"""read_write_heap"""
import sys
import os



def hack():
    """looks for a string in memory and replaces it with another"""
    if len(sys.argv) != 4:
        print("Usage: read_write_heap.py pid search_string replace_string")
        sys.exit(1)
    pid = sys.argv[1]
    search_string = sys.argv[2]
    new_string= sys.argv[3]

    with open("/proc/"+pid+"/maps", mode="r") as maps:
        for line in maps:
            toks = line.split()
            if "[heap]" in toks:
                break
        adresses = tok[0].split('-')
        start = int(adresses[0], base=16)
        end = int(adresses[1], base=16)







if __name__ == "__main__":
    hack()
