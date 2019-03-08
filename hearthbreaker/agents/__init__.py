from hearthbreaker.agents.agent_registry import AgentRegistry as __ar__
from hearthbreaker.agents.basic_agents import RandomAgent
from hearthbreaker.agents.trade_agent import TradeAgent
from hearthbreaker.agents.basic_agents import PredictableAgent
from hearthbreaker.agents.agent_tree import AgentTree

registry = __ar__()

registry.register("Random", RandomAgent)
registry.register("Trade", TradeAgent)
registry.register("PredictableAgent", PredictableAgent)
registry.register("Tree Agent", AgentTree)