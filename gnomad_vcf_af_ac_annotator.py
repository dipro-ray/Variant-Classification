# first download gnoamd chrommosome 1 exome data vcf file
# after the first download is complete, download the .tbi file
# generate small vcf file for testing using command like: head -10000 011312_363A.snp.vcf > test.vcf


import os
import subprocess
from pprint import pprint


wd = '/Users/dipster/Downloads/xxx/'
infilename = 'xxx.vcf'

with open(wd+infilename, 'rU') as infile:
	with open(wd+infilename+'_gnomad_genome_annotated.vcf', 'w') as outfile:
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
				#print 'tabix /Users/dipster/Downloads/vcf_annotator/gnomad.exomes.r2.1.1.sites.'+chrom.replace('chr', '')+'.vcf.bgz '+chrom.replace('chr','')+':'+pos+'-'+pos
				
				try:
					tbx = subprocess.check_output('tabix /Users/dipster/Downloads/gnomad.genomes.r2.1.1.sites.vcf.bgz '+chrom.replace('chr','')+':'+pos+'-'+pos, shell=True)
				except subprocess.CalledProcessError:
					tbx = ''
					while tbx == '':
						tbx = subprocess.check_output('tabix /Users/dipster/Downloads/gnomad.genomes.r2.1.1.sites.vcf.bgz '+chrom.replace('chr','')+':'+pos+'-'+pos, shell=True)


				AC = 'AC=0'
				AN = 'AN=0'
				AF = 'AF=0'
				
				AC_afr = 'AC_afr=0'
				AN_afr = 'AN_afr=0'
				AF_afr = 'AF_afr=0'

				AC_eas = 'AC_eas=0'
				AN_eas = 'AN_eas=0'
				AF_eas = 'AF_eas=0'

				AC_amr = 'AC_amr=0'
				AN_amr = 'AN_amr=0'
				AF_amr = 'AF_amr=0'

				AC_nfe = 'AC_nfe=0'
				AN_nfe = 'AN_nfe=0'
				AF_nfe = 'AF_nfe=0'

				AC_fin = 'AC_fin=0'
				AN_fin = 'AN_fin=0'
				AF_fin = 'AF_fin=0'

				AC_asj = 'AC_asj=0'
				AN_asj = 'AN_asj=0'
				AF_asj = 'AF_asj=0'

				AC_sas = 'AC_sas=0'
				AN_sas = 'AN_sas=0'
				AF_sas = 'AF_sas=0'
				
				try:
					item = tbx.strip('\n').split('\n')
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
						if pos == gpos and ref == gref and alt == galt:
							#pprint(g)
							#pprint(ginfo)
							AC = ginfo[0]
							AN = ginfo[1]
							AF = ginfo[2]
							

							for element in ginfo:

								if 'AC_afr=' in element and '_AC_afr' not in element:
									AC_afr = element
								if 'AN_afr=' in element and '_AN_afr' not in element:
									AN_afr = element
								if 'AF_afr=' in element and '_AF_afr' not in element:
									AF_afr = element

								if 'AC_eas=' in element and '_AC_eas' not in element:
									AC_eas = element
								if 'AN_eas=' in element and '_AN_eas' not in element:
									AN_eas = element
								if 'AF_eas=' in element and '_AF_eas' not in element:
									AF_eas = element

								if 'AC_amr=' in element and '_AC_amr' not in element:
									AC_amr = element
								if 'AN_amr=' in element and '_AN_amr' not in element:
									AN_amr = element
								if 'AF_amr=' in element and '_AF_amr' not in element:
									AF_amr = element

								if 'AC_nfe=' in element and '_AC_nfe' not in element:
									AC_nfe = element
								if 'AN_nfe=' in element and '_AN_nfe' not in element:
									AN_nfe = element
								if 'AF_nfe=' in element and '_AF_nfe' not in element:
									AF_nfe = element

								if 'AC_fin=' in element and '_AC_fin' not in element:
									AC_fin= element
								if 'AN_fin=' in element and '_AN_fin' not in element:
									AN_fin = element
								if 'AF_fin=' in element and '_AF_fin' not in element:
									AF_fin = element

								if 'AC_asj=' in element and '_AC_asj' not in element:
									AC_asj = element
								if 'AN_asj=' in element and '_AN_asj' not in element:
									AN_asj = element
								if 'AF_asj=' in element and '_AF_asj' not in element:
									AF_asj = element

								if 'AC_sas=' in element and '_AC_sas' not in element:
									AC_sas = element
								if 'AN_sas=' in element and '_AN_sas' not in element:
									AN_sas = element
								if 'AF_sas=' in element and '_AF_sas' not in element:
									AF_sas = element

							final_gnomad_info = ';'.join([AC, AN, AF, AC_afr, AN_afr, AF_afr, AC_eas, AN_eas, AF_eas, AC_amr, AN_amr, AF_amr, AC_nfe, AN_nfe, AF_nfe, AC_fin, AN_fin, AF_fin, AC_asj, AN_asj, AF_asj, AC_sas, AN_sas, AF_sas])
							#print final_gnomad_info
							#print '----'
				except IndexError:
					print 'caught exception'
					pass

				
				final_gnomad_info = ';'.join([AC, AN, AF, AC_afr, AN_afr, AF_afr, AC_eas, AN_eas, AF_eas, AC_amr, AN_amr, AF_amr, AC_nfe, AN_nfe, AF_nfe, AC_fin, AN_fin, AF_fin, AC_asj, AN_asj, AF_asj, AC_sas, AN_sas, AF_sas])
				#print final_gnomad_info
				#if AC != 'AC=0':
					#print final_gnomad_info

				print chrom, pos, id, ref, alt, AC, AN, AF, gchrom, gpos, gid, gref, galt, pos==gpos, ref==gref, alt==galt 
				print "\n\n\n\n\n"


				outfile.write('\t'.join([chrom, pos, id, ref, alt, qual, filter, info+';'+final_gnomad_info, format, extra])+'\n')

	

