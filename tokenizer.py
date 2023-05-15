import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk
from sklearn.feature_extraction.text import TfidfVectorizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')


# Function to preprocess text data
def preprocess_text(text):
    # Tokenize text
    tokens = word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words("english"))
    tokens = [token for token in tokens if token.lower() not in stop_words]

    # Perform part-of-speech tagging
    tagged_tokens = pos_tag(tokens)

    # Perform named entity recognition
    named_entities = ne_chunk(tagged_tokens)

    return named_entities


# Function to extract keywords using TF-IDF
def extract_keywords(text):
    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform([text])

    feature_names = tfidf.get_feature_names_out()  # Access feature names directly

    # Get top-ranking keywords
    top_keywords = [feature_names[i] for i in tfidf_matrix.toarray().argsort()[0][-5:]]

    return top_keywords


# Function to perform extractive summarization
def summarize_text(text):
    # Initialize the summarizer
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()

    summary = summarizer(parser.document, 2)  # Specify the number of sentences in the summary
    # Print the summary
    for sentence in summary:
        print(sentence)
        return sentence


# Example usage
traffic_data = "Traffic congestion in urban areas continues to worsen, resulting in increased travel times and productivity losses for commuters. The analysis of traffic data collected from various sensors and cameras provides valuable insights into traffic patterns, enabling better urban planning and traffic management strategies. The implementation of intelligent transportation systems, leveraging real-time traffic data, helps optimize traffic flow, reduce bottlenecks, and enhance overall road safety. By analyzing historical traffic data, researchers can identify recurring traffic congestion hotspots and propose targeted interventions to alleviate traffic bottlenecks."
water_data = "By analyzing water data from various sources, researchers identified a decline in water quality, highlighting the importance of implementing effective conservation measures. " \
             "The integration of IoT devices with water data monitoring systems allows for real-time monitoring of water levels, enabling early detection of potential flooding events."
energy_data = "Through the analysis of energy data, it was observed that implementing energy-efficient practices resulted in a significant reduction in carbon emissions. " \
              "Smart grids, powered by advanced analytics and energy data, enable dynamic energy distribution, optimizing energy usage and enhancing the overall efficiency of the power system."

# Preprocess and extract meta information from traffic data
traffic_entities = preprocess_text(traffic_data)
traffic_keywords = extract_keywords(traffic_data)
traffic_summary = summarize_text(traffic_data)

# Preprocess and extract meta information from water data
water_entities = preprocess_text(water_data)
water_keywords = extract_keywords(water_data)
water_summary = summarize_text(water_data)

# Preprocess and extract meta information from energy data
energy_entities = preprocess_text(energy_data)
energy_keywords = extract_keywords(energy_data)
energy_summary = summarize_text(energy_data)

# Print the extracted meta information
print("Traffic Entities:", traffic_entities)
print("Traffic Keywords:", traffic_keywords)
print("Traffic Summary:", traffic_summary)
#
print("Water Entities:", water_entities)
print("Water Keywords:", water_keywords)
print("Water Summary:", water_summary)
#
print("Energy Entities:", energy_entities)
print("Energy Keywords:", energy_keywords)
print("Energy Summary:", energy_summary)
