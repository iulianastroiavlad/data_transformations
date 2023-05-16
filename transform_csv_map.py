from rdflib.term import URIRef
from rdflib.namespace import RDF
import df2rdf.pandas  # noqa: F401
import pandas as pd

def map_csv(csv_source, specifiction_df2rdf, rdf_destination=None, rdf_format="turtle"):
    """
    Map csv file to rdf according to the kgkit specification.

    :param csv_source: str indicates the path where the source is located.
    :param specifiction_df2rdf: str indicates the path of the mapping specification.
    :param rdf_destination: str indicates the path where the rdf graph should be serialized; if None, then no
    serialization.
    :param rdf_format: str indicates the format in which to serialize the rdf graph.
    :return:
    """
    df_solutions = pd.read_csv(csv_source)
    print("columns")
    print(df_solutions.head())
    graph = df_solutions.to_rdf(mapping=specifiction_df2rdf)
    graph.serialize(destination=rdf_destination, format=rdf_format)


#account_csv = "../traffic.csv"
account_csv = "traffic.csv"

account_mapping = "map_traffic.json"
map_csv(account_csv, account_mapping, rdf_destination="mapped_traffic.ttl")
