from rdflib import Graph, Namespace

# Define the namespaces used in the TTL file
ex = Namespace("http://example.org/")

# Create an RDF graph and parse the TTL file
g = Graph()
g.parse("energy.ttl", format="turtle")

# Extract all URIs in the RDF graph
uris = set()
for s, p, o in g:
    if isinstance(s, str) and (s.startswith("http://") or s.startswith("https://")):
        uris.add(s)
    if isinstance(p, str) and (p.startswith("http://") or p.startswith("https://")):
        uris.add(p)
    if isinstance(o, str) and (o.startswith("http://") or o.startswith("https://")):
        uris.add(o)

# Print the extracted URIs
print(uris)
