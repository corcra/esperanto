#!/usr/bin/env ipython
# Suffixes and affixes in esperanto.
# The format of the dicts are:
#   affix: (transformations, explanation, conflicts)
# Transformations is a dict of how this suffix transforms endings, e.g.
#  i --> a, esti --> estanta
# Explanation is an English string describing the suffix.
# Conflicts is a set of other suffixes which this one doesn't work with.

class affix(object):
    def __init__(self, name=u'undefined', 
                 transformations={'x': 'x'}, 
                 explanation='undefined', 
                 conflicts={},
                 category='undefined'):
        self.name = name
        self.transformations = transformations
        self.explanation = explanation
        self.conflicts = conflicts
        self.category = category

suffixoids = {affix(u'ant', {'i': 'a'}, 'present active participle', {}, 'participal suffix'),
              affix(u'int', {'i': 'a'}, 'past active participle', {}, 'participal suffix'),
              affix(u'ont', {'i': 'a'}, 'future active participle', {}, 'participal suffix'),
              affix(u'at', {'i': 'a'}, 'present passive participle', {}, 'participal suffix'),
              affix(u'it', {'i': 'a'}, 'past passive participle', {}, 'participal suffix'),
              affix(u'ot', {'i': 'a'}, 'future passive participle', {}, 'participal suffix'),
              affix(u'ad', {'i': 'o'}, 'action/process defined by root', {}, 'category suffix'),
              affix(u'ajx', {'a': 'o'}, 'tangible manifestation of root', {}, 'category suffix'),
              affix(u'ec', {'a': 'o'}, 'quality/characteristic defined by root', {}, 'category suffix'),
              affix(u'ul', {'a': 'o'}, 'person characterised by root', {}, 'category suffix'),
              affix(u'an', {'o': 'o'}, 'member/participant/adherent of root', {}, 'noun suffix'),
              affix(u'ar', {'o': 'o'}, 'collection of things defined by root', {}, 'noun suffix'),
              affix(u'ej', {'o': 'o'}, 'place for things/actions of root', {}, 'noun suffix'),
              affix(u'er', {'o': 'o'}, 'smallest part/element of collective of root', {}, 'noun suffix'),
              affix(u'estr', {'o': 'o'}, 'boss of whatever defined by root', {}, 'noun suffix'),
              affix(u'id', {'o': 'o'}, 'offspring of creature defined by root', {}, 'noun suffix'),
              affix(u'il', {'i': 'o'}, 'tool for doing root', {}, 'noun suffix'),
              affix(u'in', {'o': 'o'}, 'female version of root', {}, 'noun suffix'),
              affix(u'ing', {'o': 'o'}, 'holder/sheath for object defined by root', {}, 'noun suffix'),
              affix(u'ism', {'o': 'o'}, 'doctrine/movement/system for idea defined by root', {}, 'noun suffix'),
              affix(u'ist', {'i': 'o'}, 'individual professionally/vocationally occupied with idea/activity defined by root', {}, 'noun suffix'),
              affix(u'uj', {'o': 'o'}, 'container for objects described by root', {}, 'noun suffix'),
              affix(u'ebl', {'i': 'a'}, 'suitable for having whatever is described by the root done to it', {}, 'adjective suffix'),
              affix(u'em', {'i': 'a'}, 'having incliation or tendency towards what is described by root', {}, 'adjective suffix'),
              affix(u'end', {'i': 'a'}, 'must have whatever is described by the root done to it', {}, 'adjective suffix'),
              affix(u'ind', {'i': 'a'}, 'worth having whatever is described by the root done to it', {}, 'adjective suffix'),
              affix(u'esk', {'o': 'a'}, 'similar to/in the manner of whatever is described by root', {}, 'adjective suffix'),
              affix(u'iv', {'i': 'a'}, 'capable of doing whatever is described by root', {}, 'adjective suffix'),
              affix(u'oid', {'o': 'a'}, 'with the form of whatever is described by the root', {}, 'adjective suffix'),
              affix(u'oz', {'o': 'a'}, 'to show presence of large quantity of whatever is described by root', {}, 'adjective suffix'),
              affix(u'ig', {'a': 'i'}, 'to cause something to be in the state caused by the root', {u'igx'}, 'verb suffix'),
              affix(u'igx', {'a': 'i'}, 'to become in the state described by the root', {u'ig'}, 'verb suffix'),
              affix(u'art', {'i': 'o'}, 'the art of whatever is described by the root', {}, 'quasi suffix'),
              affix(u'am', {'o': 'a'}, 'loving whatever is described by the root', {}, 'quasi suffix'),
              affix(u'hav', {'o': 'a'}, 'possessing whatever is described by the root', {}, 'quasi suffix'),
              affix(u'plen', {'o': 'a'}, 'full of whatever is described by the root', {}, 'quasi suffix'),
              affix(u'pov', {'i': 'a'}, 'capable of whatever is described by the root', {}, 'quasi suffix'),
              affix(u'ricx', {'o': 'a'}, 'rich with whatever is described by the root', {}, 'quasi_suffix'),
              affix(u'sxajn', {'a': 'a'}, 'seeming to be whatever is described by the root', {}, 'quasi suffix'),
              affix(u'aspekt', {'o': 'a'}, 'having the appearance of...', {}, 'quasi suffix'),
              affix(u'simil', {'o': 'a'}, 'being similiar to...', {}, 'quasi suffix'),
              affix(u'manier', {'o': 'a'}, 'with the manner of...', {}, 'quasi suffix')}
