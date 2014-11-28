#high level cat of all deletion instruction pages :Category:Wikipedia deletion https://www.wikidata.org/wiki/Q4615845
import pprint

from pywikibot.families.speedydeletion_family import Family
f = Family()

import os.path

if os.path.exists('testpages.py') :
    import testpages 
    pages = testpages.data
else:
    import pywikibot.speedydeletion_ng as sd
    pages = sd.pages
    f = open ('testpages.py','w')
    f.write('data=')
    f.write(pprint.pformat(pages))
    f.close()

seen = {}

for n in pages.keys() :
    for i in  pages[n]['entities']:
        e = pages[n]['entities'][i]
    
        #pprint.pprint(e)
        if 'en' in e["labels"]:
            name = e["labels"]['en']
        else:
            pprint.pprint(e["labels"])

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
                title = e["sitelinks"][wikiname]['title']
                #pprint.pprint(catname)
                parts =title.split(':')     
                justcatname = ':'.join(parts[1:])
            else:
                print "Probl",name, "missing", wikiname



