#!/usr/bin/env python

import sys
import os
import re
import argparse
from get_all_pacbio import Collectpacbio

def check_argument(args):
	if not args.corrected:
		sys.stderr.write("there is no corrected pacbio fasta file! please check this file\n")
		print "python main.py -c <corrected pacbio fasta> -r <raw pacbio fasta> -o <output dir>\n";
		sys.exit()
	if not args.all:
		sys.stderr.write("there is no all pacbio fasta file beffor correcte !please check this file\n")
		print "python main.py -c <corrected pacbio fasta> -r <raw pacbio fasta> -o <output dir>\n";
		sys.exit()
	if not args.outdir:
		sys.stderr.write("there is no output dir!please check this file\n")
		print "python main.py -c <corrected pacbio fasta> -r <raw pacbio fasta> -o <output dir>\n";
		sys.exit()
def main():
	version="1.0"
	parser=argparse.ArgumentParser(
		description='this program is used to collect sequences uncollected seq by Illumina reads.')
	parser.add_argument(
		"-c","--corrected",help="pacbio reads corrected by SMRT")
	parser.add_argument(
		"-r","--all",help="all pacbio reads before corrected")
	parser.add_argument(
		"-o","--outdir",help="dir for output")
	args=parser.parse_args()
        check_argument(args)
        run_pathfilename=os.path.realpath(__file__)
        bin_path,run_filename=GetPathAndName(run_pathfilename)
	colectpac=Collectpacbio(args.corrected,args.all)
	not_corrected_pac_fas=colectpac.main()
	outfile=os.path.join(args.outdir,"not_corrected.pacbio.fa")
	out=open(outfile,'w')
	out.write(not_corrected_pac_fas)
	out.close()
	all_pacbio=os.path.join(args.outdir,"All.pacbio.correct.fa")
	syst="cat %s %s > %s" % (args.corrected,outfile,all_pacbio)
	os.system(syst)
def GetPathAndName(pathfilename):
	full_path=os.path.abspath(pathfilename)
	[path,filename]=os.path.split(full_path)
	path+='/'
	return path,filename
if __name__=="__main__":
	main()
