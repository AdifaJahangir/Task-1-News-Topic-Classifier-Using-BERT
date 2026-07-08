import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="News Topic Classifier", page_icon="📰")

st.title("📰 News Topic Classifier")
st.write("Fine-tuned BERT model trained on the AG News dataset. Classifies headlines into "
         "**World**, **Sports**, **Business**, or **Sci/Tech**.")

MODEL_DIR = "bert-ag-news-finetuned"

@st.cache_resource
def load_classifier():
    return pipeline("text-classification", model=MODEL_DIR, tokenizer=MODEL_DIR)

classifier = load_classifier()

headline = st.text_area("Enter a news headline:", height=100,
                         placeholder="e.g., Central bank cuts interest rates to boost economy")

if st.button("Classify"):
    if headline.strip():
        result = classifier(headline)[0]
        st.success(f"**Predicted Category:** {result['label']}")
        st.write(f"Confidence: {result['score']:.2%}")
    else:
        st.warning("Please enter a headline first.")

st.markdown("---")
st.caption("Model: bert-base-uncased, fine-tuned on AG News · Built with Hugging Face Transformers + Streamlit")
