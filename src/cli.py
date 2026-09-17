import argparse

def setup_parser():
    parser = argparse.ArgumentParser(
            prog="Sh-engine",
            description="Sh-engine is a wikipedia search engine built as a MVP of an internet search engine",
            epilog="Thank you for supporting this project")

    parser.add_argument("topic", action="store")
        
    return parser

def parse(parser):
    args = parser.parse_args()

    return args 
        

