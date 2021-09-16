import argparse
import sys
from weather import get_weather

parser = argparse.ArgumentParser()
parser.add_argument("infile", type=argparse.FileType('r'), default=sys.stdin)
parser.add_argument('--temp', action='store_true')
parser.add_argument('--pressure', action='store_true')
parser.add_argument('--hum', action='store_true')
parser.add_argument('--desc', action='store_true')
args = parser.parse_args()

for row in args.infile.readlines():
    flags = []
    if args.temp:
        flags.append("temp")
    if args.pressure:
        flags.append("pressure")
    if args.hum:
        flags.append("hum")
    if args.desc:
        flags.append("desc")
    get_weather(row, flags)
