Here's a cleaner, more professional version of the README.md without emojis and with better organization:

```markdown
# Promo Sensei - Smart Offer Discovery Assistant

A Slack-integrated assistant that aggregates e-commerce promotions, using vector database storage and RAG (Retrieval-Augmented Generation) for intelligent deal discovery.

## Project Overview

Promo Sensei monitors promotional deals from major e-commerce platforms, processes deal information, and provides natural language responses to user queries through Slack integration.

## Project Structure

```
  promo_sensei/
  ├── scraper.py               # Deal scraping module
  ├── ingest_to_vector_db.py   # Vector database management
  ├── rag_query.py            # Query processing pipeline
  ├── slackbot.py             # Slack integration interface
  ├── offers.json             # Cached deal data
  ├── faiss_index/            # Vector database storage
  └── .env                    # Configuration files
```

## Setup Instructions

1. **Environment Setup**
```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Unix/MacOS
# or
.\venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Install browser automation
playwright install
```

2. **Configuration**

Create a `.env` file with required API keys:
```
SLACK_BOT_TOKEN=your-slack-bot-token
SLACK_APP_TOKEN=your-slack-app-token
GROQ_API_KEY=your-groq-api-key
HF_TOKEN=your-hugging-face-token
```

3. **Launch Application**
```bash
python slackbot.py
```

Note: Ensure Slack bot is installed in your workspace with Socket Mode enabled.

## Available Commands

| Command | Description |
|---------|-------------|
| `/deals search [query]` | Find specific deals |
| `/deals today` | View top current offers |
| `/deals store [name]` | Search by store/brand |
| `/deals refresh` | Update deals database |

## Technical Implementation

### Data Collection
- Automated scraping using Playwright
- Real-time deal extraction
- Structured data processing

### Vector Database
- FAISS-based vector storage
- HuggingFace embeddings (all-MiniLM-L6-v2)
- Efficient similarity search

### Query Processing
- LangChain-based RAG pipeline
- LLama 3.3 70B integration via Groq
- Context-aware response generation

### Slack Integration
- Real-time command processing
- Formatted response rendering
- Interactive user experience

## Dependencies

Core requirements:
```
playwright>=1.39.0
slack-bolt>=1.18.0
langchain>=0.1.0
langchain-groq>=0.1.0
faiss-cpu>=1.7.4
sentence-transformers>=2.2.2
python-dotenv>=1.0.0
```

## Installation

```bash
git clone https://github.com/ShubhGupta2002/Promo-sensai.git
cd Promo-sensai
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

1. Configure environment variables
2. Start the Slack bot
3. Use commands in any Slack channel
4. View real-time deal updates and responses

## Contributing

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Submit pull request

## License

MIT License - See LICENSE file for details
```
