# Name: ...
# CSE 140
# Homework 2: DNA analysis

# This program reads DNA sequencer output and computes statistics, such as
# the GC content.  Run it from the command line like this:
#   python dna_analysis.py myfile.fastq


###########################################################################
### Libraries
###

# The sys module supports reading files, command-line arguments, etc.
import sys


###########################################################################
### Read the nucleotides into a variable named seq
###

# You need to specify a file name
if len(sys.argv) < 2:
    print("You must supply a file name as an argument when running this program.")
    sys.exit(2)
# The file name specified on the command line, as a string.
filename = sys.argv[1]
# A file object from which data can be read.
inputfile = open(filename)

# All the nucleotides in the input file that have been read so far.
seq = ""
# The current line number (= the number of lines read so far).
linenum = 0


for line in inputfile:
    linenum = linenum + 1
    # if we are on the 2nd, 6th, 10th line...
    if linenum % 4 == 2:
        # Remove the newline characters from the end of the line
        line = line.rstrip()
        seq = seq + line


###########################################################################
### Compute statistics
###

# Total nucleotides seen so far.
total_count = 0
# Number of G and C nucleotides seen so far.
gc_count = 0
# Number of A and T nucleotides seen so far.
at_count = 0
# counts for all nucleotides
Acount = 0
Tcount = 0
Gcount = 0
Ccount = 0


# for each base pair in the string,
for bp in seq:
    # increment the total number of bps we've seen
    total_count = total_count + 1

    # check the bp and increment relevent counts.
    if bp == 'C':
        gc_count = gc_count + 1
        Ccount = Ccount + 1
    elif bp == 'G':
        gc_count = gc_count + 1
        Gcount = Gcount + 1
    elif bp == 'A':
        at_count = at_count + 1
        Acount = Acount + 1
    elif bp == 'T':
        at_count = at_count + 1
        Tcount = Tcount + 1


# divide the gc_count and at_count by the sum_count(sums of all nucleotides)
sum_count = Acount + Ccount + Gcount + Tcount
gc_content = float(gc_count) / sum_count
at_content = float(at_count) / sum_count

# Print relevent information on the sequence
print('GC-content:', gc_content)
print('AT-content:', at_content)
print('AT/GC Ratio:', at_count / gc_count)
if(gc_content > .6):
    print("high GC content")
elif(gc_content < .4):
    print("low GC content")
else:
    print("moderate GC content")
print("A nucleotides:", Acount)
print("C nucleotides:", Ccount)
print("G nucleotides:", Gcount)
print("T nucleotides:", Tcount)
print("Sum count:", sum_count)
print("Total number of bps:", total_count)
print("Length of the sequence:", len(seq))
