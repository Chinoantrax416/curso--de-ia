import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

os.environ['OPENAI_API_KEY'] = ' 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'


model = ChatOpenAI(model='gpt-3.5-turbo')