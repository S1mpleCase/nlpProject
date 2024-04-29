from argparse import ArgumentParser, FileType
from configparser import ConfigParser
from pathlib import Path

'''
Citation:

Paper: Paper: Hardt, Daniel. "Ellipsis-dependent reasoning: a new challenge for large language models." 
The 61st Annual Meeting of the Association for Computational Linguistics. Association for Computational 
Linguistics, 2023.

Code: https://github.com/DanHardtDK/ellipsisGPT3
'''

arg_parser = ArgumentParser()
arg_parser.add_argument(
    'exampleFileList',
    help='list of files containing ellipsis patterns',
    type=FileType('r'),
)

arg_parser.add_argument(
    'sampleSize',
    help='number of examples to test',
    type=int,
    choices=[1, 10, 50, 100, 500],
)

arg_parser.add_argument(
    "iterations",
    help="number of iterations",
    type=int,
    choices=[1, 2, 3, 5, 10, 50],
    default=1
)    

ARGS = arg_parser.parse_args()

# check that exampleFileList is not empty
files = ARGS.exampleFileList.readlines()
if not files:
    raise ValueError('exampleFileList is empty')

# check that all files in exampleFileList exist and are json files
data_files = Path("data").glob("*.json")
EXAMPLE_FILES = [p for p in data_files if p.name in [f.strip("\n") for f in files]]
if len(EXAMPLE_FILES) != len(files):
    raise ValueError('exampleFileList contains invalid/missing file(s)')
    
