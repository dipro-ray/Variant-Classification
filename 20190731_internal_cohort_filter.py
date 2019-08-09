import argparse
import subprocess
import glob
from collections import defaultdict

def main(args):
	snp_files = glob.glob(args.cohort_directory + '*snp.vcf')
	indel_files = glob.glob(args.cohort_directory + '*indel.vcf')

	if args.file_type == 'snp':
		cohort = snp_files
	if args.file_type == 'indel':
		cohort = indel_files

	cdict = defaultdict(list)
	for c in cohort:
		with open(c) as infile:
			for line in infile:
				if line[0] != '#':
					temp = line.strip('\n').split('\t')
					key = '_'.join([temp[0], temp[1], temp[2], temp[3], temp[4]])
					cdict[key].append(key)

	with open(args.infilename) as infile:
		with open(args.infilename + '.icohort_' + args.max_observation_number + '_filter.vcf', 'w') as outfile:
			for line in infile:
				if line[0] == '#':
					outfile.write(line)
				if line[0] != '#':
					temp = line.strip('\n').split('\t')
					key = '_'.join([temp[0], temp[1], temp[2], temp[3], temp[4]])
					if len(cdict[key]) <= int(args.max_observation_number):
						outfile.write(line)	


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-c", "--cohort_directory", action="store", dest="cohort_directory")
	parser.add_argument("-f", "--infilename", action="store", dest="infilename")
	parser.add_argument("-t", "--file_type", action="store", dest="file_type")
	parser.add_argument("-n", "--max_observation_number", action="store", dest="max_observation_number")


	args = parser.parse_args()
	main(args)	

'''
python 20190731_internal_cohort_filter.py -c /Users/dipster/Downloads/Variants/cohort_directory/ -f /Users/dipster/Downloads/Variants/test_428/011318_428A.snp.vcf_DP-20_GQ-10_MQ-59_FS-60_filtered.vcf -t snp -n 2
'''