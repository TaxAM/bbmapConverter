# PYTHON INPORTS
import os

# LOCAL INPORTS
from utils import validDelimiter
from utils.local_parses import local_parses
from utils.mapping_tools import convertMapping, storeTaxamMapping, replaceCharacters

# Local parsers
args = local_parses().__dict__.copy()

mapping_path = args['mapping_path']
output_name = args['output_name']
mappingSep = args['mapping_sep']
outputSep = args['output_sep']

mappingSep = validDelimiter(mappingSep)
outputSep = validDelimiter(outputSep)

# LIST WITH ALL MAPPING FILE NAMES
mapping_files = os.listdir(mapping_path)

for counter, file in enumerate(mapping_files):
    # CONVERTS BBMAP FILE TO TAXAM MAPPING FILE
    file_lines = convertMapping(
        mappingPath = mapping_path + '/' + file,
        mappingSep = mappingSep,
        outputSep = outputSep
    )

    # CHECK IF USER SET OUTPUT NAME
    # IF SO, CREATES A FILE LIKE: mapping_<<output_name><counter>>
    # IF NOT, USES FILE NAME TO CREATES A FILE LIKE: 
    # mapping_<<file_name><counter>>
    if args['output_name']:
        file_output_name = 'mapping_' + \
            replaceCharacters(
                output_name,
                {
                    r'\\': '',
                    r'/': '',
                    r'_': '',
                }
            ) + str(counter)
    else:
        file_output_name = 'mapping_' + \
            replaceCharacters(
                file.split('.')[-2],
                {
                    r'\\': '',
                    r'/': '',
                    r'_': '',
                }
            )

    # STORES THE NEW MAPPING IN A TXT FILE IN <root_path>/output_converter/
    storeTaxamMapping(
        file_lines = file_lines,
        output_name = file_output_name
    )