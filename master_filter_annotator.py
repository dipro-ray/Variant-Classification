"""
Master VCF annotation script
"""

import subprocess
import argparse
from pprint import pprint


def main(args):
	# Proband file processing

	# Quality filtration
	#subprocess.call('python ' + args.script_directory + '20190731_quality_filter.py -f ' + args.proband_filename + ' -DP ' + args.depth + ' -GQ ' + args.genotype_quality + ' -MQ ' + args.mapping_quality + ' -FS ' + args.fisher_strand, shell=True)
	output_filename = args.proband_filename + '_DP-' + args.depth + '_GQ-' + args.genotype_quality + '_MQ-' + args.mapping_quality + '_FS-' + args.fisher_strand + '_filtered.vcf'

	# Internal cohort filtration
	print 'python ' + args.script_directory + '20190731_internal_cohort_filter.py -c ' + args.cohort_directory + ' -f ' + output_filename + ' -t snp -n ' + args.max_observation_number
	#subprocess.call('python ' + args.script_directory + '20190731_internal_cohort_filter.py -c ' + args.cohort_directory + ' -f ' + output_filename + ' -t snp -n ' + args.max_observation_number, shell=True) 
	output_filename = output_filename + '.icohort_' + args.max_observation_number + '_filter.vcf'

	# Gnomad genome/exome annotation
	print '\n'
	print 'python ' + args.script_directory + '20190730_gnomad_genome_exome_vcf_af_ac_annotator_args.py -f ' + output_filename
	print '\n'	
	#subprocess.call('python ' + args.script_directory + '20190730_gnomad_genome_exome_vcf_af_ac_annotator_args.py -f ' + output_filename, shell=True)
	output_filename = output_filename + '_gnomAD_ge_anno.vcf'

	# Inheritance annotation
	print '\n'
	print 'python ' + args.script_directory + '20190731_inheritance_annotate_dict.py -proband ' + output_filename + ' -unfiltered_mother ' + args.mother_filename + ' -unfiltered_father ' + args.father_filename
	print '\n'
	subprocess.call('python ' + args.script_directory + '20190731_inheritance_annotate_dict.py -proband ' + output_filename + ' -unfiltered_mother ' + args.mother_filename + ' -unfiltered_father ' + args.father_filename, shell=True)
	output_filename = output_filename + '.inheritance.vcf'

	# Frequency Filtration
	print '\n'
	print 'python ' + args.script_directory + '20190731_vcf_filter.py -f ' + output_filename + ' -an ' + args.allele_number + ' -af ' + args.allele_frequency
	print '\n'
	subprocess.call('python ' + args.script_directory + '20190731_vcf_filter.py -f ' + output_filename + ' -an ' + args.allele_number + ' -af ' + args.allele_frequency, shell=True)
	output_filename = output_filename + '.AN-' + args.allele_number + '_AF-' + args.allele_frequency + '_filtered.vcf'

	# Output data table
	print '\n'
	print 'python ' +args.script_directory + '20190731_vcf_to_table.py -f ' + output_filename
	print '\n'
	subprocess.call('python ' + args.script_directory + '20190731_vcf_to_table.py -f ' + output_filename, shell=True)


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-s", "--script_directory", action="store", dest="script_directory")
	parser.add_argument("-c", "--cohort_directory", action="store", dest="cohort_directory")	
	parser.add_argument("-proband", "--proband_filename", action="store", dest="proband_filename")
	parser.add_argument("-mother", "--mother_filename", action="store", dest="mother_filename")
	parser.add_argument("-father", "--father_filename", action="store", dest="father_filename")
	parser.add_argument("-DP", "--minimum_depth", action="store", dest="depth")
	parser.add_argument("-GQ", "--genotype_quality", action="store", dest="genotype_quality")
	parser.add_argument("-MQ", "--mapping_quality", action="store", dest="mapping_quality")
	parser.add_argument("-FS", "--fisher_strand", action="store", dest="fisher_strand")
	parser.add_argument("-n", "--max_observation_number", action="store", dest="max_observation_number")
	parser.add_argument("-af", "--allele_frequency", action="store", dest="allele_frequency")
	parser.add_argument("-an", "--allele_number", action="store", dest="allele_number")
	args = parser.parse_args()
	main(args)	

"""
python master_filter_annotator.py -s/Users/dipster/Downloads/vcf_annotator/ -c /Users/dipster/Downloads/Variants/cohort_directory/ -proband /Users/dipster/Downloads/Variants/test_428/011318_428A.indel.vcf -mother /Users/dipster/Downloads/Variants/test_428/011319_428B.indel.vcf -father /Users/dipster/Downloads/Variants/test_428/011320_428C.indel.vcf -DP 20 -GQ 10 -MQ 59 -FS 60 -n 3 -af 0.005 -an 5000
"""