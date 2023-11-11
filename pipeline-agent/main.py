from gpt_agent import GPTAgent
from pipeline import Pipeline

model1 = "Json model1 location"
model2 = "Json model2 location"

# Create GPT agents
gpt_agent1 = GPTAgent(model1)
gpt_agent2 = GPTAgent(model2)

# Create a pipeline
pipeline = Pipeline()

# Add GPT agents to the pipeline
pipeline.add_agent(gpt_agent1)
pipeline.add_agent(gpt_agent2)

# Process input through the pipeline
input_text = "Hello, world!"
output_text = pipeline.process_input(input_text)

# Output the final result
print(output_text)
