# first download gnoamd chrommosome 1 exome data vcf file
# after the first download is complete, download the .tbi file
# generate small vcf file for testing using command like: head -10000 011312_363A.snp.vcf > test.vcf


import os
import subprocess
from pprint import pprint
import argparse


def main(args):

	with open(args.infilename, 'rU') as infile:
		with open(args.infilename+'_gnomAD_ge_anno.vcf', 'w') as outfile:
			for line in infile:
				
				if line[0] == '#':
					if '##INFO=<ID=set,Number=1,Type=String,Description="Source VCF for the merged record in CombineVariants">' in line:
						outfile.write(line)
						outfile.write("""##INFO=<ID=compHet,Number=A,Type=String,Description="Whether variant is compound heterozygous">
##INFO=<ID=gAC,Number=A,Type=Integer,Description="Alternate allele count for samples">
##INFO=<ID=gAN,Number=1,Type=Integer,Description="Total number of alleles in samples">
##INFO=<ID=gAF,Number=A,Type=Float,Description="Alternate allele frequency in samples">
##INFO=<ID=gnhomalt,Number=A,Type=Integer,Description="Count of homozygous individuals in samples">
##INFO=<ID=gAC_afr,Number=A,Type=Integer,Description="Alternate allele count for samples of African-American/African ancestry">
##INFO=<ID=gAN_afr,Number=1,Type=Integer,Description="Total number of alleles in samples of African-American/African ancestry">
##INFO=<ID=gAF_afr,Number=A,Type=Float,Description="Alternate allele frequency in samples of African-American/African ancestry">
##INFO=<ID=gnhomalt_afr,Number=A,Type=Integer,Description="Count of homozygous individuals in samples of African-American/African ancestry">
##INFO=<ID=gAC_amr,Number=A,Type=Integer,Description="Alternate allele count for samples of Latino ancestry">
##INFO=<ID=gAN_amr,Number=1,Type=Integer,Description="Total number of alleles in samples of Latino ancestry">
##INFO=<ID=gAF_amr,Number=A,Type=Float,Description="Alternate allele frequency in samples of Latino ancestry">
##INFO=<ID=gnhomalt_amr,Number=A,Type=Integer,Description="Count of homozygous individuals in samples of Latino ancestry">
##INFO=<ID=gAC_eas,Number=A,Type=Integer,Description="Alternate allele count for samples of East Asian ancestry">
##INFO=<ID=gAN_eas,Number=1,Type=Integer,Description="Total number of alleles in samples of East Asian ancestry">
##INFO=<ID=gAF_eas,Number=A,Type=Float,Description="Alternate allele frequency in samples of East Asian ancestry">
##INFO=<ID=gnhomalt_eas,Number=A,Type=Integer,Description="Count of homozygous individuals in samples of East Asian ancestry">
##INFO=<ID=gAC_nfe,Number=A,Type=Integer,Description="Alternate allele count for samples of Non-Finnish European ancestry">
##INFO=<ID=gAN_nfe,Number=1,Type=Integer,Description="Total number of alleles in samples of Non-Finnish European ancestry">
##INFO=<ID=gAF_nfe,Number=A,Type=Float,Description="Alternate allele frequency in samples of Non-Finnish European ancestry">
##INFO=<ID=gnhomalt_nfe,Number=A,Type=Integer,Description="Count of homozygous individuals in samples of Non-Finnish European ancestry">
##INFO=<ID=gAC_fin,Number=A,Type=Integer,Description="Alternate allele count for samples of Finnish ancestry">
##INFO=<ID=gAN_fin,Number=1,Type=Integer,Description="Total number of alleles in samples of Finnish ancestry">
##INFO=<ID=gAF_fin,Number=A,Type=Float,Description="Alternate allele frequency in samples of Finnish ancestry">
##INFO=<ID=gnhomalt_fin,Number=A,Type=Integer,Description="Count of homozygous individuals in samples of Finnish ancestry">
##INFO=<ID=gAC_asj,Number=A,Type=Integer,Description="Alternate allele count for samples of Ashkenazi Jewish ancestry">
##INFO=<ID=gAN_asj,Number=1,Type=Integer,Description="Total number of alleles in samples of Ashkenazi Jewish ancestry">
##INFO=<ID=gAF_asj,Number=A,Type=Float,Description="Alternate allele frequency in samples of Ashkenazi Jewish ancestry">
##INFO=<ID=gnhomalt_asj,Number=A,Type=Integer,Description="Count of homozygous individuals in samples of Ashkenazi Jewish ancestry">
##INFO=<ID=gAC_sas,Number=A,Type=Integer,Description="Alternate allele count for samples of South Asian ancestry">
##INFO=<ID=gAN_sas,Number=1,Type=Integer,Description="Total number of alleles in samples of South Asian ancestry">
##INFO=<ID=gAF_sas,Number=A,Type=Float,Description="Alternate allele frequency in samples of South Asian ancestry">
##INFO=<ID=gnhomalt_sas,Number=A,Type=Integer,Description="Count of homozygous individuals in samples of South Asian ancestry">
##INFO=<ID=eAC,Number=A,Type=Integer,Description="Alternate allele count for samples">
##INFO=<ID=eAN,Number=1,Type=Integer,Description="Total number of alleles in samples">
##INFO=<ID=eAF,Number=A,Type=Float,Description="Alternate allele frequency in samples">
##INFO=<ID=enhomalt,Number=A,Type=Integer,Description="Count of homozygous individuals in samples">
##INFO=<ID=eAC_afr,Number=A,Type=Integer,Description="Alternate allele count for samples of African-American/African ancestry">
##INFO=<ID=eAN_afr,Number=1,Type=Integer,Description="Total number of alleles in samples of African-American/African ancestry">
##INFO=<ID=eAF_afr,Number=A,Type=Float,Description="Alternate allele frequency in samples of African-American/African ancestry">
##INFO=<ID=enhomalt_afr,Number=A,Type=Integer,Description="Count of homozygous individuals in samples of African-American/African ancestry">
##INFO=<ID=eAC_amr,Number=A,Type=Integer,Description="Alternate allele count for samples of Latino ancestry">
##INFO=<ID=eAN_amr,Number=1,Type=Integer,Description="Total number of alleles in samples of Latino ancestry">
##INFO=<ID=eAF_amr,Number=A,Type=Float,Description="Alternate allele frequency in samples of Latino ancestry">
##INFO=<ID=enhomalt_amr,Number=A,Type=Integer,Description="Count of homozygous individuals in samples of Latino ancestry">
##INFO=<ID=eAC_eas,Number=A,Type=Integer,Description="Alternate allele count for samples of East Asian ancestry">
##INFO=<ID=eAN_eas,Number=1,Type=Integer,Description="Total number of alleles in samples of East Asian ancestry">
##INFO=<ID=eAF_eas,Number=A,Type=Float,Description="Alternate allele frequency in samples of East Asian ancestry">
##INFO=<ID=enhomalt_eas,Number=A,Type=Integer,Description="Count of homozygous individuals in samples of East Asian ancestry">
##INFO=<ID=eAC_nfe,Number=A,Type=Integer,Description="Alternate allele count for samples of Non-Finnish European ancestry">
##INFO=<ID=eAN_nfe,Number=1,Type=Integer,Description="Total number of alleles in samples of Non-Finnish European ancestry">
##INFO=<ID=eAF_nfe,Number=A,Type=Float,Description="Alternate allele frequency in samples of Non-Finnish European ancestry">
##INFO=<ID=enhomalt_nfe,Number=A,Type=Integer,Description="Count of homozygous individuals in samples of Non-Finnish European ancestry">
##INFO=<ID=eAC_fin,Number=A,Type=Integer,Description="Alternate allele count for samples of Finnish ancestry">
##INFO=<ID=eAN_fin,Number=1,Type=Integer,Description="Total number of alleles in samples of Finnish ancestry">
##INFO=<ID=eAF_fin,Number=A,Type=Float,Description="Alternate allele frequency in samples of Finnish ancestry">
##INFO=<ID=enhomalt_fin,Number=A,Type=Integer,Description="Count of homozygous individuals in samples of Finnish ancestry">
##INFO=<ID=eAC_asj,Number=A,Type=Integer,Description="Alternate allele count for samples of Ashkenazi Jewish ancestry">
##INFO=<ID=eAN_asj,Number=1,Type=Integer,Description="Total number of alleles in samples of Ashkenazi Jewish ancestry">
##INFO=<ID=eAF_asj,Number=A,Type=Float,Description="Alternate allele frequency in samples of Ashkenazi Jewish ancestry">
##INFO=<ID=enhomalt_asj,Number=A,Type=Integer,Description="Count of homozygous individuals in samples of Ashkenazi Jewish ancestry">
##INFO=<ID=eAC_sas,Number=A,Type=Integer,Description="Alternate allele count for samples of South Asian ancestry">
##INFO=<ID=eAN_sas,Number=1,Type=Integer,Description="Total number of alleles in samples of South Asian ancestry">
##INFO=<ID=eAF_sas,Number=A,Type=Float,Description="Alternate allele frequency in samples of South Asian ancestry">
##INFO=<ID=enhomalt_sas,Number=A,Type=Integer,Description="Count of homozygous individuals in samples of South Asian ancestry">
##INFO=<ID=g2AC,Number=A,Type=Integer,Description="Alternate allele count for samples for second alternate allele">
##INFO=<ID=g2AN,Number=1,Type=Integer,Description="Total number of alleles in samples">
##INFO=<ID=g2AF,Number=A,Type=Float,Description="Alternate allele frequency in samples for second alternate allele">
##INFO=<ID=g2nhomalt,Number=A,Type=Integer,Description="Count of homozygous individuals in samples for second alternate allele">
##INFO=<ID=g2AC_afr,Number=A,Type=Integer,Description="Alternate allele count for samples of African-American/African ancestry for second alternate allele">
##INFO=<ID=g2AN_afr,Number=1,Type=Integer,Description="Total number of alleles in samples of African-American/African ancestry for second alternate allele">
##INFO=<ID=g2AF_afr,Number=A,Type=Float,Description="Alternate allele frequency in samples of African-American/African ancestry for second alternate allele">
##INFO=<ID=g2nhomalt_afr,Number=A,Type=Integer,Description="Count of homozygous individuals in samples of African-American/African ancestry for second alternate allele">
##INFO=<ID=g2AC_amr,Number=A,Type=Integer,Description="Alternate allele count for samples of Latino ancestry for second alternate allele">
##INFO=<ID=g2AN_amr,Number=1,Type=Integer,Description="Total number of alleles in samples of Latino ancestry for second alternate allele">
##INFO=<ID=g2AF_amr,Number=A,Type=Float,Description="Alternate allele frequency in samples of Latino ancestry for second alternate allele">
##INFO=<ID=g2nhomalt_amr,Number=A,Type=Integer,Description="Count of homozygous individuals in samples of Latino ancestry for second alternate allele">
##INFO=<ID=g2AC_eas,Number=A,Type=Integer,Description="Alternate allele count for samples of East Asian ancestry for second alternate allele">
##INFO=<ID=g2AN_eas,Number=1,Type=Integer,Description="Total number of alleles in samples of East Asian ancestry for second alternate allele">
##INFO=<ID=g2AF_eas,Number=A,Type=Float,Description="Alternate allele frequency in samples of East Asian ancestry for second alternate allele">
##INFO=<ID=g2nhomalt_eas,Number=A,Type=Integer,Description="Count of homozygous individuals in samples of East Asian ancestry for second alternate allele">
##INFO=<ID=g2AC_nfe,Number=A,Type=Integer,Description="Alternate allele count for samples of Non-Finnish European ancestry for second alternate allele">
##INFO=<ID=g2AN_nfe,Number=1,Type=Integer,Description="Total number of alleles in samples of Non-Finnish European ancestry for second alternate allele">
##INFO=<ID=g2AF_nfe,Number=A,Type=Float,Description="Alternate allele frequency in samples of Non-Finnish European ancestry for second alternate allele">
##INFO=<ID=g2nhomalt_nfe,Number=A,Type=Integer,Description="Count of homozygous individuals in samples of Non-Finnish European ancestry for second alternate allele">
##INFO=<ID=g2AC_fin,Number=A,Type=Integer,Description="Alternate allele count for samples of Finnish ancestry for second alternate allele">
##INFO=<ID=g2AN_fin,Number=1,Type=Integer,Description="Total number of alleles in samples of Finnish ancestry for second alternate allele">
##INFO=<ID=g2AF_fin,Number=A,Type=Float,Description="Alternate allele frequency in samples of Finnish ancestry for second alternate allele">
##INFO=<ID=g2nhomalt_fin,Number=A,Type=Integer,Description="Count of homozygous individuals in samples of Finnish ancestry for second alternate allele">
##INFO=<ID=g2AC_asj,Number=A,Type=Integer,Description="Alternate allele count for samples of Ashkenazi Jewish ancestry for second alternate allele">
##INFO=<ID=g2AN_asj,Number=1,Type=Integer,Description="Total number of alleles in samples of Ashkenazi Jewish ancestry for second alternate allele">
##INFO=<ID=g2AF_asj,Number=A,Type=Float,Description="Alternate allele frequency in samples of Ashkenazi Jewish ancestry for second alternate allele">
##INFO=<ID=g2nhomalt_asj,Number=A,Type=Integer,Description="Count of homozygous individuals in samples of Ashkenazi Jewish ancestry for second alternate allele">
##INFO=<ID=g2AC_sas,Number=A,Type=Integer,Description="Alternate allele count for samples of South Asian ancestry for second alternate allele">
##INFO=<ID=g2AN_sas,Number=1,Type=Integer,Description="Total number of alleles in samples of South Asian ancestry for second alternate allele">
##INFO=<ID=g2AF_sas,Number=A,Type=Float,Description="Alternate allele frequency in samples of South Asian ancestry for second alternate allele">
##INFO=<ID=g2nhomalt_sas,Number=A,Type=Integer,Description="Count of homozygous individuals in samples of South Asian ancestry for second alternate allele">
##INFO=<ID=e2AC,Number=A,Type=Integer,Description="Alternate allele count for samples for second alternate allele">
##INFO=<ID=e2AN,Number=1,Type=Integer,Description="Total number of alleles in samples">
##INFO=<ID=e2AF,Number=A,Type=Float,Description="Alternate allele frequency in samples for second alternate allele">
##INFO=<ID=e2nhomalt,Number=A,Type=Integer,Description="Count of homozygous individuals in samples for second alternate allele">
##INFO=<ID=e2AC_afr,Number=A,Type=Integer,Description="Alternate allele count for samples of African-American/African ancestry for second alternate allele">
##INFO=<ID=e2AN_afr,Number=1,Type=Integer,Description="Total number of alleles in samples of African-American/African ancestry for second alternate allele">
##INFO=<ID=e2AF_afr,Number=A,Type=Float,Description="Alternate allele frequency in samples of African-American/African ancestry for second alternate allele">
##INFO=<ID=e2nhomalt_afr,Number=A,Type=Integer,Description="Count of homozygous individuals in samples of African-American/African ancestry for second alternate allele">
##INFO=<ID=e2AC_amr,Number=A,Type=Integer,Description="Alternate allele count for samples of Latino ancestry for second alternate allele">
##INFO=<ID=e2AN_amr,Number=1,Type=Integer,Description="Total number of alleles in samples of Latino ancestry for second alternate allele">
##INFO=<ID=e2AF_amr,Number=A,Type=Float,Description="Alternate allele frequency in samples of Latino ancestry for second alternate allele">
##INFO=<ID=e2nhomalt_amr,Number=A,Type=Integer,Description="Count of homozygous individuals in samples of Latino ancestry for second alternate allele">
##INFO=<ID=e2AC_eas,Number=A,Type=Integer,Description="Alternate allele count for samples of East Asian ancestry for second alternate allele">
##INFO=<ID=e2AN_eas,Number=1,Type=Integer,Description="Total number of alleles in samples of East Asian ancestry for second alternate allele">
##INFO=<ID=e2AF_eas,Number=A,Type=Float,Description="Alternate allele frequency in samples of East Asian ancestry for second alternate allele">
##INFO=<ID=e2nhomalt_eas,Number=A,Type=Integer,Description="Count of homozygous individuals in samples of East Asian ancestry for second alternate allele">
##INFO=<ID=e2AC_nfe,Number=A,Type=Integer,Description="Alternate allele count for samples of Non-Finnish European ancestry for second alternate allele">
##INFO=<ID=e2AN_nfe,Number=1,Type=Integer,Description="Total number of alleles in samples of Non-Finnish European ancestry for second alternate allele">
##INFO=<ID=e2AF_nfe,Number=A,Type=Float,Description="Alternate allele frequency in samples of Non-Finnish European ancestry for second alternate allele">
##INFO=<ID=e2nhomalt_nfe,Number=A,Type=Integer,Description="Count of homozygous individuals in samples of Non-Finnish European ancestry for second alternate allele">
##INFO=<ID=e2AC_fin,Number=A,Type=Integer,Description="Alternate allele count for samples of Finnish ancestry for second alternate allele">
##INFO=<ID=e2AN_fin,Number=1,Type=Integer,Description="Total number of alleles in samples of Finnish ancestry for second alternate allele">
##INFO=<ID=e2AF_fin,Number=A,Type=Float,Description="Alternate allele frequency in samples of Finnish ancestry for second alternate allele">
##INFO=<ID=e2nhomalt_fin,Number=A,Type=Integer,Description="Count of homozygous individuals in samples of Finnish ancestry for second alternate allele">
##INFO=<ID=e2AC_asj,Number=A,Type=Integer,Description="Alternate allele count for samples of Ashkenazi Jewish ancestry for second alternate allele">
##INFO=<ID=e2AN_asj,Number=1,Type=Integer,Description="Total number of alleles in samples of Ashkenazi Jewish ancestry for second alternate allele">
##INFO=<ID=e2AF_asj,Number=A,Type=Float,Description="Alternate allele frequency in samples of Ashkenazi Jewish ancestry for second alternate allele">
##INFO=<ID=e2nhomalt_asj,Number=A,Type=Integer,Description="Count of homozygous individuals in samples of Ashkenazi Jewish ancestry for second alternate allele">
##INFO=<ID=e2AC_sas,Number=A,Type=Integer,Description="Alternate allele count for samples of South Asian ancestry for second alternate allele">
##INFO=<ID=e2AN_sas,Number=1,Type=Integer,Description="Total number of alleles in samples of South Asian ancestry for second alternate allele">
##INFO=<ID=e2AF_sas,Number=A,Type=Float,Description="Alternate allele frequency in samples of South Asian ancestry for second alternate allele">
##INFO=<ID=e2nhomalt_sas,Number=A,Type=Integer,Description="Count of homozygous individuals in samples of South Asian ancestry for second alternate allele">\n""")
					
					if line != '##INFO=<ID=set,Number=1,Type=String,Description="Source VCF for the merged record in CombineVariants">':
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

					aalt = alt.split(',')
					rref = ref

					GT = extra.split(':')[0]
					GT = GT.split('/')

					compHet = False
					if GT[0] != GT[1]:
						if '0' not in GT:
							compHet = True

					if compHet == True:
						aalt = aalt[int(GT[0]) - 1]

					if compHet == False:	
						aalt = aalt[int(GT[1]) - 1]
						
					infilestr = str(infile)
					if ('indel' in infilestr):
						while True:
							if len(rref) == 1 or len(aalt) == 1:
								break
							if (rref[len(rref) - 1] == aalt[len(aalt) - 1]):
								rref = rref[:-1]
								aalt = aalt[:-1]
							else:
								break


					#print 'tabix /Users/dipster/Downloads/gnomad.genomes.r2.1.1.sites.vcf.bgz '+chrom.replace('chr','')+':'+pos+'-'+pos
					
					try:
						gtbx = subprocess.check_output('PATH=$PATH:/Users/dipster/Downloads/htslib-1.8/; tabix /Users/dipster/Downloads/gnomad.genomes.r2.1.1.sites.vcf.bgz '+chrom.replace('chr','')+':'+pos+'-'+pos, shell=True)
					except subprocess.CalledProcessError:
						gtbx = ''
						while gtbx == '':
							gtbx = subprocess.check_output('PATH=$PATH:/Users/dipster/Downloads/htslib-1.8/; tabix /Users/dipster/Downloads/gnomad.genomes.r2.1.1.sites.vcf.bgz '+chrom.replace('chr','')+':'+pos+'-'+pos, shell=True)
					
					try:
						etbx = subprocess.check_output('PATH=$PATH:/Users/dipster/Downloads/htslib-1.8/; tabix /Users/dipster/Downloads/gnomad.exomes.r2.1.1.sites.vcf.bgz '+chrom.replace('chr','')+':'+pos+'-'+pos, shell=True)
					except subprocess.CalledProcessError:
						etbx = ''
						while etbx == '':
							etbx = subprocess.check_output('PATH=$PATH:/Users/dipster/Downloads/htslib-1.8/; tabix /Users/dipster/Downloads/gnomad.exomes.r2.1.1.sites.vcf.bgz '+chrom.replace('chr','')+':'+pos+'-'+pos, shell=True)

					gAC = 'gAC=0'
					gAN = 'gAN=0'
					gAF = 'gAF=0'
					gHOM = 'gnhomalt=0'

					gAC_afr = 'gAC_afr=0'
					gAN_afr = 'gAN_afr=0'
					gAF_afr = 'gAF_afr=0'
					gHOM_afr = 'gnhomalt_afr=0'

					gAC_eas = 'gAC_eas=0'
					gAN_eas = 'gAN_eas=0'
					gAF_eas = 'gAF_eas=0'
					gHOM_eas = 'gnhomalt_eas=0'

					gAC_amr = 'gAC_amr=0'
					gAN_amr = 'gAN_amr=0'
					gAF_amr = 'gAF_amr=0'
					gHOM_amr = 'gnhomalt_amr=0'

					gAC_nfe = 'gAC_nfe=0'
					gAN_nfe = 'gAN_nfe=0'
					gAF_nfe = 'gAF_nfe=0'
					gHOM_nfe = 'gnhomalt_nfe=0'

					gAC_fin = 'gAC_fin=0'
					gAN_fin = 'gAN_fin=0'
					gAF_fin = 'gAF_fin=0'
					gHOM_fin = 'gnhomalt_fin=0'

					gAC_asj = 'gAC_asj=0'
					gAN_asj = 'gAN_asj=0'
					gAF_asj = 'gAF_asj=0'
					gHOM_asj = 'gnhomalt_asj=0'

					gAC_sas = 'gAC_sas=0'
					gAN_sas = 'gAN_sas=0'
					gAF_sas = 'gAF_sas=0'
					gHOM_sas = 'gnhomalt_sas=0'

					eAC = 'eAC=0'
					eAN = 'eAN=0'
					eAF = 'eAF=0'
					eHOM = 'enhomalt=0'

					eAC_afr = 'eAC_afr=0'
					eAN_afr = 'eAN_afr=0'
					eAF_afr = 'eAF_afr=0'
					eHOM_afr = 'enhomalt_afr=0'

					eAC_eas = 'eAC_eas=0'
					eAN_eas = 'eAN_eas=0'
					eAF_eas = 'eAF_eas=0'
					eHOM_eas = 'enhomalt_eas=0'

					eAC_amr = 'eAC_amr=0'
					eAN_amr = 'eAN_amr=0'
					eAF_amr = 'eAF_amr=0'
					eHOM_amr = 'enhomalt_amr=0'

					eAC_nfe = 'eAC_nfe=0'
					eAN_nfe = 'eAN_nfe=0'
					eAF_nfe = 'eAF_nfe=0'
					eHOM_nfe = 'enhomalt_nfe=0'

					eAC_fin = 'eAC_fin=0'
					eAN_fin = 'eAN_fin=0'
					eAF_fin = 'eAF_fin=0'
					eHOM_fin = 'enhomalt_fin=0'

					eAC_asj = 'eAC_asj=0'
					eAN_asj = 'eAN_asj=0'
					eAF_asj = 'eAF_asj=0'
					eHOM_asj = 'enhomalt_asj=0'

					eAC_sas = 'eAC_sas=0'
					eAN_sas = 'eAN_sas=0'
					eAF_sas = 'eAF_sas=0'
					eHOM_sas = 'enhomalt_sas=0'

					try:
						item = gtbx.strip('\n').split('\n')
						for g in item:
							g = g.split('\t')
							#print len(g)
							#pprint(g)
							gchrom = 'chr:'+g[0]
							gpos = g[1]
							gid = g[2]
							gref = g[3]
							galt = g[4]
							gqual = g[5]
							gfilter = g[6]
							ginfo = g[7].split(';')
							#gformat = g[8]
							#gextra = g[9]
							if pos == gpos and rref == gref and aalt == galt:
								#pprint(g)
								#pprint(ginfo)
								gAC = 'g' + ginfo[0]
								gAN = 'g' + ginfo[1]
								gAF = 'g' + ginfo[2]

								for element in ginfo:

									if 'nhomalt=' in element and '_nhomalt' not in element:
										gHOM = 'g' + element

									if 'AC_afr=' in element and '_AC_afr' not in element:
										gAC_afr = 'g' + element
									if 'AN_afr=' in element and '_AN_afr' not in element:
										gAN_afr = 'g' + element
									if 'AF_afr=' in element and '_AF_afr' not in element:
										gAF_afr = 'g' + element
									if 'nhomalt_afr=' in element and '_nhomalt' not in element:
										gHOM_afr = 'g' + element

									if 'AC_eas=' in element and '_AC_eas' not in element:
										gAC_eas = 'g' + element
									if 'AN_eas=' in element and '_AN_eas' not in element:
										gAN_eas = 'g' + element
									if 'AF_eas=' in element and '_AF_eas' not in element:
										gAF_eas = 'g' + element
									if 'nhomalt_eas=' in element and '_nhomalt' not in element:
										gHOM_eas = 'g' + element

									if 'AC_amr=' in element and '_AC_amr' not in element:
										gAC_amr = 'g' + element
									if 'AN_amr=' in element and '_AN_amr' not in element:
										gAN_amr = 'g' + element
									if 'AF_amr=' in element and '_AF_amr' not in element:
										gAF_amr = 'g' + element
									if 'nhomalt_amr=' in element and '_nhomalt' not in element:
										gHOM_amr = 'g' + element

									if 'AC_nfe=' in element and '_AC_nfe' not in element:
										gAC_nfe = 'g' + element
									if 'AN_nfe=' in element and '_AN_nfe' not in element:
										gAN_nfe = 'g' + element
									if 'AF_nfe=' in element and '_AF_nfe' not in element:
										gAF_nfe = 'g' + element
									if 'nhomalt_nfe=' in element and '_nhomalt' not in element:
										gHOM_nfe = 'g' + element

									if 'AC_fin=' in element and '_AC_fin' not in element:
										gAC_fin= 'g' + element
									if 'AN_fin=' in element and '_AN_fin' not in element:
										gAN_fin = 'g' + element
									if 'AF_fin=' in element and '_AF_fin' not in element:
										gAF_fin = 'g' + element
									if 'nhomalt_fin=' in element and '_nhomalt' not in element:
										gHOM_fin = 'g' + element

									if 'AC_asj=' in element and '_AC_asj' not in element:
										gAC_asj = 'g' + element
									if 'AN_asj=' in element and '_AN_asj' not in element:
										gAN_asj = 'g' + element
									if 'AF_asj=' in element and '_AF_asj' not in element:
										gAF_asj = 'g' + element
									if 'nhomalt_asj=' in element and '_nhomalt' not in element:
										gHOM_asj = 'g' + element

									if 'AC_sas=' in element and '_AC_sas' not in element:
										gAC_sas = 'g' + element
									if 'AN_sas=' in element and '_AN_sas' not in element:
										gAN_sas = 'g' + element
									if 'AF_sas=' in element and '_AF_sas' not in element:
										gAF_sas = 'g' + element
									if 'nhomalt_sas=' in element and '_nhomalt' not in element:
										gHOM_sas = 'g' + element


								gnomad_genome_info = ';'.join([gAC, gAN, gAF, gAC_afr, gAN_afr, gAF_afr, gHOM_afr, gAC_eas, gAN_eas, gAF_eas, gHOM_eas, gAC_amr, gAN_amr, gAF_amr, gHOM_amr,gAC_nfe, gAN_nfe, gAF_nfe, gHOM_nfe, gAC_fin, gAN_fin, gAF_fin, gHOM_fin,gAC_asj, gAN_asj, gAF_asj, gHOM_asj ,gAC_sas, gAN_sas, gAF_sas, gHOM_sas])
								#print chrom, pos, id, ref, alt
								#print pprint(gnomad_genome_info)
								#print '\n'
								#print gtbx
								#quit()
								#print final_gnomad_info
								#print '----'
					except IndexError:
						#print 'caught exception'
						pass

					
					try:
						item = etbx.strip('\n').split('\n')
						for g in item:
							g = g.split('\t')
							#print len(g)
							#pprint(g)
							gchrom = 'chr:'+g[0]
							gpos = g[1]
							gid = g[2]
							gref = g[3]
							galt = g[4]
							gqual = g[5]
							gfilter = g[6]
							ginfo = g[7].split(';')
							#gformat = g[8]
							#gextra = g[9]
							if pos == gpos and rref == gref and aalt == galt:
								#pprint(g)
								#pprint(ginfo)
								eAC = 'e' + ginfo[0]
								eAN = 'e' + ginfo[1]
								eAF = 'e' + ginfo[2]
								

								for element in ginfo:

									if 'nhomalt=' in element and '_nhomalt' not in element:
										eHOM = 'e' + element

									if 'AC_afr=' in element and '_AC_afr' not in element:
										eAC_afr = 'e' + element
									if 'AN_afr=' in element and '_AN_afr' not in element:
										eAN_afr = 'e' + element
									if 'AF_afr=' in element and '_AF_afr' not in element:
										eAF_afr = 'e' + element
									if 'nhomalt_afr=' in element and '_nhomalt' not in element:
										eHOM_afr = 'e' + element

									if 'AC_eas=' in element and '_AC_eas' not in element:
										eAC_eas = 'e' + element
									if 'AN_eas=' in element and '_AN_eas' not in element:
										eAN_eas = 'e' + element
									if 'AF_eas=' in element and '_AF_eas' not in element:
										eAF_eas = 'e' + element
									if 'nhomalt_eas=' in element and '_nhomalt' not in element:
										eHOM_eas = 'e' + element

									if 'AC_amr=' in element and '_AC_amr' not in element:
										eAC_amr = 'e' + element
									if 'AN_amr=' in element and '_AN_amr' not in element:
										eAN_amr = 'e' + element
									if 'AF_amr=' in element and '_AF_amr' not in element:
										eAF_amr = 'e' + element
									if 'nhomalt_amr=' in element and '_nhomalt' not in element:
										eHOM_amr = 'e' + element

									if 'AC_nfe=' in element and '_AC_nfe' not in element:
										eAC_nfe = 'e' + element
									if 'AN_nfe=' in element and '_AN_nfe' not in element:
										eAN_nfe = 'e' + element
									if 'AF_nfe=' in element and '_AF_nfe' not in element:
										eAF_nfe = 'e' + element
									if 'nhomalt_nfe=' in element and '_nhomalt' not in element:
										eHOM_nfe = 'e' + element

									if 'AC_fin=' in element and '_AC_fin' not in element:
										eAC_fin= 'e' + element
									if 'AN_fin=' in element and '_AN_fin' not in element:
										eAN_fin = 'e' + element
									if 'AF_fin=' in element and '_AF_fin' not in element:
										eAF_fin = 'e' + element
									if 'nhomalt_fin=' in element and '_nhomalt' not in element:
										eHOM_fin = 'e' + element

									if 'AC_asj=' in element and '_AC_asj' not in element:
										eAC_asj = 'e' + element
									if 'AN_asj=' in element and '_AN_asj' not in element:
										eAN_asj = 'e' + element
									if 'AF_asj=' in element and '_AF_asj' not in element:
										eAF_asj = 'e' + element
									if 'nhomalt_asj=' in element and '_nhomalt' not in element:
										eHOM_asj = 'e' + element

									if 'AC_sas=' in element and '_AC_sas' not in element:
										eAC_sas = 'e' + element
									if 'AN_sas=' in element and '_AN_sas' not in element:
										eAN_sas = 'e' + element
									if 'AF_sas=' in element and '_AF_sas' not in element:
										eAF_sas = 'e' + element
									if 'nhomalt_sas=' in element and '_nhomalt' not in element:
										eHOM_sas = 'e' + element

								gnomad_exome_info = ';'.join([eAC, eAN, eAF, eHOM, eAC_afr, eAN_afr, eAF_afr, eHOM_afr, eAC_eas, eAN_eas, eAF_eas, eHOM_eas, eAC_amr, eAN_amr, eAF_amr, eHOM_amr,eAC_nfe, eAN_nfe, eAF_nfe, eHOM_nfe, eAC_fin, eAN_fin, eAF_fin, eHOM_fin,eAC_asj, eAN_asj, eAF_asj, eHOM_asj ,eAC_sas, eAN_sas, eAF_sas, eHOM_sas])
								
					except IndexError:
						#print 'caught exception'
						pass

					gnomad_genome_info = ';'.join([gAC, gAN, gAF, gHOM, gAC_afr, gAN_afr, gAF_afr, gHOM_afr, gAC_eas, gAN_eas, gAF_eas, gHOM_eas, gAC_amr, gAN_amr, gAF_amr, gHOM_amr, gAC_nfe, gAN_nfe, gAF_nfe, gHOM_nfe, gAC_fin, gAN_fin, gAF_fin, gHOM_fin, gAC_asj, gAN_asj, gAF_asj, gHOM_asj ,gAC_sas, gAN_sas, gAF_sas, gHOM_sas])
					gnomad_exome_info = ';'.join([eAC, eAN, eAF, eHOM, eAC_afr, eAN_afr, eAF_afr, eHOM_afr, eAC_eas, eAN_eas, eAF_eas, eHOM_eas, eAC_amr, eAN_amr, eAF_amr, eHOM_amr, eAC_nfe, eAN_nfe, eAF_nfe, eHOM_nfe, eAC_fin, eAN_fin, eAF_fin, eHOM_fin, eAC_asj, eAN_asj, eAF_asj, eHOM_asj ,eAC_sas, eAN_sas, eAF_sas, eHOM_sas])
					final_gnomad_info = gnomad_genome_info + ';' + gnomad_exome_info



					#outfile.write('\t'.join([chrom, pos, id, ref, alt, qual, filter, info+';compHet='+str(compHet)+';'+final_gnomad_info, format, extra])+'\n')

					if compHet == True:
						rref = ref
						aalt = alt.split(',')
						aalt = aalt[int(GT[1]) - 1]


						infilestr = str(infile)
						if ('indel' in infilestr):
							while True:
								if len(rref) == 1 or len(aalt) == 1:
									break
								if (rref[len(rref) - 1] == aalt[len(aalt) - 1]):
									rref = rref[:-1]
									aalt = aalt[:-1]
								else:
									break

						
						try:
							gtbx = subprocess.check_output('PATH=$PATH:/Users/dipster/Downloads/htslib-1.8/; tabix /Users/dipster/Downloads/gnomad.genomes.r2.1.1.sites.vcf.bgz '+chrom.replace('chr','')+':'+pos+'-'+pos, shell=True)
						except subprocess.CalledProcessError:
							gtbx = ''
							while gtbx == '':
								gtbx = subprocess.check_output('PATH=$PATH:/Users/dipster/Downloads/htslib-1.8/; tabix /Users/dipster/Downloads/gnomad.genomes.r2.1.1.sites.vcf.bgz '+chrom.replace('chr','')+':'+pos+'-'+pos, shell=True)
						
						try:
							etbx = subprocess.check_output('PATH=$PATH:/Users/dipster/Downloads/htslib-1.8/; tabix /Users/dipster/Downloads/gnomad.exomes.r2.1.1.sites.vcf.bgz '+chrom.replace('chr','')+':'+pos+'-'+pos, shell=True)
						except subprocess.CalledProcessError:
							etbx = ''
							while etbx == '':
								etbx = subprocess.check_output('PATH=$PATH:/Users/dipster/Downloads/htslib-1.8/; tabix /Users/dipster/Downloads/gnomad.exomes.r2.1.1.sites.vcf.bgz '+chrom.replace('chr','')+':'+pos+'-'+pos, shell=True)


						g2AC = 'g2AC=0'
						g2AN = 'g2AN=0'
						g2AF = 'g2AF=0'
						g2HOM = 'g2nhomalt=0'

						g2AC_afr = 'g2AC_afr=0'
						g2AN_afr = 'g2AN_afr=0'
						g2AF_afr = 'g2AF_afr=0'
						g2HOM_afr = 'g2nhomalt_afr=0'

						g2AC_eas = 'g2AC_eas=0'
						g2AN_eas = 'g2AN_eas=0'
						g2AF_eas = 'g2AF_eas=0'
						g2HOM_eas = 'g2nhomalt_eas=0'

						g2AC_amr = 'g2AC_amr=0'
						g2AN_amr = 'g2AN_amr=0'
						g2AF_amr = 'g2AF_amr=0'
						g2HOM_amr = 'g2nhomalt_amr=0'

						g2AC_nfe = 'g2AC_nfe=0'
						g2AN_nfe = 'g2AN_nfe=0'
						g2AF_nfe = 'g2AF_nfe=0'
						g2HOM_nfe = 'g2nhomalt_nfe=0'

						g2AC_fin = 'g2AC_fin=0'
						g2AN_fin = 'g2AN_fin=0'
						g2AF_fin = 'g2AF_fin=0'
						g2HOM_fin = 'g2nhomalt_fin=0'

						g2AC_asj = 'g2AC_asj=0'
						g2AN_asj = 'g2AN_asj=0'
						g2AF_asj = 'g2AF_asj=0'
						g2HOM_asj = 'g2nhomalt_asj=0'

						g2AC_sas = 'g2AC_sas=0'
						g2AN_sas = 'g2AN_sas=0'
						g2AF_sas = 'g2AF_sas=0'
						g2HOM_sas = 'g2nhomalt_sas=0'

						e2AC = 'e2AC=0'
						e2AN = 'e2AN=0'
						e2AF = 'e2AF=0'
						e2HOM = 'e2nhomalt=0'

						e2AC_afr = 'e2AC_afr=0'
						e2AN_afr = 'e2AN_afr=0'
						e2AF_afr = 'e2AF_afr=0'
						e2HOM_afr = 'e2nhomalt_afr=0'

						e2AC_eas = 'e2AC_eas=0'
						e2AN_eas = 'e2AN_eas=0'
						e2AF_eas = 'e2AF_eas=0'
						e2HOM_eas = 'e2nhomalt_eas=0'

						e2AC_amr = 'e2AC_amr=0'
						e2AN_amr = 'e2AN_amr=0'
						e2AF_amr = 'e2AF_amr=0'
						e2HOM_amr = 'e2nhomalt_amr=0'

						e2AC_nfe = 'e2AC_nfe=0'
						e2AN_nfe = 'e2AN_nfe=0'
						e2AF_nfe = 'e2AF_nfe=0'
						e2HOM_nfe = 'e2nhomalt_nfe=0'

						e2AC_fin = 'e2AC_fin=0'
						e2AN_fin = 'e2AN_fin=0'
						e2AF_fin = 'e2AF_fin=0'
						e2HOM_fin = 'e2nhomalt_fin=0'

						e2AC_asj = 'e2AC_asj=0'
						e2AN_asj = 'e2AN_asj=0'
						e2AF_asj = 'e2AF_asj=0'
						e2HOM_asj = 'e2nhomalt_asj=0'

						e2AC_sas = 'e2AC_sas=0'
						e2AN_sas = 'e2AN_sas=0'
						e2AF_sas = 'e2AF_sas=0'
						e2HOM_sas = 'e2nhomalt_sas=0'

						try:
							item = gtbx.strip('\n').split('\n')
							for g in item:
								g = g.split('\t')
								#print len(g)
								#pprint(g)
								gchrom = 'chr:'+g[0]
								gpos = g[1]
								gid = g[2]
								gref = g[3]
								galt = g[4]
								gqual = g[5]
								gfilter = g[6]
								ginfo = g[7].split(';')
								#gformat = g[8]
								#gextra = g[9]
								if pos == gpos and rref == gref and aalt == galt:
									#pprint(g)
									#pprint(ginfo)
									g2AC = 'g2' + ginfo[0]
									g2AN = 'g2' + ginfo[1]
									g2AF = 'g2' + ginfo[2]

									for element in ginfo:

										if 'nhomalt=' in element and '_nhomalt' not in element:
											g2HOM = 'g2' + element

										if 'AC_afr=' in element and '_AC_afr' not in element:
											g2AC_afr = 'g2' + element
										if 'AN_afr=' in element and '_AN_afr' not in element:
											g2AN_afr = 'g2' + element
										if 'AF_afr=' in element and '_AF_afr' not in element:
											g2AF_afr = 'g2' + element
										if 'nhomalt_afr=' in element and '_nhomalt' not in element:
											g2HOM_afr = 'g2' + element

										if 'AC_eas=' in element and '_AC_eas' not in element:
											g2AC_eas = 'g2' + element
										if 'AN_eas=' in element and '_AN_eas' not in element:
											g2AN_eas = 'g2' + element
										if 'AF_eas=' in element and '_AF_eas' not in element:
											g2AF_eas = 'g2' + element
										if 'nhomalt_eas=' in element and '_nhomalt' not in element:
											g2HOM_eas = 'g2' + element

										if 'AC_amr=' in element and '_AC_amr' not in element:
											g2AC_amr = 'g2' + element
										if 'AN_amr=' in element and '_AN_amr' not in element:
											g2AN_amr = 'g2' + element
										if 'AF_amr=' in element and '_AF_amr' not in element:
											g2AF_amr = 'g2' + element
										if 'nhomalt_amr=' in element and '_nhomalt' not in element:
											g2HOM_amr = 'g2' + element

										if 'AC_nfe=' in element and '_AC_nfe' not in element:
											g2AC_nfe = 'g2' + element
										if 'AN_nfe=' in element and '_AN_nfe' not in element:
											g2AN_nfe = 'g2' + element
										if 'AF_nfe=' in element and '_AF_nfe' not in element:
											g2AF_nfe = 'g2' + element
										if 'nhomalt_nfe=' in element and '_nhomalt' not in element:
											g2HOM_nfe = 'g2' + element

										if 'AC_fin=' in element and '_AC_fin' not in element:
											g2AC_fin= 'g2' + element
										if 'AN_fin=' in element and '_AN_fin' not in element:
											g2AN_fin = 'g2' + element
										if 'AF_fin=' in element and '_AF_fin' not in element:
											g2AF_fin = 'g2' + element
										if 'nhomalt_fin=' in element and '_nhomalt' not in element:
											g2HOM_fin = 'g2' + element

										if 'AC_asj=' in element and '_AC_asj' not in element:
											g2AC_asj = 'g2' + element
										if 'AN_asj=' in element and '_AN_asj' not in element:
											g2AN_asj = 'g2' + element
										if 'AF_asj=' in element and '_AF_asj' not in element:
											g2AF_asj = 'g2' + element
										if 'nhomalt_asj=' in element and '_nhomalt' not in element:
											g2HOM_asj = 'g2' + element

										if 'AC_sas=' in element and '_AC_sas' not in element:
											g2AC_sas = 'g2' + element
										if 'AN_sas=' in element and '_AN_sas' not in element:
											g2AN_sas = 'g2' + element
										if 'AF_sas=' in element and '_AF_sas' not in element:
											g2AF_sas = 'g2' + element
										if 'nhomalt_sas=' in element and '_nhomalt' not in element:
											g2HOM_sas = 'g2' + element


									gnomad_genome_info2 = ';'.join([g2AC, g2AN, g2AF, g2AC_afr, g2AN_afr, g2AF_afr, g2HOM_afr, g2AC_eas, g2AN_eas, g2AF_eas, g2HOM_eas, g2AC_amr, g2AN_amr, g2AF_amr, g2HOM_amr,g2AC_nfe, g2AN_nfe, g2AF_nfe, g2HOM_nfe, g2AC_fin, g2AN_fin, g2AF_fin, g2HOM_fin,g2AC_asj, g2AN_asj, g2AF_asj, g2HOM_asj ,g2AC_sas, g2AN_sas, g2AF_sas, g2HOM_sas])
									#print chrom, pos, id, ref, alt
									#print pprint(gnomad_genome_info)
									#print '\n'
									#print gtbx
									#quit()
									#print final_gnomad_info
									#print '----'
						except IndexError:
							#print 'caught exception'
							pass

						
						try:
							item = etbx.strip('\n').split('\n')
							for g in item:
								g = g.split('\t')
								#print len(g)
								#pprint(g)
								gchrom = 'chr:'+g[0]
								gpos = g[1]
								gid = g[2]
								gref = g[3]
								galt = g[4]
								gqual = g[5]
								gfilter = g[6]
								ginfo = g[7].split(';')
								#gformat = g[8]
								#gextra = g[9]
								if pos == gpos and rref == gref and aalt == galt:
									#pprint(g)
									#pprint(ginfo)
									e2AC = 'e2' + ginfo[0]
									e2AN = 'e2' + ginfo[1]
									e2AF = 'e2' + ginfo[2]
									

									for element in ginfo:

										if 'nhomalt=' in element and '_nhomalt' not in element:
											e2HOM = 'e2' + element

										if 'AC_afr=' in element and '_AC_afr' not in element:
											e2AC_afr = 'e2' + element
										if 'AN_afr=' in element and '_AN_afr' not in element:
											e2AN_afr = 'e2' + element
										if 'AF_afr=' in element and '_AF_afr' not in element:
											e2AF_afr = 'e2' + element
										if 'nhomalt_afr=' in element and '_nhomalt' not in element:
											e2HOM_afr = 'e2' + element

										if 'AC_eas=' in element and '_AC_eas' not in element:
											e2AC_eas = 'e2' + element
										if 'AN_eas=' in element and '_AN_eas' not in element:
											e2AN_eas = 'e2' + element
										if 'AF_eas=' in element and '_AF_eas' not in element:
											e2AF_eas = 'e2' + element
										if 'nhomalt_eas=' in element and '_nhomalt' not in element:
											e2HOM_eas = 'e2' + element

										if 'AC_amr=' in element and '_AC_amr' not in element:
											e2AC_amr = 'e2' + element
										if 'AN_amr=' in element and '_AN_amr' not in element:
											e2AN_amr = 'e2' + element
										if 'AF_amr=' in element and '_AF_amr' not in element:
											e2AF_amr = 'e2' + element
										if 'nhomalt_amr=' in element and '_nhomalt' not in element:
											e2HOM_amr = 'e2' + element

										if 'AC_nfe=' in element and '_AC_nfe' not in element:
											e2AC_nfe = 'e2' + element
										if 'AN_nfe=' in element and '_AN_nfe' not in element:
											e2AN_nfe = 'e2' + element
										if 'AF_nfe=' in element and '_AF_nfe' not in element:
											e2AF_nfe = 'e2' + element
										if 'nhomalt_nfe=' in element and '_nhomalt' not in element:
											e2HOM_nfe = 'e2' + element

										if 'AC_fin=' in element and '_AC_fin' not in element:
											e2AC_fin= 'e2' + element
										if 'AN_fin=' in element and '_AN_fin' not in element:
											e2AN_fin = 'e2' + element
										if 'AF_fin=' in element and '_AF_fin' not in element:
											e2AF_fin = 'e2' + element
										if 'nhomalt_fin=' in element and '_nhomalt' not in element:
											e2HOM_fin = 'e2' + element

										if 'AC_asj=' in element and '_AC_asj' not in element:
											e2AC_asj = 'e2' + element
										if 'AN_asj=' in element and '_AN_asj' not in element:
											e2AN_asj = 'e2' + element
										if 'AF_asj=' in element and '_AF_asj' not in element:
											e2AF_asj = 'e2' + element
										if 'nhomalt_asj=' in element and '_nhomalt' not in element:
											e2HOM_asj = 'e2' + element

										if 'AC_sas=' in element and '_AC_sas' not in element:
											e2AC_sas = 'e2' + element
										if 'AN_sas=' in element and '_AN_sas' not in element:
											e2AN_sas = 'e2' + element
										if 'AF_sas=' in element and '_AF_sas' not in element:
											e2AF_sas = 'e2' + element
										if 'nhomalt_sas=' in element and '_nhomalt' not in element:
											e2HOM_sas = 'e2' + element

									gnomad_exome_info2 = ';'.join([e2AC, e2AN, e2AF, e2HOM, e2AC_afr, e2AN_afr, e2AF_afr, e2HOM_afr, e2AC_eas, e2AN_eas, e2AF_eas, e2HOM_eas, e2AC_amr, e2AN_amr, e2AF_amr, e2HOM_amr,e2AC_nfe, e2AN_nfe, e2AF_nfe, e2HOM_nfe, e2AC_fin, e2AN_fin, e2AF_fin, e2HOM_fin,e2AC_asj, e2AN_asj, e2AF_asj, e2HOM_asj ,e2AC_sas, e2AN_sas, e2AF_sas, e2HOM_sas])
									
						except IndexError:
							#print 'caught exception'
							pass

						gnomad_genome_info2 = ';'.join([g2AC, g2AN, g2AF, g2HOM, g2AC_afr, g2AN_afr, g2AF_afr, g2HOM_afr, g2AC_eas, g2AN_eas, g2AF_eas, g2HOM_eas, g2AC_amr, g2AN_amr, g2AF_amr, g2HOM_amr, g2AC_nfe, g2AN_nfe, g2AF_nfe, g2HOM_nfe, g2AC_fin, g2AN_fin, g2AF_fin, g2HOM_fin, g2AC_asj, g2AN_asj, g2AF_asj, g2HOM_asj ,g2AC_sas, g2AN_sas, g2AF_sas, g2HOM_sas])
						gnomad_exome_info2 = ';'.join([e2AC, e2AN, e2AF, e2HOM, e2AC_afr, e2AN_afr, e2AF_afr, e2HOM_afr, e2AC_eas, e2AN_eas, e2AF_eas, e2HOM_eas, e2AC_amr, e2AN_amr, e2AF_amr, e2HOM_amr, e2AC_nfe, e2AN_nfe, e2AF_nfe, e2HOM_nfe, e2AC_fin, e2AN_fin, e2AF_fin, e2HOM_fin, e2AC_asj, e2AN_asj, e2AF_asj, e2HOM_asj ,e2AC_sas, e2AN_sas, e2AF_sas, e2HOM_sas])
						final_gnomad_info2 = gnomad_genome_info2 + ';' + gnomad_exome_info2


					if compHet == True:
						outfile.write('\t'.join([chrom, pos, id, ref, alt, qual, filter, info+';compHet='+str(compHet)+';'+final_gnomad_info+';'+final_gnomad_info2, format, extra])+'\n')
					else:
						outfile.write('\t'.join([chrom, pos, id, ref, alt, qual, filter, info+';compHet='+str(compHet)+';'+final_gnomad_info, format, extra])+'\n')





