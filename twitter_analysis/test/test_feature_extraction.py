
from core.textutils.feature_extraction import FeatureExtractor

THIS = ["O rato roeu", 
        "O rato roeu a roupa",  
        "A roupa é bonita",  
        "papai noel chegou", 
        "Feliz natal pessoal",
        "O rato come queijo", 
        "Zip Zap Zum ele vai para lugar nenhum", 
        "Não a lugar como o lar", 
        "O rato morreu no natal",
        "O natal é amanha"]

def test_count_vectorizer():

    # Extract features using a count vectorizer
    fe = FeatureExtractor(THIS)
    doc_term_matrix, vocabulary = fe.count_vectorizer()

    top_terms = fe.get_top_words(vocabulary, doc_term_matrix)

    for term, weight in top_terms:
        print ("word: %s, weight: %s" % (term, weight))