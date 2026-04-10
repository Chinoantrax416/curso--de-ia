import os
from langchain_openai import OpenAI, ChatOpenAI


os.environ['OPENAI_API_KEY'] = ' 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'

'''model = OpenAI()

response = model.invoke(
    input = 'Quem foi Alan Turing?',
    temperature = 1,
    max_tokens=500,
)


print (response)'''


model = ChatOpenAI(

    model = 'gpt-5-nano',
)
messages = [
    {'role':'system','content': 'Você é um assitente que fornece informações sobre figuras historicas'},
    {'role':'user','content':'Quem foi Alan Turing?'}
]

response = model.invoke(messages)
print(response)
print(response.content)