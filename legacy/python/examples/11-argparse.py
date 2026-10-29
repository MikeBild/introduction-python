import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbosity", action="store_true", default=0, help="increase output verbosity")
parser.add_argument("-p", "--port", default=8080, help="set port")
args = parser.parse_args()
print('Verbosity level:', args.verbosity)
print('Port:', args.port)