from langchain.agents.agent_toolkits import GmailToolkit
# tools = toolkit.get_tools()
# print(tools)
import os
os.environ["OPENAI_API_KEY"] = "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"
from langchain import OpenAI
from langchain.agents import initialize_agent, AgentType
llm = OpenAI(temperature=0)
agent = initialize_agent(
    tools=GmailToolkit().get_tools(),
    llm=llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
)
choice = input(
    "Enter 1 to send an email to A,\n 2 to send an email to B,\n or any other key to send an email to C: "
)
if choice == "1":
    print(
        agent.run(
            "create an email of Success Meeting and send it to sankalpwaghe123@gmail.com"
        )
    )
elif choice == "2":
    print(
        agent.run(
            "create an email of Loan Approved and send it to sankalpwaghe123@gmail.com"
        )
    )
elif choice == "3":
    print(
        agent.run(
            "create an email of Salary Credited and send it to sankalpwaghe123@gmail.com"
        )
    )
else:
    print("Error")

# print(agent.run("create an gmail draft of sankalpwaghe123@gmail.com of success meeting"))
# print(
#     agent.run(
#         "create an email of Success Meeting and send it to sankalpwaghe123@gmail.com"
#     )
# )
#   "scopes": ["https://mail.google.com/"],
# print(agent.run("send email message to sankalpwaghe123@gmail.com that you have passed in Maths"))
