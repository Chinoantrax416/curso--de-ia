import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

os.environ['OPENAI_API_KEY'] = ' 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'

model = ChatOpenAI(model='gpt-5-nano')

template = '''
Traduza o  texto do {idioma1} para o {idioma2}:
{texto}
'''

prompt_template = PromptTemplate.from_template(
    template=template
)

prompt = prompt_template.format(
    idioma1='portugês',
    idioma2='francês',
    texto='Bom dia!',
)

response = model.invoke(prompt)

print(response.content)