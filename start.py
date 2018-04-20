from agent import Agent
from abce import *

simulation = Simulation(name='Test')
agents = simulation.build_agents(Agent, 'agent', 2)
for time in range(100):
  simulation.advance_round(time)
  agents.one()
  agents.two()
  agents.three()
simulation.graphs()
