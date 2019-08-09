import argparse


class Variant(object):
	def __init__(self):
		self.self = self
		self.chrom = ''
		self.position = ''
		self.ref = ''
		self.alt = ''
		self.transcript = ''
		self.exon = ''
		self.inheritance = ''
		self.gene = ''
		self.cdot = ''
		self.pdot = ''
		self.snpeff_pdot = ''
		self.consequence = ''
		self.effect = ''
		self.compHet = ''
		self.gAC = ''
		self.gAN = ''
		self.gAF = ''
		self.gHOM = ''
		self.eAC = ''
		self.eAN = ''
		self.eAF = ''
		self.eHOM = ''
		self.g2AC = ''
		self.g2AN = ''
		self.g2AF = ''
		self.g2HOM = ''
		self.e2AC = ''
		self.e2AN = ''
		self.e2AF = ''
		self.e2HOM = ''
		self.depth = ''
		self.genotype = ''


def main(args):


	with open(args.filename) as infile:
		with open(args.filename + '_table.txt', 'w') as outfile:
			variant_list = []
			for line in infile:
				if line[0] != '#':
					temp = line.strip('\n').split('\t')
					v = Variant()
					v.chrom = temp[0]
					v.position = temp[1]
					v.ref = temp[3]
					v.alt = temp[4]
					try:
						v.transcript = temp[7].split('SNPEFF_TRANSCRIPT_ID=')[1].split(';')[0]
					except IndexError:
						pass
					try:
						v.exon = temp[7].split('SNPEFF_EXON_ID=')[1].split(';')[0]
					except IndexError:
						pass					
					try:
						v.inheritance = temp[7].split('Inheritance=')[1]
					except IndexError:
						pass
					try:
						v.gene = temp[7].split('SNPEFF_GENE_NAME=')[1].split(';')[0]
					except IndexError:
						pass
					try:
						v.cdot = temp[7].split('AAChange=')[1].split(':')[1].split(';')[0]
					except IndexError:
						pass
					try:
						v.pdot = temp[7].split('AAChange=')[1].split(':')[2].split(';')[0]
					except IndexError:
						pass
					try:
						v.consequence = temp[7].split('SNPEFF_FUNCTIONAL_CLASS=')[1].split(';')[0]
					except IndexError:
						pass
					try:
						v.effect = temp[7].split('SNPEFF_EFFECT=')[1].split(';')[0]
					except IndexError:
						pass		
					try:
						v.compHet = temp[7].split('compHet=')[1].split(';')[0]
					except IndexError:
						pass	
					try:
						v.gAC = temp[7].split('gAC=')[1].split(';')[0]
					except IndexError:
						pass					
					try:
						v.gAN = temp[7].split('gAN=')[1].split(';')[0]
					except IndexError:
						pass						
					try:
						v.gAF = temp[7].split('gAF=')[1].split(';')[0]
					except IndexError:
						pass	
					try:
						v.gHOM = temp[7].split('gnhomalt=')[1].split(';')[0]
					except IndexError:
						pass	
					try:
						v.eAC = temp[7].split('eAC=')[1].split(';')[0]
					except IndexError:
						pass
					try:
						v.eAN = temp[7].split('eAN=')[1].split(';')[0]
					except IndexError:
						pass		
					try:
						v.eAF = temp[7].split('eAF=')[1].split(';')[0]
					except IndexError:
						pass	
					try:
						v.eHOM = temp[7].split('enhomalt=')[1].split(';')[0]
					except IndexError:
						pass	
					try:
						v.g2AC = temp[7].split('g2AC=')[1].split(';')[0]
					except IndexError:
						pass
					try:
						v.g2AN = temp[7].split('g2AN=')[1].split(';')[0]
					except IndexError:
						pass
					try:
						v.g2AF = temp[7].split('g2AF=')[1].split(';')[0]
					except IndexError:
						pass
					try:
						v.g2HOM = temp[7].split('g2nhomalt=')[1].split(';')[0]
					except IndexError:
						pass	
					try:
						v.e2AC = temp[7].split('e2AC=')[1].split(';')[0]
					except IndexError:
						pass
					try:
						v.e2AN = temp[7].split('e2AN=')[1].split(';')[0]
					except IndexError:
						pass		
					try:
						v.e2AF = temp[7].split('e2AF=')[1].split(';')[0]
					except IndexError:
						pass
					try:
						v.e2HOM = temp[7].split('e2nhomalt=')[1].split(';')[0]
					except IndexError:
						pass	
					try:
						v.depth = temp[9].split(':')[2]
					except IndexError:
						pass	
					try:
						v.genotype = "'" + temp[9].split(':')[0]
					except IndexError:
						pass
					variant_list.append(v)
			header = ['chrom', 'position', 'ref', 'alt', 'transcript', 'exon', 'inheritance', 'gene', 'cdot', 'pdot', 'snpeff_pdot', 'consequence', 'effect', 'compHet', 'gAC', 'gAN', 'gAF', 'gHOM', 'eAC', 'eAN', 'eAF', 'eHOM', 'g2AC', 'g2AN', 'g2AF', 'g2HOM', 'e2AC', 'e2AN', 'e2AF', 'e2HOM', 'depth', 'genotype']
			outfile.write('\t'.join(header) + '\n')
			for v in variant_list:
				outlist = [v.chrom, v.position, v.ref, v.alt, v.transcript, v.exon, v.inheritance, v.gene, v.cdot, v.pdot, v.snpeff_pdot, v.consequence, v.effect, v.compHet, v.gAC, v.gAN, v.gAF, v.gHOM, v.eAC, v.eAN, v.eAF, v.eHOM, v.g2AC, v.g2AN, v.g2AF, v.g2HOM, v.e2AC, v.e2AN, v.e2AF, v.e2HOM, v.depth, v.genotype]
				outfile.write('\t'.join(outlist) + '\n')


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-f", "--filenamename", action="store", dest="filename")
	args = parser.parse_args()
	main(args)

'''
python 20190731_vcf_to_table.py -f /Users/dipster/Downloads/Variants/test_428/011318_428A.snp.vcf_DP-20_GQ-10_MQ-59_FS-60_filtered.vcf.icohort_3_filter.vcf_gnomAD_ge_anno.vcf.inheritance.vcf.AC-3000_AF-0.002_filtered.vcf
'''

