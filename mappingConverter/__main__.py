import os

from utils import validDelimiter
from utils.local_parses import local_parses
from utils.mapping_tools import convertMapping, storeTaxamMapping

# Local parsers
args = local_parses().__dict__.copy()

mapping_path = args['mapping_path']
output_name = args['output_name']
mappingSep = args['mapping_sep']
outputSep = args['output_sep']

mappingSep = validDelimiter(mappingSep)
outputSep = validDelimiter(outputSep)

file_lines = convertMapping(
    mapping_path,
    mappingSep,
    outputSep
)

storeTaxamMapping(
    file_lines,
    output_name
)
