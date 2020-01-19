import pandas as pd
import argparse

#Main function
def main():
    '''
        Initialize argparse to get paramenters from CLI
        this will also generate a -h and --help switch to provide details for the command
    '''

    argparser = argparse.ArgumentParser(
        description = "A utility to convert csv file to json file"
        )

    # Add argument source this will be the source file to be convereted
    argparser.add_argument(
        'source',
         action = 'store',
         metavar = '<source>',
         help = 'source csv file'
        )

    # Add argument destination this will be the destination of the converted file
    argparser.add_argument(
        'destination',
         action = 'store',
         metavar = '<destination>',
         help = 'destination json file'
         )
    # parse those argument and convert them to an object
    args = argparser.parse_args()
    try:
        #read csv file and store it on a Dataframe
        csv = pd.read_csv(args.source)
        #convert the Dataframe to a json file
        csv.to_json(args.destination)

        print('success')
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
