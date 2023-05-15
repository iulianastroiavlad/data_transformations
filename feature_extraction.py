from rdflib import Graph, Namespace

# Define the namespaces used in the TTL file
ex = Namespace("http://example.org/")
rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
# sosa = Namespace("http://www.w3.org/ns/sosa/")
# xsd = Namespace("http://www.w3.org/2001/XMLSchema#")

# Create an RDF graph and parse the TTL file
g = Graph()
g.parse("energy.ttl", format="turtle")


# Define a function to extract features from the sensor observations
def extract_features(observation):
    # Extract the observed property, feature of interest, phenomenon time, and result
    timestamp = str(g.value(observation, ex.timestamp))
    building_id = str(g.value(observation, ex.building_id))
    consumption = int(g.value(observation, ex.consumption))
    # result = float(g.value(observation, sosa.result))

    # Return a dictionary of the extracted features
    return {
        "timestamp": timestamp,
        "building_id": building_id,
        "consumption": consumption
    }


# Extract features from all sensor observations in the graph
features = []
for observation in g.subjects(predicate=rdf.type, object=ex.EnergyData):
    features.append(extract_features(observation))

# Print the extracted features
print(features)
