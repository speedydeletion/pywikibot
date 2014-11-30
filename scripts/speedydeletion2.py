#high level cat of all deletion instruction pages :Category:Wikipedia deletion https://www.wikidata.org/wiki/Q4615845
import pprint
from wikipedia import wikipedia
from pywikibot.families.speedydeletion_family import Family
f = Family()

webnames = ('quote',
            'source',
            'voyage',
            'news',
            '')

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
            name = e["labels"]['en']['value']
        else:
            pprint.pprint(e["labels"])

        for wikiname in e["sitelinks"]:
            l = e["sitelinks"][wikiname]['title']
            n = wikiname.replace('wiki','')
            n = n.replace('quote','')
            n = n.replace('source','')
            n = n.replace('voyage','')
            n = n.replace('news','')
            if n not in f.langs:

                if n not in seen:

                    # search for the matching website
                    for w in webnames :
                        if w == '':
                            p = 'pedia'
                        else:
                            p = w 
                        if wikiname.endswith('wiki%s' % w):
                            agent = wikipedia.Agent()
                            #print ('before %s' % n)
                            n= n.replace('_','-')
                            #print ('after %s' % n)
                            
                            #pprint.pprint(['lang',p,n,l])
                            agent.set_site_lang(p, n)
                            pg = agent.page(l)
                            #pprint.pprint(['page',pg])
                            #pprint.pprint(['page links',pg.links])
                            #pprint.pprint(['page ref',pg.references])
                            #pprint.pprint(['page content',pg.content])
                            #pprint.pprint(['page content',pg.category_members()])
                            count = 0 
                            for p in pg.category_members():
                                count = count + 1
                                print "Found", n, wikiname,  p['title']
                            if (count > 0):
                                print "Has Articles", count, n, wikiname
                            
                            
                            #link = "http://%s.wiki%s.org/wiki/%s" % ( n, p, l)
                            #link =  link.replace(" ",'%20')
                            #print "Check for %s / %s in %s with link %s" % ( n, wikiname, name, link)
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



