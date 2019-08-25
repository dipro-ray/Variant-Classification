import argparse

def main(args):

	with open(args.filename, 'rU') as infile:
		with open(args.filename+'.AN-' +args.allele_number + '_AF-' + args.allele_frequency + '_filtered.vcf', 'w') as outfile:
			for line in infile:
				
				if line[0] == '#':
					outfile.write(line)

				if line[0] != '#':
					temp = line.strip('\n').split('\t')
					chrom = temp[0]
					pos = temp[1]
					id = temp[2]
					ref = temp[3]
					alt = temp[4]
					qual = temp[5]
					filter = temp[6]
					info = temp[7]
					format = temp[8]
					extra = temp[9]

					infosec = info.split(';')

					#Since there are AN & AF earlier in info section, only looking for gnomad AN & AF (6 was picked arbitrarily after 1)
					compHet = ''
					for section in infosec:
						if "compHet" in section:
							compHet = section.split('=')[1]
						if "gAN=" in section and "MLEAN=" not in section:
							gAN = section
							gAN = gAN.split('=')[1]
						if "gAF=" in section and "MLEAF=" not in section:
							gAF = section
							gAF = gAF.split('=')[1]
						if "eAN=" in section and "MLEAN=" not in section:
							eAN = section
							eAN = eAN.split('=')[1]
						if "eAF=" in section and "MLEAF=" not in section:
							eAF = section
							eAF = eAF.split('=')[1]

						if "g2AN=" in section:
							g2AN = float(section.split('=')[1])
						if "g2AF=" in section:
							g2AF = float(section.split('=')[1])
						if "e2AN=" in section:
							e2AN = float(section.split('=')[1])
						if "e2AF=" in section:
							e2AF = float(section.split('=')[1])

					gAN = float(gAN)
					gAF = float(gAF)
					eAN = float(eAN)
					eAF = float(eAF)

					gPass = 1
					ePass = 1
					if gAF > float(args.allele_frequency) or gAN < int(args.allele_number):
						gPass = 0
						if gAN == 0:
							gPass = 1
					if eAF > float(args.allele_frequency) or eAN < int(args.allele_number):
						ePass = 0
						if eAN == 0:
							ePass = 1
					if compHet == "False":
						if gPass == 1 or (ePass == 1 and gPass == 1):
							#print chrom, pos, gPass, ePass, 'gAN='+ str(gAN), 'gAF='+str(gAF), 'eAN='+ str(eAN), 'eAF='+str(eAF)
							outfile.write('\t'.join([chrom, pos, id, ref, alt, qual, filter, info, format, extra])+'\n')
					else:
						g2Pass = 1
						e2Pass = 1
						if g2AF > float(args.allele_frequency) or g2AN < int(args.allele_number):
							g2Pass = 0
							if g2AN == 0:
								g2Pass = 1
						if e2AF > float(args.allele_frequency) or e2AN < int(args.allele_number):
							e2Pass = 0
							if e2AN == 0:
								e2Pass = 1
						if ((gPass == 1 or (ePass == 1 and gPass == 1)) or (g2Pass == 1 or (e2Pass == 1 and g2Pass == 1))):
							#print chrom, pos, gPass, ePass, 'gAN='+ str(gAN), 'gAF='+str(gAF), 'eAN='+ str(eAN), 'eAF='+str(eAF)
							outfile.write('\t'.join([chrom, pos, id, ref, alt, qual, filter, info, format, extra])+'\n')

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-f", "--filenamename", action="store", dest="filename")
	parser.add_argument("-af", "--allele_frequency", action="store", dest="allele_frequency")
	parser.add_argument("-an", "--allele_number", action="store", dest="allele_number")
	args = parser.parse_args()
	main(args)

'''
python 20190731_vcf_filter.py -f /Users/dipster/Downloads/Variants/test_428/011318_428A.snp.vcf_DP-20_GQ-10_MQ-59_FS-60_filtered.vcf.icohort_3_filter.vcf_gnomad_genome_exome_annotated.vcf.inheritance.vcf -an 5000 -af 0.005
'''
