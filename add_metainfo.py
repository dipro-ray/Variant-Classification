
wd = '/Users/name/abc/def/'
filename = 'xxx.vcf'

additionalMetainfo = "##INFO=<ID=AC,Number=A,Type=Integer,Description=\"Alternate allele count for samples\">\n##INFO=<ID=AN,Number=1,Type=Integer,Description=\"Total number of alleles in samples\">\n##INFO=<ID=AF,Number=A,Type=Float,Description=\"Alternate allele frequency in samples\">\n##INFO=<ID=AC_afr,Number=A,Type=Integer,Description=\"Alternate allele count for samples of African-American/African ancestry\">\n##INFO=<ID=AN_afr,Number=1,Type=Integer,Description=\"Total number of alleles in samples of African-American/African ancestry\">\n##INFO=<ID=AF_afr,Number=A,Type=Float,Description=\"Alternate allele frequency in samples of African-American/African ancestry\">\n##INFO=<ID=AC_amr,Number=A,Type=Integer,Description=\"Alternate allele count for samples of Latino ancestry\">\n##INFO=<ID=AN_amr,Number=1,Type=Integer,Description=\"Total number of alleles in samples of Latino ancestry\">\n##INFO=<ID=AF_amr,Number=A,Type=Float,Description=\"Alternate allele frequency in samples of Latino ancestry\">\n##INFO=<ID=AC_eas,Number=A,Type=Integer,Description=\"Alternate allele count for samples of East Asian ancestry\">\n##INFO=<ID=AN_eas,Number=1,Type=Integer,Description=\"Total number of alleles in samples of East Asian ancestry\">\n##INFO=<ID=AF_eas,Number=A,Type=Float,Description=\"Alternate allele frequency in samples of East Asian ancestry\">\n##INFO=<ID=AC_nfe,Number=A,Type=Integer,Description=\"Alternate allele count for samples of Non-Finnish European ancestry\">\n##INFO=<ID=AN_nfe,Number=1,Type=Integer,Description=\"Total number of alleles in samples of Non-Finnish European ancestry\">\n##INFO=<ID=AF_nfe,Number=A,Type=Float,Description=\"Alternate allele frequency in samples of Non-Finnish European ancestry\">\n##INFO=<ID=AC_fin,Number=A,Type=Integer,Description=\"Alternate allele count for samples of Finnish ancestry\">\n##INFO=<ID=AN_fin,Number=1,Type=Integer,Description=\"Total number of alleles in samples of Finnish ancestry\">\n##INFO=<ID=AF_fin,Number=A,Type=Float,Description=\"Alternate allele frequency in samples of Finnish ancestry\">\n##INFO=<ID=AC_asj,Number=A,Type=Integer,Description=\"Alternate allele count for samples of Ashkenazi Jewish ancestry\">\n##INFO=<ID=AN_asj,Number=1,Type=Integer,Description=\"Total number of alleles in samples of Ashkenazi Jewish ancestry\">\n##INFO=<ID=AF_asj,Number=A,Type=Float,Description=\"Alternate allele frequency in samples of Ashkenazi Jewish ancestry\">\n##INFO=<ID=AC_sas,Number=A,Type=Integer,Description=\"Alternate allele count for samples of South Asian ancestry\">\n##INFO=<ID=AN_sas,Number=1,Type=Integer,Description=\"Total number of alleles in samples of South Asian ancestry\">\n##INFO=<ID=AF_sas,Number=A,Type=Float,Description=\"Alternate allele frequency in samples of South Asian ancestry\">"


with open(wd+filename, 'r') as myfile:
	contents = myfile.read()
	contents = contents.split('\n')

	for line in contents[0:80]:
		if ("##INFO=<ID=set" in line):
			contents.insert(contents.index(line) + 1, additionalMetainfo)

	contents = '\n'.join(contents).strip()

	with open(wd+filename, 'w') as outfile:
		outfile.write(contents)