from smolagents import CodeAgent, LiteLLMModel


model = LiteLLMModel(model_id="groq/gemma2-9b-it") # You can choose to not pass any model_id to HfApiModel to use a default free model
# you can also specify a particular provider e.g. provider="together" or provider="sambanova"
from smolagents import CodeAgent, DuckDuckGoSearchTool


web_agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()],
    model=model,
    name="web_searcher",
    description="Runs web searches for you. Give it your query as an argument."
)

manager_agent = CodeAgent(
    tools=[], model=model, managed_agents=[web_agent]
)

manager_agent.run("Who is the CEO of Hugging Face?")