import argparse


def setup_parser():

    parser = argparse.ArgumentParser(prog="sh-engine",
                                     description="Sh-engine is a tool built to allow developers a fast and highly accessible search engine.",
                                     epilog="Thank you for supporting this project")
    
    parser.add_argument("query")

    return parser

def parse(parser):
    return parser.parse_args()

