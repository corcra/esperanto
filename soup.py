#!/usr/bin/env ipython
# coding=utf-8
# Let's play a word-learning game, sort of.

from __future__ import print_function

greenheart = u'💚 '

import random
from affixes import affixes
import numpy as np

max_retry = min(len(affixes['prefixes']), len(affixes['suffixes']))
word_endings = ['o', 'a', 'e', 'i', 'as', 'os', 'is', 'us', 'u', 'on']

def affix_is_inconsistent(added_affixes, new_affix):
    """
    Some affixes don't make sense together. This script identifies violations
    and rejects new affixes.
    It relies on the conflicts annotated in the affixes dictionary.
    """
    try:
        conflicts = affixes['prefixes'][new_affix].conflicts
    except KeyError:
        conflicts = affixes['suffixes'][new_affix].conflicts
    for c in conflicts:
        if c in added_affixes:
            print('Conflict detected between', new_affix, 'and', ', '.join(added_affixes))
            return True
    else:
        return False

def make_soup(root, n_p, n_s, verbose=False):
    """
    Make a new word from a root, containing n_prefixes and n_suffixes
    Also adds a random ending (grammatical form)
    """
    soup = root[:-1]
    ending = root[-1]
    assert ending in {'i', 'o', 'e'}
    added_affixes = []
    meanings = []
    for p in range(n_p):
        prefix_ok = True
        prefix = random.choice(list(affixes['prefixes'].keys()))
        transformation = affixes['prefixes'][prefix].transformations
        retry = 0
        if not ending in transformation or affix_is_inconsistent(added_affixes, prefix) or prefix in added_affixes:
            prefix_ok = False
        while not prefix_ok:
            prefix = random.choice(list(affixes['prefixes'].keys()))
            transformation = affixes['prefixes'][prefix].transformations
            retry += 1
            if ending in transformation and not affix_is_inconsistent(added_affixes, prefix) and not prefix in added_affixes:
                prefix_ok = True
            if retry >= max_retry: 
                if verbose: print('Warning: couldn\'t find suitable prefix')
                continue
        soup = prefix + soup
        added_affixes.append(prefix)
        meanings.append(affixes['prefixes'][prefix].explanation)
        ending = transformation[ending]
    for s in range(n_s):
        suffix_ok = True
        suffix = random.choice(list(affixes['suffixes'].keys()))
        transformation = affixes['suffixes'][suffix].transformations
        retry = 0
        if not ending in transformation or affix_is_inconsistent(added_affixes, suffix) or suffix in added_affixes:
            suffix_ok = False
        while not suffix_ok:
            suffix = random.choice(list(affixes['suffixes'].keys()))
            transformation = affixes['suffixes'][suffix].transformations
            retry += 1
            if ending in transformation and not affix_is_inconsistent(added_affixes, suffix) and not suffix in added_affixes:
                suffix_ok = True
            if retry >= max_retry:
                if verbose: print('Warning: couldn\'t find suitable suffix')
                continue
        soup = soup + suffix
        added_affixes.append(suffix)
        meanings.append(affixes['suffixes'][suffix].explanation)
        ending = transformation[ending]
    soup += ending
    return soup, list(zip(added_affixes, meanings))

def soup(root, n_p, n_s, cheat=False):
    """
    Pretty print the results.
    """
    soup, meanings = make_soup(root, n_p, n_s)
    if cheat:
        print(root, '\t', end=' ')
        for (i, (affix, explanation)) in enumerate(meanings):
            if i > 0:
                print('\t', end=' ')
            print('+', affix, ':', explanation)
    print(soup)
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
        print(last_two)
    return soup

def tweet_soup(root, root_explanation='dog'):
    """
    Generate a random number of suffixes and prefixes.
    Produce a tweet.
    """
    n_p = np.random.poisson(lam=0.1)
    n_s = np.random.poisson(lam=1.2)
    if n_p == 0 and n_s == 0:
        n_s = 1
    soup, meanings = make_soup(root, n_p, n_s)
    # pretty-print the tweet
    tweet = soup + '\n' + '='*15 + '\n' + root + '\t: ' + root_explanation + '\n'
    for (i, (affix, explanation)) in enumerate(meanings):
        tweet += ' + ' + affix + '\t: ' + explanation +'\n'
    return tweet
