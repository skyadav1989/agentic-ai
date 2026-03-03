# 🚀 AI Multi-Agent Magento System

Hybrid LLM-powered AI Agent system built with FastAPI + Gemini + Llama 3.3 70B + Magento GraphQL.

---

## ✅ Features

- Parallel Agents  
- Sequential Agents  
- Loop Agents  
- Hybrid LLM (Gemini + Llama 3.3 70B via Groq)  
- Magento GraphQL Integration  
- AJAX-Based Modern UI  
- Product Card Rendering  
- Circuit Breaker + Retry Logic  
- Quota-Safe Architecture  

---

## 🧠 Architecture Overview

User (UI)
   ↓
FastAPI Backend
   ↓
Agent Layer
   ├── Parallel Agent
   ├── Sequential Agent
   └── Loop Agent
   ↓
Hybrid LLM Layer
   ├── Gemini
   └── Llama 3.3 70B (Groq fallback)
   ↓
Magento GraphQL Tool
   ↓
Product Response

---

## ⚙️ Tech Stack

Backend: FastAPI  
Primary LLM: Gemini  
Fallback LLM: Llama-3.3-70b-versatile (Groq)  
Ecommerce: Magento GraphQL  
Frontend: HTML + CSS + AJAX  
HTTP Client: requests  
Async Handling: asyncio  

---

## 📁 Project Structure

agentic_ai/
│
├── main.py
├── agents.py
├── tools.py
├── utils/
│   └── gemini.py
├── templates/
│   └── index.html
├── .env
├── requirements.txt
└── README.md

---

## 🔐 Environment Variables

Create a .env file:

GEMINI_API_KEY=your_gemini_key  
GROQ_API_KEY=your_groq_key  
MAGENTO_GRAPHQL_URL=https://cmiestore.com/graphql  

---

## 📦 Installation

### 1️⃣ Create Virtual Environment

python -m venv .venv

Activate:

Windows:
.venv\Scripts\activate

Mac/Linux:
source .venv/bin/activate

---

### 2️⃣ Install Dependencies

pip install -r requirements.txt

---

## ▶️ Run Application

uvicorn main:app --reload

Open in browser:

http://127.0.0.1:8000

---

## 🤖 Agents Explained

### 1️⃣ Parallel Agent
- Calls LLM and Magento simultaneously  
- Returns AI explanation + Product list  

### 2️⃣ Sequential Agent
- Calls LLM first  
- Uses LLM output to refine Magento search  

### 3️⃣ Loop Agent
- Optimized single LLM call (quota-safe)  
- Used for reasoning-heavy responses  

---

## 🔄 Hybrid LLM Logic

1. Gemini is called first  
2. If quota exceeded → switches to Llama 3.3 70B  
3. If both fail → safe fallback message  

---

## 🛍 Magento GraphQL Query

query ($search: String!) {
  products(search: $search, pageSize: 5) {
    items {
      name
      sku
      price_range {
        minimum_price {
          regular_price {
            value
            currency
          }
        }
      }
    }
  }
}

---

## 🛡 Production Safety Features

- Retry mechanism  
- Exponential backoff  
- Circuit breaker  
- Timeout protection  
- Safe parallel execution  
- Graceful error handling  

---

## 🎨 UI Features

- Modern gradient layout  
- AJAX-based requests (no reload)  
- Loading spinner  
- AI response section  
- Responsive product cards  

---

## 🚀 Future Enhancements

- Redis caching  
- Streaming responses  
- LLM ensemble voting  
- Observability dashboard  
- Pagination & filtering  
- Docker deployment  
- Kubernetes scaling  

---

## 👨‍💻 Author

Developed by SANTOSH SIR  
AI Agent + Magento Integration System  

---
