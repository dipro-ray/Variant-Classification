import glob
import os
import datetime, time
from collections import defaultdict
import argparse

ts = time.time()
current_date = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d')


def collate(infiles, filetype):
    if filetype == 'cdot':
        invariants = defaultdict(list)
        for f in infiles:
            with open(f, 'rU') as infile:
                for line in infile:
                    try:
                        line = line.strip('\n').split('\t')
                        anno = '|'.join([line[0], ' ', line[2], line[3], line[4], line[5], ' ', line[7]])
                        refs = line[8].strip('\n').split('_')
                        if invariants[anno]:
                            invariants[anno] += refs
                        if not invariants[anno]:
                            invariants[anno] = refs
                    except IndexError:
                        pass
        with open(args.dir+args.date+'_archive_summary_all_genes_cdot_db_summary_collated.txt', 'w') as outfile:
            print args.dir+args.date+'_archive_summary_all_genes_cdot_db_summary_collated.txt', 'AAAA'
            outfile.write('\t'.join(['Symbol', 'Dict', 'cDot', 'pDot_Letter', 'pDot_Three', 'Position', 'Reference Count', 'Transcripts', 'Reference PMIDs'])+'\n')
            for v in invariants:
                temp = v.split('|')
                symbol = temp[0]
                dict = temp[1]
                cdot = temp[2]
                pdot_letter = temp[3]
                pdot_three = temp[4]
                position = temp[5]
                count = str(len(set(invariants[v])))
                trans = temp[7]
                refs = '_'.join(list(set(invariants[v])))
                outfile.write('\t'.join([symbol, dict, cdot, pdot_letter, pdot_three, position, count, trans, refs])+'\n')

    if filetype == 'pdot':
        invariants = defaultdict(list)
        for f in infiles:
            with open(f, 'rU') as infile:
                for line in infile:
                    try:
                        line = line.strip('\n').split('\t')
                        anno = '|'.join([line[0], ' ', line[2], line[3], line[4], line[5], ' ', line[7]])
                        refs = line[8].strip('\n').split('_')
                        if invariants[anno]:
                            invariants[anno] += refs
                        if not invariants[anno]:
                            invariants[anno] = refs
                    except IndexError:
                        pass
        print len(invariants)
        with open(args.dir+args.date+'_archive_summary_all_genes_pdot_db_summary_collated.txt', 'w') as outfile:
            outfile.write('\t'.join(['Symbol', 'Dict', 'cDot', 'pDot_Letter', 'pDot_Three', 'Position', 'Reference Count', 'Transcripts', 'Reference PMIDs'])+'\n')
            for v in invariants:
                temp = v.split('|')
                symbol = temp[0]
                dict = temp[1]
                cdot = temp[2]
                pdot_letter = temp[3]
                pdot_three = temp[4]
                position = temp[5]
                count = str(len(set(invariants[v])))
                trans = temp[7]
                refs = '_'.join(list(set(invariants[v])))
                outfile.write('\t'.join([symbol, dict, cdot, pdot_letter, pdot_three, position, count, trans, refs])+'\n')

    if filetype == 'pair':
        invariants = defaultdict(list)
        for f in infiles:
            with open(f, 'rU') as infile:
                for line in infile:
                    try:
                        line = line.strip('\n').split('\t')
                        anno = '$'.join([line[0], ' ', line[2], line[3], line[4], line[5], ' ', line[7]])
                        refs = line[8].strip('\n').split('_')
                        if invariants[anno]:
                            invariants[anno] += refs
                        if not invariants[anno]:
                            invariants[anno] = refs
                    except IndexError:
                        pass
        with open(args.dir+args.date+'_archive_summary_all_cdot_pdot_pairs_db_summary_collated.txt', 'w') as outfile:
            outfile.write('\t'.join(['Symbol', 'Dict', 'cDot', 'pDot_Letter', 'pDot_Three', 'Position', 'Reference Count', 'Transcripts', 'Reference PMIDs'])+'\n')
            for v in invariants:
                temp = v.split('$')
                symbol = temp[0]
                dict = temp[1]
                cdot = temp[2]
                pdot_letter = temp[3]
                pdot_three = temp[4]
                position = temp[5]
                count = str(len(set(invariants[v])))
                trans = temp[7]
                refs = '_'.join(list(set(invariants[v])))
                outfile.write('\t'.join([symbol, dict, cdot, pdot_letter, pdot_three, position, count, trans, refs])+'\n')


def main(args):
    if args.cdots == 'true':
        inlist = glob.glob(args.dir + '*' + args.date + '*archive*all_genes_cdot_db_summary.txt')
        collate(inlist, 'cdot')
    if args.pdots == 'true':
        inlist = glob.glob(args.dir + '*' + args.date + '*archive*all_genes_pdot_db_summary.txt')
        print inlist
        collate(inlist, 'pdot')
    if args.pairs == 'true':
        inlist = glob.glob(args.dir + '*' + args.date + '*archive*all_cdot_pdot_pairs_db_summary.txt')
        print inlist
        collate(inlist, 'pair')


__version__ = '1.0'

if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--input_directory", action="store", dest="dir")
    parser.add_argument("-c", "--merge_cdots", action="store", dest="cdots")
    parser.add_argument("-p", "--merge_pdots", action="store", dest="pdots")
    parser.add_argument("-a", "--merge_pairs", action="store", dest="pairs")
    parser.add_argument("-date", "--date", action="store", dest="date")

    # Specify output of "--version"
    parser.add_argument(
        "--version", action="version", version="%(prog)s (version {version})".format(version=__version__))
    args = parser.parse_args()
    main(args)