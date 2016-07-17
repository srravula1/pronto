# coding: utf-8
"""
Test lots of ontologies from the OBO Foundry.
"""

OBO_CATALOG = 'http://www.obofoundry.org/registry/ontologies.jsonld'

BLOCKLIST = ('chebi.owl')

import json
import pronto
import signal
import time
import multiprocessing
import multiprocessing.pool


try:
    import urllib.request as rq
except ImportError:
    import urllib2 as rq


def timer(signum, frame):
    #print('Quitter called with signal', signum)
    raise IOError("        Couldn't parse ontology within time limit !")

def task(ontology):
    ontid = ontology["id"]
    print('Testing: {}'.format(ontid))

    if not 'products' in ontology.keys():
        return

    for product in ontology["products"]:

        if product['id'] in BLOCKLIST:
            continue

        print('    file: {}'.format(product["id"]))

        t = time.time()
        try:
           ont = pronto.Ontology(product["ontology_purl"])
           print("      {} terms extracted in {}s.".format(len(ont), round(time.time()-t, 1)))
        except OSError:
           continue

#signal.signal(signal.SIGALRM, timer)

content = rq.urlopen(OBO_CATALOG).read()
catalog = json.loads(content.decode('utf-8'))

#pool = multiprocessing.pool.Pool(multiprocessing.cpu_count() * 4)

#pool.
list(map(task, catalog["ontologies"]))



