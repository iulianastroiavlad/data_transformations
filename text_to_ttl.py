import spacy
import rdflib
from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS

# Load the spaCy language model
nlp = spacy.load("en_core_web_sm")

# Example text
text = "Apple Inc. is planning to open a new store in New York City."

# Initialize an RDF graph
graph = rdflib.Graph()

# Preprocess the text (tokenization and normalization)
doc = nlp(text)

# Apply semantic tagging
ex = Namespace('http://example.com/')
for entity in doc.ents:
    subject = ex[entity.text.replace(" ", "_")]
    graph.add((subject, RDF.type, RDFS.Class))
    graph.add((subject, RDFS.label, Literal(entity.text)))

# Serialize the graph in Turtle format
turtle_data = graph.serialize(format="turtle")
print(turtle_data)
