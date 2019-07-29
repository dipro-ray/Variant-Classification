wd = '/Users/dipster/Downloads/Indels/2234/'
infilename = '011329_2234F.snp.vcf_gnomad_genome_annotated.vcf'

with open(wd+infilename, 'rU') as infile:
	with open(wd+infilename+'_filtered.vcf', 'w') as outfile:
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

				#Since there are AC & AF earlier in info section, only looking for gnomad AC & AF (6 was picked arbitrarily after 1)
				for section in infosec[10:len(infosec)]:
					if "AC=" in section and "MLEAC=" not in section:
						AC = section
						AC = AC[3:len(AC)]
					if "AF=" in section and "MLEAF=" not in section:
						AF = section
						AF = AF[3:len(AF)]

				AC = float(AC)
				AF = float(AF)
				
				if (AC < 5000 or AF <= 0.005):
					print chrom, pos, 'AC='+ str(AC), 'AF='+str(AF)
					outfile.write('\t'.join([chrom, pos, id, ref, alt, qual, filter, info, format, extra])+'\n')