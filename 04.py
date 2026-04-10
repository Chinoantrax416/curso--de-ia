import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

os.environ['OPENAI_API_KEY'] = ' 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'

model = ChatOpenAI(model='gpt-5-nano')

chat_template = ChatPromptTemplate.from_messages(
    [
          SystemMessage(content='Você deve responder baseado em dados geográficos de regiões do Brasil'),
          HumanMessagePromptTemplate.from_template('Por favor, me fale sobre a região {regiao}.'),
          AIMessage(content='Claro,vou começar coletando informações sobre a região e analisando os dados disponíveis.'),
          HumanMessage(content='Certifique-se de incluir dados demográficos'),
          AIMessage(content='Entendido.Aqui estão todos:'),

    ]
)

prompt = chat_template.format_messages(regiao='Sul')
response = model.invoke(prompt)

print(response.content)