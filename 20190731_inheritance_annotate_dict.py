from collections import defaultdict
import argparse

def main(args):

	proband_file= args.proband_filename
	mother_file = args.unfiltered_mother_filename
	father_file = args.unfiltered_father_filename

	with open(proband_file+'.inheritance.vcf', 'w') as outfile:
		prod = defaultdict(list)
		prod2 = defaultdict(list)
		with open(proband_file, 'rU') as infile:
			for line in infile:
				if line[0] == '#' and line[1] == '#':
					outfile.write(line)

				if line[0] != '#':
					#print line
					temp = line.strip('\n').split('\t')

					info = temp[7].split(';')
					for sec in info:
						if 'compHet' in sec:
							compHet = sec.split('=')[1]

					proband_GT = temp[9].split(':')[0].split('/')

					ref = temp[3]
					rref = ref
					alt = temp[4]
					aalt = alt.split(',')

					if compHet == "True":
						aalt = aalt[int(proband_GT[0]) - 1]

						while True:
							if len(rref) == 1 or len(aalt) == 1:
								break
							if (rref[len(rref) - 1] == aalt[len(aalt) - 1]):
								rref = rref[:-1]
								aalt = aalt[:-1]
							else:
								break

						key = '_'.join([temp[0], temp[1], temp[2], rref, str(aalt)])
						prod2[key] = line
					

					rref = ref
					aalt = alt.split(',')
					aalt = aalt[int(proband_GT[1]) - 1]

					while True:
						if len(rref) == 1 or len(aalt) == 1:
							break
						if (rref[len(rref) - 1] == aalt[len(aalt) - 1]):
							rref = rref[:-1]
							aalt = aalt[:-1]
						else:
							break

					key = '_'.join([temp[0], temp[1], temp[2], rref, str(aalt)])
					prod[key] = line

		matd = defaultdict(list)
		matd2 = defaultdict(list)
		with open(mother_file, 'rU') as infile:
			for line in infile:
				if line[0] != '#':

					temp = line.strip('\n').split('\t')
					
					mother_GT = temp[9].split(':')[0].split('/')

					ref = temp[3]
					rref = ref
					alt = temp[4]
					aalt = alt.split(',')

					mCompHet = False
					try:
						aalt[1]
						mCompHet = True
						aalt = aalt[int(mother_GT[0]) - 1]

						while True:
							if len(rref) == 1 or len(aalt) == 1:
								break
							if (rref[len(rref) - 1] == aalt[len(aalt) - 1]):
								rref = rref[:-1]
								aalt = aalt[:-1]
							else:
								break

						key = '_'.join([temp[0], temp[1], temp[2], rref, str(aalt)])
						matd2[key] = line
					except IndexError:
						pass


					rref = ref
					aalt = alt.split(',')
					aalt = aalt[int(mother_GT[1]) - 1]

					while True:
						if len(rref) == 1 or len(aalt) == 1:
							break
						if (rref[len(rref) - 1] == aalt[len(aalt) - 1]):
							rref = rref[:-1]
							aalt = aalt[:-1]
						else:
							break

					key = '_'.join([temp[0], temp[1], temp[2], rref, str(aalt)])
					matd[key] = line

		patd = defaultdict(list)
		patd2 = defaultdict(list)
		with open(father_file, 'rU') as infile:
			for line in infile:
				if line[0] != '#':

					temp = line.strip('\n').split('\t')
					
					father_GT = temp[9].split(':')[0].split('/')

					ref = temp[3]
					rref = ref
					alt = temp[4]
					aalt = alt.split(',')

					fCompHet = False
					try:
						if aalt[1]:
							fCompHet = True
							aalt = aalt[int(father_GT[0]) - 1]

							while True:
								if len(rref) == 1 or len(aalt) == 1:
									break
								if (rref[len(rref) - 1] == aalt[len(aalt) - 1]):
									rref = rref[:-1]
									aalt = aalt[:-1]
								else:
									break

							key = '_'.join([temp[0], temp[1], temp[2], rref, str(aalt)])
							patd2[key] = line
					except IndexError:
						pass
					except ValueError:
						pass	
					
					rref = ref
					aalt = alt.split(',')
					try:
						aalt = aalt[int(father_GT[1]) - 1]
					except ValueError:
						pass

					#if father_GT[1] == '.':
					#	if father_GT[0] == father_GT[1]

					while True:
						if len(rref) == 1 or len(aalt) == 1:
							break
						if (rref[len(rref) - 1] == aalt[len(aalt) - 1]):
							rref = rref[:-1]
							aalt = aalt[:-1]
						else:
							break

					key = '_'.join([temp[0], temp[1], temp[2], rref, str(aalt)])
					patd[key] = line

		outfile.write('##INFO=<ID=Inheritance,Number=1,Type=String,Description="Inheritance_Pattern">\n')
		outfile.write('#CHROM	POS	ID	REF	ALT	QUAL	FILTER	INFO	FORMAT	8731835336\n')
		#print prod
		for e in prod:
			m = 0
			n = 0
			inheritance_pattern = ''
			# get proband genotype
			temp = prod[e].strip('\n').split('\t')
			info = temp[7].split(';')
			for sec in info:
				if 'compHet' in sec:
					compHet = sec.split('=')[1]

			proband_GT = temp[9].split(':')[0]
			if proband_GT.split('/')[0] != proband_GT.split('/')[1]:
				proband_zygosity = 'het'
				n = 1
			if proband_GT.split('/')[0] == proband_GT.split('/')[1]:
				proband_zygosity = 'hom'
				n = 1
			# if inherited only from mother - genotype agnostic
			if matd[e] and not patd[e]:
				if proband_zygosity == 'het':
					inheritance_pattern = 'Maternal'
					m = 1
				if proband_zygosity == 'hom':
					inheritance_pattern = 'Maternal+'
					m = 1

			# if inherited only from father - genotype agnostic
			if patd[e] and not matd[e]:
				if proband_zygosity == 'het':
					inheritance_pattern = 'Paternal'
					m = 2
				if proband_zygosity == 'hom':
					inheritance_pattern = 'Paternal+'
					m = 2
			# if present in mom and dad 
			if matd[e] and patd[e]:
				if proband_zygosity == 'hom':
					inheritance_pattern = 'Maternal & Paternal'
					m = 3
				if proband_zygosity == 'het':
					inheritance_pattern = 'Maternal or Paternal'
					m = 3
			
			if matd2[e]:
				if m == 2:
					if proband_zygosity == 'hom':
						inheritance_pattern = 'Maternal & Paternal'
						m = 3
					if proband_zygosity == 'het':
						inheritance_pattern = 'Maternal or Paternal'
						m = 3
				if m == 0:
					if proband_zygosity == 'het':
						inheritance_pattern = 'Maternal'
						m = 1
					if proband_zygosity == 'hom':
						inheritance_pattern = 'Maternal+'
						m = 1

			if patd2[e]:
				if m == 1:
					if proband_zygosity == 'hom':
						inheritance_pattern = 'Maternal & Paternal'
						m = 3
					if proband_zygosity == 'het':
						inheritance_pattern = 'Maternal or Paternal'
						m = 3
				if m == 0:
					if proband_zygosity == 'het':
						inheritance_pattern = 'Paternal'
						m = 2
					if proband_zygosity == 'hom':
						inheritance_pattern = 'Paternal+'
						m = 2
			
			if not matd[e] and not patd[e] and not matd2[e] and not patd2[e]:
				inheritance_pattern = 'Unknown'
				m = 4
				#print prod[e]


			if compHet == "False":
				temp[7] = temp[7] + ';Inheritance=' + inheritance_pattern
				outfile.write('\t'.join(temp)+'\n')
				#if m == 0 or n == 0:
					#print e
			else:
				inheritance_pattern1 = inheritance_pattern
				for f in prod2:
					if f.split('_')[0] == e.split('_')[0] and f.split('_')[1] == e.split('_')[1] and f.split('_')[2] == e.split('_')[2] and f.split('_')[3] and e.split('_')[3]:
					# if inherited only from mother - genotype agnostic
						m = 0
						if matd[f] and not patd[f]:
							inheritance_pattern = 'Maternal'
							m = 1

						# if inherited only from father - genotype agnostic
						if patd[f] and not matd[f]:
							inheritance_pattern = 'Paternal'
							m = 2

						# if present in mom and dad 
						if matd[f] and patd[f]:
							inheritance_pattern = 'Maternal or Paternal'
							m = 3
						
						if matd2[f]:
							if m == 2:
								inheritance_pattern = 'Maternal or Paternal'
								m = 3
							if m == 0:
								inheritance_pattern = 'Maternal'
								m = 1

						if patd2[f]:
							if m == 1:
								inheritance_pattern = 'Maternal or Paternal'
								m = 3
							if m == 0:
								inheritance_pattern = 'Paternal'
								m = 2
						
						if not matd[f] and not patd[f] and not matd2[f] and not patd2[f]:
							inheritance_pattern = 'Unknown'
							m = 4

				temp[7] = temp[7] + ';Inheritance=' + inheritance_pattern + ' and ' + inheritance_pattern1
				outfile.write('\t'.join(temp)+'\n')
				if m == 5 or n == 0:
					print prod2[f]

			#if m == 1:
			#	print inheritance_pattern
			#print '________\n'

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-proband", "--proband_filename", action="store", dest="proband_filename")
	parser.add_argument("-unfiltered_mother", "--mother_filename", action="store", dest="unfiltered_mother_filename")
	parser.add_argument("-unfiltered_father", "--father_filename", action="store", dest="unfiltered_father_filename")
	args = parser.parse_args()
	main(args)	


'''
python 20190731_inheritance_annotate_dict.py -proband /Users/dipster/Downloads/Variants/test_428/011318_428A.snp.vcf_DP-20_GQ-10_MQ-59_FS-60_filtered.vcf.icohort_2_filter.vcf_gnomAD_ge_anno.vcf -unfiltered_mother /Users/dipster/Downloads/Variants/test_428/011319_428B.snp.vcf -unfiltered_father /Users/dipster/Downloads/Variants/test_428/011320_428C.snp.vcf
'''

