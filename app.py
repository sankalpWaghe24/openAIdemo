from flask import Flask, render_template, request, jsonify
from langchain.agents.agent_toolkits import GmailToolkit
from langchain import OpenAI, PromptTemplate
from langchain.agents import initialize_agent, AgentType
import os
from langchain.agents import load_tools

app = Flask(__name__, template_folder=".")

toolkit = GmailToolkit()
os.environ["OPENAI_API_KEY"] = "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"
os.environ[
    "SERPAPI_API_KEY"
] = "515ab56f2a11cd6571551f6c528cb1ce311132a4889a89533d29dcfde0670fe3"

# tool_names = ["serpapi"]
# tools = load_tools(tool_names)
llm = OpenAI(temperature=0)
email_agent = initialize_agent(
    tools=toolkit.get_tools(),
    llm=llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
)
# google_agent = initialize_agent(
#     tools,
#     llm=llm,
#     agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
#     # agent="conversational-react-description",
# )

template = """
If your weight is below 50 then show Underweight
If your weight is between 51-100 then show Moderate
If weight is above 100 then show Overweight
weight is {weight}"""

prompt = PromptTemplate(
    input_variables=["weight"],
    template=template,
)
#########################################################


@app.route("/num/<int:number>/")
def incrementer(number):
    return f"Incremented number is {str(number + 1)}"


#########################################################


@app.route("/users", methods=["POST"])
def create_user():
    request_body = request.get_json()
    new_user = {
        "name": request_body["name"],
        "age": request_body["age"],
    }
    return jsonify(new_user)


#########################################################


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        weight = int(request.form["weight"])
        final_prompt = prompt.format(weight=weight)
        llm_output = llm(final_prompt)
        # email_agent.run(
        #     "create an email in the response of the template and send it to sankalpwaghe123@gmail.com"
        # )
        # print(google_agent.run("open gmail and send an email to sankalpwaghe123@gmail.com that your loan has been approved"))

        return render_template("result.html", prompt=final_prompt, output=llm_output)
    return render_template("index.html")


#########################################################

incomes = [{"description": "salary", "amount": 5000}]


@app.route("/incomes")
def get_incomes():
    return jsonify(incomes)


@app.route("/incomes", methods=["POST"])
def add_income():
    incomes.append(request.get_json())
    return "", 204


#########################################################

if __name__ == "__main__":
    app.run(debug=True)
