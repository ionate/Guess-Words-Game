# GuessWords.Py
# (originally called "chains.py")
# v1.00
# 
import random

from langchain_openai import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate
from langchain.schema import BaseOutputParser
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class CommaSeparatedListOutputParser(BaseOutputParser):
    def parse(self, text: str):
        """ Return lists of comma separated values """
        return text.strip().split(", ")

def use_chains():
    try:
        chat_model = ChatOpenAI()

        template = """You are a helpful assistant who generates comma separated lists.
        A user will pass in a category, and you should generate 5 objects in that category in a comma separated list.
        ONLY return a comma separated list, and nothing more.
        """
        human_template  = "{text}"

        chat_prompt = ChatPromptTemplate.from_messages([
            ("system", template),
            ("human", human_template)
            ])
        
        chain = chat_prompt | chat_model | CommaSeparatedListOutputParser()
        topic_list = ["sunshine", "guitars", "birds", "politics", "president", "watch"]
        randtopic = random.choice(topic_list)
        result = chain.invoke({"text": randtopic})
        return randtopic, result
    except Exception as ex:
        print(f'EXC={ex}')
        return None, None

r_topic, r_reply = use_chains()
print('*'*40)
print(f'Topic:{r_topic}\nReply:{r_reply}\n')
print('*'*40)
