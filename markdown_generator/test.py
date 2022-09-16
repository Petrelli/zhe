from pybtex.database.input import bibtex
from pybtex.database import parse_file
import pybtex.database.input.bibtex
bib_data = parse_file('pub.bib')
print (bib_data)
