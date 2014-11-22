#high level cat of all deletion instruction pages :Category:Wikipedia deletion https://www.wikidata.org/wiki/Q4615845
import pprint

from pywikibot.families.speedydeletion_family import Family
f = Family()

#Category:Articles for deletion
#https://www.wikidata.org/wiki/Q4989296
#https://www.wikidata.org/w/api.php?action=wbgetentities&ids=Q4989296
articles_for_deletion={
    "entities": {
        "Q4989296": {
            "pageid": 4768919,
            "ns": 0,
            "title": "Q4989296",
            "lastrevid": 175961676,
            "modified": "2014-11-22T12:01:18Z",
            "id": "Q4989296",
            "type": "item",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "Category:Articles for deletion"
                },
                "bug": {
                    "language": "bug",
                    "value": "Kategori:Halaman yang diusulkan untuk dihapus"
                },
                "ce": {
                    "language": "ce",
                    "value": "\u041a\u0430\u0434\u0435\u0433\u0430\u0440:\u0412\u0438\u043a\u0438\u043f\u0435\u0434\u0438\u0439\u0430:\u0414l\u0430\u044f\u043a\u043a\u0445\u0430\u0440\u043d\u0430 \u0445\u0430\u0440\u0436\u0430\u043c\u0445\u043e\u0439"
                },
                "dsb": {
                    "language": "dsb",
                    "value": "Kategorija:Kandidaty za la\u0161owanje"
                },
                "es": {
                    "language": "es",
                    "value": "Categor\u00eda:Wikipedia:Consultas de borrado"
                },
                "et": {
                    "language": "et",
                    "value": "Kategooria:Kustutamiseks esitatud artiklid"
                },
                "fa": {
                    "language": "fa",
                    "value": "\u0631\u062f\u0647:\u0645\u0642\u0627\u0644\u0647\u200c\u0647\u0627\u06cc \u0646\u0627\u0645\u0632\u062f \u062d\u0630\u0641"
                },
                "fi": {
                    "language": "fi",
                    "value": "Luokka:Poistettavat"
                },
                "fr": {
                    "language": "fr",
                    "value": "Cat\u00e9gorie:Page propos\u00e9e \u00e0 la suppression"
                },
                "hsb": {
                    "language": "hsb",
                    "value": "Kategorija:Kandidaty za \u0161m\u00f3rnjenje"
                },
                "ia": {
                    "language": "ia",
                    "value": "Categoria:Paginas sub voto pro deletion"
                },
                "ja": {
                    "language": "ja",
                    "value": "Category:\u524a\u9664\u4f9d\u983c\u4e2d\u306e\u30da\u30fc\u30b8"
                },
                "ko": {
                    "language": "ko",
                    "value": "\ubd84\ub958:\uc0ad\uc81c \ud1a0\ub860"
                },
                "mk": {
                    "language": "mk",
                    "value": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0458\u0430:\u0421\u0442\u0430\u0442\u0438\u0438 \u0437\u0430 \u0431\u0440\u0438\u0448\u0435\u045a\u0435"
                },
                "pt": {
                    "language": "pt",
                    "value": "Categoria:!P\u00e1ginas para eliminar"
                },
                "ru": {
                    "language": "ru",
                    "value": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f:\u0412\u0438\u043a\u0438\u043f\u0435\u0434\u0438\u044f:\u041a\u0430\u043d\u0434\u0438\u0434\u0430\u0442\u044b \u043d\u0430 \u0443\u0434\u0430\u043b\u0435\u043d\u0438\u0435"
                },
                "sv": {
                    "language": "sv",
                    "value": "Kategori:Sidor f\u00f6reslagna f\u00f6r radering"
                },
                "yi": {
                    "language": "yi",
                    "value": "\u05e7\u05d0\u05b7\u05d8\u05e2\u05d2\u05d0\u05b8\u05e8\u05d9\u05e2:\u05d2\u05e2\u05e9\u05d8\u05e2\u05dc\u05d8\u05e2 \u05e6\u05d5 \u05de\u05e2\u05e7\u05df"
                },
                "zh": {
                    "language": "zh",
                    "value": "Category:\u6761\u76ee\u5220\u9664\u5019\u9009"
                },
                "cs": {
                    "language": "cs",
                    "value": "Kategorie:Str\u00e1nky navr\u017een\u00e9 ke smaz\u00e1n\u00ed"
                },
                "eo": {
                    "language": "eo",
                    "value": "Kategorio:Forigendaj artikoloj"
                },
                "ur": {
                    "language": "ur",
                    "value": "\u0632\u0645\u0631\u06c1:\u0645\u0636\u0627\u0645\u06cc\u0646 \u0628\u0631\u0627\u0626\u06d2 \u062d\u0630\u0641"
                },
                "da": {
                    "language": "da",
                    "value": "Kategori:Sletningsforslag"
                },
                "simple": {
                    "language": "simple",
                    "value": "Category:Deletion requests"
                },
                "gu": {
                    "language": "gu",
                    "value": "\u0ab6\u0acd\u0ab0\u0ac7\u0aa3\u0ac0:Deletion requests"
                },
                "sk": {
                    "language": "sk",
                    "value": "Kateg\u00f3ria:Wikip\u00e9dia:Kandid\u00e1ti na zmazanie"
                },
                "bg": {
                    "language": "bg",
                    "value": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f:\u041f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u044f \u0437\u0430 \u0438\u0437\u0442\u0440\u0438\u0432\u0430\u043d\u0435"
                },
                "kw": {
                    "language": "kw",
                    "value": "Klass:Ombrofyoryon rag dileans"
                },
                "nn": {
                    "language": "nn",
                    "value": "Kategori:Sider merkte for sletting"
                },
                "de": {
                    "language": "de",
                    "value": "Kategorie:Wikipedia:L\u00f6schkandidat/Seiten"
                },
                "oc": {
                    "language": "oc",
                    "value": "Categoria:Wikip\u00e8dia:Supression"
                },
                "uk": {
                    "language": "uk",
                    "value": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0456\u044f:\u0421\u0442\u0430\u0442\u0442\u0456-\u043a\u0430\u043d\u0434\u0438\u0434\u0430\u0442\u0438 \u043d\u0430 \u0432\u0438\u043b\u0443\u0447\u0435\u043d\u043d\u044f"
                },
                "vls": {
                    "language": "vls",
                    "value": "Categorie:Wikipedia:Weg"
                },
                "nl": {
                    "language": "nl",
                    "value": "Categorie:Wikipedia:Pagina weg"
                },
                "af": {
                    "language": "af",
                    "value": "Kategorie:Bladsye vir verwydering"
                },
                "be": {
                    "language": "be",
                    "value": "\u041a\u0430\u0442\u044d\u0433\u043e\u0440\u044b\u044f:\u0412\u0456\u043a\u0456\u043f\u0435\u0434\u044b\u044f:\u0412\u044b\u0434\u0430\u043b\u0435\u043d\u043d\u0435 \u0441\u0442\u0430\u0440\u043e\u043d\u0430\u043a"
                },
                "it": {
                    "language": "it",
                    "value": "Categoria:Richieste di cancellazione"
                },
                "nap": {
                    "language": "nap",
                    "value": "Categur\u00eca:Paggene 'a scancell\u00e0"
                },
                "ar": {
                    "language": "ar",
                    "value": "\u062a\u0635\u0646\u064a\u0641:\u0635\u0641\u062d\u0627\u062a \u062a\u062e\u0636\u0639 \u0644\u0646\u0642\u0627\u0634 \u0627\u0644\u062d\u0630\u0641"
                },
                "ext": {
                    "language": "ext",
                    "value": "Category:Art\u00edculus pol esborral"
                },
                "wa": {
                    "language": "wa",
                    "value": "Categoreye:P\u00e5djes a disfacer"
                },
                "csb": {
                    "language": "csb",
                    "value": "Kateg\u00f2r\u00ebj\u00f4:Artikle do r\u00ebmni\u00e3c\u00f4"
                }
            },
            "descriptions": {
                "fr": {
                    "language": "fr",
                    "value": "page de cat\u00e9gorie d'un projet Wikimedia"
                },
                "es": {
                    "language": "es",
                    "value": "categor\u00eda de Wikipedia"
                },
                "de": {
                    "language": "de",
                    "value": "Wikimedia-Kategorie"
                },
                "it": {
                    "language": "it",
                    "value": "categoria di un progetto Wikimedia"
                },
                "pt": {
                    "language": "pt",
                    "value": "categoria de um projeto da Wikimedia"
                },
                "pt-br": {
                    "language": "pt-br",
                    "value": "categoria de um projeto da Wikimedia"
                },
                "ru": {
                    "language": "ru",
                    "value": "\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f \u0432 \u043f\u0440\u043e\u0435\u043a\u0442\u0435 \u0412\u0438\u043a\u0438\u043c\u0435\u0434\u0438\u0430"
                },
                "sv": {
                    "language": "sv",
                    "value": "kategorisida"
                },
                "en": {
                    "language": "en",
                    "value": "A category for articles to be deleted, not speedily"
                }
            },
            "claims": {
                "P31": [
                    {
                        "id": "q4989296$DC49C8D0-FF2A-4A27-86BC-1DBBAE125FEC",
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P31",
                            "datatype": "wikibase-item",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 15647814
                                },
                                "type": "wikibase-entityid"
                            }
                        },
                        "type": "statement",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "2b2e2969856fa3920ccaa143d169b94c6ec43589",
                                "snaks": {
                                    "P143": [
                                        {
                                            "snaktype": "value",
                                            "property": "P143",
                                            "datatype": "wikibase-item",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 4115441
                                                },
                                                "type": "wikibase-entityid"
                                            }
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P143"
                                ]
                            },
                            {
                                "hash": "5529b10d4eab9f71e5b729897f3b4c21ad94bbf3",
                                "snaks": {
                                    "P143": [
                                        {
                                            "snaktype": "value",
                                            "property": "P143",
                                            "datatype": "wikibase-item",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 199698
                                                },
                                                "type": "wikibase-entityid"
                                            }
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P143"
                                ]
                            }
                        ]
                    },
                    {
                        "id": "Q4989296$8E0429E5-05D0-4D80-8882-5491F53D7C7A",
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P31",
                            "datatype": "wikibase-item",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 4167836
                                },
                                "type": "wikibase-entityid"
                            }
                        },
                        "type": "statement",
                        "rank": "normal"
                    }
                ],
                "P279": [
                    {
                        "id": "Q4989296$014f9faf-40aa-ebb2-af6b-66423debbf8e",
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P279",
                            "datatype": "wikibase-item",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 4615845
                                },
                                "type": "wikibase-entityid"
                            }
                        },
                        "type": "statement",
                        "rank": "normal"
                    }
                ]
            },
            "sitelinks": {
                "afwiki": {
                    "site": "afwiki",
                    "title": "Kategorie:Bladsye vir verwydering",
                    "badges": []
                },
                "arwikisource": {
                    "site": "arwikisource",
                    "title": "\u062a\u0635\u0646\u064a\u0641:\u0635\u0641\u062d\u0627\u062a \u062a\u062e\u0636\u0639 \u0644\u0646\u0642\u0627\u0634 \u0627\u0644\u062d\u0630\u0641",
                    "badges": []
                },
                "bewiki": {
                    "site": "bewiki",
                    "title": "\u041a\u0430\u0442\u044d\u0433\u043e\u0440\u044b\u044f:\u0412\u0456\u043a\u0456\u043f\u0435\u0434\u044b\u044f:\u0412\u044b\u0434\u0430\u043b\u0435\u043d\u043d\u0435 \u0441\u0442\u0430\u0440\u043e\u043d\u0430\u043a",
                    "badges": []
                },
                "bgwiki": {
                    "site": "bgwiki",
                    "title": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f:\u041f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u044f \u0437\u0430 \u0438\u0437\u0442\u0440\u0438\u0432\u0430\u043d\u0435",
                    "badges": []
                },
                "csbwiki": {
                    "site": "csbwiki",
                    "title": "Kateg\u00f2r\u00ebj\u00f4:Artikle do r\u00ebmni\u00e3c\u00f4",
                    "badges": []
                },
                "cswiki": {
                    "site": "cswiki",
                    "title": "Kategorie:Str\u00e1nky navr\u017een\u00e9 ke smaz\u00e1n\u00ed",
                    "badges": []
                },
                "dsbwiki": {
                    "site": "dsbwiki",
                    "title": "Kategorija:Kandidaty za la\u0161owanje",
                    "badges": []
                },
                "enwiki": {
                    "site": "enwiki",
                    "title": "Category:Articles for deletion",
                    "badges": []
                },
                "eowiki": {
                    "site": "eowiki",
                    "title": "Kategorio:Forigendaj artikoloj",
                    "badges": []
                },
                "eswiki": {
                    "site": "eswiki",
                    "title": "Categor\u00eda:Wikipedia:Consultas de borrado",
                    "badges": []
                },
                "eswikisource": {
                    "site": "eswikisource",
                    "title": "Categor\u00eda:Wikisource:P\u00e1ginas para borrar",
                    "badges": []
                },
                "etwiki": {
                    "site": "etwiki",
                    "title": "Kategooria:Kustutamiseks esitatud artiklid",
                    "badges": []
                },
                "extwiki": {
                    "site": "extwiki",
                    "title": "Category:Art\u00edculus pol esborral",
                    "badges": []
                },
                "fawiki": {
                    "site": "fawiki",
                    "title": "\u0631\u062f\u0647:\u0645\u0642\u0627\u0644\u0647\u200c\u0647\u0627\u06cc \u0646\u0627\u0645\u0632\u062f \u062d\u0630\u0641",
                    "badges": []
                },
                "frwiki": {
                    "site": "frwiki",
                    "title": "Cat\u00e9gorie:Page propos\u00e9e \u00e0 la suppression",
                    "badges": []
                },
                "frwikiquote": {
                    "site": "frwikiquote",
                    "title": "Cat\u00e9gorie:Page propos\u00e9e \u00e0 la suppression",
                    "badges": []
                },
                "hsbwiki": {
                    "site": "hsbwiki",
                    "title": "Kategorija:Kandidaty za \u0161m\u00f3rnjenje",
                    "badges": []
                },
                "iawiki": {
                    "site": "iawiki",
                    "title": "Categoria:Paginas sub voto pro deletion",
                    "badges": []
                },
                "itwiki": {
                    "site": "itwiki",
                    "title": "Categoria:Pagine in cancellazione per argomento",
                    "badges": []
                },
                "jawiki": {
                    "site": "jawiki",
                    "title": "Category:\u524a\u9664\u4f9d\u983c\u4e2d\u306e\u30da\u30fc\u30b8",
                    "badges": []
                },
                "knwiki": {
                    "site": "knwiki",
                    "title": "\u0cb5\u0cb0\u0ccd\u0c97:\u0c85\u0cb3\u0cbf\u0cb8\u0cc1\u0cb5\u0cbf\u0c95\u0cc6\u0c97\u0cc6 \u0cb9\u0cbe\u0c95\u0cb2\u0cbe\u0c97\u0cbf\u0cb0\u0cc1\u0cb5 \u0cb2\u0cc7\u0c96\u0ca8\u0c97\u0cb3\u0cc1",
                    "badges": []
                },
                "kowiki": {
                    "site": "kowiki",
                    "title": "\ubd84\ub958:\uc0ad\uc81c \ud1a0\ub860",
                    "badges": []
                },
                "kwwiki": {
                    "site": "kwwiki",
                    "title": "Klass:Ombrofyoryon rag dileans",
                    "badges": []
                },
                "mkwiki": {
                    "site": "mkwiki",
                    "title": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0458\u0430:\u0421\u0442\u0430\u0442\u0438\u0438 \u0437\u0430 \u0431\u0440\u0438\u0448\u0435\u045a\u0435",
                    "badges": []
                },
                "napwiki": {
                    "site": "napwiki",
                    "title": "Categur\u00eca:Paggene 'a scancell\u00e0",
                    "badges": []
                },
                "nlwiki": {
                    "site": "nlwiki",
                    "title": "Categorie:Wikipedia:Pagina weg",
                    "badges": []
                },
                "nlwikiquote": {
                    "site": "nlwikiquote",
                    "title": "Categorie:Wikiquote:Te verwijderen pagina's",
                    "badges": []
                },
                "nnwiki": {
                    "site": "nnwiki",
                    "title": "Kategori:Sider merkte for sletting",
                    "badges": []
                },
                "ptwiki": {
                    "site": "ptwiki",
                    "title": "Categoria:!P\u00e1ginas para eliminar",
                    "badges": []
                },
                "ptwikiquote": {
                    "site": "ptwikiquote",
                    "title": "Categoria:!P\u00e1ginas para eliminar",
                    "badges": []
                },
                "ruwiki": {
                    "site": "ruwiki",
                    "title": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f:\u0412\u0438\u043a\u0438\u043f\u0435\u0434\u0438\u044f:\u041a\u0430\u043d\u0434\u0438\u0434\u0430\u0442\u044b \u043d\u0430 \u0443\u0434\u0430\u043b\u0435\u043d\u0438\u0435",
                    "badges": []
                },
                "skwiki": {
                    "site": "skwiki",
                    "title": "Kateg\u00f3ria:Wikip\u00e9dia:Kandid\u00e1ti na zmazanie",
                    "badges": []
                },
                "sqwiki": {
                    "site": "sqwiki",
                    "title": "Kategoria:Faqe p\u00ebr grisje",
                    "badges": []
                },
                "svwiki": {
                    "site": "svwiki",
                    "title": "Kategori:Sidor f\u00f6reslagna f\u00f6r radering",
                    "badges": []
                },
                "svwikiquote": {
                    "site": "svwikiquote",
                    "title": "Kategori:Sidor f\u00f6reslagna f\u00f6r radering",
                    "badges": []
                },
                "ukwiki": {
                    "site": "ukwiki",
                    "title": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0456\u044f:\u0421\u0442\u0430\u0442\u0442\u0456-\u043a\u0430\u043d\u0434\u0438\u0434\u0430\u0442\u0438 \u043d\u0430 \u0432\u0438\u043b\u0443\u0447\u0435\u043d\u043d\u044f",
                    "badges": []
                },
                "urwiki": {
                    "site": "urwiki",
                    "title": "\u0632\u0645\u0631\u06c1:\u0645\u0636\u0627\u0645\u06cc\u0646 \u0628\u0631\u0627\u0626\u06d2 \u062d\u0630\u0641",
                    "badges": []
                },
                "wawiki": {
                    "site": "wawiki",
                    "title": "Categoreye:P\u00e5djes a disfacer",
                    "badges": []
                },
                "yiwiki": {
                    "site": "yiwiki",
                    "title": "\u05e7\u05d0\u05b7\u05d8\u05e2\u05d2\u05d0\u05b8\u05e8\u05d9\u05e2:\u05d2\u05e2\u05e9\u05d8\u05e2\u05dc\u05d8\u05e2 \u05e6\u05d5 \u05de\u05e2\u05e7\u05df",
                    "badges": []
                },
                "zhwiki": {
                    "site": "zhwiki",
                    "title": "Category:\u6761\u76ee\u5220\u9664\u5019\u9009",
                    "badges": []
                }
            }
        }
    },
    "success": 1
}

