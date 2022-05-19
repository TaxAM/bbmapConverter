import os
from utils import ROOT_PATH, validDelimiter
from utils.local_parses import local_parses

# Local parsers
args = local_parses().__dict__.copy()

mapping_path = args['mapping_path']
output_name = args['output_name']
mappingSep = args['mapping_sep']
outputSep = args['output_sep']

mappingSep = validDelimiter(mappingSep)
outputSep = validDelimiter(outputSep)

file_line = ''
with open(mapping_path, 'r') as contig_file:
    contig_lines = contig_file.readlines()
    for i in contig_lines:
        line = i.split(mappingSep)
        if line[0][0] != '@':
            file_line += line[0] + outputSep + line[2] + '\n'

# CHECKING IF OUTPUT FILE EXISTS
OUT_PUT_FOLDER = ROOT_PATH + r'/output_converter/'
if(not os.path.isdir(OUT_PUT_FOLDER)):
        os.mkdir(OUT_PUT_FOLDER)

with open(OUT_PUT_FOLDER + output_name + '.txt', 'w') as output_file:
    output_file.write(file_line)
