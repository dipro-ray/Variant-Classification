import argparse

def main(args):

	with open(args.filename) as infile:
		with open(args.filename + '_DP-' + args.depth + '_GQ-' + args.genotype_quality + '_MQ-' + args.mapping_quality + '_FS-' + args.fisher_strand + '_filtered.vcf', 'w') as outfile:
			args.depth = int(args.depth)
			args.genotype_quality = int(args.genotype_quality)
			#args.quality_by_depth = float(args.quality_by_depth)
			args.mapping_quality = float(args.mapping_quality)
			args.fisher_strand = float(args.fisher_strand)
			for line in infile:
				if line[0] == '#':
					outfile.write(line)
				if line[0] != '#':
					temp = line.strip('\n').split('\t')
					#print temp
					GT = temp[9].split(':')[0]
					AD = temp[9].split(':')[1]
					DP = int(temp[9].split(':')[2])
					GQ = int(temp[9].split(':')[3])
					#PL = temp[9].split(':')[4]
					QD = float(temp[7].split('QD=')[1].split(';')[0])
					MQ = float(temp[7].split('MQ=')[1].split(';')[0])
					FS = float(temp[7].split('FS=')[1].split(';')[0])
					if DP >= args.depth and GQ >= args.genotype_quality and FS <= args.fisher_strand and MQ >= args.mapping_quality:
						outfile.write(line)


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-f", "--filenamename", action="store", dest="filename")
	parser.add_argument("-DP", "--minimum_depth", action="store", dest="depth")
	parser.add_argument("-GQ", "--genotype_quality", action="store", dest="genotype_quality")
	#parser.add_argument("-QD", "--quality_by_depth", action="store", dest="quality_by_depth")
	parser.add_argument("-MQ", "--mapping_quality", action="store", dest="mapping_quality")
	parser.add_argument("-FS", "--fisher_strand", action="store", dest="fisher_strand")
	args = parser.parse_args()
	main(args)	

'''
python 20190731_quality_filter.py -f /Users/dipster/Downloads/Variants/test_428/011318_428A.snp.vcf -DP 20 -GQ 10 -MQ 59 -FS 60
'''
