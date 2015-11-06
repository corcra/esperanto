#!/usr/bin/env ipython
# Suffixes and affixes in esperanto.
# The format of the dicts are:
#   affix: (transformations, explanatiion)
# Transformations is a dict of how this suffix transforms endings, e.g.
#  i --> a, esti --> estanta

suffixoids = {u'ant': ({'i': 'a'}, 'present active participle'),
              u'int': ({'i': 'a'}, 'past active participle'),
              u'ont': ({'i': 'a'}, 'future active participle'),
              u'at': ({'i': 'a'}, 'present passive participle'),
              u'it': ({'i': 'a'}, 'past passive participle'),
              u'ot': ({'i': 'a'}, 'future passive participle'),
              u'ad': ({'i': 'o'}, 'action/process defined by root'),
              u'ajx': ({'a': 'o'}, 'tangible manifestation of root'),
              u'ec': ({'a': 'o'}, 'quality/characteristic defined by root'),
              u'ul': ({'a': 'o'}, 'person characterised by root'),
              u'an': ({'o': 'o'}, 'member/participant/adherent of root'),
              u'ar': ({'o': 'o'}, 'collection of things defined by root'),
              u'ej': ({'o': 'o'}, 'place for things/actions of root'),
              u'er': ({'o': 'o'}, 'smallest part/element of collective of root'),
              u'estr': ({'o': 'o'}, 'boss of whatever defined by root'),
              u'id': ({'o': 'o'}, 'offspring of creature defined by root'),
              u'il': ({'i': 'o'}, 'tool for doing root'),
              u'in': ({'o': 'o'}, 'female version of root'),
              u'ing': ({'o': 'o'}, 'holder/sheath for object defined by root'),
              u'ism': ({'o': 'o'}, 'doctrine/movement/system for idea defined by root'),
              u'ist': ({'i': 'o'}, 'individual professionally/vocationally occupied with idea/activity defined by root'),
              u'uj': ({'o': 'o'}, 'container for objects described by root'),
              u'ebl': ({'i': 'a'}, 'suitable for having whatever is described by the root done to it'),
              u'em': ({'i': 'a'}, 'having incliation or tendency towards what is described by root'),
              u'end': ({'i': 'a'}, 'must have whatever is described by the root done to it'),
              u'ind': ({'i': 'a'}, 'worth having whatever is described by the root done to it'),
              u'esk': ({'o': 'a'}, 'similar to/in the manner of whatever is described by root'),
              u'iv': ({'i': 'a'}, 'capable of doing whatever is described by root'),
              u'oid': ({'o': 'a'}, 'with the form of whatever is described by the root'),
              u'oz': ({'o': 'a'}, 'to show presence of large quantity of whatever is described by root'),
              u'ig': ({'a': 'i'}, 'to cause something to be in the state caused by the root'),
              u'igx': ({'a': 'i'}, 'to become in the state described by the root'),
              u'art': ({'i': 'o'}, 'the art of whatever is described by the root'),
              u'am': ({'o': 'a'}, 'loving whatever is described by the root'),
              u'hav': ({'o': 'a'}, 'possessing whatever is described by the root'),
              u'plen': ({'o': 'a'}, 'full of whatever is described by the root'),
              u'pov': ({'i': 'a'}, 'capable of whatever is described by the root'),
              u'ricx': ({'o': 'a'}, 'rich with whatever is described by the root'),
              u'sxajn': ({'a': 'a'}, 'seeming to be whatever is described by the root'),
              u'aspekt': ({'o': 'a'}, 'having the appearance of...'),
              u'simil': ({'o': 'a'}, 'being similiar to...'),
              u'manier': ({'o': 'a'}, 'with the manner of...')}
prefixoids = {u'dis': ({'i': 'i'}, 'having to do with separation, in all possible directions'),
              u'ek': ({'i': 'i'}, 'beginning of an action described by root'),
              u'for': ({'i': 'i'}, 'away'),
              u'mis': ({'i': 'i'}, 'wrongly, incorrectly'),
              u're': ({'i': 'i'}, 'back to the beginning again'),
              u'retro': ({'i': 'i'}, 'in the opposite direction'),
              u'cxef': ({'o': 'o'}, 'greatest or most important'),
              u'vir': ({'o': 'o'}, 'male eqivalent of -in'),
              u'fi': ({'a': 'a', 'i': 'i', 'o': 'o', 'e': 'e'}, 'expressing indignation/disgust'),
              u'fusx': ({'a': 'a', 'i': 'i', 'o': 'o', 'e': 'e'}, 'screwed up'),
              u'ne': ({'a': 'a', 'i': 'i', 'o': 'o', 'e': 'e'}, 'creates the negative (not the opposite) of the root'),
              u'vic': ({'o': 'o'}, 'second in rank, acting regent for')}
suffixes = {u'acx': ({'a': 'a', 'i': 'i', 'o': 'o', 'e': 'e'}, 'add contempt/detestation'),
        u'eg': ({'a': 'a', 'i': 'i', 'o': 'o', 'e': 'e'}, 'augments or strengthens idea shown by root (opposite of -et)'),
        u'et': ({'a': 'a', 'i': 'i', 'o': 'o', 'e': 'e'}, 'diminishes idea shown by root (opposite of -eg)'),
            u'if': ({'o': 'i'}, 'to turn something into the root'),
            u'cxj': ({'o': 'o'}, 'takes a man\'s name and makes it intimate'),
            u'nj': ({'o': 'o'}, 'takes a woman\'s name and makes it intimate')}
prefixes = {u'bo': ({'o': 'o'}, 'related through marriage'),
            u'eks': ({'o': 'o'}, 'former'),
            u'ge': ({'o': 'o'}, 'both sexes taken together'),
            u'mal': ({'a': 'a', 'i': 'i', 'o': 'o', 'e': 'e'}, 'turns a word into its opposite'),
            u'pra': ({'a': 'a', 'i': 'i', 'o': 'o', 'e': 'e'}, 'distant in time (usually in past) or relationship'),
            u'pseuxdo': ({'a': 'a', 'i': 'i', 'o': 'o', 'e': 'e'}, 'false')}


# combine the -oids
suffixes.update(suffixoids)
prefixes.update(prefixoids)
# combine everything
affixes = dict()
affixes['prefixes'] = prefixes
affixes['suffixes'] = suffixes
