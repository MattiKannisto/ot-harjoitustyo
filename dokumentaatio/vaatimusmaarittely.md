# Requirements specification for the software DnaSequencingToolPython

## Intended use
The software allows the user to automatically generate primer pairs for sequencing reactions. The user gives the software the DNA sequence to be sequenced as text and the software generates a list of primer pairs suitable for sequencing the region of interest.

## Users
There will be only one group of users. If a need arises, more user groups will be added.

## Draft user interface


## Basic functionalities
### Before logging in to the system
- The user can create a new user account
  - The user name needs to be unique and needs to be at least 5 characters long
  - The password needs to be at least 10 characters long and at maximum 30 characters long
- The user can log in if he/she has created a user account

### After logging in to the system
- The user can add new gene sequences
  - A gene sequence needs to contain a name and a string of characters
    - Only characters 'A', 'T', 'G' and 'C' are allowed. If the gene sequence contains other characters, the gene cannot be added
  - The gene sequences will be stored in an SQL database
- The user can browse his/her gene sequences
- The user can export the gene in FASTA format
- The user can generate a list of primers for a selected gene sequence
  - The primers generated will contain an automatically generated name and a sequence corresponding to the region it anneals to in the gene
  - The primers will be added to the SQL database and mapped to the gene they are used to sequence
- The user can export primers generated for a gene in spreadsheet format
  - The spreadsheet will be formatted so that the user can copy paste the primer list into ordering sheet of primer synthesis company

## Advanced functionalities
Once all basic functionalities have been implemented with sufficient quality, following advanced functionalities will be implemented
- Logged in user can adjust the parameters used by the software in detection of suitable primer annealing sites
- Logged in user can visualize the DNA sequence and see where the generated primer pairs would bind
- Logged in user can add annotations to the genes to indicate different gene experssion control elements, protein coding sequences, *etc*.
- Logged in user can download DNA sequences from [GenBank](https://www.ncbi.nlm.nih.gov/genbank/) by giving its identifier