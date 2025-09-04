# Medico - Medical AI Assistant

A RAG-based medical chatbot built with LangChain, Pinecone, and Google Gemini AI. Provides evidence-based health information with a modern web interface.

## 🏥 Features

- **AI-Powered Medical Assistant**: Uses Google Gemini 2.0 Flash for intelligent responses
- **RAG (Retrieval-Augmented Generation)**: Combines medical knowledge with AI reasoning
- **Vector Search**: Pinecone vector database for semantic document retrieval
- **Modern UI**: Clean, responsive chat interface with medical theming
- **Real-time Chat**: Interactive conversation with typing indicators
- **Medical Disclaimer**: Built-in safety warnings and professional guidance

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **AI/LLM**: Google Gemini 2.0 Flash (langchain-google-genai)
- **Vector Database**: Pinecone
- **Embeddings**: HuggingFace sentence-transformers/all-MiniLM-L6-v2
- **RAG Framework**: LangChain
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 4
- **Environment**: Python virtual environment

## 📋 Prerequisites

- Python 3.8+
- Pinecone account and API key
- Google AI API key (Gemini)

## 🚀 Quick Start

### 1. Clone and Setup

```bash
# Clone the repository
git clone <repository-url>
cd medical-chatbot

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure API Keys

Create a `.env` file in the project root:

```env
PINECONE_API_KEY=your_pinecone_api_key_here
GOOGLE_API_KEY=your_google_ai_api_key_here
```

**Get API Keys:**
- **Pinecone**: Sign up at [pinecone.io](https://pinecone.io) → Create project → Get API key
- **Google AI**: Visit [Google AI Studio](https://makersuite.google.com/app/apikey) → Create API key

### 3. Setup Pinecone Index

The app expects a Pinecone index named `medical-chatbot` with:
- **Dimensions**: 384 (for sentence-transformers/all-MiniLM-L6-v2)
- **Metric**: cosine
- **Environment**: Choose based on your region

If you need to create the index, run:
```bash
python store_index.py
```

### 4. Run the Application

```bash
# Set environment variables (Windows PowerShell)
$env:PINECONE_API_KEY="your_pinecone_key"
$env:GOOGLE_API_KEY="your_google_key"

# Start the server
python app.py
```

The application will be available at: **http://localhost:8080**

## 🎨 UI Features

- **Medical Header**: Red-themed header with stethoscope icon
- **Safety Disclaimer**: Prominent medical disclaimer with warning icon
- **Chat Interface**: Modern bubble-style chat with avatars
- **Responsive Design**: Works on desktop and mobile devices
- **Dark Theme**: Professional dark theme with medical color scheme
- **Real-time Updates**: Live chat with typing indicators



## 🚀 Deployment

### Local Development
```bash
python app.py
```

### Production (Heroku/Render)
```bash
# Install gunicorn
pip install gunicorn

# Create Procfile
echo "web: gunicorn app:app --bind 0.0.0.0:\${PORT:-8080}" > Procfile

# Create runtime.txt
echo "python-3.10.x" > runtime.txt
```
### API Requirements
- **Pinecone**: Required for vector search functionality
- **Google AI**: Required for LLM responses
- Both APIs must be valid and active

### Data Privacy
- Medical queries are processed by Google AI
- Vector embeddings are stored in Pinecone
- No local data persistence

## 📄 License

This project is for educational purposes only. Please ensure compliance with medical AI regulations in your jurisdiction.
---

**⚠️ Medical Disclaimer**: This tool is for educational purposes only. Always consult healthcare professionals for medical advice.
