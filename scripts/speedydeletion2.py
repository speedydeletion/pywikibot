#high level cat of all deletion instruction pages :Category:Wikipedia deletion https://www.wikidata.org/wiki/Q4615845
import pprint
import pywikibot.speedydeletion
from pywikibot.families.speedydeletion_family import Family
f = Family()

pages = speedydeletion.pages

seen = {}

for e in pages :
    name = e["labels"]['en']
        
    for wikiname in e["sitelinks"]:
        n = wikiname.replace('wiki','')
        n = n.replace('quote','')
        n = n.replace('source','')
        n = n.replace('voyage','')
        n = n.replace('news','')
        if n not in f.langs:
            if n not in seen:
                print "Check", n
                seen[n]=1

    for lc in f.langs:
        wikiname = '%swiki' % lc
        if wikiname in e["sitelinks"]:
            catname = e["sitelinks"][wikiname]
            parts =catname.split(':')     
            justcatname = ':'.join(parts[1:])
        else:
            print "Probl",name, "missing", wikiname

                

