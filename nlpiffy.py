import streamlit as st
import spacy
from textblob import TextBlob
from gensim.summarization import summarize


# tokenizer and lemmatizer
def text_analyzer(my_text):
    # https://spacy.io/usage/models#models-download
    # python -m spacy download en_core_web_sm
    nlp = spacy.load("en_core_web_sm")
    docs = nlp(my_text)
    tokens = [f"Token: {token.text}, Lemma: {token.lemma_}" for token in docs]
    return tokens


# extract names
def entity_analyzer(my_text):
    nlp = spacy.load("en_core_web_sm")
    docs = nlp(my_text)
    entities = [
        f"Entity: {entity.text}, Label: {entity.label_}" for entity in docs.ents
    ]
    return entities


def main():
    st.subheader("Natural Language Processing On-the-Go")

    analyzer = st.sidebar.selectbox("Select the Analyzer", ("Tokens & Lemmas", "Name Entities", "Sentiment Analysis", "Text Summarization"))
    sample_text = open("sample_text.txt", "r").read() if st.checkbox("Sample Text") else ""

    # tokenization
    if analyzer == "Tokens & Lemmas":
        msg = st.text_area("Extract Tokens & Lemmas from Your Text with spaCy", sample_text)
        if st.button("Extract"):
            nlp_result = text_analyzer(msg)
            st.json(nlp_result)

    # name extraction
    if analyzer == "Name Entities":
        msg = st.text_area("Extract Name Entities from Your Text with spaCy", sample_text)
        if st.button("Extract"):
            nlp_result = entity_analyzer(msg)
            st.json(nlp_result)

    # sentiment analysis
    if analyzer == "Sentiment Analysis":
        msg = st.text_area("Analyze the Sentiment of Your Text with TextBlob", sample_text)
        if st.button("Analyze"):
            blob = TextBlob(msg)
            sentiment_result = blob.sentiment
            st.success(sentiment_result)

    # text summarization
    if analyzer == "Text Summarization":

        msg = st.text_area("Summarize Your Text with gensim", sample_text)
        if st.button("Summarize"):
            summary_result = summarize(msg)
            st.success(summary_result)


if __name__ == "__main__":
    main()
