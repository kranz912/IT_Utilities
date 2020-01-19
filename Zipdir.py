from zipfile import  ZipFile
import argparse
import  os


'''
    Get list of filepaths from a directory
'''

def get_files_from_directory(directory):

    file_paths = []

    for root, dir, files in os.walk(directory):
        for filename in files:

            filepath = os.path.join(root,filename)
            file_paths.append(filepath)

    return file_paths


def main():

    '''
        Initialize argparse to get paramenters from CLI
        This will also generate a -h and --help switch to provide details for the command
    '''
    argparser = argparse.ArgumentParser(
        description= 'a utility that will convert a directory into a ZipFile'
    )

    argparser.add_argument(
     'source',
      action = 'store',
      metavar = '<source>',
      help = 'source directory directory path'
     )

    argparser.add_argument(
      'destination',
      action = 'store',
      metavar = '<destination>',
      help = 'destination directory path'
     )

    args = argparser.parse_args()


    files = get_files_from_directory(args.source)

    with ZipFile(args.destination, 'w') as zip:
        for file in files:
            print(file)
            zip.write(file)

    print('All files are ZipFile')

if __name__ == "__main__":
    main()
