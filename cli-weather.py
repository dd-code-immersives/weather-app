import argparse
import sys
from weather import get_weather


def determine_flags(args):
    flags = []
    if args.temp:
        flags.append("temp")
    if args.humidity:
        flags.append("hum")
    if args.pressure:
        flags.append("pressure")
    if args.desc:
        flags.append("desc")

    return flags


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', type=argparse.FileType('r'),
                        default=sys.stdin)
    parser.add_argument('temp', action="store_true")
    parser.add_argument('humidity', action="store_true")
    parser.add_argument('pressure', action="store_true")
    parser.add_argument('desc', action="store_true")
    args = parser.parse_args()
    flags = determine_flags(args)
    for row in args.infile.readlines():
        row = row.strip()
        resp = get_weather(row, flags)
        print(resp)
