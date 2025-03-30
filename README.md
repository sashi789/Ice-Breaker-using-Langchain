```md
# 🔍 Ice Breaker Agent – Find the Perfect Opener Using LinkedIn & Twitter!

Ever feel stuck starting a conversation with someone you just found online?  
This AI-powered agent does the work for you — it finds a person’s **LinkedIn** and **Twitter** profiles, scrapes their activity, and uses **OpenAI GPT** to generate a personalized ice breaker that includes a short **summary** and **two interesting facts**.

---

## ✨ Features

- 🌐 **URL Discovery**: Finds LinkedIn and Twitter using **Tavily search**
- 🕵️ **Profile Scraping**: Extracts data from LinkedIn using **Scrapin.io**
- 🐦 **Twitter Analysis**: Pulls recent tweets and bio details
- 🤖 **LLM-Powered Generation**:
  - Creates a **short summary** about the person
  - Extracts **two interesting facts** based on their LinkedIn profile
- 🔁 **Modular Design**: Easily extensible to support other platforms like GitHub or Medium

---

## 🧠 Tech Stack

| Technology     | Purpose                          |
|----------------|----------------------------------|
| **LangChain**  | Agent orchestration & LLM logic  |
| **OpenAI API** | GPT model for text generation    |
| **Tavily API** | URL search for LinkedIn/Twitter  |
| **Scrapin.io** | LinkedIn scraping                |
| **Python**     | Core logic and scripting         |

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
   This project requires API keys to function. Create a file named `.env` in the root folder and add:

   ```env
   OPENAI_API_KEY=your_openai_key_here
   TAVILY_API_KEY=your_tavily_key_here
   ```

   > 🔐 **Important**: Do not commit this file to GitHub. It's listed in `.gitignore` for security.

---

## 🧪 Usage

Run the main script:

```bash
python main.py
```

Then follow the prompt to enter a person’s name. The agent will:
1. Search for their LinkedIn & Twitter profiles
2. Scrape available data
3. Use OpenAI to generate a short summary and two interesting facts

---

## 💬 Example Output

> **Name**: Jane Doe  
> **LinkedIn**: https://linkedin.com/in/janedoe  
> **Twitter**: https://twitter.com/janedoe_ai  
>
> **Summary**:  
> Jane is a passionate AI researcher working on large language models at a startup in San Francisco. She frequently shares insights on AI ethics and real-world applications of generative models.  
>
> **Interesting Facts**:  
> 1. Jane recently gave a TEDx talk on responsible AI and bias mitigation.  
> 2. She volunteers at AI4ALL, mentoring students from underrepresented communities.

---

## 🌱 What's Next?

- 🧠 Add GitHub, Medium, and blog analysis support
- 🌍 Multi-language support
- 🖥️ Streamlit or web frontend
- 📤 Export reports to PDF or Markdown

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use, remix, and share!

---

## 🙌 Built With

- [LangChain](https://github.com/hwchase17/langchain)
- [OpenAI](https://platform.openai.com/)
- [Tavily](https://www.tavily.com/)
- [Scrapin.io](https://scrapin.io)

---

## 🔗 Connect

Made with ❤️ by [Sashi789](https://github.com/sashi789)  
If you like this project, please ⭐ star the repo and share it!
```
