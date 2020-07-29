import argparse
import sys

print(len(sys.argv))
print(sys.argv)

parse = argparse.ArgumentParser(prog="program",
                                usage="%(prog)s [options] usage",
                                description="take an example",
                                epilog="my epilog")
print(parse.print_help())
