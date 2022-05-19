def convertMapping(mappingPath, mappingSep, outputSep):
    """Converts a mapping file type BBMap, to a type that TaxAM can understand.

    Parameters
    ----------
    mappingPath : str
        Mapping to file to be converted.
    mappingSep : str
        Separator for the BBMap mapping file.
    outputSep : str
        Separator for the TaxAM mapping file.

    Returns
    -------
    str
        String with all the line of the final file.
    """    
    file_lines = ''
    with open(mappingPath, 'r') as mapping_file:
        mapping_lines = mapping_file.readlines()
        for mapping_line in mapping_lines:
            line = mapping_line.split(mappingSep)
            # If the first character of the first element is not @
            if line[0][0] != '@':
                reads_id = line[0]
                contigs_id = line[2]
                file_lines += reads_id + outputSep + contigs_id + '\n'

    return file_lines

def storeTaxamMapping(file_lines, output_name):
    """_summary_

    Parameters
    ----------
    file_lines : str
        All the line of the final file.
    output_name : str
        Name of output file.
    """    
    import os
    from utils import ROOT_PATH
    # CHECKING IF OUTPUT FILE EXISTS
    OUT_PUT_FOLDER = ROOT_PATH + r'/output_converter/'
    if(not os.path.isdir(OUT_PUT_FOLDER)):
            os.mkdir(OUT_PUT_FOLDER)

    with open(OUT_PUT_FOLDER + output_name + '.txt', 'w') as output_file:
        output_file.write(file_lines)