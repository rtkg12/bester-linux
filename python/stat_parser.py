#!/usr/bin/env python
import sys
import json

def parse_cpu_line(vals):
    # Note there are more fields than this, but they are of no use to us
    keys = (
        "user", # normal processes executing in user mode
        "nice", # niced processes executing in user mode
        "system", # processes executing in kernel mode
        "idle", # processes currently idling
        "iowait", # processes waiting on io to complete
        "irq", # processes serving an interrupt call
        "softirq", # processes serving a soft interrupt call
    )
    return dict(zip(keys, vals))

# An example of how to calculate the amount a cpu is idleing for
def calc_idle_percent(cpu_info):
    total_ticks = sum(cpu_info.values())
    return (cpu_info["idle"] / total_ticks) * 100

# Parse the string value of a /proc/stat file
def parse_stat(input_str):
    lines = input_str.splitlines()
    out_dict = {}

    for line in lines:
        cols = line.split(" ")
        pred, info = cols[0], map(int, filter(lambda x: x != '', cols[1:]))
        out_dict[pred] = parse_cpu_line(info) if pred.startswith("cpu") else list(info)

    return out_dict

def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        with open(filename) as fi:
            out_dict = parse_stat(fi.read())
            print(json.dumps(out_dict, indent=4))
    else:
        raise Exception("Usage: pass stat file as first arg")

if __name__ == "__main__":
    main()
