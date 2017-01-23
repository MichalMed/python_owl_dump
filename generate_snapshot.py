import rdflib
import datetime

# http://rdflib3.readthedocs.io/en/latest/intro_to_parsing.html

# číst graf

g = rdflib.Graph()
g.parse("../output.ttl", format="turtle")
#tady bude výsledek
resG = rdflib.Graph()

# hledat v grafu objekty
from rdflib import URIRef
from rdflib.namespace import RDF
from rdflib import Namespace
ssvuNamespace = 'http://onto.fel.cvut.cz/ontologies/town-plan/urk_ss_vyuzitizakl_p/'
REF_SYS = URIRef("http://onto.fel.cvut.cz/ontologies/town-plan/spatial_ref_sys")

## vytvoř seznam URI snapshotů
snapsUri = list()
d = datetime.datetime.today()

for s,p,o in g.triples( (None, RDF.type, None) ):
    if (o != REF_SYS):
        snapsUri.append(URIRef(ssvuNamespace + str(d.date()) + 'T' + str(d.time()) + '/' + str(s.split('/')[-1])))

# převést vazby z objektu na snapshot

# vytvořit vazby mezi objektem a snapshotem

# uložit do nového grafu