if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-f", "--infilename", action="store", dest="infilename")
	args = parser.parse_args()
	main(args)	
		

'''
python 20190730_gnomad_genome_exome_vcf_af_ac_annotator_args.py -f /Users/dipster/Downloads/Variants/test_428/011318_428A.snp.vcf_DP-20_GQ-10_MQ-59_FS-60_filtered.vcf.icohort_2_filter.vcf
11	17396807	.	G	A	302.46	PASS	AC=1;AF=3.22935e-05;AN=30966;BaseQRankSum=1.44000e+00;ClippingRankSum=3.82000e-01;DP=651226;FS=5.28700e+00;InbreedingCoeff=1.40000e-03;MQ=6.00000e+01;MQRankSum=2.37000e-01;QD=9.17000e+00;ReadPosRankSum=7.47000e-01;SOR=1.20600e+00;VQSLOD=1.49000e+01;VQSR_culprit=MQ;GQ_HIST_ALT=0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|1;DP_HIST_ALT=0|0|0|0|0|0|1|0|0|0|0|0|0|0|0|0|0|0|0|0;AB_HIST_ALT=0|0|0|0|0|0|0|0|1|0|0|0|0|0|0|0|0|0|0|0;GQ_HIST_ALL=3|0|1|2|11|11|39|72|96|289|479|320|1597|409|1406|549|1971|246|1804|6191;DP_HIST_ALL=0|9|104|678|2330|3099|3724|4561|859|88|19|10|4|4|3|0|2|1|0|1;AB_HIST_ALL=0|0|0|0|0|0|0|0|1|0|0|0|0|0|0|0|0|0|0|0;AC_Male=1;AC_Female=0;AN_Male=17116;AN_Female=13850;AF_Male=5.84249e-05;AF_Female=0.00000e+00;GC_Male=8557,1,0;GC_Female=6925,0,0;GC_raw=15495,1,0;AC_raw=1;AN_raw=30992;GC=15482,1,0;AF_raw=3.22664e-05;Hom_AFR=0;Hom_AMR=0;Hom_ASJ=0;Hom_EAS=0;Hom_FIN=0;Hom_NFE=0;Hom_OTH=0;Hom=0;Hom_raw=0;AC_AFR=1;AC_AMR=0;AC_ASJ=0;AC_EAS=0;AC_FIN=0;AC_NFE=0;AC_OTH=0;AN_AFR=8724;AN_AMR=838;AN_ASJ=300;AN_EAS=1622;AN_FIN=3494;AN_NFE=15006;AN_OTH=982;AF_AFR=1.14626e-04;AF_AMR=0.00000e+00;AF_ASJ=0.00000e+00;AF_EAS=0.00000e+00;AF_FIN=0.00000e+00;AF_NFE=0.00000e+00;AF_OTH=0.00000e+00;POPMAX=AFR;AC_POPMAX=1;AN_POPMAX=8724;AF_POPMAX=1.14626e-04;DP_MEDIAN=33;DREF_MEDIAN=3.16228e-37;GQ_MEDIAN=99;AB_MEDIAN=4.24242e-01;AS_RF=9.81621e-01;AS_FilterStatus=PASS;CSQ=A|3_prime_UTR_variant|MODIFIER|NCR3LG1|ENSG00000188211|Transcript|ENST00000338965|protein_coding|5/5||ENST00000338965.4:c.*2748G>A||4357||||||1||1||SNV|1|HGNC|42400|YES|||CCDS55748.1|ENSP00000341637|Q68D85||UPI00001F9E11||||||||||||||||||||||||||||||||||,A|downstream_gene_variant|MODIFIER|NCR3LG1|ENSG00000188211|Transcript|ENST00000530403|nonsense_mediated_decay|||||||||||1|1606|1||SNV|1|HGNC|42400||||CCDS55748.1|ENSP00000434394|Q68D85||UPI00001F9E11||||||||||||||||||||||||||||||||||;GC_AFR=4361,1,0;GC_AMR=419,0,0;GC_ASJ=150,0,0;GC_EAS=811,0,0;GC_FIN=1747,0,0;GC_NFE=7503,0,0;GC_OTH=491,0,0;Hom_Male=0;Hom_Female=0
'''

