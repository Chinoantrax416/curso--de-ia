import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

os.environ['OPENAI_API_KEY'] = ' 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'


model = ChatOpenAI(model='gpt-3.5-turbo')

prompt_template = PromptTemplate.from_template(
    'Me fale sobre o carro {carro}.'

)
runnable_sequence = prompt_template| model | StrOutputParser()


response = runnable_sequence.invoke({'carro': 'Marea 20v 1999'})

print(response)