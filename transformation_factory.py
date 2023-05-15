import csv
import json
from abc import ABC, abstractmethod
from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import RDF


# Abstract factory interface
class DataConverterFactory(ABC):
    @abstractmethod
    def create_converter(self):
        pass


# CSV to JSON-LD converter
class CsvToJsonLdConverter:
    def __init__(self, csv_file, namespace, class_uri):
        self.csv_file = csv_file
        self.namespace = namespace
        self.class_uri = class_uri

    def convert(self):
        graph = Graph()

        with open(self.csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                subject_uri = URIRef(self.namespace + row['id'])
                graph.add((subject_uri, RDF.type, self.class_uri))
                for key, value in row.items():
                    if key != 'id':
                        graph.add((subject_uri, URIRef(self.namespace + key), Literal(value)))

        return graph.serialize(format='json-ld', indent=4)


# JSON to JSON-LD converter
class JsonToJsonLdConverter:
    def __init__(self, json_data, namespace, class_uri):
        self.json_data = json_data
        self.namespace = namespace
        self.class_uri = class_uri

    def convert(self):
        graph = Graph()

        for item in self.json_data:
            subject_uri = URIRef(self.namespace + item['id'])
            graph.add((subject_uri, RDF.type, self.class_uri))
            for key, value in item.items():
                if key != 'id':
                    graph.add((subject_uri, URIRef(self.namespace + key), Literal(value)))

        return graph.serialize(format='json-ld', indent=4)


# Concrete factory for CSV to JSON-LD converter
class CsvToJsonLdConverterFactory(DataConverterFactory):
    def __init__(self, csv_file, namespace, class_uri):
        self.csv_file = csv_file
        self.namespace = namespace
        self.class_uri = class_uri

    def create_converter(self):
        return CsvToJsonLdConverter(self.csv_file, self.namespace, self.class_uri)


# Concrete factory for JSON to JSON-LD converter
class JsonToJsonLdConverterFactory(DataConverterFactory):
    def __init__(self, json_data, namespace, class_uri):
        self.json_data = json_data
        self.namespace = namespace
        self.class_uri = class_uri

    def create_converter(self):
        return JsonToJsonLdConverter(self.json_data, self.namespace, self.class_uri)


# Example usage
csv_file = 'traffic.csv'
json_file = 'water.json'

# Define the namespace and class URI for your data
namespace = Namespace('http://example.com/')
class_uri = URIRef('http://example.com/MyDataClass')

# Create a CSV to JSON-LD converter using the factory
csv_factory = CsvToJsonLdConverterFactory(csv_file, namespace, class_uri)
csv_converter = csv_factory.create_converter()
csv_jsonld = csv_converter.convert()
print(csv_jsonld)

# Create a JSON to JSON-LD converter using the factory
with open(json_file, 'r') as file:
    json_data = json.load(file)

json_factory = JsonToJsonLdConverterFactory(json_data, namespace, class_uri)
json_converter = json_factory.create_converter()
json_jsonld = json_converter.convert()
print(json_jsonld)
