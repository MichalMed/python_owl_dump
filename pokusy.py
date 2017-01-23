import rdflib
import pprint
import datetime


from rdflib.namespace import FOAF
g = rdflib.Graph()

#tady bude výsledek
res = rdflib.Graph()

g.parse("../output.ttl", format="turtle")

from rdflib import URIRef
from rdflib.namespace import RDF
SSVU = URIRef("http://onto.fel.cvut.cz/ontologies/town-plan/databaseTableSSVU")
REF_SYS = URIRef("http://onto.fel.cvut.cz/ontologies/town-plan/spatial_ref_sys")
ssvuNamespace = 'http://onto.fel.cvut.cz/ontologies/town-plan/urk_ss_vyuzitizakl_p/'
#for s,p,o in g.triples( (None, RDF.type, SSVU) ):
#   pprint.pprint(s + " " + p + " " + o)


# vytvořím seznam objektů
uris = list()
d = datetime.datetime.today()


for s,p,o in g.triples( (None, RDF.type, None) ):
    if (o != REF_SYS):
        #do grafu objekty ukládám truply, kde s je objekt jiného typu než REF_SYS
        #objekty += g.triples( (s, RDF.type, None) )
        # je to zbytečné, v praxi mi stačí seznam id těchto objektů
        uris.append(URIRef(ssvuNamespace + str(d.date()) + 'T' + str(d.time()) + '/' + str(s.split('/')[-1])))
for t in uris:
    pprint.pprint(t)


g.serialize(format="turtle")
