class Pipeline:
    def __init__(self):
        self.agents = []

    def add_agent(self, agent):
        self.agents.append(agent)

    def process_input(self, input_text):
        result = input_text
        for agent in self.agents:
            result = agent.process(result)
        return result
