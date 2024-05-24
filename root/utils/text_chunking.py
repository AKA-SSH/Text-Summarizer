from sentence_transformers import SentenceTransformer
from nltk.tokenize import sent_tokenize
from sklearn.cluster import KMeans
from kneed import KneeLocator

model = SentenceTransformer('bert-base-nli-mean-tokens')

def _embedding_generation(preprocessed_text):
    sentences = sent_tokenize(preprocessed_text)
    sentence_embeddings = model.encode(sentences)

    return sentence_embeddings, sentences

def _find_optimal_clusters(sentence_embeddings, max_clusters=10):
    wcss = []
    for i in range(1, max_clusters + 1):
        kmeans = KMeans(n_clusters=i, n_init='auto', random_state=42)
        kmeans.fit(sentence_embeddings)
        wcss.append(kmeans.inertia_)
    
    kneedle = KneeLocator(range(1, max_clusters + 1), wcss, curve="convex", direction="decreasing")
    optimal_clusters = kneedle.elbow

    return optimal_clusters

def semantic_chunking(preprocessed_text, max_clusters=10):
    sentence_embeddings, sentences = _embedding_generation(preprocessed_text)
    
    optimal_clusters = _find_optimal_clusters(sentence_embeddings, max_clusters)
    
    kmeans = KMeans(n_clusters=optimal_clusters, n_init='auto', random_state=42)
    kmeans.fit(sentence_embeddings)

    clusters = {}
    for idx, label in enumerate(kmeans.labels_):
        if label not in clusters:
            clusters[label] = []
        clusters[label].append(sentences[idx])

    return clusters