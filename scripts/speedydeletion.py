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


todo = codecs.open('todo.sh','wb','utf-8')

for e in pages :
 #   pprint.pprint(e['labels'])
 
    #for eid in p["entities"] :
    #    e = p["entities"][eid]
    # pprint.pprint(e)
    name = e["labels"]['en']
#    print 'name',name
    
    for lc in f.langs:
        wikiname = '%swiki' % lc
        if wikiname in e["sitelinks"]:
            catname = e["sitelinks"][wikiname]
            parts =catname.split(':')     
            justcatname = ':'.join(parts[1:])
            todo.write( u"python  ./pwb.py transferbot -lang:%s -tolang:%s -tofamily:speedydeletion  -family:wikipedia '-catr:%s'\n" % (lc, lc, justcatname))

        else:
            #print name, "missing", wikiname
            pass
                

todo.close()

