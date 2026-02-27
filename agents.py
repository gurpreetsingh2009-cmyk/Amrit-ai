import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Agent:
    def __init__(self, name):
        self.name = name
        self.memory = {}

    def remember(self, key, value):
        self.memory[key] = value
        logger.info(f"{self.name} remembered {key}: {value}")

    def recall(self, key):
        value = self.memory.get(key)
        logger.info(f"{self.name} recalled {key}: {value}")
        return value

    def execute_task(self):
        # Override in subclasses
        pass

class TaskPlanner:
    def __init__(self):
        self.tasks = []

    def schedule_task(self, task):
        self.tasks.append(task)
        logger.info(f"Task scheduled: {task}")

    def get_tasks(self):
        return self.tasks

class ExecutionEngine:
    def __init__(self, agents):
        self.agents = agents

    def execute(self, task):
        try:
            logger.info(f"Executing task: {task}")
            for agent in self.agents:
                agent.execute_task()
            logger.info("Execution completed successfully.")
        except Exception as e:
            logger.error(f"Error during execution: {e}")

class AgentOrchestrator:
    def __init__(self, agents):
        self.agents = agents
        self.planner = TaskPlanner()
        self.engine = ExecutionEngine(agents)

    def orchestrate(self):
        tasks = self.planner.get_tasks()
        for task in tasks:
            self.engine.execute(task)

# Example usage
if __name__ == '__main__':
    agent1 = Agent('Agent1')
    agent2 = Agent('Agent2')
    orchestrator = AgentOrchestrator([agent1, agent2])
    orchestrator.planner.schedule_task('Task 1')
    orchestrator.orchestrate()