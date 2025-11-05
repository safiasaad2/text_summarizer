import streamlit as st 
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.text_rank import TextRankSummarizer

def summarize(text, summarizer_type="lsa", sentence_count=5):
    """
    Summarize text using different algorithms
    
    Args:
        text (str): Input text to summarize
        summarizer_type (str): Type of summarizer (lsa, luhn, lexrank, textrank)
        sentence_count (int): Number of sentences in summary
    
    Returns:
        str: Summarized text
    """
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    
    if summarizer_type == "lsa":
        summarizer = LsaSummarizer()
    elif summarizer_type == "luhn":
        summarizer = LuhnSummarizer()
    elif summarizer_type == "lexrank":
        summarizer = LexRankSummarizer()
    elif summarizer_type == "textrank":
        summarizer = TextRankSummarizer()
    else:
        st.error("Please enter a valid name for summarizer")
        return None
    
    summary = summarizer(parser.document, sentence_count)
    return " ".join(str(sentence) for sentence in summary)

# Streamlit UI
st.title("📝 Text Summarization App")
st.write("Enter your text below and choose a summarization algorithm")

# Text input
text = st.text_area("Please enter some text", height=200, 
                    placeholder="Paste your article or long text here...")

# Summarizer selection
col1, col2 = st.columns(2)
with col1:
    summarizer_type = st.selectbox(
        "Choose Summarizer",
        ("lsa", "luhn", "lexrank", "textrank"),
        help="Different algorithms for text summarization"
    )

with col2:
    sentence_count = st.slider(
        "Number of Sentences",
        min_value=1,
        max_value=10,
        value=4,
        help="Select how many sentences you want in the summary"
    )

# Summarize button
if st.button("Summarize", type="primary"):
    if text:
        with st.spinner("Summarizing..."):
            summary = summarize(text, summarizer_type, sentence_count)
            if summary:
                st.subheader("📄 Summary")
                st.write(summary)
                
                # Show statistics
                st.divider()
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Original Length", f"{len(text.split())} words")
                with col2:
                    st.metric("Summary Length", f"{len(summary.split())} words")
                with col3:
                    reduction = round((1 - len(summary.split()) / len(text.split())) * 100, 1)
                    st.metric("Reduction", f"{reduction}%")
    else:
        st.warning("⚠️ Please enter some text to summarize")