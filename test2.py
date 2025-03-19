from dotenv import load_dotenv
load_dotenv()

import datasets
from pinecone import Pinecone
from smolagents import LiteLLMModel, CodeAgent
from smolagents import Tool
from fastembed import TextEmbedding
import os
import voyageai

embedding_model = TextEmbedding()
API = os.getenv("PINECONE_API_KEY")
pc = Pinecone(api_key=API)
vo = voyageai.Client()


class RetrieverTool(Tool):
    name = "retriever"
    description = "Uses semantic search to retrieve the parts of transformers documentation that could be most relevant to answer your query."
    inputs = {
        "query": {
            "type": "string",
            "description": "The query to perform. This should be semantically close to your target documents. Use the affirmative form rather than a question.",
        }
    }
    output_type = "string"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.index = pc.Index("unified-pyano")

    def forward(self, query: str) -> str:
        # assert isinstance(query_embeddings, list), "Your search query must be a list of floats"
        query_embedding = vo.embed([query], input_type="query")
        query_embedding = query_embedding.embeddings
        docs = self.index.query(
            namespace="",
            vector=query_embedding,
            top_k=2,
            include_values=False,
            include_metadata=True,
        )
        return "\nRetrieved documents:\n" + "".join(
            [
                f"\n\n===== Document {str(i)} =====\n" + doc[i].metadata["text"]
                for i, doc in enumerate([docs.matches])
            ]
        )

retriever_tool = RetrieverTool()


agent = CodeAgent(
    tools=[retriever_tool], model=LiteLLMModel(model_id="groq/llama3-8b-8192"), max_steps=2, verbosity_level=2
)

agent_output = agent.run("Do u know about divyraj? what did he build?")

print("Final output:")
print(agent_output)