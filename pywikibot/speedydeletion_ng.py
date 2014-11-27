#high level cat of all deletion instruction pages :Category:Wikipedia deletion https://www.wikidata.org/wiki/Q4615845
import pprint
import codecs
#import pywikibot

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
        pass

site = Site('en',"wikipedia")
repo = site.data_repository()

_logger = "speedydeletion"
#import pywikibot

def p(n):
    debug('going to load %s.' % n, _logger)
    #print 'SD going to load %s' % n
    return ItemPage(repo, n).get()

articles_for_deletion = p("Q4989296")
proposed_deletion = p("Q7927732")
speedy_deletion = p("Q5964")
wpdeletion = p("Q4615845") # this is normally the wrong one...

# take each language and check if it is the family.
pages = [
    articles_for_deletion,
    speedy_deletion,
    proposed_deletion,
    wpdeletion,
]
