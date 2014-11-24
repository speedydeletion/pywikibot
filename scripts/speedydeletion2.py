#high level cat of all deletion instruction pages :Category:Wikipedia deletion https://www.wikidata.org/wiki/Q4615845
import pprint

from pywikibot.families.speedydeletion_family import Family
f = Family()

#high level cat of all deletion instruction pages :Category:Wikipedia deletion https://www.wikidata.org/wiki/Q4615845
import pprint
import codecs
import pywikibot
from pywikibot.families.speedydeletion_family import Family
f = Family()

site = pywikibot.Site('en',"wikipedia")
repo = site.data_repository()

def p(n):
    return pywikibot.ItemPage(repo, n).get()

articles_for_deletion = p("Q4989296")
proposed_deletion = p("Q7927732")
speedy_deletion = p("Q5964")

# take each language and check if it is the family.
pages = [
    articles_for_deletion,
    speedy_deletion,
    proposed_deletion,
]


for e in pages :
    name = e["labels"]['en']
        
    for wikiname in e["sitelinks"]:
        n = wikiname.replace('wiki','')
        n = n.replace('quote','')
        n = n.replace('source','')
        n = n.replace('voyage','')
        n = n.replace('news','')
        if n not in f.langs:
            print "Check", n

    for lc in f.langs:
        wikiname = '%swiki' % lc
        if wikiname in e["sitelinks"]:
            catname = e["sitelinks"][wikiname]
            parts =catname.split(':')     
            justcatname = ':'.join(parts[1:])
        else:
            print "Probl",name, "missing", wikiname

                

