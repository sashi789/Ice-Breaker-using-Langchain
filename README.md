```md
# 🔍 Ice Breaker Agent – Find the Perfect Opener Using LinkedIn & Twitter!

Ever feel stuck starting a conversation with someone you just found online?  
This AI-powered agent does the work for you — it finds a person’s **LinkedIn** and **Twitter** profiles, scrapes their activity, and uses **OpenAI GPT** to generate a personalized ice breaker.

---

## ✨ Features

- 🌐 **URL Discovery**: Finds LinkedIn and Twitter using **Tavily search**.
- 🕵️ **Profile Scraping**: Extracts info using **Scrapin.io**.
- 🐦 **Twitter Analysis**: Pulls recent tweets and bio data.
- 🤖 **Smart Ice Breakers**: Uses **OpenAI GPT** to generate intros.
- 🔁 **Modular Design**: Easily extensible for other platforms or agents.

---

## 🧠 Tech Stack

| Technology     | Purpose                          |
|----------------|----------------------------------|
| **LangChain**  | Agent orchestration & LLM logic  |
| **OpenAI API** | GPT model for text generation    |
| **Tavily API** | URL search for LinkedIn/Twitter  |
| **Scrapin.io** | LinkedIn scraping                |
| **Python**     | Core logic and tooling           |

---

## 📦 Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/sashi789/Ice-Breaker-using-Langchain.git
   cd Ice-Breaker-using-Langchain
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create your `.env` file**
   This project requires API keys to work. Inside the project root, create a file named `.env` and add the following:

   ```env
   OPENAI_API_KEY=your_openai_key_here
   TAVILY_API_KEY=your_tavily_key_here
   ```

   > 🔐 **Note**: Never commit this file to GitHub. It contains your sensitive API keys. The `.gitignore` is already set up to exclude it.

---

## 🧪 Usage

Simply run the main script:

```bash
python main.py
```

Enter a person’s name when prompted — the tool will:
1. Search for their LinkedIn & Twitter profiles
2. Scrape data from those URLs
3. Generate a custom conversation starter

---

## 💬 Example Output

> **Name**: Jane Doe  
> **LinkedIn**: https://linkedin.com/in/janedoe  
> **Twitter**: https://twitter.com/janedoe_ai  
> **Ice Breaker**:  
> “Hi Jane! I noticed your recent work on conversational agents — I’m building something similar with LangChain and Tavily. Would love to swap notes!”

---

## 🌱 What's Next?

- 🌍 Add GitHub and Medium support
- 🧪 Integrate email lookup or People Data APIs
- 🖥️ Web interface using Streamlit
- 📤 Export reports as PDFs

---

## 📄 License

MIT License. Use it, modify it, and make cool stuff.

---

## 🙌 Built With

- [LangChain](https://github.com/hwchase17/langchain)
- [OpenAI](https://platform.openai.com/)
- [Tavily](https://www.tavily.com/)
- [Scrapin.io](https://scrapin.io)

---

## 🔗 Connect

Made with ❤️ by [Sashi789](https://github.com/sashi789)  
Feel free to star ⭐ the repo or reach out with feedback!
```