'''
11	17396807	.	G	A	302.46	PASS	AC=1;AF=3.22935e-05;AN=30966;BaseQRankSum=1.44000e+00;ClippingRankSum=3.82000e-01;DP=651226;FS=5.28700e+00;InbreedingCoeff=1.40000e-03;MQ=6.00000e+01;MQRankSum=2.37000e-01;QD=9.17000e+00;ReadPosRankSum=7.47000e-01;SOR=1.20600e+00;VQSLOD=1.49000e+01;VQSR_culprit=MQ;GQ_HIST_ALT=0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|1;DP_HIST_ALT=0|0|0|0|0|0|1|0|0|0|0|0|0|0|0|0|0|0|0|0;AB_HIST_ALT=0|0|0|0|0|0|0|0|1|0|0|0|0|0|0|0|0|0|0|0;GQ_HIST_ALL=3|0|1|2|11|11|39|72|96|289|479|320|1597|409|1406|549|1971|246|1804|6191;DP_HIST_ALL=0|9|104|678|2330|3099|3724|4561|859|88|19|10|4|4|3|0|2|1|0|1;AB_HIST_ALL=0|0|0|0|0|0|0|0|1|0|0|0|0|0|0|0|0|0|0|0;AC_Male=1;AC_Female=0;AN_Male=17116;AN_Female=13850;AF_Male=5.84249e-05;AF_Female=0.00000e+00;GC_Male=8557,1,0;GC_Female=6925,0,0;GC_raw=15495,1,0;AC_raw=1;AN_raw=30992;GC=15482,1,0;AF_raw=3.22664e-05;Hom_AFR=0;Hom_AMR=0;Hom_ASJ=0;Hom_EAS=0;Hom_FIN=0;Hom_NFE=0;Hom_OTH=0;Hom=0;Hom_raw=0;AC_AFR=1;AC_AMR=0;AC_ASJ=0;AC_EAS=0;AC_FIN=0;AC_NFE=0;AC_OTH=0;AN_AFR=8724;AN_AMR=838;AN_ASJ=300;AN_EAS=1622;AN_FIN=3494;AN_NFE=15006;AN_OTH=982;AF_AFR=1.14626e-04;AF_AMR=0.00000e+00;AF_ASJ=0.00000e+00;AF_EAS=0.00000e+00;AF_FIN=0.00000e+00;AF_NFE=0.00000e+00;AF_OTH=0.00000e+00;POPMAX=AFR;AC_POPMAX=1;AN_POPMAX=8724;AF_POPMAX=1.14626e-04;DP_MEDIAN=33;DREF_MEDIAN=3.16228e-37;GQ_MEDIAN=99;AB_MEDIAN=4.24242e-01;AS_RF=9.81621e-01;AS_FilterStatus=PASS;CSQ=A|3_prime_UTR_variant|MODIFIER|NCR3LG1|ENSG00000188211|Transcript|ENST00000338965|protein_coding|5/5||ENST00000338965.4:c.*2748G>A||4357||||||1||1||SNV|1|HGNC|42400|YES|||CCDS55748.1|ENSP00000341637|Q68D85||UPI00001F9E11||||||||||||||||||||||||||||||||||,A|downstream_gene_variant|MODIFIER|NCR3LG1|ENSG00000188211|Transcript|ENST00000530403|nonsense_mediated_decay|||||||||||1|1606|1||SNV|1|HGNC|42400||||CCDS55748.1|ENSP00000434394|Q68D85||UPI00001F9E11||||||||||||||||||||||||||||||||||;GC_AFR=4361,1,0;GC_AMR=419,0,0;GC_ASJ=150,0,0;GC_EAS=811,0,0;GC_FIN=1747,0,0;GC_NFE=7503,0,0;GC_OTH=491,0,0;Hom_Male=0;Hom_Female=0
'''

