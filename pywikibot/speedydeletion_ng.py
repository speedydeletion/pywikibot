#high level cat of all deletion instruction pages :Category:Wikipedia deletion https://www.wikidata.org/wiki/Q4615845
import pprint
import codecs
#import pywikibot

from wikipedia import wikipedia as wikipedia_api

wikipedia_api.set_wikidata()


def debug(x,l):
    print x

class Data:
    def __init__(self, site):
        self._site=site

class Site:
    def __init__(self, lang, site):
        self._lang=lang
        self._site=site

    def data_repository(self):
        return Data(self)

class ItemPage:
    def __init__(self,repo,number):
        self._repo=repo
        self._number=number
        
    def get(self):
        return wikipedia_api.page(self._number)

site = Site('en',"wikipedia")
repo = site.data_repository()

_logger = "speedydeletion"
#import pywikibot

def p(n):
    debug('going to load %s.' % n, _logger)
    #print 'SD going to load %s' % n
    item = ItemPage(repo, n)
    g = item.get()
    return g.wbgetentities()

# take each language and check if it is the family.
pages = {
    'articles_for_deletion' : "Q4989296",
    'speedy_deletion' :  'Q5964',
    'proposed_deletion' :  'Q7927732',
    'wpdeletion' : "Q4615845",
}

for x in pages:
    n = pages[x]
    d  = p(n)
    pages[x] = d
    #pprint.pprint(d)
