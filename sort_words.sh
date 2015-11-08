#!/usr/bin/env bash

# verbs
echo "===== verbs =====" > verbs.tmp
awk '$1 ~ /i$/ { print $0 }' words.txt | sort >> verbs.tmp

# nouns
echo "===== nouns =====" > nouns.tmp
awk '$1 ~ /o$/ { print $0 }' words.txt | sort >> nouns.tmp

# adjectives
echo "===== adjectives =====" > adjectives.tmp
awk '$1 ~ /a$/ { print $0 }' words.txt | sort >> adjectives.tmp

# adverbs
echo "===== adverbs =====" > adverbs.tmp
awk '$1 ~ /e$/ { print $0 }' words.txt | sort >> adverbs.tmp

# misc
echo "===== misc =====" > misc.tmp
awk '($1 !~ /i$/)&&($1 !~ /o$/)&&($1 !~ /e$/) { print $0 }' words.txt | sort >> misc.tmp

# combine
cat nouns.tmp verbs.tmp adjectives.tmp misc.tmp > words_sorted.txt

# tidy
rm -v *.tmp