prefixoids = {affix(u'dis', {'i': 'i'}, 'having to do with separation, in all possible directions', {}, 'adverb prefix'),
              affix(u'ek', {'i': 'i'}, 'beginning of an action described by root', {}, 'adverb prefix'),
              affix(u'for', {'i': 'i'}, 'away', {}, 'adverb prefix'),
              affix(u'mis', {'i': 'i'}, 'wrongly, incorrectly', {}, 'adverb prefix'),
              affix(u're', {'i': 'i'}, 'back to the beginning again', {}, 'adverb prefix'),
              affix(u'retro', {'i': 'i'}, 'in the opposite direction', {}, 'adverb prefix'),
              affix(u'cxef', {'o': 'o'}, 'greatest or most important', {}, 'root prefix'),
              affix(u'vir', {'o': 'o'}, 'male eqivalent of -in', {}, 'root prefix'),
              affix(u'fi', {'a': 'a', 'i': 'i', 'o': 'o', 'e': 'e'}, 'expressing indignation/disgust', {}),
              affix(u'fusx', {'a': 'a', 'i': 'i', 'o': 'o', 'e': 'e'}, 'screwed up', {}),
              affix(u'ne', {'a': 'a', 'i': 'i', 'o': 'o', 'e': 'e'}, 'creates the negative affix(not the opposite) of the root', {}),
              affix(u'vic', {'o': 'o'}, 'second in rank, acting regent for', {})}
suffixes = {affix(u'acx', {'a': 'a', 'i': 'i', 'o': 'o', 'e': 'e'}, 'add contempt/detestation', {}),
        affix(u'eg', {'a': 'a', 'i': 'i', 'o': 'o', 'e': 'e'}, 'augments or strengthens idea shown by root affix(opposite of -et)', {u'et'}),
        affix(u'et', {'a': 'a', 'i': 'i', 'o': 'o', 'e': 'e'}, 'diminishes idea shown by root affix(opposite of -eg)', {u'eg'}),
            affix(u'if', {'o': 'i'}, 'to turn something into the root', {}),
            affix(u'cxj', {'o': 'o'}, 'takes a man\'s name and makes it intimate', {u'nj'}),
            affix(u'nj', {'o': 'o'}, 'takes a woman\'s name and makes it intimate', {u'cxj'})}
prefixes = {affix(u'bo', {'o': 'o'}, 'related through marriage', {}),
            affix(u'eks', {'o': 'o'}, 'former', {}),
            affix(u'ge', {'o': 'o'}, 'both sexes taken together', {}),
            affix(u'mal', {'a': 'a', 'i': 'i', 'o': 'o', 'e': 'e'}, 'turns a word into its opposite', {}),
            affix(u'pra', {'a': 'a', 'i': 'i', 'o': 'o', 'e': 'e'}, 'distant in time affix(usually in past) or relationship', {}),
            affix(u'pseuxdo', {'a': 'a', 'i': 'i', 'o': 'o', 'e': 'e'}, 'false', {})}

# combine the -oids
suffixes.update(suffixoids)
prefixes.update(prefixoids)
# combine everything
affixes = dict()
affixes['prefixes'] = dict((x.name, x) for x in prefixes)
affixes['suffixes'] = dict((x.name, x) for x in suffixes)
