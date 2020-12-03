""" Program author name: Analia Treviño-Flitton
- The function of this program is to read in a FASTA format file, parse the comment lines or title lines, and saves the
  output to a text file.
- Returns: The sequence identifier, the length of the sequence & number of reads in a text file.
"""


##----------------------------------------------------------------------------------------------------------------------


def fasta_comment_parser(file_name):
    import re

    # Open & Read
    with open(file_name, 'r') as f:
        file = f.read()

    # Regex for Title Part 1
    title_pat = (r">(\w{3}\d)_")
    title_list = re.findall(title_pat, file)

    # Regex for Title Part 2
    title2_pat = (r"_(\w{6}\d{5})")
    title2_list = re.findall(title2_pat, file)

    # Regex for Length
    len_pat = (r"length=(\d+)")
    length = re.findall(len_pat, file)

    # Regex for Number Reads
    num_pat = (r"numreads=(\d+)")
    num = re.findall(num_pat, file)

    ## Write output file
    out_file = open("MIDS2_comment_out.txt", 'w')
    out_file.write("Written by Analia Treviño-Flitton\n\n")
    for i in range(len(num)):
        formatting = (title_list[i], '\t', title2_list[i], '\t\t', length[i], '\t\t', num[i], '\n')
        for x in formatting:
            out_file.write(str(x))

    ## Close output file
    out_file.close()


## Calling the function, specifying the file with the FASTA sequences in local directory
fasta_comment_parser("MID2_454AllContigs.fna")
