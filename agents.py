import os
import asyncio
import google.generativeai as genai
from groq import Groq
from google.api_core.exceptions import ResourceExhausted
from tools import search_products
from dotenv import load_dotenv

load_dotenv()

# -------------------------
# Configure Gemini
# -------------------------
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# -------------------------
# Configure Groq (Llama 3.3 70B)
# -------------------------
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))


class BaseAgent:
    def __init__(self):
        self.gemini_model = genai.GenerativeModel("gemini-2.5-flash-lite")

    async def think(self, prompt):
        """
        Hybrid LLM Call:
        1️⃣ Try Gemini first
        2️⃣ If quota exceeded → fallback to Llama 3.3 70B
        """

        # -------- TRY GEMINI FIRST --------
        try:
            response = self.gemini_model.generate_content(prompt)
            return {
                "provider": "gemini",
                "output": response.text
            }

        except ResourceExhausted:
            print("⚠ Gemini quota exceeded. Switching to Llama...")

        except Exception as e:
            print("Gemini error:", str(e))

        # -------- FALLBACK TO LLAMA 3.3 --------
        try:
            llama_response = groq_client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant."},
                    {"role": "user", "content": prompt}
                ]
            )

            return {
                "provider": "llama-3.3-70b-versatile",
                "output": llama_response.choices[0].message.content
            }

        except Exception as e:
            return {
                "provider": "fallback",
                "output": f"⚠ All LLM providers failed: {str(e)}"
            }


# -------------------------------------------------
# PARALLEL AGENT
# -------------------------------------------------

class ParallelAgent(BaseAgent):

    async def run(self, query):

        task1 = asyncio.create_task(self.think(query))
        task2 = asyncio.create_task(search_products(query))

        llm_result, magento_result = await asyncio.gather(task1, task2)

        return {
            "type": "parallel",
            "llm": llm_result,
            "magento": magento_result
        }


# -------------------------------------------------
# SEQUENTIAL AGENT
# -------------------------------------------------

class SequentialAgent(BaseAgent):

    async def run(self, query):

        llm_result = await self.think(query)

        # Use LLM output for Magento search
        search_query = llm_result["output"]

        products = await search_products(search_query)

        return {
            "type": "sequential",
            "llm": llm_result,
            "products": products
        }


# -------------------------------------------------
# LOOP AGENT (Quota Safe Hybrid)
# -------------------------------------------------

class LoopAgent(BaseAgent):

    async def run(self, query):

        current = query

        # Only 1 LLM call to reduce quota usage
        result = await self.think(current)

        return {
            "type": "loop",
            "final_output": result
        }