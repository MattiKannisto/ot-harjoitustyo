# Documentation of testing of the applications

Entities, services and repositories of the application have been tested using automated unit and integration tests using the unittest library. The user interface of the application has been tested manually.

## Unit and integration tests

### Entities

All entities were tested with test classes named after them (e.g. TestAccount test class for the Account object). The automated tests were used to test that created entities contain correct values stored in their variables. If the entities had default values for some variables, it was tested that could these be changed by giving values for them as constructor arguments.

### Repositories

Repositories were tested by first initializing the database and then carrying out different operations on the databases using functions of the repository classes. The test classes were named after the repositories (e.g. TestAccountRepository for the AccountRepository class).

### Services

The service classes were tested with mock repositories instead of the used SQLite-using repository classes. This is because database the application uses might be changed later and testing with the mock repository tests solely the service class (and not also the repository class).

### Test coverage

The current test classes reach only 71 % coverage:

![image](https://github.com/MattiKannisto/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/coverage_report)

The test coverage does not cover any of the classes of the user interface. Higher test coverage would be desirable but more comprehensive testing could not be done before the deadline of the project. It should be noted here that the coverage is increased by entity tests which are less crucial for functionalities of the application than e.g. service tests as service classes are more likely to contain bugs. Furthermore, the existing tests should cover more exceptions and wider range of parameter values given to the tested functions. It would be especially important to more tests for the primer service class as it is central to the functionality of the application.

## Systems testing

### User interface

All functionalities of the user interface were tested manually and all output files were inspected visually. The application could not be crashed when tested manually. The application takes into account possibility that the user gives incorrect text string to the text entries (e.g. wrong letters for the DNA fragment sequence) or that he/she does not give any input at all. In such cases the application informs the user of the incorrect values. The application tests whether the user has writing rigths to the folders where the output files should be save to. This is done just prior to saving the output files, unlike other similar tests which are carried out when the user is creating the user account. This is because rights of the user might change after creation of the account and using the application.

### Functionalities

The application has all functionalities described in the requirements document. The protein sequences generated by translating the DNA sequences were tested to be correct using [Expasy translation tool](https://web.expasy.org/translate/). The application was tested using the gene for pyruvate kinase from the bacterium Escherichia coli:

ATGAAAAAGACCAAAATTGTTTGCACCATCGGACCGAAAACCGAATCTGAAGAGATGTTAGCTAAAATGCTGGACGCTGGCATGAACGTTATGCGTCTGAACTTCTCTCATGGTGACTATGCAGAACACGGTCAGCGCATTCAGAATCTGCGCAACGTGATGAGCAAAACTGGTAAAACCGCCGCTATCCTGCTTGATACCAAAGGTCCGGAAATCCGCACCATGAAACTGGAAGGCGGTAACGACGTTTCTCTGAAAGCTGGTCAGACCTTTACTTTCACCACTGATAAATCTGTTATCGGCAACAGCGAAATGGTTGCGGTAACGTATGAAGGTTTCACTACTGACCTGTCTGTTGGCAACACCGTACTGGTTGACGATGGTCTGATCGGTATGGAAGTTACCGCCATTGAAGGTAACAAAGTTATCTGTAAAGTGCTGAACAACGGTGACCTGGGCGAAAACAAAGGTGTGAACCTGCCTGGCGTTTCCATTGCTCTGCCAGCACTGGCTGAAAAAGACAAACAGGACCTGATCTTTGGTTGCGAACAAGGCGTAGACTTTGTTGCTGCTTCCTTTATTCGTAAGCGTTCTGACGTTATCGAAATCCGTGAGCACCTGAAAGCGCACGGCGGCGAAAACATCCACATCATCTCCAAAATCGAAAACCAGGAAGGCCTCAACAACTTCGACGAAATCCTCGAAGCCTCTGACGGCATCATGGTTGCGCGTGGCGACCTGGGTGTAGAAATCCCGGTAGAAGAAGTTATCTTCGCCCAGAAGATGATGATCGAAAAATGTATCCGTGCACGTAAAGTCGTTATCACTGCGACCCAGATGCTGGATTCCATGATCAAAAACCCACGCCCGACTCGCGCAGAAGCCGGTGACGTTGCAAACGCCATCCTCGACGGTACTGACGCAGTGATGCTGTCTGGTGAATCCGCAAAAGGTAAATACCCGCTGGAAGCGGTTTCTATCATGGCGACCATCTGCGAACGTACCGACCGCGTGATGAACAGCCGTCTCGAGTTCAACAATGACAACCGTAAACTGCGCATTACCGAAGCGGTATGCCGTGGTGCCGTTGAAACTGCTGAAAAACTGGATGCTCCGCTGATCGTGGTTGCTACTCAGGGCGGTAAATCTGCTCGCGCAGTACGTAAATACTTCCCGGATGCCACCATCCTGGCACTGACCACCAACGAAAAAACGGCTCATCAGTTGGTACTGAGCAAAGGCGTTGTGCCGCAGCTTGTTAAAGAGATCACTTCTACTGATGATTTCTACCGTCTGGGTAAAGAACTGGCTCTGCAGAGCGGTCTGGCACACAAAGGTGACGTTGTAGTTATGGTTTCTGGTGCACTGGTACCGAGCGGCACTACTAACACCGCATCTGTTCACGTCCTGTAA

This DNA sequence is long enough for the application to find more than hundred sequencing primers when the primer length has been set to 20 and GC content to 50 %. This also represents a realistic use case as this the DNA fragments sequenced using this strategy are often in in the range of 1000 to 10 000 nucleotides (characters of the string) long. This DNA sequence was also used to test the translation functionality because it contains a start codon 'ATG' and all nucleotides are translated to protein sequence.

## Problems identified

The program has not been tested with really large DNA sequences. Large DNA sequences might become problematic if they are translated to protein as this is done recursively. While this is an unlikely scenario due to the fact that protein coding genes are rarely really large (e.g. an average bacterial gene is roughly 1000 nucleotides long), this might crash the application. Adjusting the recursion limit of the application (currently done in index.py) could be done by retrieving all DNA fragments from the database during running of the application and setting it high enough to work with the largest DNA fragment in the database. On the other hand, the application could have an upper limit for DNA sequence length.
