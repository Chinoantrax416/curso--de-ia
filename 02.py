import os
from langchain_openai import OpenAI
from langchain_community.cache import InMemoryCache, SQLiteCache
from langchain_core.globals import set_llm_cache

os.environ['OPENAI_API_KEY'] = ' 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'

model = OpenAI()

set_llm_cache(
    SQLiteCache(database_path='openai_cache.db')
)

prompt = 'Me diga quem foi Albert Einstein.'

response1 = model.invoke(prompt)
print(f'Chamada 1: {response1}')

response1 = model.invoke(prompt)
print(f'Chamada 2: {response1}')



