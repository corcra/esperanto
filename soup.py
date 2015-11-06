#!/usr/bin/env ipython
# Let's play a word-learning game, sort of.

import random
from affixes import affixes

max_retry = min(len(affixes['prefixes']), len(affixes['suffixes']))
word_endings = ['o', 'a', 'e', 'i', 'as', 'os', 'is', 'us', 'u', 'on']

def make_soup(root, n_p, n_s):
    """
    Make a new word from a root, containing n_prefixes and n_suffixes
    Also adds a random ending (grammatical form)
    """
    soup = root[:-1]
    ending = root[-1]
    assert ending in {'i', 'o', 'e'}
    meanings = []
    for p in xrange(n_p):
        prefix = random.choice(affixes['prefixes'].keys())
        transformation = affixes['prefixes'][prefix][0]
        retry = 0
        while not ending in transformation:
            prefix = random.choice(affixes['prefixes'].keys())
            transformation = affixes['prefixes'][prefix][0]
            retry += 1
            if retry >= max_retry: 
                print 'Warning: couldn\'t find suitable affix for ending', ending
                continue
        soup = prefix + soup
        meanings.append((prefix, affixes['prefixes'][prefix][1]))
        ending = transformation[ending]
    for s in xrange(n_s):
        suffix = random.choice(affixes['suffixes'].keys())
        transformation = affixes['suffixes'][suffix][0]
        retry = 0
        while not ending in transformation:
            suffix = random.choice(affixes['suffixes'].keys())
            transformation = affixes['suffixes'][suffix][0]
            retry += 1
            if retry >= max_retry:
                print 'Warning: couldn\'t find suitable affix for ending', ending
                continue
        soup = soup + suffix
        meanings.append((suffix, affixes['suffixes'][suffix][1]))
        ending = transformation[ending]
    soup += ending
    return soup, meanings

def soup(root, n_p, n_s, cheat=False):
    """
    Pretty print the results.
    """
    soup, meanings = make_soup(root, n_p, n_s)
    if cheat:
        print root, '\t',
        for (i, (affix, explanation)) in enumerate(meanings):
            if i > 0:
                print '\t',
            print '+', affix, ':', explanation
    print soup
    return True

def read_soup(soup):
    """
    Try to decompile a soup.
    TODO: finish
    """
    desoup = soup
    ending = soup[-1]
    
    last_two = soup[-3:-1]
    if last_two in affixes['suffixes']:
        print last_two
    return soup
