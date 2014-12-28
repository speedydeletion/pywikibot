
import pprint
import codecs
import pywikibot
import pywikibot.speedydeletion
from pywikibot.families.speedydeletion_family import Family


print 'high level cat of all deletion instruction pages :Category:Wikipedia deletion https://www.wikidata.org/wiki/Q4615845'
f = Family()

print 'take each language and check if it is the family.'

pages = pywikibot.speedydeletion.load_pages()

todo = codecs.open('todo.sh','wb','utf-8')

for e in pages :
    pprint.pprint(e['labels'])
 
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

            justcatname = justcatname.replace('(','\(').replace(')','\)')

            todo.write( u"python  ./pwb.py transferbot -lang:%s -tolang:%s -tofamily:speedydeletion  -family:wikipedia \"-catr:%s\"\n" % (lc, lc, justcatname))

        else:
            #print name, "missing", wikiname
            pass
                

todo.close()