#Category:Proposed deletion
#https://www.wikidata.org/wiki/Q7927732
#https://www.wikidata.org/w/api.php?action=wbgetentities&ids=Q7927732
proposed_deletion = {
    "entities": {
        "Q7927732": {
            "pageid": 7867109,
            "ns": 0,
            "title": "Q7927732",
            "lastrevid": 172921296,
            "modified": "2014-11-11T03:57:22Z",
            "id": "Q7927732",
            "type": "item",
            "labels": {
                "en": {
                    "language": "en",
                    "value": "Category:Proposed deletion"
                },
                "es": {
                    "language": "es",
                    "value": "Categor\u00eda:Wikipedia:Propuestas de borrado"
                },
                "ja": {
                    "language": "ja",
                    "value": "Category:\u63d0\u6848\u524a\u9664"
                },
                "fa": {
                    "language": "fa",
                    "value": "\u0635\u0641\u062d\u0647\u200c\u0647\u0627\u06cc \u062d\u0630\u0641 \u0632\u0645\u0627\u0646\u200c\u062f\u0627\u0631"
                },
                "ur": {
                    "language": "ur",
                    "value": "\u0645\u062c\u0648\u0632\u06c1 \u062d\u0630\u0641 \u0634\u062f\u06af\u06cc\u0627\u06ba"
                },
                "lt": {
                    "language": "lt",
                    "value": "Kategorija:Kandidatai trinti"
                },
                "pt-br": {
                    "language": "pt-br",
                    "value": "Categoria:!P\u00e1ginas para elimina\u00e7\u00e3o semirr\u00e1pida"
                },
                "tt": {
                    "language": "tt",
                    "value": "\u0422\u04e9\u0440\u043a\u0435\u043c:\u0411\u0435\u0442\u0435\u0440\u04af\u0433\u04d9 \u043a\u0430\u043d\u0434\u0438\u0434\u0430\u0442\u043b\u0430\u0440"
                },
                "pt": {
                    "language": "pt",
                    "value": "Categoria:!P\u00e1ginas para elimina\u00e7\u00e3o semirr\u00e1pida"
                },
                "ru": {
                    "language": "ru",
                    "value": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f:\u0412\u0438\u043a\u0438\u043c\u0435\u0434\u0438\u044f:\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u044b \u043a \u0443\u0434\u0430\u043b\u0435\u043d\u0438\u044e"
                },
                "en-ca": {
                    "language": "en-ca",
                    "value": "Category:Proposed deletion"
                },
                "en-gb": {
                    "language": "en-gb",
                    "value": "Category:Proposed deletion"
                },
                "ba": {
                    "language": "ba",
                    "value": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f:\u0412\u0438\u043a\u0438\u043f\u0435\u0434\u0438\u044f:\u042e\u0439\u044b\u043b\u0430\u0441\u0430\u04a1 \u043c\u04d9\u04a1\u04d9\u043b\u04d9\u043b\u04d9\u0440"
                },
                "it": {
                    "language": "it",
                    "value": "Categoria:Da cancellare"
                }
            },
            "descriptions": {
                "fr": {
                    "language": "fr",
                    "value": "page de cat\u00e9gorie d'un projet Wikimedia"
                },
                "es": {
                    "language": "es",
                    "value": "categor\u00eda de Wikimedia"
                },
                "it": {
                    "language": "it",
                    "value": "categoria di un progetto Wikimedia"
                },
                "pt": {
                    "language": "pt",
                    "value": "categoria de um projeto da Wikimedia"
                },
                "pt-br": {
                    "language": "pt-br",
                    "value": "categoria de um projeto da Wikimedia"
                },
                "de": {
                    "language": "de",
                    "value": "Wikimedia-Kategorie"
                },
                "ru": {
                    "language": "ru",
                    "value": "\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f \u0432 \u043f\u0440\u043e\u0435\u043a\u0442\u0435 \u0412\u0438\u043a\u0438\u043c\u0435\u0434\u0438a"
                },
                "sv": {
                    "language": "sv",
                    "value": "Wikimedia-kategori"
                },
                "bn": {
                    "language": "bn",
                    "value": "\u0989\u0987\u0995\u09bf\u09aa\u09bf\u09a1\u09bf\u09af\u09bc\u09be \u09ac\u09bf\u09b7\u09af\u09bc\u09b6\u09cd\u09b0\u09c7\u09a3\u09c0"
                },
                "ckb": {
                    "language": "ckb",
                    "value": "\u067e\u06c6\u0644\u06cc \u0648\u06cc\u06a9\u06cc\u067e\u06cc\u062f\u06cc\u0627"
                },
                "cs": {
                    "language": "cs",
                    "value": "kategorie Wikimedie"
                },
                "da": {
                    "language": "da",
                    "value": "Wikimedia-kategori"
                },
                "en": {
                    "language": "en",
                    "value": "Wikimedia category page"
                },
                "fa": {
                    "language": "fa",
                    "value": "\u0631\u062f\u0647\u0654 \u0648\u06cc\u06a9\u06cc\u200c\u0645\u062f\u06cc\u0627"
                },
                "fi": {
                    "language": "fi",
                    "value": "Wikimedia-luokka"
                },
                "gl": {
                    "language": "gl",
                    "value": "categor\u00eda de Wikimedia"
                },
                "gu": {
                    "language": "gu",
                    "value": "\u0ab5\u0abf\u0a95\u0abf\u0aaa\u0ac0\u0aa1\u0abf\u0aaf\u0abe \u0ab6\u0acd\u0ab0\u0ac7\u0aa3\u0ac0"
                },
                "he": {
                    "language": "he",
                    "value": "\u05e7\u05d8\u05d2\u05d5\u05e8\u05d9\u05d4 \u05d1\u05d5\u05d5\u05d9\u05e7\u05d9\u05e4\u05d3\u05d9\u05d4"
                },
                "mk": {
                    "language": "mk",
                    "value": "\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0458\u0430 \u043d\u0430 \u0412\u0438\u043a\u0438\u043f\u0435\u0434\u0438\u0458\u0430"
                },
                "ja": {
                    "language": "ja",
                    "value": "\u30a6\u30a3\u30ad\u30e1\u30c7\u30a3\u30a2\u306e\u30ab\u30c6\u30b4\u30ea"
                },
                "ko": {
                    "language": "ko",
                    "value": "\uc704\ud0a4\ubbf8\ub514\uc5b4 \ubd84\ub958"
                },
                "nb": {
                    "language": "nb",
                    "value": "Wikimedia-kategori"
                },
                "nds": {
                    "language": "nds",
                    "value": "Kategorie op Wikimedia"
                },
                "nn": {
                    "language": "nn",
                    "value": "Wikimedia-kategori"
                },
                "pl": {
                    "language": "pl",
                    "value": "kategoria projektu Wikimedia"
                },
                "zh": {
                    "language": "zh",
                    "value": "\u7ef4\u57fa\u5a92\u4f53\u5de5\u7a0b\u5206\u7c7b"
                },
                "zh-hans": {
                    "language": "zh-hans",
                    "value": "\u7ef4\u57fa\u5a92\u4f53\u5de5\u7a0b\u5206\u7c7b"
                },
                "zh-hant": {
                    "language": "zh-hant",
                    "value": "\u7dad\u57fa\u5a92\u9ad4\u5de5\u7a0b\u5206\u985e"
                },
                "nl": {
                    "language": "nl",
                    "value": "Wikimedia-categorie"
                },
                "et": {
                    "language": "et",
                    "value": "Wikimedia kategooria"
                }
            },
            "claims": {
                "P31": [
                    {
                        "id": "Q7927732$32133E5A-FB94-4C1B-954A-1FDE599DAB18",
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P31",
                            "datatype": "wikibase-item",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 4167836
                                },
                                "type": "wikibase-entityid"
                            }
                        },
                        "type": "statement",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "7eb64cf9621d34c54fd4bd040ed4b61a88c4a1a0",
                                "snaks": {
                                    "P143": [
                                        {
                                            "snaktype": "value",
                                            "property": "P143",
                                            "datatype": "wikibase-item",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 328
                                                },
                                                "type": "wikibase-entityid"
                                            }
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P143"
                                ]
                            },
                            {
                                "hash": "d6e3ab4045fb3f3feea77895bc6b27e663fc878a",
                                "snaks": {
                                    "P143": [
                                        {
                                            "snaktype": "value",
                                            "property": "P143",
                                            "datatype": "wikibase-item",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 206855
                                                },
                                                "type": "wikibase-entityid"
                                            }
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P143"
                                ]
                            }
                        ]
                    }
                ]
            },
            "sitelinks": {
                "bawiki": {
                    "site": "bawiki",
                    "title": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f:\u0412\u0438\u043a\u0438\u043f\u0435\u0434\u0438\u044f:\u042e\u0439\u044b\u043b\u0430\u0441\u0430\u04a1 \u043c\u04d9\u04a1\u04d9\u043b\u04d9\u043b\u04d9\u0440",
                    "badges": []
                },
                "enwiki": {
                    "site": "enwiki",
                    "title": "Category:Proposed deletion",
                    "badges": []
                },
                "enwikiquote": {
                    "site": "enwikiquote",
                    "title": "Category:Proposed deletion",
                    "badges": []
                },
                "eswiki": {
                    "site": "eswiki",
                    "title": "Categor\u00eda:Wikipedia:Propuestas de borrado",
                    "badges": []
                },
                "fawiki": {
                    "site": "fawiki",
                    "title": "\u0631\u062f\u0647:\u0635\u0641\u062d\u0647\u200c\u0647\u0627\u06cc \u062d\u0630\u0641 \u0632\u0645\u0627\u0646\u200c\u062f\u0627\u0631",
                    "badges": []
                },
                "itwikiquote": {
                    "site": "itwikiquote",
                    "title": "Categoria:Da cancellare",
                    "badges": []
                },
                "jawiki": {
                    "site": "jawiki",
                    "title": "Category:\u63d0\u6848\u524a\u9664",
                    "badges": []
                },
                "ltwiki": {
                    "site": "ltwiki",
                    "title": "Kategorija:Kandidatai trinti",
                    "badges": []
                },
                "ltwikisource": {
                    "site": "ltwikisource",
                    "title": "Kategorija:Kandidatai skubiai trinti",
                    "badges": []
                },
                "ptwiki": {
                    "site": "ptwiki",
                    "title": "Categoria:!P\u00e1ginas para elimina\u00e7\u00e3o semirr\u00e1pida",
                    "badges": []
                },
                "ruwiki": {
                    "site": "ruwiki",
                    "title": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f:\u0412\u0438\u043a\u0438\u043f\u0435\u0434\u0438\u044f:\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u044b \u043a \u0443\u0434\u0430\u043b\u0435\u043d\u0438\u044e",
                    "badges": []
                },
                "ruwikisource": {
                    "site": "ruwikisource",
                    "title": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f:\u0412\u0438\u043a\u0438\u0442\u0435\u043a\u0430:\u0421\u0442\u0430\u0442\u044c\u0438 \u043a \u0443\u0434\u0430\u043b\u0435\u043d\u0438\u044e",
                    "badges": []
                },
                "ttwiki": {
                    "site": "ttwiki",
                    "title": "\u0422\u04e9\u0440\u043a\u0435\u043c:\u0411\u0435\u0442\u0435\u0440\u04af\u0433\u04d9 \u043a\u0430\u043d\u0434\u0438\u0434\u0430\u0442\u043b\u0430\u0440",
                    "badges": []
                },
                "urwiki": {
                    "site": "urwiki",
                    "title": "\u0632\u0645\u0631\u06c1:\u0645\u062c\u0648\u0632\u06c1 \u062d\u0630\u0641 \u0634\u062f\u06af\u06cc\u0627\u06ba",
                    "badges": []
                }
            }
        }
    },
    "success": 1
}

#starting point is :
#speedydeletion
#https://www.wikidata.org/w/api.php?action=wbgetentities&ids=Q5964

