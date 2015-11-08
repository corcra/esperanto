#!/usr/bin/env bash

# verbs
echo "===== verbs =====" > verbs.tmp
awk '$1 ~ /i$/ { print $0 }' words.txt | sort -u >> verbs.tmp

# nouns
echo "===== nouns =====" > nouns.tmp
awk '$1 ~ /o$/ { print $0 }' words.txt | sort -u>> nouns.tmp

# adjectives
echo "===== adjectives =====" > adjectives.tmp
awk '$1 ~ /a$/ { print $0 }' words.txt | sort -u >> adjectives.tmp

# adverbs
echo "===== adverbs =====" > adverbs.tmp
awk '$1 ~ /e$/ { print $0 }' words.txt | sort -u >> adverbs.tmp

# misc
echo "===== misc =====" > misc.tmp
awk '($1 !~ /i$/)&&($1 !~ /o$/)&&($1 !~ /e$/)&&($1 !~ /a$/) { print $0 }' words.txt | sort -u >> misc.tmp

# combine
cat nouns.tmp adjectives.tmp verbs.tmp adverbs.tmp misc.tmp > EO-EN_dictionary.txt

nwords=`grep -cv "=" EO-EN_dictionary.txt`
echo there are $nwords words in the dictionary

# tidy
rm *.tmp
