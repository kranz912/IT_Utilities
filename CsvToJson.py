import pandas as pd
import argparse


argparser = argparse.ArgumentParser(
    description = "A utility to convert csv file to json file"
    )
argparser.add_argument(
    'source',
     action = 'store',
     metavar = '<source>',
     help = 'source csv file'
    )
argparser.add_argument(
    'destination',
     action = 'store',
     metavar = '<destination>',
     help = 'destination json file'
     )

args = argparser.parse_args()
print(args)
try:

    csv = pd.read_csv(args.source)
    csv.to_json(args.destination)

except Exception as e:
    print(e)