speedy_deletion = {
    "entities": {
        "Q5964": {
            "pageid": 7063,
            "ns": 0,
            "title": "Q5964",
            "lastrevid": 175954810,
            "modified": "2014-11-22T11:33:57Z",
            "id": "Q5964",
            "type": "item",
            "labels": {
                "de": {
                    "language": "de",
                    "value": "Kategorie:Wikipedia:Schnelll\u00f6schen"
                },
                "fr": {
                    "language": "fr",
                    "value": "Cat\u00e9gorie:Wiki:Suppression imm\u00e9diate demand\u00e9e"
                },
                "en": {
                    "language": "en",
                    "value": "Category:Candidates for speedy deletion"
                },
                "ru": {
                    "language": "ru",
                    "value": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f:\u0412\u0438\u043a\u0438\u043f\u0435\u0434\u0438\u044f:\u041a \u0431\u044b\u0441\u0442\u0440\u043e\u043c\u0443 \u0443\u0434\u0430\u043b\u0435\u043d\u0438\u044e"
                },
                "ab": {
                    "language": "ab",
                    "value": "\u0410\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0430:Candidates for speedy deletion"
                },
                "ace": {
                    "language": "ace",
                    "value": "Kawan:\u00d4n-\u00f4n nyang peureul\u00e8\u00eb geusamp\u00f4h rijang"
                },
                "af": {
                    "language": "af",
                    "value": "Kategorie:Kandidate vir spoedige verwydering"
                },
                "ak": {
                    "language": "ak",
                    "value": "Kategori:Candidates for speedy deletion"
                },
                "am": {
                    "language": "am",
                    "value": "\u1218\u12f0\u1265:\u1208\u121b\u1325\u134b\u1275 \u12e8\u1240\u1228\u1261 \u1308\u133e\u127d"
                },
                "an": {
                    "language": "an",
                    "value": "Categor\u00eda:Borrar"
                },
                "ang": {
                    "language": "ang",
                    "value": "Flocc:Candidates for speedy deletion"
                },
                "ar": {
                    "language": "ar",
                    "value": "\u062a\u0635\u0646\u064a\u0641:\u0635\u0641\u062d\u0627\u062a \u0644\u0644\u062d\u0630\u0641 \u0627\u0644\u0633\u0631\u064a\u0639"
                },
                "arc": {
                    "language": "arc",
                    "value": "\u0723\u0715\u072a\u0710:Candidates for speedy deletion"
                },
                "arz": {
                    "language": "arz",
                    "value": "\u062a\u0635\u0646\u064a\u0641:\u0635\u0641\u062d \u0639\u0634\u0627\u0646 \u062a\u062a\u0645\u0633\u062d \u0628\u0633\u0631\u0639\u0647 \u0645\u0646-\u063a\u064a\u0631 \u0633\u0628\u0628"
                },
                "ast": {
                    "language": "ast",
                    "value": "Categor\u00eda:Uiquipedia:Destruir"
                },
                "av": {
                    "language": "av",
                    "value": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f:Candidates for speedy deletion"
                },
                "ay": {
                    "language": "ay",
                    "value": "Categor\u00eda:Candidatos para ser borrados"
                },
                "az": {
                    "language": "az",
                    "value": "Kateqoriya:Vikipediya:Silin\u0259c\u0259k s\u0259hif\u0259l\u0259r"
                },
                "ba": {
                    "language": "ba",
                    "value": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f:Delete"
                },
                "bar": {
                    "language": "bar",
                    "value": "Kategorie:Wikipedia:Schnelll\u00f6schen"
                },
                "bcl": {
                    "language": "bcl",
                    "value": "Kategorya:Tolos-tolos na mga pagpar\u00e0"
                },
                "be": {
                    "language": "be",
                    "value": "\u041a\u0430\u0442\u044d\u0433\u043e\u0440\u044b\u044f:\u0410\u0440\u0442\u044b\u043a\u0443\u043b\u044b \u0434\u0430 \u0432\u044b\u0434\u0430\u043b\u0435\u043d\u043d\u044f"
                },
                "bg": {
                    "language": "bg",
                    "value": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f:\u041f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u044f \u0437\u0430 \u0438\u0437\u0442\u0440\u0438\u0432\u0430\u043d\u0435"
                },
                "bh": {
                    "language": "bh",
                    "value": "\u0936\u094d\u0930\u0947\u0923\u0940:Candidates for speedy deletion"
                },
                "bi": {
                    "language": "bi",
                    "value": "Category:Candidates for speedy deletion"
                },
                "bjn": {
                    "language": "bjn",
                    "value": "Tumbung:Artikal nang layak hagan dihapus"
                },
                "bm": {
                    "language": "bm",
                    "value": "Cat\u00e9gorie:Deleteme"
                },
                "bo": {
                    "language": "bo",
                    "value": "Category:Candidates for speedy deletion"
                },
                "bpy": {
                    "language": "bpy",
                    "value": "\u09a5\u09be\u0995:Candidates for speedy deletion"
                },
                "br": {
                    "language": "br",
                    "value": "Rummad:Candidates for speedy deletion"
                },
                "bs": {
                    "language": "bs",
                    "value": "Kategorija:Kandidati za brisanje"
                },
                "bug": {
                    "language": "bug",
                    "value": "Kategori:Candidates for speedy deletion"
                },
                "bxr": {
                    "language": "bxr",
                    "value": "Category:Candidates for speedy deletion"
                },
                "ca": {
                    "language": "ca",
                    "value": "Categoria:Sol\u00b7licituds de supressi\u00f3 immediata"
                },
                "cbk-zam": {
                    "language": "cbk-zam",
                    "value": "Categor\u00eda:Maga Pagina Nominado Para Bora"
                },
                "cdo": {
                    "language": "cdo",
                    "value": "Category:Ch\u00e9\u0324\u1e73k-k\u00e1ik ch\u0113ng-d\u1e73\u0300"
                },
                "ce": {
                    "language": "ce",
                    "value": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438:\u0412\u0438\u043a\u0438\u043f\u0435\u0434\u0438:\u0421\u0438\u0445\u0430 \u0434\u04c0\u0430\u044f\u043a\u043a\u0445\u0430\u0440\u0435 \u0434\u0438\u043b\u043b\u0430\u0440"
                },
                "ceb": {
                    "language": "ceb",
                    "value": "Kategoriya:Kandidato sa pagtangtang dayon"
                },
                "ch": {
                    "language": "ch",
                    "value": "Katigoria:Candidates for speedy deletion"
                },
                "chr": {
                    "language": "chr",
                    "value": "Category:Candidates for speedy deletion"
                },
                "chy": {
                    "language": "chy",
                    "value": "Category:Candidates for speedy deletion"
                },
                "ckb": {
                    "language": "ckb",
                    "value": "\u067e\u06c6\u0644:\u067e\u06d5\u0695\u06d5\u06a9\u0627\u0646 \u0628\u06c6 \u0633\u0695\u06cc\u0646\u06d5\u0648\u06d5\u06cc \u062e\u06ce\u0631\u0627"
                },
                "co": {
                    "language": "co",
                    "value": "Category:Da supprim\u00e0"
                },
                "cr": {
                    "language": "cr",
                    "value": "Category:Candidates for speedy deletion"
                },
                "cs": {
                    "language": "cs",
                    "value": "Kategorie:Str\u00e1nky ke smaz\u00e1n\u00ed"
                },
                "csb": {
                    "language": "csb",
                    "value": "Kateg\u00f2r\u00ebj\u00f4:Artikle do r\u00ebmni\u00e3c\u00f4"
                },
                "cv": {
                    "language": "cv",
                    "value": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438:\u0422\u04f3\u0440\u0435\u0445 \u043a\u0103\u043b\u0430\u0440\u0441\u0430 \u043f\u0103\u0440\u0430\u0445\u043c\u0430\u043b\u043b\u0438 \u0441\u0442\u0430\u0442\u044c\u044f\u0441\u0435\u043c"
                },
                "cy": {
                    "language": "cy",
                    "value": "Categori:Tudalennau amheus"
                },
                "da": {
                    "language": "da",
                    "value": "Kategori:Sletningsforslag"
                },
                "diq": {
                    "language": "diq",
                    "value": "Kategoriye:Bestere"
                },
                "dsb": {
                    "language": "dsb",
                    "value": "Kategorija:Boki k malsnemu la\u0161owanju"
                },
                "dv": {
                    "language": "dv",
                    "value": "\u07a4\u07a8\u0790\u07b0\u0789\u07aa:Candidates for speedy deletion"
                },
                "dz": {
                    "language": "dz",
                    "value": "Category:Candidates for speedy deletion"
                },
                "ee": {
                    "language": "ee",
                    "value": "Category:Candidates for speedy deletion"
                },
                "el": {
                    "language": "el",
                    "value": "\u039a\u03b1\u03c4\u03b7\u03b3\u03bf\u03c1\u03af\u03b1:\u03a3\u03b5\u03bb\u03af\u03b4\u03b5\u03c2 \u03b3\u03b9\u03b1 \u03b3\u03c1\u03ae\u03b3\u03bf\u03c1\u03b7 \u03b4\u03b9\u03b1\u03b3\u03c1\u03b1\u03c6\u03ae"
                },
                "eml": {
                    "language": "eml",
                    "value": "Categoria:CANCELLA"
                },
                "en-ca": {
                    "language": "en-ca",
                    "value": "Category:Candidates for speedy deletion"
                },
                "en-gb": {
                    "language": "en-gb",
                    "value": "Category:Candidates for speedy deletion"
                },
                "eo": {
                    "language": "eo",
                    "value": "Kategorio:Forigendaj artikoloj"
                },
                "es": {
                    "language": "es",
                    "value": "Categor\u00eda:Wikipedia:Borrar (definitivo)"
                },
                "eu": {
                    "language": "eu",
                    "value": "Kategoria:Ezabatzeko"
                },
                "ext": {
                    "language": "ext",
                    "value": "Category:Art\u00edculus pol esborral"
                },
                "fa": {
                    "language": "fa",
                    "value": "\u0631\u062f\u0647:\u0645\u0642\u0627\u0644\u0647\u200c\u0647\u0627\u06cc \u0646\u0627\u0645\u0632\u062f \u062d\u0630\u0641 \u0633\u0631\u06cc\u0639"
                },
                "ff": {
                    "language": "ff",
                    "value": "Cat\u00e9gorie:Candidates for speedy deletion"
                },
                "fi": {
                    "language": "fi",
                    "value": "Luokka:Pikapoisto"
                },
                "fj": {
                    "language": "fj",
                    "value": "Category:Candidates for speedy deletion"
                },
                "fo": {
                    "language": "fo",
                    "value": "B\u00f3lkur:Strikingarbo\u00f0"
                },
                "frp": {
                    "language": "frp",
                    "value": "Cat\u00e8gorie:Candidates for speedy deletion"
                },
                "frr": {
                    "language": "frr",
                    "value": "Kategorie:Wikipedia:Delete"
                },
                "fur": {
                    "language": "fur",
                    "value": "Categorie:Vichipedie:Elements di distruzi"
                },
                "fy": {
                    "language": "fy",
                    "value": "Kategory:Siden mei wiskwarsk\u00f4ging"
                },
                "ga": {
                    "language": "ga",
                    "value": "Catag\u00f3ir:Leathanaigh le luas-scrios"
                },
                "gan": {
                    "language": "gan",
                    "value": "\u5206\u985e:\u5feb\u901f\u522a\u5425"
                },
                "gd": {
                    "language": "gd",
                    "value": "Roinn-se\u00f2rsa:Candidates for speedy deletion"
                },
                "gl": {
                    "language": "gl",
                    "value": "Categor\u00eda:Limpar"
                },
                "glk": {
                    "language": "glk",
                    "value": "\u0631\u062f\u0647:Candidates for speedy deletion"
                },
                "gn": {
                    "language": "gn",
                    "value": "\u00d1emohenda:Candidates for speedy deletion"
                },
                "got": {
                    "language": "got",
                    "value": "\ud800\udf37\ud800\udf30\ud800\udf3d\ud800\udf43\ud800\udf30:Candidates for speedy deletion"
                },
                "gv": {
                    "language": "gv",
                    "value": "Ronney:Duillagyn er \u00e7hionn-scryssey"
                },
                "ha": {
                    "language": "ha",
                    "value": "Category:Candidates for speedy deletion"
                },
                "hak": {
                    "language": "hak",
                    "value": "Category:Candidates for speedy deletion"
                },
                "haw": {
                    "language": "haw",
                    "value": "M\u0101hele:Candidates for speedy deletion"
                },
                "he": {
                    "language": "he",
                    "value": "\u05e7\u05d8\u05d2\u05d5\u05e8\u05d9\u05d4:\u05d5\u05d9\u05e7\u05d9\u05e4\u05d3\u05d9\u05d4: \u05dc\u05de\u05d7\u05d9\u05e7\u05d4 \u05de\u05d4\u05d9\u05e8\u05d4"
                },
                "hi": {
                    "language": "hi",
                    "value": "\u0936\u094d\u0930\u0947\u0923\u0940:\u0936\u0940\u0918\u094d\u0930 \u0939\u091f\u093e\u0928\u0947 \u092f\u094b\u0917\u094d\u092f \u092a\u0943\u0937\u094d\u0920"
                },
                "hif": {
                    "language": "hif",
                    "value": "vibhag:Request for deletion"
                },
                "hr": {
                    "language": "hr",
                    "value": "Kategorija:Predlo\u0161ci za neodgovaraju\u0107i sadr\u017eaj"
                },
                "hsb": {
                    "language": "hsb",
                    "value": "Kategorija:Strony k sp\u011b\u0161nemu wu\u0161m\u00f3rnjenju"
                },
                "ht": {
                    "language": "ht",
                    "value": "Kategori:Pou efase"
                },
                "hu": {
                    "language": "hu",
                    "value": "Kateg\u00f3ria:Azonnali t\u00f6rl\u00e9sre v\u00e1r\u00f3 lapok"
                },
                "ia": {
                    "language": "ia",
                    "value": "Categoria:Wikipedia:Eliminar"
                },
                "id": {
                    "language": "id",
                    "value": "Kategori:Artikel yang layak untuk dihapus"
                },
                "ie": {
                    "language": "ie",
                    "value": "Categorie:Candidates for speedy deletion"
                },
                "ig": {
                    "language": "ig",
                    "value": "\u00d2t\u00f9:Candidates for speedy deletion"
                },
                "ilo": {
                    "language": "ilo",
                    "value": "Kategoria:Kandidato ti nadaras a panagikkat"
                },
                "is": {
                    "language": "is",
                    "value": "Flokkur:Ey\u00f0ingartill\u00f6gur"
                },
                "it": {
                    "language": "it",
                    "value": "Categoria:Cancellare subito"
                },
                "ja": {
                    "language": "ja",
                    "value": "Category:\u5373\u6642\u524a\u9664\u5bfe\u8c61\u306e\u30da\u30fc\u30b8"
                },
                "jbo": {
                    "language": "jbo",
                    "value": "Category:sutra vimcu"
                },
                "jv": {
                    "language": "jv",
                    "value": "Kategori:Artikel sing layak dibusak"
                },
                "ka": {
                    "language": "ka",
                    "value": "\u10d9\u10d0\u10e2\u10d4\u10d2\u10dd\u10e0\u10d8\u10d0:\u10ec\u10d0\u10e1\u10d0\u10e8\u10da\u10d4\u10da\u10d8 \u10d2\u10d5\u10d4\u10e0\u10d3\u10d4\u10d1\u10d8"
                },
                "kaa": {
                    "language": "kaa",
                    "value": "Kategoriya:Candidates for speedy deletion"
                },
                "kab": {
                    "language": "kab",
                    "value": "Taggayt:Candidates for speedy deletion"
                },
                "kg": {
                    "language": "kg",
                    "value": "Category:Candidates for speedy deletion"
                },
                "ki": {
                    "language": "ki",
                    "value": "Category:Candidates for speedy deletion"
                },
                "kk": {
                    "language": "kk",
                    "value": "\u0421\u0430\u043d\u0430\u0442:\u0416\u0435\u0434\u0435\u043b \u0436\u043e\u044e\u0493\u0430 \u04b1\u0441\u044b\u043d\u044b\u043b\u0493\u0430\u043d\u0434\u0430\u0440"
                },
                "kl": {
                    "language": "kl",
                    "value": "Sumut atassuseq:Candidates for speedy deletion"
                },
                "km": {
                    "language": "km",
                    "value": "\u1785\u17c6\u178e\u17b6\u178f\u17cb\u1790\u17d2\u1793\u17b6\u1780\u17cb\u1780\u17d2\u179a\u17bb\u1798:\u179b\u17bb\u1794"
                },
                "kn": {
                    "language": "kn",
                    "value": "\u0cb5\u0cb0\u0ccd\u0c97:\u0c85\u0cb3\u0cbf\u0cb8\u0cc1\u0cb5\u0cbf\u0c95\u0cc6\u0c97\u0cc6 \u0cb9\u0cbe\u0c95\u0cb2\u0cbe\u0c97\u0cbf\u0cb0\u0cc1\u0cb5 \u0cb2\u0cc7\u0c96\u0ca8\u0c97\u0cb3\u0cc1"
                },
                "ko": {
                    "language": "ko",
                    "value": "\ubd84\ub958:\uc0ad\uc81c \uc2e0\uccad \ubb38\uc11c"
                },
                "koi": {
                    "language": "koi",
                    "value": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f:Candidates for speedy deletion"
                },
                "krc": {
                    "language": "krc",
                    "value": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f:\u0412\u0438\u043a\u0438\u043f\u0435\u0434\u0438\u044f:\u0422\u0435\u0440\u043a \u043a\u0435\u0442\u0435\u0440\u0438\u043b\u0438\u0440\u0433\u0435"
                },
                "ks": {
                    "language": "ks",
                    "value": "Category:Candidates for speedy deletion"
                },
                "ksh": {
                    "language": "ksh",
                    "value": "Saachjrupp:Wikipedia:Schmie\u00df Fott!"
                },
                "ku": {
                    "language": "ku",
                    "value": "Kategor\u00ee:Gotar\u00ean ku b\u00ean j\u00eabirin"
                },
                "kv": {
                    "language": "kv",
                    "value": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f:Wikipedia:Candidates for speedy deletion"
                },
                "kw": {
                    "language": "kw",
                    "value": "Klass:Ombrofyoryon rag dileans"
                },
                "ky": {
                    "language": "ky",
                    "value": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f:Deletion"
                },
                "la": {
                    "language": "la",
                    "value": "Categoria:Deletiones propositae"
                },
                "lb": {
                    "language": "lb",
                    "value": "Kategorie:L\u00e4schen"
                },
                "lbe": {
                    "language": "lbe",
                    "value": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f:Speedy deletion requests"
                },
                "lg": {
                    "language": "lg",
                    "value": "Category:Candidates for speedy deletion"
                },
                "li": {
                    "language": "li",
                    "value": "Categorie:Kandidate veur sjnel eweg te goeje"
                },
                "lij": {
                    "language": "lij",
                    "value": "Categor\u00eea:Candidates for speedy deletion"
                },
                "lmo": {
                    "language": "lmo",
                    "value": "Categuria:De scancel\u00e0"
                },
                "ln": {
                    "language": "ln",
                    "value": "Cat\u00e9gorie:Candidates for speedy deletion"
                },
                "lo": {
                    "language": "lo",
                    "value": "\u0edd\u0ea7\u0e94:Candidates for speedy deletion"
                },
                "lt": {
                    "language": "lt",
                    "value": "Kategorija:Kandidatai skubiai trinti"
                },
                "lv": {
                    "language": "lv",
                    "value": "Kategorija:Lapas, kas izvirz\u012btas dz\u0113\u0161anai"
                },
                "map-bms": {
                    "language": "map-bms",
                    "value": "Kategori:Artikel sing arep dibusak"
                },
                "mdf": {
                    "language": "mdf",
                    "value": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0435:Candidates for speedy deletion"
                },
                "mg": {
                    "language": "mg",
                    "value": "Sokajy:Candidates for speedy deletion"
                },
                "mhr": {
                    "language": "mhr",
                    "value": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0439:\u0428\u04e7\u0440\u0430\u0448"
                },
                "mi": {
                    "language": "mi",
                    "value": "Category:Mukua"
                },
                "mk": {
                    "language": "mk",
                    "value": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0458\u0430:\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0438 \u0437\u0430 \u0431\u0440\u0437\u043e \u0431\u0440\u0438\u0448\u0435\u045a\u0435"
                },
                "ml": {
                    "language": "ml",
                    "value": "\u0d35\u0d7c\u0d17\u0d4d\u0d17\u0d02:\u0d2a\u0d46\u0d1f\u0d4d\u0d1f\u0d46\u0d28\u0d4d\u0d28\u0d4d \u0d28\u0d40\u0d15\u0d4d\u0d15\u0d02 \u0d1a\u0d46\u0d2f\u0d4d\u0d2f\u0d41\u0d35\u0d3e\u0d7b \u0d38\u0d3e\u0d27\u0d4d\u0d2f\u0d24\u0d2f\u0d41\u0d33\u0d4d\u0d33\u0d35"
                },
                "mn": {
                    "language": "mn",
                    "value": "\u0410\u043d\u0433\u0438\u043b\u0430\u043b:\u0423\u0441\u0442\u0433\u0430\u043b\u0434 \u043e\u0440\u043e\u0445 \u0445\u0443\u0443\u0434\u0441\u0443\u0443\u0434"
                },
                "mr": {
                    "language": "mr",
                    "value": "\u0935\u0930\u094d\u0917:Speedy deletion requests"
                },
                "ms": {
                    "language": "ms",
                    "value": "Kategori:Calon untuk penghapusan segera"
                },
                "mt": {
                    "language": "mt",
                    "value": "Kategorija:Proposti g\u0127at-t\u0127assir minnufih"
                },
                "mwl": {
                    "language": "mwl",
                    "value": "Catadorie:Maintenance:Delete"
                },
                "my": {
                    "language": "my",
                    "value": "Category:Deleteme"
                },
                "myv": {
                    "language": "myv",
                    "value": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f:Candidates for speedy deletion"
                },
                "mzn": {
                    "language": "mzn",
                    "value": "\u0631\u062c:\u0632\u0648\u062f \u0628\u0623\u0626\u06cc\u062a\u0646 \u0646\u0648\u0645\u0632\u062f\u0648\u0646"
                },
                "na": {
                    "language": "na",
                    "value": "Category:Candidates for speedy deletion"
                },
                "nah": {
                    "language": "nah",
                    "value": "Neneuhc\u0101y\u014dtl:Huiquipedia:Borrar"
                },
                "nap": {
                    "language": "nap",
                    "value": "Categur\u00eca:Paggene 'a scancell\u00e0"
                },
                "nds": {
                    "language": "nds",
                    "value": "Kategorie:Wikipedia:Gauweg"
                },
                "nds-nl": {
                    "language": "nds-nl",
                    "value": "Kategorie:Vort"
                },
                "ne": {
                    "language": "ne",
                    "value": "\u0936\u094d\u0930\u0947\u0923\u0940:Delete"
                },
                "new": {
                    "language": "new",
                    "value": "\u092a\u0941\u091a\u0903:Candidates for speedy deletion"
                },
                "nl": {
                    "language": "nl",
                    "value": "Categorie:Wiki:Nuweg"
                },
                "nn": {
                    "language": "nn",
                    "value": "Kategori:Sider merkte for sletting"
                },
                "nov": {
                    "language": "nov",
                    "value": "Category:Candidates for speedy deletion"
                },
                "nrm": {
                    "language": "nrm",
                    "value": "Category:Candidates for speedy deletion"
                },
                "nv": {
                    "language": "nv",
                    "value": "T\u02bc\u00e1\u00e1\u0142\u00e1h\u00e1gi \u00e1t\u02bc\u00e9ego:Candidates for speedy deletion"
                },
                "ny": {
                    "language": "ny",
                    "value": "Category:Candidates for speedy deletion"
                },
                "oc": {
                    "language": "oc",
                    "value": "Categoria:Pagina prepausada a la supression"
                },
                "om": {
                    "language": "om",
                    "value": "Category:Wikipedia:Candidates for speedy deletion"
                },
                "or": {
                    "language": "or",
                    "value": "\u0b36\u0b4d\u0b30\u0b47\u0b23\u0b40:Candidates for speedy deletion"
                },
                "os": {
                    "language": "os",
                    "value": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438:\u0412\u0438\u043a\u0438\u043f\u0435\u0434\u0438:\u0410\u043f\u043f\u0430\u0440\u044b\u043d\u043c\u00e6 \u043b\u00e6\u0432\u00e6\u0440\u0434 \u0444\u00e6\u0440\u0441\u0442\u00e6"
                },
                "pa": {
                    "language": "pa",
                    "value": "\u0a38\u0a3c\u0a4d\u0a30\u0a47\u0a23\u0a40:\u0a1b\u0a47\u0a24\u0a40 \u0a2e\u0a3f\u0a1f\u0a3e\u0a09\u0a23\u0a2f\u0a4b\u0a17 \u0a38\u0a2b\u0a3c\u0a47"
                },
                "pag": {
                    "language": "pag",
                    "value": "Category:Candidates for speedy deletion"
                },
                "pam": {
                    "language": "pam",
                    "value": "Category:Candidates for speedy deletion"
                },
                "pap": {
                    "language": "pap",
                    "value": "Category:Deleteme"
                },
                "pcd": {
                    "language": "pcd",
                    "value": "Cat\u00e9gorie:Candidates for speedy deletion"
                },
                "pdc": {
                    "language": "pdc",
                    "value": "Abdeeling:Wikipedia:Lesche"
                },
                "pfl": {
                    "language": "pfl",
                    "value": "Kategorie:Wikipedia:L\u00f6sche"
                },
                "pi": {
                    "language": "pi",
                    "value": "\u0935\u093f\u092d\u093e\u0917:Deleteme"
                },
                "pih": {
                    "language": "pih",
                    "value": "Category:Candidates for speedy deletion"
                },
                "pl": {
                    "language": "pl",
                    "value": "Kategoria:Ekspresowe kasowanie"
                },
                "pms": {
                    "language": "pms",
                    "value": "Categor\u00eca:Gav-me"
                },
                "pnt": {
                    "language": "pnt",
                    "value": "\u039a\u03b1\u03c4\u03b7\u03b3\u03bf\u03c1\u03af\u03b1\u03bd:\u03a3\u03b5\u03bb\u03af\u03b4\u03b5\u03c2 \u03b3\u03b9\u03b1 \u03b3\u03c1\u03ae\u03b3\u03bf\u03c1\u03b7 \u03b4\u03b9\u03b1\u03b3\u03c1\u03b1\u03c6\u03ae"
                },
                "ps": {
                    "language": "ps",
                    "value": "\u0648\u06d0\u0634\u0646\u064a\u0632\u0647:\u062f \u0686\u067c\u06a9\u0648 \u0693\u0646\u06ab\u0648\u0644\u0648 \u06a9\u0627\u0646\u062f\u064a\u062f \u0645\u062e\u0648\u0646\u0647"
                },
                "pt": {
                    "language": "pt",
                    "value": "Categoria:!P\u00e1ginas para elimina\u00e7\u00e3o r\u00e1pida"
                },
                "qu": {
                    "language": "qu",
                    "value": "Katiguriya:Wikipidiya:Champana"
                },
                "rm": {
                    "language": "rm",
                    "value": "Categoria:Candidates for speedy deletion"
                },
                "rmy": {
                    "language": "rmy",
                    "value": "Shopni:Khosipnaske lekha"
                },
                "rn": {
                    "language": "rn",
                    "value": "Category:Candidates for speedy deletion"
                },
                "ro": {
                    "language": "ro",
                    "value": "Categorie:Pagini de \u0219ters rapid"
                },
                "roa-tara": {
                    "language": "roa-tara",
                    "value": "Category:Candidate pa scangellaziona veloce"
                },
                "rw": {
                    "language": "rw",
                    "value": "Category:Candidates for speedy deletion"
                },
                "sa": {
                    "language": "sa",
                    "value": "\u0935\u0930\u094d\u0917\u0903:Delete"
                },
                "sah": {
                    "language": "sah",
                    "value": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f:\u0411\u0438\u043a\u0438\u043f\u0438\u044d\u0434\u044c\u0438\u0439\u044d:\u0422\u04af\u0440\u0433\u044d\u043d\u043d\u0438\u043a \u0441\u043e\u0442\u043e\u0440\u0433\u043e"
                },
                "sc": {
                    "language": "sc",
                    "value": "Categoria:De fuliai immoi"
                },
                "scn": {
                    "language": "scn",
                    "value": "Catigur\u00eca:Pruposti pi eliminazzioni lesta"
                },
                "sco": {
                    "language": "sco",
                    "value": "Category:Candidates for speedy deletion"
                },
                "sd": {
                    "language": "sd",
                    "value": "\u0632\u0645\u0631\u0648:\u062a\u0631\u062a \u068a\u0627\u067a \u062c\u0627 \u0627\u0645\u064a\u062f\u0648\u0627\u0631"
                },
                "se": {
                    "language": "se",
                    "value": "Kategoriija:Njuolggosihkkun"
                },
                "sg": {
                    "language": "sg",
                    "value": "Cat\u00e9gorie:Candidates for speedy deletion"
                },
                "sh": {
                    "language": "sh",
                    "value": "Kategorija:Kandidati za brzo brisanje"
                },
                "si": {
                    "language": "si",
                    "value": "\u0db4\u0dca\u200d\u0dbb\u0dc0\u0dbb\u0dca\u0d9c\u0dba:Candidates for speedy deletion"
                },
                "simple": {
                    "language": "simple",
                    "value": "Category:Quick deletion requests"
                },
                "sk": {
                    "language": "sk",
                    "value": "Kateg\u00f3ria:Wikip\u00e9dia:Kandid\u00e1ti na zmazanie"
                },
                "sl": {
                    "language": "sl",
                    "value": "Kategorija:Predlogi za hitro brisanje"
                },
                "sm": {
                    "language": "sm",
                    "value": "Category:Candidates for speedy deletion"
                },
                "sn": {
                    "language": "sn",
                    "value": "Category:Candidates for speedy deletion"
                },
                "so": {
                    "language": "so",
                    "value": "Category:Delete"
                },
                "sq": {
                    "language": "sq",
                    "value": "Kategoria:Faqe p\u00ebr grisje"
                },
                "sr": {
                    "language": "sr",
                    "value": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0458\u0430:\u0411\u0440\u0437\u043e \u0431\u0440\u0438\u0441\u0430\u045a\u0435"
                },
                "srn": {
                    "language": "srn",
                    "value": "Guru:Candidates for speedy deletion"
                },
                "ss": {
                    "language": "ss",
                    "value": "Category:Candidates for speedy deletion"
                },
                "st": {
                    "language": "st",
                    "value": "Category:Candidates for speedy deletion"
                },
                "stq": {
                    "language": "stq",
                    "value": "Kategorie:Candidates for speedy deletion"
                },
                "su": {
                    "language": "su",
                    "value": "Kategori:Artikel anu kudu dihapus"
                },
                "sv": {
                    "language": "sv",
                    "value": "Kategori:Snabbraderingar"
                },
                "sw": {
                    "language": "sw",
                    "value": "Jamii:Makala kwa ufutaji"
                },
                "szl": {
                    "language": "szl",
                    "value": "Kategoryjo:Gibke wy\u0107epowa\u0144y"
                },
                "ta": {
                    "language": "ta",
                    "value": "\u0baa\u0b95\u0bc1\u0baa\u0bcd\u0baa\u0bc1:\u0bb5\u0bbf\u0bb0\u0bc8\u0ba8\u0bcd\u0ba4\u0bc1 \u0ba8\u0bc0\u0b95\u0bcd\u0b95\u0baa\u0bcd\u0baa\u0b9f \u0bb5\u0bc7\u0ba3\u0bcd\u0b9f\u0bbf\u0baf \u0baa\u0b95\u0bcd\u0b95\u0b99\u0bcd\u0b95\u0bb3\u0bcd"
                },
                "te": {
                    "language": "te",
                    "value": "\u0c35\u0c30\u0c4d\u0c17\u0c02:Candidates for speedy deletion"
                },
                "tet": {
                    "language": "tet",
                    "value": "Kategoria:Kandidatu ba halakon lailais"
                },
                "tg": {
                    "language": "tg",
                    "value": "\u0413\u0443\u0440\u04ef\u04b3:\u041c\u0430\u049b\u043e\u043b\u0430\u04b3\u043e\u0438 \u043d\u043e\u043c\u0437\u0430\u0434\u0438 \u04b3\u0430\u0437\u0444"
                },
                "th": {
                    "language": "th",
                    "value": "\u0e2b\u0e21\u0e27\u0e14\u0e2b\u0e21\u0e39\u0e48:\u0e2b\u0e19\u0e49\u0e32\u0e17\u0e35\u0e48\u0e16\u0e39\u0e01\u0e41\u0e08\u0e49\u0e07\u0e25\u0e1a"
                },
                "ti": {
                    "language": "ti",
                    "value": "Category:Candidates for speedy deletion"
                },
                "tk": {
                    "language": "tk",
                    "value": "Kategori\u00fda:Deleteme"
                },
                "tl": {
                    "language": "tl",
                    "value": "Kategorya:Mga pahinang mabilisang buburahin"
                },
                "tn": {
                    "language": "tn",
                    "value": "Category:Wikipedia:Delete"
                },
                "to": {
                    "language": "to",
                    "value": "Category:Ngaahi fili ma\u02bba e t\u0101mate\u02bbi vave"
                },
                "tpi": {
                    "language": "tpi",
                    "value": "Grup:All articles proposed for deletion"
                },
                "tr": {
                    "language": "tr",
                    "value": "Kategori:Vikipedi silinecek sayfalar"
                },
                "ts": {
                    "language": "ts",
                    "value": "Category:Candidates for speedy deletion"
                },
                "tt": {
                    "language": "tt",
                    "value": "\u0422\u04e9\u0440\u043a\u0435\u043c:Candidates for speedy deletion"
                },
                "tum": {
                    "language": "tum",
                    "value": "Category:Candidates for speedy deletion"
                },
                "tw": {
                    "language": "tw",
                    "value": "Category:Candidates for speedy deletion"
                },
                "ty": {
                    "language": "ty",
                    "value": "Cat\u00e9gorie:Candidates for speedy deletion"
                },
                "udm": {
                    "language": "udm",
                    "value": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f:\u0412\u0438\u043a\u0438\u043f\u0435\u0434\u0438\u044f:\u041a \u0431\u044b\u0441\u0442\u0440\u043e\u043c\u0443 \u0443\u0434\u0430\u043b\u0435\u043d\u0438\u044e"
                },
                "ug": {
                    "language": "ug",
                    "value": "\u062a\u06c8\u0631:Candidates for speedy deletion"
                },
                "uk": {
                    "language": "uk",
                    "value": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0456\u044f:\u0421\u0442\u0430\u0442\u0442\u0456 \u0434\u043e \u0448\u0432\u0438\u0434\u043a\u043e\u0433\u043e \u0432\u0438\u043b\u0443\u0447\u0435\u043d\u043d\u044f"
                },
                "ur": {
                    "language": "ur",
                    "value": "\u0632\u0645\u0631\u06c1:\u0627\u0645\u06cc\u062f\u0648\u0627\u0631 \u0628\u0631\u0627\u06d3 \u062d\u0630\u0641 \u0634\u062f\u06af\u06cc"
                },
                "uz": {
                    "language": "uz",
                    "value": "Turkum:Vikipediya:Yo\u02bbqotilish uchun maqolalar"
                },
                "ve": {
                    "language": "ve",
                    "value": "Category:Candidates for speedy deletion"
                },
                "vec": {
                    "language": "vec",
                    "value": "Categoria:Da scanse\u0142are suito"
                },
                "vep": {
                    "language": "vep",
                    "value": "Kategorii:\u010cuta poi\u0161"
                },
                "vi": {
                    "language": "vi",
                    "value": "Th\u1ec3 lo\u1ea1i:Ch\u1edd x\u00f3a"
                },
                "vls": {
                    "language": "vls",
                    "value": "Categorie:Wikipedia:Nuweg"
                },
                "vo": {
                    "language": "vo",
                    "value": "Klad:Pads mo\u00fckabik"
                },
                "wa": {
                    "language": "wa",
                    "value": "Categoreye:P\u00e5djes a disfacer"
                },
                "war": {
                    "language": "war",
                    "value": "Kaarangay:Candidates for speedy deletion"
                },
                "wuu": {
                    "language": "wuu",
                    "value": "\u5206\u7c7b:\u5feb\u901f\u5220\u9664\u5019\u9009"
                },
                "xal": {
                    "language": "xal",
                    "value": "\u04d8\u04d9\u0448\u043b:Candidates for speedy deletion"
                },
                "xh": {
                    "language": "xh",
                    "value": "Category:Candidates for speedy deletion"
                },
                "xmf": {
                    "language": "xmf",
                    "value": "\u10d9\u10d0\u10e2\u10d4\u10d2\u10dd\u10e0\u10d8\u10d0:Candidates for speedy deletion"
                },
                "yi": {
                    "language": "yi",
                    "value": "\u05e7\u05d0\u05b7\u05d8\u05e2\u05d2\u05d0\u05b8\u05e8\u05d9\u05e2:\u05d2\u05e2\u05e9\u05d8\u05e2\u05dc\u05d8\u05e2 \u05e6\u05d5 \u05e9\u05e0\u05e2\u05dc \u05de\u05e2\u05e7\u05df"
                },
                "yo": {
                    "language": "yo",
                    "value": "\u1eb8\u0300ka:\u00c0w\u1ecdn oj\u00faew\u00e9 f\u00fan \u00ecpar\u1eb9\u0301 k\u00ed\u00e1k\u00ed\u00e1"
                },
                "za": {
                    "language": "za",
                    "value": "\u5206\u7c7b:Candidates for speedy deletion"
                },
                "zea": {
                    "language": "zea",
                    "value": "Categorie:Wikipedia:Categorie w\u00e9g erme\u00ea"
                },
                "zh": {
                    "language": "zh",
                    "value": "Category:\u5feb\u901f\u5220\u9664\u5019\u9009"
                },
                "zh-cn": {
                    "language": "zh-cn",
                    "value": "Category:\u5feb\u901f\u5220\u9664\u5019\u9009"
                },
                "zh-hans": {
                    "language": "zh-hans",
                    "value": "\u5206\u7c7b:\u5feb\u901f\u5220\u9664\u5019\u9009"
                },
                "zh-hant": {
                    "language": "zh-hant",
                    "value": "\u5206\u985e:\u5feb\u901f\u522a\u9664\u5019\u9078"
                },
                "zu": {
                    "language": "zu",
                    "value": "Category:Candidates for speedy deletion"
                },
                "nb": {
                    "language": "nb",
                    "value": "Kategori:Sider som er foresl\u00e5tt raskt slettet"
                },
                "de-ch": {
                    "language": "de-ch",
                    "value": "Kategorie:Wikipedia:Schnelll\u00f6schen"
                },
                "pt-br": {
                    "language": "pt-br",
                    "value": "Categoria:!P\u00e1ginas para elimina\u00e7\u00e3o r\u00e1pida"
                },
                "yue": {
                    "language": "yue",
                    "value": "Category:\u5373\u523b\u522a\u9664\u5019\u9078"
                },
                "mrj": {
                    "language": "mrj",
                    "value": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438:Candidates for speedy deletion"
                },
                "tyv": {
                    "language": "tyv",
                    "value": "\u0410\u04a3\u0433\u044b\u043b\u0430\u043b:Candidates for speedy deletion"
                },
                "gsw": {
                    "language": "gsw",
                    "value": "Kategorie:Wikipedia:L\u00f6sche"
                },
                "crh-latn": {
                    "language": "crh-latn",
                    "value": "Kategoriya:Vikipediya:Delete"
                },
                "sgs": {
                    "language": "sgs",
                    "value": "Kateguor\u0117j\u0117:Kand\u0117dat\u0101 skob\u0113 trint\u0117"
                },
                "nan": {
                    "language": "nan",
                    "value": "Category:T\u00e1n-th\u0101i kho\u00e0i-sok th\u00e2i-t\u00fb \u00ea ia\u030dh"
                },
                "lzh": {
                    "language": "lzh",
                    "value": "Category:\u901f\u522a\u5019"
                },
                "be-tarask": {
                    "language": "be-tarask",
                    "value": "\u041a\u0430\u0442\u044d\u0433\u043e\u0440\u044b\u044f:\u0412\u0456\u043a\u0456\u043f\u044d\u0434\u044b\u044f:\u041a\u0430\u043d\u0434\u044b\u0434\u0430\u0442\u0443\u0440\u044b \u043d\u0430 \u0432\u044b\u0434\u0430\u043b\u0435\u043d\u044c\u043d\u0435"
                },
                "vro": {
                    "language": "vro",
                    "value": "Kat\u00f5gooria:Kistutaq"
                },
                "rup": {
                    "language": "rup",
                    "value": "Category:Deleteme"
                },
                "gu": {
                    "language": "gu",
                    "value": "\u0ab6\u0acd\u0ab0\u0ac7\u0aa3\u0ac0:Candidates for speedy deletion"
                },
                "hy": {
                    "language": "hy",
                    "value": "\u053f\u0561\u057f\u0565\u0563\u0578\u0580\u056b\u0561:\u0531\u0580\u0561\u0563 \u057b\u0576\u057b\u0574\u0561\u0576 \u0569\u0565\u056f\u0576\u0561\u056e\u0578\u0582\u0576\u0565\u0580"
                },
                "bn": {
                    "language": "bn",
                    "value": "\u09ac\u09bf\u09b7\u09af\u09bc\u09b6\u09cd\u09b0\u09c7\u09a3\u09c0:\u09a6\u09cd\u09b0\u09c1\u09a4 \u0985\u09aa\u09b8\u09be\u09b0\u09a3\u09c7\u09b0 \u09af\u09cb\u0997\u09cd\u09af"
                },
                "ik": {
                    "language": "ik",
                    "value": "Category:Candidates for speedy deletion"
                },
                "ltg": {
                    "language": "ltg",
                    "value": "Kategoreja:Candidates for speedy deletion"
                },
                "gag": {
                    "language": "gag",
                    "value": "Kategoriya:Candidates for speedy deletion"
                },
                "as": {
                    "language": "as",
                    "value": "\u09b6\u09cd\u09f0\u09c7\u09a3\u09c0:Candidates for speedy deletion"
                }
            },
            "descriptions": {
                "de": {
                    "language": "de",
                    "value": "Wikimedia-Kategorie"
                },
                "es": {
                    "language": "es",
                    "value": "categor\u00eda de Wikimedia"
                },
                "it": {
                    "language": "it",
                    "value": "categoria di un progetto Wikimedia"
                },
                "en": {
                    "language": "en",
                    "value": "Wikimedia category page"
                },
                "nl": {
                    "language": "nl",
                    "value": "Wikimedia-categorie"
                },
                "en-gb": {
                    "language": "en-gb",
                    "value": "Wikimedia category page"
                },
                "bs": {
                    "language": "bs",
                    "value": "Kategorija Wikipedije"
                },
                "cs": {
                    "language": "cs",
                    "value": "kategorie Wikimedie"
                },
                "da": {
                    "language": "da",
                    "value": "Wikimedia-kategori"
                },
                "fi": {
                    "language": "fi",
                    "value": "Wikimedia-luokka"
                },
                "gl": {
                    "language": "gl",
                    "value": "categor\u00eda de Wikipedia"
                },
                "nds": {
                    "language": "nds",
                    "value": "Kategorie op Wikipedia"
                },
                "pl": {
                    "language": "pl",
                    "value": "kategoria Wikipedii"
                },
                "sv": {
                    "language": "sv",
                    "value": "Wikimedia-kategori"
                },
                "fr": {
                    "language": "fr",
                    "value": "page de cat\u00e9gorie d'un projet Wikimedia"
                },
                "pt": {
                    "language": "pt",
                    "value": "categoria de um projeto da Wikimedia"
                },
                "pt-br": {
                    "language": "pt-br",
                    "value": "categoria de um projeto da Wikimedia"
                },
                "ru": {
                    "language": "ru",
                    "value": "\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f \u0432 \u043f\u0440\u043e\u0435\u043a\u0442\u0435 \u0412\u0438\u043a\u0438\u043c\u0435\u0434\u0438a"
                },
                "th": {
                    "language": "th",
                    "value": "\u0e2b\u0e19\u0e49\u0e32\u0e2b\u0e21\u0e27\u0e14\u0e2b\u0e21\u0e39\u0e48\u0e27\u0e34\u0e01\u0e34\u0e1e\u0e35\u0e40\u0e14\u0e35\u0e22"
                },
                "en-ca": {
                    "language": "en-ca",
                    "value": "Wikimedia category page"
                },
                "ar": {
                    "language": "ar",
                    "value": "\u0635\u0641\u062d\u0629 \u062a\u0635\u0646\u064a\u0641 \u0648\u064a\u0643\u064a\u0645\u064a\u062f\u064a\u0627"
                },
                "fa": {
                    "language": "fa",
                    "value": "\u0631\u062f\u0647\u0654 \u0648\u06cc\u06a9\u06cc\u200c\u0645\u062f\u06cc\u0627"
                },
                "nn": {
                    "language": "nn",
                    "value": "Wikimedia-kategori"
                },
                "nb": {
                    "language": "nb",
                    "value": "Wikimedia-kategori"
                },
                "et": {
                    "language": "et",
                    "value": "Wikimedia kategooria"
                },
                "ja": {
                    "language": "ja",
                    "value": "\u30a6\u30a3\u30ad\u30e1\u30c7\u30a3\u30a2\u306e\u30ab\u30c6\u30b4\u30ea"
                }
            },
            "claims": {
                "P31": [
                    {
                        "id": "q5964$29abb3ce-4f88-55ac-35a7-f8e150c69098",
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P31",
                            "datatype": "wikibase-item",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 15647814
                                },
                                "type": "wikibase-entityid"
                            }
                        },
                        "type": "statement",
                        "rank": "normal"
                    },
                    {
                        "id": "Q5964$EFFBB720-6344-4D51-95D4-9DD39B52E3D8",
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P31",
                            "datatype": "wikibase-item",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 4167836
                                },
                                "type": "wikibase-entityid"
                            }
                        },
                        "type": "statement",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "11235c8ef158cb6e45a8480b93b0f78887e2fc28",
                                "snaks": {
                                    "P143": [
                                        {
                                            "snaktype": "value",
                                            "property": "P143",
                                            "datatype": "wikibase-item",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 3181422
                                                },
                                                "type": "wikibase-entityid"
                                            }
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P143"
                                ]
                            },
                            {
                                "hash": "3a6413ea9bdd92b87a35f6b8a4b671cb4aecf2b5",
                                "snaks": {
                                    "P143": [
                                        {
                                            "snaktype": "value",
                                            "property": "P143",
                                            "datatype": "wikibase-item",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 208533
                                                },
                                                "type": "wikibase-entityid"
                                            }
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P143"
                                ]
                            }
                        ]
                    }
                ],
                "P373": [
                    {
                        "id": "Q5964$9A7334AC-84D0-4234-8894-F84979B44F5C",
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P373",
                            "datatype": "string",
                            "datavalue": {
                                "value": "Candidates for speedy deletion",
                                "type": "string"
                            }
                        },
                        "type": "statement",
                        "rank": "normal",
                        "references": [
                            {
                                "hash": "7a07c248d59b68eba79e5c5c2a59c6d07cf2cec5",
                                "snaks": {
                                    "P143": [
                                        {
                                            "snaktype": "value",
                                            "property": "P143",
                                            "datatype": "wikibase-item",
                                            "datavalue": {
                                                "value": {
                                                    "entity-type": "item",
                                                    "numeric-id": 181163
                                                },
                                                "type": "wikibase-entityid"
                                            }
                                        }
                                    ]
                                },
                                "snaks-order": [
                                    "P143"
                                ]
                            }
                        ]
                    }
                ]
            },
            "sitelinks": {
                "abwiki": {
                    "site": "abwiki",
                    "title": "\u0410\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0430:Candidates for speedy deletion",
                    "badges": []
                },
                "afwiki": {
                    "site": "afwiki",
                    "title": "Kategorie:Kandidate vir spoedige verwydering",
                    "badges": []
                },
                "afwikiquote": {
                    "site": "afwikiquote",
                    "title": "Kategorie:Kandidate vir spoedige verwydering",
                    "badges": []
                },
                "amwiki": {
                    "site": "amwiki",
                    "title": "\u1218\u12f0\u1265:\u1208\u121b\u1325\u134b\u1275 \u12e8\u1240\u1228\u1261 \u1308\u133e\u127d",
                    "badges": []
                },
                "angwiki": {
                    "site": "angwiki",
                    "title": "Flocc:Candidates for speedy deletion",
                    "badges": []
                },
                "arcwiki": {
                    "site": "arcwiki",
                    "title": "\u0723\u0715\u072a\u0710:Candidates for speedy deletion",
                    "badges": []
                },
                "arwiki": {
                    "site": "arwiki",
                    "title": "\u062a\u0635\u0646\u064a\u0641:\u0635\u0641\u062d\u0627\u062a \u0644\u0644\u062d\u0630\u0641 \u0627\u0644\u0633\u0631\u064a\u0639",
                    "badges": []
                },
                "arwikiquote": {
                    "site": "arwikiquote",
                    "title": "\u062a\u0635\u0646\u064a\u0641:\u0635\u0641\u062d\u0627\u062a \u0644\u0644\u062d\u0630\u0641 \u0627\u0644\u0633\u0631\u064a\u0639",
                    "badges": []
                },
                "arwikisource": {
                    "site": "arwikisource",
                    "title": "\u062a\u0635\u0646\u064a\u0641:\u0635\u0641\u062d\u0627\u062a \u062d\u0630\u0641 \u0633\u0631\u064a\u0639",
                    "badges": []
                },
                "arzwiki": {
                    "site": "arzwiki",
                    "title": "\u062a\u0635\u0646\u064a\u0641:\u0635\u0641\u062d\u0627\u062a \u0644\u0644\u0645\u0633\u062d \u0627\u0644\u0633\u0631\u064a\u0639",
                    "badges": []
                },
                "aswiki": {
                    "site": "aswiki",
                    "title": "\u09b6\u09cd\u09f0\u09c7\u09a3\u09c0:Candidates for speedy deletion",
                    "badges": []
                },
                "avwiki": {
                    "site": "avwiki",
                    "title": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f:Candidates for speedy deletion",
                    "badges": []
                },
                "azwiki": {
                    "site": "azwiki",
                    "title": "Kateqoriya:Vikipediya:Silin\u0259c\u0259k s\u0259hif\u0259l\u0259r",
                    "badges": []
                },
                "barwiki": {
                    "site": "barwiki",
                    "title": "Kategorie:Wikipedia:Schnelll\u00f6schen",
                    "badges": []
                },
                "bat_smgwiki": {
                    "site": "bat_smgwiki",
                    "title": "Kateguor\u0117j\u0117:Kand\u0117dat\u0101 skob\u0113 trint\u0117",
                    "badges": []
                },
                "bclwiki": {
                    "site": "bclwiki",
                    "title": "Kategorya:Tolos-tolos na mga pagpar\u00e0",
                    "badges": []
                },
                "be_x_oldwiki": {
                    "site": "be_x_oldwiki",
                    "title": "\u041a\u0430\u0442\u044d\u0433\u043e\u0440\u044b\u044f:\u0412\u0456\u043a\u0456\u043f\u044d\u0434\u044b\u044f:\u041a\u0430\u043d\u0434\u044b\u0434\u0430\u0442\u0443\u0440\u044b \u043d\u0430 \u0432\u044b\u0434\u0430\u043b\u0435\u043d\u044c\u043d\u0435",
                    "badges": []
                },
                "bewiki": {
                    "site": "bewiki",
                    "title": "\u041a\u0430\u0442\u044d\u0433\u043e\u0440\u044b\u044f:\u0410\u0440\u0442\u044b\u043a\u0443\u043b\u044b \u0434\u0430 \u0432\u044b\u0434\u0430\u043b\u0435\u043d\u043d\u044f",
                    "badges": []
                },
                "bgwiki": {
                    "site": "bgwiki",
                    "title": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f:\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0438 \u0437\u0430 \u0431\u044a\u0440\u0437\u043e \u0438\u0437\u0442\u0440\u0438\u0432\u0430\u043d\u0435",
                    "badges": []
                },
                "bgwikisource": {
                    "site": "bgwikisource",
                    "title": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f:\u0423\u0438\u043a\u0438\u0438\u0437\u0442\u043e\u0447\u043d\u0438\u043a:\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0438 \u0437\u0430 \u0431\u044a\u0440\u0437\u043e \u0438\u0437\u0442\u0440\u0438\u0432\u0430\u043d\u0435",
                    "badges": []
                },
                "bhwiki": {
                    "site": "bhwiki",
                    "title": "\u0936\u094d\u0930\u0947\u0923\u0940:Candidates for speedy deletion",
                    "badges": []
                },
                "biwiki": {
                    "site": "biwiki",
                    "title": "Category:Candidates for speedy deletion",
                    "badges": []
                },
                "bjnwiki": {
                    "site": "bjnwiki",
                    "title": "Tumbung:Artikal nang layak hagan dihapus",
                    "badges": []
                },
                "bnwiki": {
                    "site": "bnwiki",
                    "title": "\u09ac\u09bf\u09b7\u09af\u09bc\u09b6\u09cd\u09b0\u09c7\u09a3\u09c0:\u09a6\u09cd\u09b0\u09c1\u09a4 \u0985\u09aa\u09b8\u09be\u09b0\u09a3\u09c7\u09b0 \u09af\u09cb\u0997\u09cd\u09af",
                    "badges": []
                },
                "bowiki": {
                    "site": "bowiki",
                    "title": "Category:Candidates for speedy deletion",
                    "badges": []
                },
                "bpywiki": {
                    "site": "bpywiki",
                    "title": "\u09a5\u09be\u0995:Candidates for speedy deletion",
                    "badges": []
                },
                "brwiki": {
                    "site": "brwiki",
                    "title": "Rummad:Candidates for speedy deletion",
                    "badges": []
                },
                "brwikiquote": {
                    "site": "brwikiquote",
                    "title": "Rummad:Candidates for speedy deletion",
                    "badges": []
                },
                "bswikinews": {
                    "site": "bswikinews",
                    "title": "Kategorija:Kandidati za brisanje",
                    "badges": []
                },
                "bswikiquote": {
                    "site": "bswikiquote",
                    "title": "Kategorija:Kandidati za brisanje",
                    "badges": []
                },
                "bugwiki": {
                    "site": "bugwiki",
                    "title": "Kategori:Halaman yang diusulkan untuk dihapus",
                    "badges": []
                },
                "bxrwiki": {
                    "site": "bxrwiki",
                    "title": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438:Candidates for speedy deletion",
                    "badges": []
                },
                "cawikiquote": {
                    "site": "cawikiquote",
                    "title": "Categoria:Sol\u00b7licituds de supressi\u00f3 immediata",
                    "badges": []
                },
                "cbk_zamwiki": {
                    "site": "cbk_zamwiki",
                    "title": "Categor\u00eda:Maga Pagina Nominado Para Bora",
                    "badges": []
                },
                "cdowiki": {
                    "site": "cdowiki",
                    "title": "\u5206\u985e:Ch\u00e9\u0324\u1e73k-k\u00e1ik ch\u0113ng-d\u1e73\u0300",
                    "badges": []
                },
                "cebwiki": {
                    "site": "cebwiki",
                    "title": "Kategoriya:Kandidato sa pagtangtang dayon",
                    "badges": []
                },
                "cewiki": {
                    "site": "cewiki",
                    "title": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438:\u0412\u0438\u043a\u0438\u043f\u0435\u0434\u0438:\u0421\u0438\u0445\u0430 \u0434\u04c0\u0430\u044f\u043a\u043a\u0445\u0430\u0440\u0435 \u0434\u0438\u043b\u043b\u0430\u0440",
                    "badges": []
                },
                "chrwiki": {
                    "site": "chrwiki",
                    "title": "Category:Candidates for speedy deletion",
                    "badges": []
                },
                "chwiki": {
                    "site": "chwiki",
                    "title": "Katigoria:Candidates for speedy deletion",
                    "badges": []
                },
                "chywiki": {
                    "site": "chywiki",
                    "title": "Category:Candidates for speedy deletion",
                    "badges": []
                },
                "ckbwiki": {
                    "site": "ckbwiki",
                    "title": "\u067e\u06c6\u0644:\u067e\u06d5\u0695\u06d5\u06a9\u0627\u0646 \u0628\u06c6 \u0633\u0695\u06cc\u0646\u06d5\u0648\u06d5\u06cc \u062e\u06ce\u0631\u0627",
                    "badges": []
                },
                "commonswiki": {
                    "site": "commonswiki",
                    "title": "Category:Candidates for speedy deletion",
                    "badges": []
                },
                "crwiki": {
                    "site": "crwiki",
                    "title": "Category:Candidates for speedy deletion",
                    "badges": []
                },
                "crwikiquote": {
                    "site": "crwikiquote",
                    "title": "Category:Candidates for speedy deletion",
                    "badges": []
                },
                "cswiki": {
                    "site": "cswiki",
                    "title": "Kategorie:Str\u00e1nky ke smaz\u00e1n\u00ed",
                    "badges": []
                },
                "cswikinews": {
                    "site": "cswikinews",
                    "title": "Kategorie:\u00dadr\u017eba:Smazat",
                    "badges": []
                },
                "cswikiquote": {
                    "site": "cswikiquote",
                    "title": "Kategorie:\u00dadr\u017eba:Smazat",
                    "badges": []
                },
                "cswikisource": {
                    "site": "cswikisource",
                    "title": "Kategorie:\u00dadr\u017eba:Smazat",
                    "badges": []
                },
                "cvwiki": {
                    "site": "cvwiki",
                    "title": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438:\u0422\u04f3\u0440\u0435\u0445 \u043a\u0103\u043b\u0430\u0440\u0441\u0430 \u043f\u0103\u0440\u0430\u0445\u043c\u0430\u043b\u043b\u0438 \u0441\u0442\u0430\u0442\u044c\u044f\u0441\u0435\u043c",
                    "badges": []
                },
                "cywiki": {
                    "site": "cywiki",
                    "title": "Categori:Tudalennau amheus",
                    "badges": []
                },
                "cywikiquote": {
                    "site": "cywikiquote",
                    "title": "Categori:Tudalennau amheus",
                    "badges": []
                },
                "dawiki": {
                    "site": "dawiki",
                    "title": "Kategori:Sider der er foresl\u00e5et slettet hurtigt",
                    "badges": []
                },
                "dawikiquote": {
                    "site": "dawikiquote",
                    "title": "Kategori:Sider der b\u00f8r slettes pga. h\u00e6rv\u00e6rk",
                    "badges": []
                },
                "dewiki": {
                    "site": "dewiki",
                    "title": "Kategorie:Wikipedia:Schnelll\u00f6schen",
                    "badges": []
                },
                "dewikivoyage": {
                    "site": "dewikivoyage",
                    "title": "Kategorie:Schnelll\u00f6schen",
                    "badges": []
                },
                "dsbwiki": {
                    "site": "dsbwiki",
                    "title": "Kategorija:Boki k malsnemu la\u0161owanju",
                    "badges": []
                },
                "dvwiki": {
                    "site": "dvwiki",
                    "title": "\u07a4\u07a8\u0790\u07b0\u0789\u07aa:Candidates for speedy deletion",
                    "badges": []
                },
                "dzwiki": {
                    "site": "dzwiki",
                    "title": "Category:Candidates for speedy deletion",
                    "badges": []
                },
                "eewiki": {
                    "site": "eewiki",
                    "title": "Category:Candidates for speedy deletion",
                    "badges": []
                },
                "elwiki": {
                    "site": "elwiki",
                    "title": "\u039a\u03b1\u03c4\u03b7\u03b3\u03bf\u03c1\u03af\u03b1:\u03a3\u03b5\u03bb\u03af\u03b4\u03b5\u03c2 \u03b3\u03b9\u03b1 \u03b3\u03c1\u03ae\u03b3\u03bf\u03c1\u03b7 \u03b4\u03b9\u03b1\u03b3\u03c1\u03b1\u03c6\u03ae",
                    "badges": []
                },
                "elwikiquote": {
                    "site": "elwikiquote",
                    "title": "\u039a\u03b1\u03c4\u03b7\u03b3\u03bf\u03c1\u03af\u03b1:\u03a3\u03b5\u03bb\u03af\u03b4\u03b5\u03c2 \u03b3\u03b9\u03b1 \u03b3\u03c1\u03ae\u03b3\u03bf\u03c1\u03b7 \u03b4\u03b9\u03b1\u03b3\u03c1\u03b1\u03c6\u03ae",
                    "badges": []
                },
                "elwikivoyage": {
                    "site": "elwikivoyage",
                    "title": "\u039a\u03b1\u03c4\u03b7\u03b3\u03bf\u03c1\u03af\u03b1:\u03a3\u03b5\u03bb\u03af\u03b4\u03b5\u03c2 \u03b3\u03b9\u03b1 \u03b3\u03c1\u03ae\u03b3\u03bf\u03c1\u03b7 \u03b4\u03b9\u03b1\u03b3\u03c1\u03b1\u03c6\u03ae",
                    "badges": []
                },
                "enwiki": {
                    "site": "enwiki",
                    "title": "Category:Candidates for speedy deletion",
                    "badges": []
                },
                "enwikinews": {
                    "site": "enwikinews",
                    "title": "Category:Speedy deletion",
                    "badges": []
                },
                "enwikiquote": {
                    "site": "enwikiquote",
                    "title": "Category:Candidates for speedy deletion",
                    "badges": []
                },
                "enwikisource": {
                    "site": "enwikisource",
                    "title": "Category:Speedy deletion requests",
                    "badges": []
                },
                "enwikivoyage": {
                    "site": "enwikivoyage",
                    "title": "Category:Speedy deletion candidates",
                    "badges": []
                },
                "eowiki": {
                    "site": "eowiki",
                    "title": "Kategorio:Tujforigendaj artikoloj",
                    "badges": []
                },
                "eowikiquote": {
                    "site": "eowikiquote",
                    "title": "Kategorio:Forigendaj artikoloj",
                    "badges": []
                },
                "eswiki": {
                    "site": "eswiki",
                    "title": "Categor\u00eda:Wikipedia:Borrar (definitivo)",
                    "badges": []
                },
                "eswikivoyage": {
                    "site": "eswikivoyage",
                    "title": "Categor\u00eda:Wikiviajes:Solicitudes de borrado en cuarentena",
                    "badges": []
                },
                "euwikiquote": {
                    "site": "euwikiquote",
                    "title": "Kategoria:Ezabatzeko",
                    "badges": []
                },
                "fawiki": {
                    "site": "fawiki",
                    "title": "\u0631\u062f\u0647:\u0645\u0642\u0627\u0644\u0647\u200c\u0647\u0627\u06cc \u0646\u0627\u0645\u0632\u062f \u062d\u0630\u0641 \u0633\u0631\u06cc\u0639",
                    "badges": []
                },
                "fawikinews": {
                    "site": "fawikinews",
                    "title": "\u0631\u062f\u0647:\u0635\u0641\u062d\u0647\u200c\u0647\u0627\u06cc \u0646\u0627\u0645\u0632\u062f \u062d\u0630\u0641 \u0633\u0631\u06cc\u0639",
                    "badges": []
                },
                "fawikisource": {
                    "site": "fawikisource",
                    "title": "\u0631\u062f\u0647:\u062f\u0631\u062e\u0648\u0627\u0633\u062a\u200c\u0647\u0627\u06cc \u062d\u0630\u0641 \u0633\u0631\u06cc\u0639",
                    "badges": []
                },
                "fawikivoyage": {
                    "site": "fawikivoyage",
                    "title": "\u0631\u062f\u0647:\u0645\u0642\u0627\u0644\u0647\u200c\u0647\u0627\u06cc \u0646\u0627\u0645\u0632\u062f \u062d\u0630\u0641 \u0633\u0631\u06cc\u0639",
                    "badges": []
                },
                "ffwiki": {
                    "site": "ffwiki",
                    "title": "Cat\u00e9gorie:Candidates for speedy deletion",
                    "badges": []
                },
                "fiwiki": {
                    "site": "fiwiki",
                    "title": "Luokka:Pikapoisto",
                    "badges": []
                },
                "fiwikiquote": {
                    "site": "fiwikiquote",
                    "title": "Luokka:Roskaa",
                    "badges": []
                },
                "fjwiki": {
                    "site": "fjwiki",
                    "title": "Category:Candidates for speedy deletion",
                    "badges": []
                },
                "frpwiki": {
                    "site": "frpwiki",
                    "title": "Cat\u00e8gorie:Candidates for speedy deletion",
                    "badges": []
                },
                "frwiki": {
                    "site": "frwiki",
                    "title": "Cat\u00e9gorie:Wikip\u00e9dia:Suppression imm\u00e9diate demand\u00e9e",
                    "badges": []
                },
                "frwikivoyage": {
                    "site": "frwikivoyage",
                    "title": "Cat\u00e9gorie:Pages \u00e0 supprimer rapidement",
                    "badges": []
                },
                "gagwiki": {
                    "site": "gagwiki",
                    "title": "Kategoriya:Candidates for speedy deletion",
                    "badges": []
                },
                "ganwiki": {
                    "site": "ganwiki",
                    "title": "\u5206\u985e:\u5feb\u901f\u522a\u5425",
                    "badges": []
                },
                "gawiki": {
                    "site": "gawiki",
                    "title": "Catag\u00f3ir:Leathanaigh le luas-scrios",
                    "badges": []
                },
                "gdwiki": {
                    "site": "gdwiki",
                    "title": "Roinn-se\u00f2rsa:Candidates for speedy deletion",
                    "badges": []
                },
                "glkwiki": {
                    "site": "glkwiki",
                    "title": "\u0631\u062f\u0647:Candidates for speedy deletion",
                    "badges": []
                },
                "glwikiquote": {
                    "site": "glwikiquote",
                    "title": "Categor\u00eda:Limpar",
                    "badges": []
                },
                "gnwiki": {
                    "site": "gnwiki",
                    "title": "\u00d1emohenda:Candidates for speedy deletion",
                    "badges": []
                },
                "gotwiki": {
                    "site": "gotwiki",
                    "title": "\ud800\udf37\ud800\udf30\ud800\udf3d\ud800\udf43\ud800\udf30:Candidates for speedy deletion",
                    "badges": []
                },
                "guwikiquote": {
                    "site": "guwikiquote",
                    "title": "\u0ab6\u0acd\u0ab0\u0ac7\u0aa3\u0ac0:Candidates for speedy deletion",
                    "badges": []
                },
                "gvwiki": {
                    "site": "gvwiki",
                    "title": "Ronney:Duillagyn er \u00e7hionn-scryssey",
                    "badges": []
                },
                "hakwiki": {
                    "site": "hakwiki",
                    "title": "\u5206\u985e:Candidates for speedy deletion",
                    "badges": []
                },
                "hawiki": {
                    "site": "hawiki",
                    "title": "Category:Candidates for speedy deletion",
                    "badges": []
                },
                "hawwiki": {
                    "site": "hawwiki",
                    "title": "M\u0101hele:Candidates for speedy deletion",
                    "badges": []
                },
                "hewiki": {
                    "site": "hewiki",
                    "title": "\u05e7\u05d8\u05d2\u05d5\u05e8\u05d9\u05d4:\u05d5\u05d9\u05e7\u05d9\u05e4\u05d3\u05d9\u05d4: \u05dc\u05de\u05d7\u05d9\u05e7\u05d4 \u05de\u05d4\u05d9\u05e8\u05d4",
                    "badges": []
                },
                "hiwiki": {
                    "site": "hiwiki",
                    "title": "\u0936\u094d\u0930\u0947\u0923\u0940:\u0936\u0940\u0918\u094d\u0930 \u0939\u091f\u093e\u0928\u0947 \u092f\u094b\u0917\u094d\u092f \u092a\u0943\u0937\u094d\u0920",
                    "badges": []
                },
                "hrwiki": {
                    "site": "hrwiki",
                    "title": "Kategorija:Predlo\u0161ci za neodgovaraju\u0107i sadr\u017eaj",
                    "badges": []
                },
                "hsbwiki": {
                    "site": "hsbwiki",
                    "title": "Kategorija:Strony k sp\u011b\u0161nemu wu\u0161m\u00f3rnjenju",
                    "badges": []
                },
                "huwiki": {
                    "site": "huwiki",
                    "title": "Kateg\u00f3ria:Azonnali t\u00f6rl\u00e9sre v\u00e1r\u00f3 lapok",
                    "badges": []
                },
                "huwikinews": {
                    "site": "huwikinews",
                    "title": "Kateg\u00f3ria:Azonnali t\u00f6rl\u00e9sre v\u00e1r\u00f3 lapok",
                    "badges": []
                },
                "huwikisource": {
                    "site": "huwikisource",
                    "title": "Kateg\u00f3ria:Azonnali t\u00f6rl\u00e9sre v\u00e1r\u00f3 lapok",
                    "badges": []
                },
                "hywikiquote": {
                    "site": "hywikiquote",
                    "title": "\u053f\u0561\u057f\u0565\u0563\u0578\u0580\u056b\u0561:\u0531\u0580\u0561\u0563 \u057b\u0576\u057b\u0574\u0561\u0576 \u0569\u0565\u056f\u0576\u0561\u056e\u0578\u0582\u0576\u0565\u0580",
                    "badges": []
                },
                "idwiki": {
                    "site": "idwiki",
                    "title": "Kategori:Artikel yang layak untuk dihapus",
                    "badges": []
                },
                "idwikiquote": {
                    "site": "idwikiquote",
                    "title": "Kategori:Artikel yang layak untuk dihapus",
                    "badges": []
                },
                "iewiki": {
                    "site": "iewiki",
                    "title": "Categorie:Candidates for speedy deletion",
                    "badges": []
                },
                "igwiki": {
                    "site": "igwiki",
                    "title": "\u00d2t\u00f9:Candidates for speedy deletion",
                    "badges": []
                },
                "ikwiki": {
                    "site": "ikwiki",
                    "title": "Category:Candidates for speedy deletion",
                    "badges": []
                },
                "ilowiki": {
                    "site": "ilowiki",
                    "title": "Kategoria:Kandidato ti nadaras a panagikkat",
                    "badges": []
                },
                "iswikiquote": {
                    "site": "iswikiquote",
                    "title": "Flokkur:Ey\u00f0ingartill\u00f6gur",
                    "badges": []
                },
                "itwiki": {
                    "site": "itwiki",
                    "title": "Categoria:Cancellare subito",
                    "badges": []
                },
                "itwikinews": {
                    "site": "itwikinews",
                    "title": "Categoria:Da cancellare subito",
                    "badges": []
                },
                "itwikiquote": {
                    "site": "itwikiquote",
                    "title": "Categoria:Da cancellare subito",
                    "badges": []
                },
                "itwikisource": {
                    "site": "itwikisource",
                    "title": "Categoria:Da cancellare subito",
                    "badges": []
                },
                "itwikivoyage": {
                    "site": "itwikivoyage",
                    "title": "Categoria:Da cancellare subito",
                    "badges": []
                },
                "jawiki": {
                    "site": "jawiki",
                    "title": "Category:\u5373\u6642\u524a\u9664\u5bfe\u8c61\u306e\u30da\u30fc\u30b8",
                    "badges": []
                },
                "jawikinews": {
                    "site": "jawikinews",
                    "title": "\u30ab\u30c6\u30b4\u30ea:\u5373\u6642\u524a\u9664",
                    "badges": []
                },
                "jawikiquote": {
                    "site": "jawikiquote",
                    "title": "\u30ab\u30c6\u30b4\u30ea:\u5373\u6642\u524a\u9664",
                    "badges": []
                },
                "jawikisource": {
                    "site": "jawikisource",
                    "title": "\u30ab\u30c6\u30b4\u30ea:\u5373\u6642\u524a\u9664",
                    "badges": []
                },
                "jbowiki": {
                    "site": "jbowiki",
                    "title": "Category:sutra vimcu",
                    "badges": []
                },
                "jvwiki": {
                    "site": "jvwiki",
                    "title": "Kategori:Artikel sing layak dibusak",
                    "badges": []
                },
                "kaawiki": {
                    "site": "kaawiki",
                    "title": "Kategoriya:Candidates for speedy deletion",
                    "badges": []
                },
                "kabwiki": {
                    "site": "kabwiki",
                    "title": "Taggayt:Candidates for speedy deletion",
                    "badges": []
                },
                "kawiki": {
                    "site": "kawiki",
                    "title": "\u10d9\u10d0\u10e2\u10d4\u10d2\u10dd\u10e0\u10d8\u10d0:\u10ec\u10d0\u10e1\u10d0\u10e8\u10da\u10d4\u10da\u10d8 \u10d2\u10d5\u10d4\u10e0\u10d3\u10d4\u10d1\u10d8",
                    "badges": []
                },
                "kawikiquote": {
                    "site": "kawikiquote",
                    "title": "\u10d9\u10d0\u10e2\u10d4\u10d2\u10dd\u10e0\u10d8\u10d0:\u10ec\u10d0\u10e1\u10d0\u10e8\u10da\u10d4\u10da\u10d8 \u10d2\u10d5\u10d4\u10e0\u10d3\u10d4\u10d1\u10d8",
                    "badges": []
                },
                "kgwiki": {
                    "site": "kgwiki",
                    "title": "Kalasi:Candidates for speedy deletion",
                    "badges": []
                },
                "kiwiki": {
                    "site": "kiwiki",
                    "title": "Category:Candidates for speedy deletion",
                    "badges": []
                },
                "kkwiki": {
                    "site": "kkwiki",
                    "title": "\u0421\u0430\u043d\u0430\u0442:\u0416\u0435\u0434\u0435\u043b \u0436\u043e\u044e\u0493\u0430 \u04b1\u0441\u044b\u043d\u044b\u043b\u0493\u0430\u043d\u0434\u0430\u0440",
                    "badges": []
                },
                "klwiki": {
                    "site": "klwiki",
                    "title": "Sumut atassuseq:Candidates for speedy deletion",
                    "badges": []
                },
                "kmwiki": {
                    "site": "kmwiki",
                    "title": "\u1785\u17c6\u178e\u17b6\u178f\u17cb\u1790\u17d2\u1793\u17b6\u1780\u17cb\u1780\u17d2\u179a\u17bb\u1798:\u179b\u17bb\u1794",
                    "badges": []
                },
                "knwiki": {
                    "site": "knwiki",
                    "title": "\u0cb5\u0cb0\u0ccd\u0c97:Candidates for speedy deletion",
                    "badges": []
                },
                "koiwiki": {
                    "site": "koiwiki",
                    "title": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f:Candidates for speedy deletion",
                    "badges": []
                },
                "kowiki": {
                    "site": "kowiki",
                    "title": "\ubd84\ub958:\uc0ad\uc81c \uc2e0\uccad \ubb38\uc11c",
                    "badges": []
                },
                "kowikinews": {
                    "site": "kowikinews",
                    "title": "\ubd84\ub958:\uc0ad\uc81c \uc2e0\uccad",
                    "badges": []
                },
                "kowikiquote": {
                    "site": "kowikiquote",
                    "title": "\ubd84\ub958:\uc0ad\uc81c \uc2e0\uccad \ubb38\uc11c",
                    "badges": []
                },
                "kowikisource": {
                    "site": "kowikisource",
                    "title": "\ubd84\ub958:\uc0ad\uc81c \uc2e0\uccad \ubb38\uc11c",
                    "badges": []
                },
                "krcwiki": {
                    "site": "krcwiki",
                    "title": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f:\u0412\u0438\u043a\u0438\u043f\u0435\u0434\u0438\u044f:\u0422\u0435\u0440\u043a \u043a\u0435\u0442\u0435\u0440\u0438\u043b\u0438\u0440\u0433\u0435",
                    "badges": []
                },
                "kswiki": {
                    "site": "kswiki",
                    "title": "\u0632\u0672\u0698:Candidates for speedy deletion",
                    "badges": []
                },
                "kuwiki": {
                    "site": "kuwiki",
                    "title": "Kategor\u00ee:Gotar\u00ean ku b\u00ean j\u00eabirin",
                    "badges": []
                },
                "kuwikiquote": {
                    "site": "kuwikiquote",
                    "title": "Kategor\u00ee:Gotar\u00ean ku b\u00ean j\u00eabirin",
                    "badges": []
                },
                "kvwiki": {
                    "site": "kvwiki",
                    "title": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f:Wikipedia:Candidates for speedy deletion",
                    "badges": []
                },
                "kwwiki": {
                    "site": "kwwiki",
                    "title": "Klass:Profyansow rag dilea",
                    "badges": []
                },
                "lbewiki": {
                    "site": "lbewiki",
                    "title": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f:Speedy deletion requests",
                    "badges": []
                },
                "lgwiki": {
                    "site": "lgwiki",
                    "title": "Category:Candidates for speedy deletion",
                    "badges": []
                },
                "lijwiki": {
                    "site": "lijwiki",
                    "title": "Categor\u00eea:Candidates for speedy deletion",
                    "badges": []
                },
                "liwiki": {
                    "site": "liwiki",
                    "title": "Categorie:Kandidate veur sjnel eweg te goeje",
                    "badges": []
                },
                "lnwiki": {
                    "site": "lnwiki",
                    "title": "Cat\u00e9gorie:Candidates for speedy deletion",
                    "badges": []
                },
                "lowiki": {
                    "site": "lowiki",
                    "title": "\u0edd\u0ea7\u0e94:Candidates for speedy deletion",
                    "badges": []
                },
                "ltgwiki": {
                    "site": "ltgwiki",
                    "title": "Kategoreja:Candidates for speedy deletion",
                    "badges": []
                },
                "ltwiki": {
                    "site": "ltwiki",
                    "title": "Kategorija:Kandidatai skubiai trinti",
                    "badges": []
                },
                "ltwikiquote": {
                    "site": "ltwikiquote",
                    "title": "Kategorija:Kandidatai skubiai trinti",
                    "badges": []
                },
                "lvwiki": {
                    "site": "lvwiki",
                    "title": "Kategorija:Lapas, kas izvirz\u012btas dz\u0113\u0161anai",
                    "badges": []
                },
                "map_bmswiki": {
                    "site": "map_bmswiki",
                    "title": "Kategori:Artikel sing arep dibusak",
                    "badges": []
                },
                "mdfwiki": {
                    "site": "mdfwiki",
                    "title": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0435:Candidates for speedy deletion",
                    "badges": []
                },
                "mgwiki": {
                    "site": "mgwiki",
                    "title": "Sokajy:Candidates for speedy deletion",
                    "badges": []
                },
                "mhrwiki": {
                    "site": "mhrwiki",
                    "title": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0439:\u0428\u04e7\u0440\u0430\u0448",
                    "badges": []
                },
                "miwiki": {
                    "site": "miwiki",
                    "title": "Category:Mukua",
                    "badges": []
                },
                "mkwiki": {
                    "site": "mkwiki",
                    "title": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0458\u0430:\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0438 \u0437\u0430 \u0431\u0440\u0437\u043e \u0431\u0440\u0438\u0448\u0435\u045a\u0435",
                    "badges": []
                },
                "mlwiki": {
                    "site": "mlwiki",
                    "title": "\u0d35\u0d7c\u0d17\u0d4d\u0d17\u0d02:\u0d2a\u0d46\u0d1f\u0d4d\u0d1f\u0d46\u0d28\u0d4d\u0d28\u0d4d \u0d28\u0d40\u0d15\u0d4d\u0d15\u0d02 \u0d1a\u0d46\u0d2f\u0d4d\u0d2f\u0d41\u0d35\u0d3e\u0d7b \u0d38\u0d3e\u0d27\u0d4d\u0d2f\u0d24\u0d2f\u0d41\u0d33\u0d4d\u0d33\u0d35 (\u0d0e\u0d32\u0d4d\u0d32\u0d3e\u0d02)",
                    "badges": []
                },
                "mnwiki": {
                    "site": "mnwiki",
                    "title": "\u0410\u043d\u0433\u0438\u043b\u0430\u043b:\u0423\u0441\u0442\u0433\u0430\u043b\u0434 \u043e\u0440\u043e\u0445 \u0445\u0443\u0443\u0434\u0441\u0443\u0443\u0434",
                    "badges": []
                },
                "mrjwiki": {
                    "site": "mrjwiki",
                    "title": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438:Candidates for speedy deletion",
                    "badges": []
                },
                "mswiki": {
                    "site": "mswiki",
                    "title": "Kategori:Calon untuk penghapusan segera",
                    "badges": []
                },
                "mtwiki": {
                    "site": "mtwiki",
                    "title": "Kategorija:Proposti g\u0127at-t\u0127assir minnufih",
                    "badges": []
                },
                "myvwiki": {
                    "site": "myvwiki",
                    "title": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f:Candidates for speedy deletion",
                    "badges": []
                },
                "mznwiki": {
                    "site": "mznwiki",
                    "title": "\u0631\u062c:\u0632\u0648\u062f \u0628\u0623\u0626\u06cc\u062a\u0646 \u0646\u0648\u0645\u0632\u062f\u0648\u0646",
                    "badges": []
                },
                "nahwiki": {
                    "site": "nahwiki",
                    "title": "Neneuhc\u0101y\u014dtl:Huiquipedia:Borrar (definitivo)",
                    "badges": []
                },
                "nawiki": {
                    "site": "nawiki",
                    "title": "Category:Wikipedia:Animwen iyababa",
                    "badges": []
                },
                "ndswiki": {
                    "site": "ndswiki",
                    "title": "Kategorie:Wikipedia:Gauweg",
                    "badges": []
                },
                "newwiki": {
                    "site": "newwiki",
                    "title": "\u092a\u0941\u091a\u0903:Candidates for speedy deletion",
                    "badges": []
                },
                "nlwiki": {
                    "site": "nlwiki",
                    "title": "Categorie:Wikipedia:Nuweg",
                    "badges": []
                },
                "nlwikiquote": {
                    "site": "nlwikiquote",
                    "title": "Categorie:Wikiquote:Nuweg",
                    "badges": []
                },
                "nlwikisource": {
                    "site": "nlwikisource",
                    "title": "Categorie:Wikisource:Nuweg",
                    "badges": []
                },
                "nlwikivoyage": {
                    "site": "nlwikivoyage",
                    "title": "Categorie:Wikivoyage:Artikelen die direct verwijderd moeten worden",
                    "badges": []
                },
                "nnwiki": {
                    "site": "nnwiki",
                    "title": "Kategori:Sider merkte for sn\u00f8ggsletting",
                    "badges": []
                },
                "nnwikiquote": {
                    "site": "nnwikiquote",
                    "title": "Kategori:Sider merkte for sletting",
                    "badges": []
                },
                "novwiki": {
                    "site": "novwiki",
                    "title": "Category:Candidates for speedy deletion",
                    "badges": []
                },
                "nowiki": {
                    "site": "nowiki",
                    "title": "Kategori:Sider som er foresl\u00e5tt raskt slettet",
                    "badges": []
                },
                "nowikiquote": {
                    "site": "nowikiquote",
                    "title": "Kategori:Sider som er foresl\u00e5tt raskt slettet",
                    "badges": []
                },
                "nowikisource": {
                    "site": "nowikisource",
                    "title": "Kategori:Sider som er foresl\u00e5tt raskt slettet",
                    "badges": []
                },
                "nrmwiki": {
                    "site": "nrmwiki",
                    "title": "Category:Candidates for speedy deletion",
                    "badges": []
                },
                "nvwiki": {
                    "site": "nvwiki",
                    "title": "T\u02bc\u00e1\u00e1\u0142\u00e1h\u00e1gi \u00e1t\u02bc\u00e9ego:Candidates for speedy deletion",
                    "badges": []
                },
                "nywiki": {
                    "site": "nywiki",
                    "title": "Category:Candidates for speedy deletion",
                    "badges": []
                },
                "omwiki": {
                    "site": "omwiki",
                    "title": "Category:Wikipedia:Candidates for speedy deletion",
                    "badges": []
                },
                "orwiki": {
                    "site": "orwiki",
                    "title": "\u0b36\u0b4d\u0b30\u0b47\u0b23\u0b40:Candidates for speedy deletion",
                    "badges": []
                },
                "oswiki": {
                    "site": "oswiki",
                    "title": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438:\u0412\u0438\u043a\u0438\u043f\u0435\u0434\u0438:\u0410\u043f\u043f\u0430\u0440\u044b\u043d\u043c\u00e6 \u043b\u00e6\u0432\u00e6\u0440\u0434 \u0444\u00e6\u0440\u0441\u0442\u00e6",
                    "badges": []
                },
                "pagwiki": {
                    "site": "pagwiki",
                    "title": "Category:Candidates for speedy deletion",
                    "badges": []
                },
                "pamwiki": {
                    "site": "pamwiki",
                    "title": "Category:Candidates for speedy deletion",
                    "badges": []
                },
                "pawiki": {
                    "site": "pawiki",
                    "title": "\u0a38\u0a3c\u0a4d\u0a30\u0a47\u0a23\u0a40:\u0a1b\u0a47\u0a24\u0a40 \u0a2e\u0a3f\u0a1f\u0a3e\u0a09\u0a23\u0a2f\u0a4b\u0a17 \u0a38\u0a2b\u0a3c\u0a47",
                    "badges": []
                },
                "pcdwiki": {
                    "site": "pcdwiki",
                    "title": "Cat\u00e9gorie:Candidates for speedy deletion",
                    "badges": []
                },
                "pihwiki": {
                    "site": "pihwiki",
                    "title": "Category:Candidates for speedy deletion",
                    "badges": []
                },
                "plwiki": {
                    "site": "plwiki",
                    "title": "Kategoria:Ekspresowe kasowanie",
                    "badges": []
                },
                "plwikinews": {
                    "site": "plwikinews",
                    "title": "Kategoria:Ekspresowe kasowanko",
                    "badges": []
                },
                "plwikiquote": {
                    "site": "plwikiquote",
                    "title": "Kategoria:Ekspresowe kasowanko",
                    "badges": []
                },
                "plwikisource": {
                    "site": "plwikisource",
                    "title": "Kategoria:Ekspresowe kasowanie",
                    "badges": []
                },
                "plwikivoyage": {
                    "site": "plwikivoyage",
                    "title": "Kategoria:Ekspresowe kasowanie",
                    "badges": []
                },
                "pntwiki": {
                    "site": "pntwiki",
                    "title": "\u039a\u03b1\u03c4\u03b7\u03b3\u03bf\u03c1\u03af\u03b1\u03bd:\u03a3\u03b5\u03bb\u03af\u03b4\u03b5\u03c2 \u03b3\u03b9\u03b1 \u03b3\u03c1\u03ae\u03b3\u03bf\u03c1\u03b7 \u03b4\u03b9\u03b1\u03b3\u03c1\u03b1\u03c6\u03ae",
                    "badges": []
                },
                "ptwiki": {
                    "site": "ptwiki",
                    "title": "Categoria:!P\u00e1ginas para elimina\u00e7\u00e3o r\u00e1pida",
                    "badges": []
                },
                "ptwikiquote": {
                    "site": "ptwikiquote",
                    "title": "Categoria:P\u00e1ginas para elimina\u00e7\u00e3o r\u00e1pida",
                    "badges": []
                },
                "ptwikisource": {
                    "site": "ptwikisource",
                    "title": "Categoria:!P\u00e1ginas para elimina\u00e7\u00e3o r\u00e1pida",
                    "badges": []
                },
                "ptwikivoyage": {
                    "site": "ptwikivoyage",
                    "title": "Categoria:Eliminar",
                    "badges": []
                },
                "quwiki": {
                    "site": "quwiki",
                    "title": "Katiguriya:Wikipidiya:Champana",
                    "badges": []
                },
                "rmwiki": {
                    "site": "rmwiki",
                    "title": "Categoria:Candidates for speedy deletion",
                    "badges": []
                },
                "rmywiki": {
                    "site": "rmywiki",
                    "title": "Shopni:Khosipnaske lekha",
                    "badges": []
                },
                "rnwiki": {
                    "site": "rnwiki",
                    "title": "Category:Candidates for speedy deletion",
                    "badges": []
                },
                "roa_tarawiki": {
                    "site": "roa_tarawiki",
                    "title": "Category:Candidate pa scangellaziona veloce",
                    "badges": []
                },
                "rowiki": {
                    "site": "rowiki",
                    "title": "Categorie:Pagini de \u0219ters rapid",
                    "badges": []
                },
                "rowikisource": {
                    "site": "rowikisource",
                    "title": "Categorie:Propuneri pentru \u015ftergere rapid\u0103",
                    "badges": []
                },
                "rowikivoyage": {
                    "site": "rowikivoyage",
                    "title": "Categorie:Pagini de \u0219ters",
                    "badges": []
                },
                "ruwiki": {
                    "site": "ruwiki",
                    "title": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f:\u0412\u0438\u043a\u0438\u043f\u0435\u0434\u0438\u044f:\u041a \u0431\u044b\u0441\u0442\u0440\u043e\u043c\u0443 \u0443\u0434\u0430\u043b\u0435\u043d\u0438\u044e",
                    "badges": []
                },
                "ruwikiquote": {
                    "site": "ruwikiquote",
                    "title": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f:\u0412\u0438\u043a\u0438\u0446\u0438\u0442\u0430\u0442\u043d\u0438\u043a:\u041a \u0431\u044b\u0441\u0442\u0440\u043e\u043c\u0443 \u0443\u0434\u0430\u043b\u0435\u043d\u0438\u044e",
                    "badges": []
                },
                "ruwikisource": {
                    "site": "ruwikisource",
                    "title": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f:\u0412\u0438\u043a\u0438\u0442\u0435\u043a\u0430:\u041a \u0431\u044b\u0441\u0442\u0440\u043e\u043c\u0443 \u0443\u0434\u0430\u043b\u0435\u043d\u0438\u044e",
                    "badges": []
                },
                "rwwiki": {
                    "site": "rwwiki",
                    "title": "Category:Candidates for speedy deletion",
                    "badges": []
                },
                "sahwiki": {
                    "site": "sahwiki",
                    "title": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f:\u0411\u0438\u043a\u0438\u043f\u0438\u044d\u0434\u044c\u0438\u0439\u044d:\u0422\u04af\u0440\u0433\u044d\u043d\u043d\u0438\u043a \u0441\u043e\u0442\u043e\u0440\u0433\u043e",
                    "badges": []
                },
                "scnwiki": {
                    "site": "scnwiki",
                    "title": "Catigur\u00eca:Pruposti pi eliminazzioni lesta",
                    "badges": []
                },
                "scowiki": {
                    "site": "scowiki",
                    "title": "Category:Candidates for speedy deletion",
                    "badges": []
                },
                "scwiki": {
                    "site": "scwiki",
                    "title": "Categoria:De fuliai immoi",
                    "badges": []
                },
                "sdwiki": {
                    "site": "sdwiki",
                    "title": "\u0632\u0645\u0631\u0648:\u062a\u0631\u062a \u068a\u0627\u067a \u062c\u0627 \u0627\u0645\u064a\u062f\u0648\u0627\u0631",
                    "badges": []
                },
                "sewiki": {
                    "site": "sewiki",
                    "title": "Kategoriija:Njuolggosihkkun",
                    "badges": []
                },
                "sgwiki": {
                    "site": "sgwiki",
                    "title": "Cat\u00e9gorie:Candidates for speedy deletion",
                    "badges": []
                },
                "shwiki": {
                    "site": "shwiki",
                    "title": "Kategorija:Kandidati za brzo brisanje",
                    "badges": []
                },
                "simplewiki": {
                    "site": "simplewiki",
                    "title": "Category:Quick deletion requests",
                    "badges": []
                },
                "siwiki": {
                    "site": "siwiki",
                    "title": "\u0db4\u0dca\u200d\u0dbb\u0dc0\u0dbb\u0dca\u0d9c\u0dba:Candidates for speedy deletion",
                    "badges": []
                },
                "skwiki": {
                    "site": "skwiki",
                    "title": "Kateg\u00f3ria:Wikip\u00e9dia:Kandid\u00e1ti na r\u00fdchle zmazanie",
                    "badges": []
                },
                "skwikiquote": {
                    "site": "skwikiquote",
                    "title": "Kateg\u00f3ria:Str\u00e1nky na zmazanie",
                    "badges": []
                },
                "skwikisource": {
                    "site": "skwikisource",
                    "title": "Kateg\u00f3ria:Na zmazanie",
                    "badges": []
                },
                "slwiki": {
                    "site": "slwiki",
                    "title": "Kategorija:Predlogi za hitro brisanje",
                    "badges": []
                },
                "smwiki": {
                    "site": "smwiki",
                    "title": "Category:Candidates for speedy deletion",
                    "badges": []
                },
                "snwiki": {
                    "site": "snwiki",
                    "title": "Category:Candidates for speedy deletion",
                    "badges": []
                },
                "sqwikinews": {
                    "site": "sqwikinews",
                    "title": "Kategoria:Candidates for speedy deletion",
                    "badges": []
                },
                "srnwiki": {
                    "site": "srnwiki",
                    "title": "Guru:Candidates for speedy deletion",
                    "badges": []
                },
                "srwiki": {
                    "site": "srwiki",
                    "title": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0458\u0430:\u0411\u0440\u0437\u043e \u0431\u0440\u0438\u0441\u0430\u045a\u0435",
                    "badges": []
                },
                "srwikinews": {
                    "site": "srwikinews",
                    "title": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0458\u0430:\u0411\u0440\u0437\u043e \u0431\u0440\u0438\u0441\u0430\u045a\u0435",
                    "badges": []
                },
                "srwikiquote": {
                    "site": "srwikiquote",
                    "title": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0458\u0430:\u0411\u0440\u0437\u043e \u0431\u0440\u0438\u0441\u0430\u045a\u0435",
                    "badges": []
                },
                "srwikisource": {
                    "site": "srwikisource",
                    "title": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0458\u0430:\u0411\u0440\u0437\u043e \u0431\u0440\u0438\u0441\u0430\u045a\u0435",
                    "badges": []
                },
                "sswiki": {
                    "site": "sswiki",
                    "title": "Category:Candidates for speedy deletion",
                    "badges": []
                },
                "stqwiki": {
                    "site": "stqwiki",
                    "title": "Kategorie:Candidates for speedy deletion",
                    "badges": []
                },
                "stwiki": {
                    "site": "stwiki",
                    "title": "Category:Candidates for speedy deletion",
                    "badges": []
                },
                "suwiki": {
                    "site": "suwiki",
                    "title": "Kategori:Artikel anu kudu dihapus",
                    "badges": []
                },
                "svwiki": {
                    "site": "svwiki",
                    "title": "Kategori:Snabbraderingar",
                    "badges": []
                },
                "svwikiquote": {
                    "site": "svwikiquote",
                    "title": "Kategori:Snabba raderingar",
                    "badges": []
                },
                "swwiki": {
                    "site": "swwiki",
                    "title": "Jamii:Makala kwa ufutaji",
                    "badges": []
                },
                "szlwiki": {
                    "site": "szlwiki",
                    "title": "Kategoryjo:Gibke wy\u0107epowa\u0144y",
                    "badges": []
                },
                "tawiki": {
                    "site": "tawiki",
                    "title": "\u0baa\u0b95\u0bc1\u0baa\u0bcd\u0baa\u0bc1:\u0bb5\u0bbf\u0bb0\u0bc8\u0ba8\u0bcd\u0ba4\u0bc1 \u0ba8\u0bc0\u0b95\u0bcd\u0b95\u0baa\u0bcd\u0baa\u0b9f \u0bb5\u0bc7\u0ba3\u0bcd\u0b9f\u0bbf\u0baf \u0baa\u0b95\u0bcd\u0b95\u0b99\u0bcd\u0b95\u0bb3\u0bcd",
                    "badges": []
                },
                "tawikiquote": {
                    "site": "tawikiquote",
                    "title": "\u0baa\u0b95\u0bc1\u0baa\u0bcd\u0baa\u0bc1:\u0bb5\u0bbf\u0bb0\u0bc8\u0ba8\u0bcd\u0ba4\u0bc1 \u0ba8\u0bc0\u0b95\u0bcd\u0b95\u0baa\u0bcd\u0baa\u0b9f \u0bb5\u0bc7\u0ba3\u0bcd\u0b9f\u0bbf\u0baf \u0baa\u0b95\u0bcd\u0b95\u0b99\u0bcd\u0b95\u0bb3\u0bcd",
                    "badges": []
                },
                "tetwiki": {
                    "site": "tetwiki",
                    "title": "Kategoria:Kandidatu ba halakon lailais",
                    "badges": []
                },
                "tewiki": {
                    "site": "tewiki",
                    "title": "\u0c35\u0c30\u0c4d\u0c17\u0c02:Candidates for speedy deletion",
                    "badges": []
                },
                "tgwiki": {
                    "site": "tgwiki",
                    "title": "\u0413\u0443\u0440\u04ef\u04b3:\u041c\u0430\u049b\u043e\u043b\u0430\u04b3\u043e\u0438 \u043d\u043e\u043c\u0437\u0430\u0434\u0438 \u04b3\u0430\u0437\u0444",
                    "badges": []
                },
                "thwiki": {
                    "site": "thwiki",
                    "title": "\u0e2b\u0e21\u0e27\u0e14\u0e2b\u0e21\u0e39\u0e48:\u0e2b\u0e19\u0e49\u0e32\u0e17\u0e35\u0e48\u0e16\u0e39\u0e01\u0e41\u0e08\u0e49\u0e07\u0e25\u0e1a",
                    "badges": []
                },
                "thwikiquote": {
                    "site": "thwikiquote",
                    "title": "\u0e2b\u0e21\u0e27\u0e14\u0e2b\u0e21\u0e39\u0e48:\u0e2b\u0e19\u0e49\u0e32\u0e17\u0e35\u0e48\u0e16\u0e39\u0e01\u0e41\u0e08\u0e49\u0e07\u0e25\u0e1a",
                    "badges": []
                },
                "tiwiki": {
                    "site": "tiwiki",
                    "title": "Category:Candidates for speedy deletion",
                    "badges": []
                },
                "tlwiki": {
                    "site": "tlwiki",
                    "title": "Kategorya:Mga pahinang mabilisang buburahin",
                    "badges": []
                },
                "towiki": {
                    "site": "towiki",
                    "title": "Category:Ngaahi fili ma\u02bba e t\u0101mate\u02bbi vave",
                    "badges": []
                },
                "tpiwiki": {
                    "site": "tpiwiki",
                    "title": "Grup:All articles proposed for deletion",
                    "badges": []
                },
                "trwiki": {
                    "site": "trwiki",
                    "title": "Kategori:Vikipedi silinecek sayfalar",
                    "badges": []
                },
                "tswiki": {
                    "site": "tswiki",
                    "title": "Category:Candidates for speedy deletion",
                    "badges": []
                },
                "tumwiki": {
                    "site": "tumwiki",
                    "title": "Category:Candidates for speedy deletion",
                    "badges": []
                },
                "twwiki": {
                    "site": "twwiki",
                    "title": "Category:Candidates for speedy deletion",
                    "badges": []
                },
                "tyvwiki": {
                    "site": "tyvwiki",
                    "title": "\u0410\u04a3\u0433\u044b\u043b\u0430\u043b:Candidates for speedy deletion",
                    "badges": []
                },
                "tywiki": {
                    "site": "tywiki",
                    "title": "Cat\u00e9gorie:Candidates for speedy deletion",
                    "badges": []
                },
                "udmwiki": {
                    "site": "udmwiki",
                    "title": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f:\u0412\u0438\u043a\u0438\u043f\u0435\u0434\u0438\u044f:\u041a \u0431\u044b\u0441\u0442\u0440\u043e\u043c\u0443 \u0443\u0434\u0430\u043b\u0435\u043d\u0438\u044e",
                    "badges": []
                },
                "ugwiki": {
                    "site": "ugwiki",
                    "title": "\u062a\u06c8\u0631:Candidates for speedy deletion",
                    "badges": []
                },
                "ukwiki": {
                    "site": "ukwiki",
                    "title": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0456\u044f:\u0421\u0442\u0430\u0442\u0442\u0456 \u0434\u043e \u0448\u0432\u0438\u0434\u043a\u043e\u0433\u043e \u0432\u0438\u043b\u0443\u0447\u0435\u043d\u043d\u044f",
                    "badges": []
                },
                "ukwikiquote": {
                    "site": "ukwikiquote",
                    "title": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0456\u044f:\u0421\u0442\u0430\u0442\u0442\u0456 \u0434\u043e \u0448\u0432\u0438\u0434\u043a\u043e\u0433\u043e \u0432\u0438\u043b\u0443\u0447\u0435\u043d\u043d\u044f",
                    "badges": []
                },
                "ukwikisource": {
                    "site": "ukwikisource",
                    "title": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0456\u044f:\u0421\u0442\u043e\u0440\u0456\u043d\u043a\u0438 \u0434\u043e \u0448\u0432\u0438\u0434\u043a\u043e\u0433\u043e \u0432\u0438\u043b\u0443\u0447\u0435\u043d\u043d\u044f",
                    "badges": []
                },
                "ukwikivoyage": {
                    "site": "ukwikivoyage",
                    "title": "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0456\u044f:\u0421\u0442\u0430\u0442\u0442\u0456 \u0434\u043e \u0448\u0432\u0438\u0434\u043a\u043e\u0433\u043e \u0432\u0438\u043b\u0443\u0447\u0435\u043d\u043d\u044f",
                    "badges": []
                },
                "urwiki": {
                    "site": "urwiki",
                    "title": "\u0632\u0645\u0631\u06c1:\u0627\u0645\u06cc\u062f\u0648\u0627\u0631 \u0628\u0631\u0627\u06d3 \u062d\u0630\u0641 \u0634\u062f\u06af\u06cc",
                    "badges": []
                },
                "vecwiki": {
                    "site": "vecwiki",
                    "title": "Categoria:Da scanse\u0142are suito",
                    "badges": []
                },
                "vecwikisource": {
                    "site": "vecwikisource",
                    "title": "Categoria:Da scancelar",
                    "badges": []
                },
                "vepwiki": {
                    "site": "vepwiki",
                    "title": "Kategorii:\u010cuta poi\u0161",
                    "badges": []
                },
                "vewiki": {
                    "site": "vewiki",
                    "title": "Category:Candidates for speedy deletion",
                    "badges": []
                },
                "viwiki": {
                    "site": "viwiki",
                    "title": "Th\u1ec3 lo\u1ea1i:Ch\u1edd x\u00f3a",
                    "badges": []
                },
                "viwikiquote": {
                    "site": "viwikiquote",
                    "title": "Th\u1ec3 lo\u1ea1i:Ch\u1edd x\u00f3a",
                    "badges": []
                },
                "viwikisource": {
                    "site": "viwikisource",
                    "title": "Th\u1ec3 lo\u1ea1i:\u0110\u1ec1 ngh\u1ecb x\u00f3a nhanh",
                    "badges": []
                },
                "viwikivoyage": {
                    "site": "viwikivoyage",
                    "title": "Th\u1ec3 lo\u1ea1i:Ch\u1edd x\u00f3a",
                    "badges": []
                },
                "vlswiki": {
                    "site": "vlswiki",
                    "title": "Categorie:Wikipedia:Nuweg",
                    "badges": []
                },
                "vowiki": {
                    "site": "vowiki",
                    "title": "Klad:Pads mo\u00fckabik",
                    "badges": []
                },
                "warwiki": {
                    "site": "warwiki",
                    "title": "Kaarangay:Candidates for speedy deletion",
                    "badges": []
                },
                "wuuwiki": {
                    "site": "wuuwiki",
                    "title": "\u5206\u7c7b:\u5feb\u901f\u5220\u9664\u5019\u9009",
                    "badges": []
                },
                "xalwiki": {
                    "site": "xalwiki",
                    "title": "\u04d8\u04d9\u0448\u043b:Candidates for speedy deletion",
                    "badges": []
                },
                "xhwiki": {
                    "site": "xhwiki",
                    "title": "Category:Candidates for speedy deletion",
                    "badges": []
                },
                "xmfwiki": {
                    "site": "xmfwiki",
                    "title": "\u10d9\u10d0\u10e2\u10d4\u10d2\u10dd\u10e0\u10d8\u10d0:Candidates for speedy deletion",
                    "badges": []
                },
                "yiwiki": {
                    "site": "yiwiki",
                    "title": "\u05e7\u05d0\u05b7\u05d8\u05e2\u05d2\u05d0\u05b8\u05e8\u05d9\u05e2:\u05d2\u05e2\u05e9\u05d8\u05e2\u05dc\u05d8\u05e2 \u05e6\u05d5 \u05e9\u05e0\u05e2\u05dc \u05de\u05e2\u05e7\u05df",
                    "badges": []
                },
                "yowiki": {
                    "site": "yowiki",
                    "title": "\u1eb8\u0300ka:\u00c0w\u1ecdn oj\u00faew\u00e9 f\u00fan \u00ecpar\u1eb9\u0301 k\u00ed\u00e1k\u00ed\u00e1",
                    "badges": []
                },
                "zawiki": {
                    "site": "zawiki",
                    "title": "\u5206\u7c7b:Candidates for speedy deletion",
                    "badges": []
                },
                "zeawiki": {
                    "site": "zeawiki",
                    "title": "Categorie:Wikipedia:Noeweg",
                    "badges": []
                },
                "zh_classicalwiki": {
                    "site": "zh_classicalwiki",
                    "title": "Category:\u901f\u522a\u5019",
                    "badges": []
                },
                "zh_min_nanwiki": {
                    "site": "zh_min_nanwiki",
                    "title": "\u5206\u985e:T\u00e1n-th\u0101i kho\u00e0i-sok th\u00e2i-t\u00fb \u00ea ia\u030dh",
                    "badges": []
                },
                "zh_min_nanwikiquote": {
                    "site": "zh_min_nanwikiquote",
                    "title": "\u5206\u985e:T\u00e1n-th\u0101i kho\u00e0i-sok th\u00e2i-t\u00fb \u00ea ia\u030dh",
                    "badges": []
                },
                "zh_yuewiki": {
                    "site": "zh_yuewiki",
                    "title": "Category:\u5373\u523b\u522a\u9664\u5019\u9078",
                    "badges": []
                },
                "zhwiki": {
                    "site": "zhwiki",
                    "title": "Category:\u5feb\u901f\u5220\u9664\u5019\u9009",
                    "badges": []
                },
                "zhwikinews": {
                    "site": "zhwikinews",
                    "title": "Category:\u5feb\u901f\u5220\u9664\u5019\u9009",
                    "badges": []
                },
                "zhwikiquote": {
                    "site": "zhwikiquote",
                    "title": "Category:\u5feb\u901f\u5220\u9664\u5019\u9009",
                    "badges": []
                },
                "zhwikisource": {
                    "site": "zhwikisource",
                    "title": "Category:\u5feb\u901f\u5220\u9664\u5019\u9009",
                    "badges": []
                },
                "zhwikivoyage": {
                    "site": "zhwikivoyage",
                    "title": "Category:\u5feb\u901f\u5220\u9664\u5019\u9009",
                    "badges": []
                },
                "zuwiki": {
                    "site": "zuwiki",
                    "title": "Category:Candidates for speedy deletion",
                    "badges": []
                }
            }
        }
    },
    "success": 1
}

# take each language and check if it is the family.
pages = [
    articles_for_deletion,
    speedy_deletion,
    proposed_deletion,
]


for p in pages :
    for eid in p["entities"] :
        e = p["entities"][eid]
        #pprint.pprint(e)
        name = e["labels"]['en']['value']
        #print name
        
        for lc in f.langs:
            wikiname = '%swiki' % lc
            if wikiname in e["sitelinks"]:
                catname = e["sitelinks"][wikiname]['title']
                parts =catname.split(':')     
                justcatname = ':'.join(parts[1:])
                print "python  ./pwb.py transferbot -lang:%s -tolang:%s -tofamily:speedydeletion  -family:wikipedia '-catr:%s'" % (lc, lc, justcatname)
   
            else:
                #print name, "missing", wikiname
                pass
                

