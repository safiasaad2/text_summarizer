# 📝 Text Summarization App

A simple web app for summarizing text using different algorithms: LSA, Luhn, LexRank, and TextRank. Built with **Python**, **Streamlit**, and **Sumy**.
[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Libraries](https://img.shields.io/badge/Libraries-Streamlit%20%7C%20Sumy%20%7C%20NLTK-lightgrey)](https://streamlit.io/)
[![Summarizers](https://img.shields.io/badge/Summarizers-LSA%20%7C%20Luhn%20%7C%20LexRank%20%7C%20TextRank-yellow)]()
[![Status](https://img.shields.io/badge/Status-Active-brightgreen)]()
[![Visualization](https://img.shields.io/badge/Interface-Streamlit-blueviolet)]()
[![Text%20Processing](https://img.shields.io/badge/Tokenization-NLTK-lightgrey)]()
[![Export](https://img.shields.io/badge/Export-None-success)]()


## ✨ Features

- **Multiple Summarization Algorithms**: Choose from LSA, Luhn, LexRank, and TextRank
- **Customizable Summary Length**: Control the number of sentences in your summary
- **Interactive UI**: Built with Streamlit for a smooth user experience
- **Statistics Display**: See word count and reduction percentage

## 🚀 Algorithms

1. **LSA (Latent Semantic Analysis)**: Uses linear algebra to find important sentences
2. **Luhn**: Based on word frequency and clustering
3. **LexRank**: Graph-based algorithm inspired by PageRank
4. **TextRank**: Similar to LexRank with different weighting

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/safiasaad2/text_summarizer.git
cd text_summarizer
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Download required NLTK data:
```bash
python -c "import nltk; nltk.download('punkt')"
```

## 🎯 Usage

Run the Streamlit app:
```bash
streamlit run summary.py
```

Then:
1. Open your browser to `http://localhost:8501`
2. Enter or paste your text
3. Choose a summarization algorithm
4. Select the number of sentences
5. Click "Summarize"

## 🛠️ Requirements

- Python 3.7+
- streamlit
- sumy
- nltk

## 📝 Example

Input a long article or document, and get a concise summary in seconds!
<p align="center">
  <img src="output.gif" alt="Text Summarization" width="700">
</p>

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

**Safia Saad**
💼 AI Engineer | Computer Vision & Deep Learning Enthusiast
📧 [safiakotb123@gmail.com](mailto:safiakotb123@gmail.com)

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [Sumy](https://github.com/miso-belica/sumy)
