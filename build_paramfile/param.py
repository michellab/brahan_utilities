from __future__ import print_function
import sys
import re

pdbfile = sys.argv[1]
topolfile = sys.argv[2]
ffnb = sys.argv[3]
outputfile = pdbfile+'.param'
RFILE1 = open( pdbfile, "r")
RFILE2 = open( topolfile, "r")
RFILE3 = open( ffnb, "r")

lines =RFILE1.readlines()
lines2 =RFILE2.readlines()
lines3 = RFILE3.readlines()
WFILE = open( outputfile, "w" )


print("#index name type sigma epsilon charge", file=WFILE, end="\n")
for line in lines: # read line in pdb
	colpdb = line.split()
        if colpdb[0] == 'ATOM':
	   #print("index %s " % colpdb[1])
           atom_number = colpdb[1]
           resid = colpdb[5]
           atom_name = colpdb[2]
           for line2 in lines2: #read line2 in topology file
		if re.search( atom_name, line2) and re.search( resid, line2):
			coltop = line2.split()
                        # coltop[0]=atom_number, coltop[1]=atom_type, coltop[4]=atom_name, coltop[6]=atom_charge, coltop[5]= resid
                        atom_type = coltop[1]
			atom_charge = coltop[6]
			for line3 in lines3: # read line3 in ffnonbond file
				if re.search(atom_type+'     ', line3):
					colff = line3.split()
					sigma = colff[5]
					epsilon = colff[6]
		

           WFILE.write('{0:8s}  {1:8s}  {2:8s}  {3:8s}  {4:8s}   {5:8s}\n'.format(atom_number, atom_name, atom_type, sigma, epsilon, atom_charge ))
               #         print("atom number %s" % atom_number)


print("output file %s" % outputfile)

RFILE1.close()
WFILE.close()



