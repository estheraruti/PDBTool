# PDBTool
This was the first large python program I wrote, in collaboration with Ravindu Lakshan and Yasmin El Houzaly.

The purpose of this program is to search a protein data bank for information about a given protein.
The possible commands that can be used are: 

'atomfreq' - searches the PDB file and outputs the atom symbol next to the amount of atoms of that type that are present in the protein.

'resfreq' -  this command searches the PDB file and displays the name of an amino acid next to the number of how many times it is present in the protein.

'reslength' -  this command searches the PDB file for the residue provided by the user and its three arguments and calculates the distance between each atom in the amino acid to output the maximum distance between each. If the user inputs the incorrect number of arguments or invalid arguments, an ERROR message will be displayed.

'tempcheck' -  this command takes the decimal value input by the user to search the PDB file and report the number of atoms present at that value, as well as the values above it and below it. If the user inputs the incorrect number of arguments or invalid arguments, an ERROR message will be displayed.

'occupancy' -  this command takes the decimal value input by the user to search the PDB file and report the frequency of atom occupancy present at that value, as well as the values above it and below it. If the user inputs the incorrect number of arguments or invalid arguments, an ERROR message will be displayed.

'quit' -  this command closes the program. If the user spells the command incorrectly and/or uses incorrect capitalization, an ERROR message will be displayed.

'help' - this command displays a list of possible commands that the program can execute, the arguments required for it to function, and their output.
