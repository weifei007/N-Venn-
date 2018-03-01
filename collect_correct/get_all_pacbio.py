#!/usr/bin/evn python
#-*-coding:utf8-*-

import sys
import os
import re
import argparse

class Collectpacbio():
	def __init__(self,corrf,raw):
		self.corrf=corrf
		self.raw=raw
		cord=os.path.exists(corrf)
		rawd=os.path.exists(raw)
	def readfa(self,file):
		id_fa={}
		id=""
		with open(file,'r') as con:
			for line in con:
				if line[0]==">":
					lines=line.strip().split()
					id=re.sub(">","",lines[0])
					id_fa[id]=""
				#	print id
				else:
					id_fa[id]+=line.strip()
		return id_fa
	def _formatid(self,list):
		newlist=[]
		for id in list:
			idn=re.findall(r'(.*)\|[\d+|\.]',id)
			newlist.append(idn[0])
		return newlist
	def main(self):
		all_seq=""
		corf=self.corrf
		rawf=self.raw
		coridseq=self.readfa(corf)
		rawidseq=self.readfa(rawf)
		corids=coridseq.keys()
		coridnewset=set(self._formatid(corids))
		rawidset=set(rawidseq.keys())
		rlen=len(rawidset)
		clen=len(coridnewset)
		print "raw:",rlen,"correct:",clen
		nocorid=rawidset-coridnewset
		for id in nocorid:
			seq=rawidseq[id]
			all_seq+=">"+id+"\n"+seq+"\n"
		return all_seq
	
						
