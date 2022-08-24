def base_count(seq):
    '''
    Return the counts of the bases in a sequence
    Inputs: seq
    '''
    # init an empty dictionary for counts
    counts = dict()
    # check all bases in the sequence
    for base in seq:
        # if this is a new base in the count dict
        if base not in counts:
            # mark the occurence as 1
            counts[base] = 1
        else:
            # otherwise, add one count
            counts[base] += 1
    return counts

def calc_freq(counts):
    '''
    Calculate the frequencies of the nucleotiedes in the given sequence
    Params:
        counts: dictionay that tracks the counts of difference bases in a sequence
    '''
    # the first line of the output
    print('freqs')
    # calculate the total number of counts
    total = float(sum([counts[base] for base in counts.keys()]))
    # print freq one by one
    for base in counts.keys():
        print(base + ':' + str(counts[base]/total))

calc_freq(base_count('ATCTGACGCGCGCCGC'))
