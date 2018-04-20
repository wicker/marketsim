import abce

class Agent(abce.Agent):

  def init(self, parameters, agent_parameters):
    self.grid = parameters['grid']
