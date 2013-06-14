#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nltk
from nltk.corpus.reader import *
from nltk.corpus.reader.util import *
from nltk.text import Text
#import MeCab
import pprint

jp_sent_tokenizer = nltk.RegexpTokenizer(u'[^　「」！？。]*[！？。]')
jp_chartype_tokenizer = nltk.RegexpTokenizer(u'([ぁ-んー]+|[ァ-ンー]+|[\u4e00-\u9FFF]+|[^ぁ-んァ-ンー\u4e00-\u9FFF]+)')
ss = PlaintextCorpusReader(".", r'data/novels/sosowa-all-plain.txt',
                          encoding='utf-8',
                          para_block_reader=read_line_block,
                          sent_tokenizer=jp_sent_tokenizer,
                          word_tokenizer=jp_chartype_tokenizer)

text = Text(w.encode("utf-8") for w in ss.words())
fdist = nltk.FreqDist(ss.words())
fdist.plot(50, cumulative=True)