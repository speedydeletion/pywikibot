#high level cat of all deletion instruction pages :Category:Wikipedia deletion https://www.wikidata.org/wiki/Q4615845
import pprint
import codecs
import pywikibot


_logger = "speedydeletion"
import pywikibot

def p(n):

    pywikibot.debug('going to load %s.' % n, _logger)
    site = pywikibot.Site('en',"wikipedia")
    repo = site.data_repository()

    print 'SD going to load %s' % n
    return pywikibot.ItemPage(repo, n).get()

def load_pages():
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
    return pages


