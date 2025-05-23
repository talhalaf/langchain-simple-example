from dotenv import load_dotenv
from langchain import hub
from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain_experimental.tools import PythonREPLTool
from langchain_experimental.agents import create_csv_agent
from langchain.schema import SystemMessage
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder


load_dotenv()


def main():

    print("Start...")

    instructions = """You are an agent designed to write and execute python code to answer questions.
    You have access to a python REPL, which you can use to execute python code.
    If you get an error, debug your code and try again.
    Only use the output of your code to answer the question. 
    You might know the answer without running any code, but you should still run the code to get the answer.
    If it does not seem like you can write code to answer the question, just return "I don't know" as the answer.
    """

    base_prompt = hub.pull("langchain-ai/react-agent-template")

    prompt = base_prompt.partial(instructions=instructions)

    tools = [PythonREPLTool()]

    agent = create_react_agent(
        llm=ChatOpenAI(temperature=0, model="o4-mini"),
        tools=tools,
        prompt=prompt,
    )

    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    csv_agent = create_csv_agent(
        llm=ChatOpenAI(temperature=0, model="o4-mini"),
        path="episode_info.csv",
        verbose=True,
    )

    # agent_executor.invoke(input={"input": """generate and save in current working directory 3 QRcodes
    #                             that point to www.google.com, you have qrcode package installed already"""})

    csv_agent.invoke(input={
        "input": """
        Which writer wrote the most episodes? how many episodes did he write?
        """})

if __name__ == "__main__":
    main()
