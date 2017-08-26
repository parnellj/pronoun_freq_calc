from __future__ import division

from collections import defaultdict
from itertools import groupby

import nltk
import os
import numpy as np
import re
import matplotlib.pyplot as plt

pronouns = {'1 1st sg':['i','im','ive','id','ill','me','my','myself'],
            '2 1st pl':['we','weve','wed','ours', 'our',
                      'ourselves'],
            '3 2nd sg':['you','youre','youve','youd','youll','your','yourself',
                      'yourselves'],
            '4 3rd sg':['he','she','hes','shes','hed','shed','hell','shell',
                      'his','hers','his','her','himself','herself'],
            '5 3rd pl':['they','theyre','theyve','theyre','theyd','theyll',
                      'theirs','their','themselves']
            }

name = 'stateoftheunion1790-2016.txt'

dir = os.path.join('.', 'inputs')
r = re.compile(r"\*\*\*\n")

speeches = []

with open(os.path.join(dir, name), "rU") as f:
    for k, g in groupby(f, key=lambda x:r.search(x)):
        if not k:
            whole = list(g)
            speeches += [[whole[2].replace("\n",""),
                          whole[3][-5:].replace("\n",""),
                          ' '.join([a.replace("\n","") for a in whole[4:]])
                          ]]

all_freqs = []

for speech in speeches[1:]:
    a = nltk.word_tokenize(speech[2])
    a = [w.lower() for w in a if w.isalpha()]
    length = len(a)
    fd = nltk.FreqDist(a)
    pfreq = []
    for pn in sorted(pronouns.iterkeys()):
        pfreq += [sum([fd.freq(a) for a in pronouns[pn]])]
    all_freqs += [[speech[1], pfreq]]

year = [int(a[0]) for a in all_freqs]
pronoun_freqs = {}
for num, k in enumerate(sorted(pronouns.iterkeys())):
    pronoun_freqs[k[2:]] = [a[1][num] for a in all_freqs]

styles = {'1st sg':['r','+','None'],
          '1st pl':['g','+','None'],
          '2nd sg':['b','+','None'],
          '3rd sg':['c','+','None'],
          '3rd pl':['m','+','None']}

for k, v in pronoun_freqs.iteritems():
    x = year
    y = [a * 100 for a in v]
    #plt.plot(x, y,
    #         color=styles[k][0], marker=styles[k][1],
    #         linestyle=styles[k][2], label=k)
    coeffs = np.polyfit(x, y, 2)
    p = np.poly1d(coeffs)
    yhat = p(x)
    ybar = np.sum(y)/len(y)
    ssreg = np.sum((yhat-ybar)**2)
    sstot = np.sum((y - ybar)**2)
    print k + " " + str(ssreg/sstot)
    plt.plot(year, p(year), color=styles[k][0], label=k)
plt.xlabel('Year')
plt.ylabel('% Frequency')
plt.title('Pronoun Frequency in SOTU Addresses')
plt.legend()
plt.show()
