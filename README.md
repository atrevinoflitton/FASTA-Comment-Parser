# FASTA-Comment-Parser
Parses the comment, or title, lines of a FASTA formatted sequence document and saves them to a text file in the local system.

*Only valid with FASTA files that include length and numreads in description*

Two versions of the function:

* *fasta_comment_parser(file_name)*: The function is hard-coded with the file : "MID2_454AllContigs.fna" 
and saves the results as: "MIDS2_comment_out.txt"

* *user_fasta_comment_parser()*: Prompts the user for the file name and allows the user to name the output file


<dl>
  <dt> Required files for program </dt>
  
  <dd>

--- 
FASTAcommentParser.py
* Uses one function to open, read, parse, and write the output file
---

---
MID2_454AllContigs.fna
* Test file with various FASTA sequences
---
</dt>
