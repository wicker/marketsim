import abce, pandas

# Supplier Agent class
#
# The agent parameters should be
#   id: integer
#   county: string
#   marg_cost: float
#   marg_qty: float

class Supplier_Agent(abce.Agent):

  # use init function, not __init__ function, because
  # the agent needs to inherit from abce.Agents
  def init(self, parameters, agent_parameter):
    self.id = agent_parameter['id']
    self.county = agent_parameter['county']
    self.marg_cost = agent_parameter['marg_cost']
    self.marg_qty = agent_parameter['marg_qty']

  def print_info(self):
    print("Round "+str(self.round)+": "+self.group+" "+self.county+" (ID "+str(self.id)+")")

  def whether_to_sell(self):
    if (market_price > self.marg_cost):
      print("(ID: "+str(self.id)+") "+self.county+" sold with margin cost of "+str(self.marg_cost))

# Preparation step! Nothing in here requires abce
# Use Pandas to create a dataframe from the suppliers CSV
# Select random 100 of the suppliers list

suppliers_csv_filename = 'crc_supply.csv'
suppliers_list = []

with open(suppliers_csv_filename, 'r') as csvfile:
  suppliers_df = pandas.read_csv(csvfile)

  suppliers_df = suppliers_df.sample(n=100)

  # get access to each row of the dataframe
  for i in range(1, len(suppliers_df)):
    s = {
      'id': suppliers_df.iloc[i].ID,
      'county': suppliers_df.iloc[i].County_Soil,
      'marg_cost': suppliers_df.iloc[i].marginal_cost,
      'marg_qty': suppliers_df.iloc[i].marginal_qty
    }
    suppliers_list.append(s)

# Create simulation

market_price = 10.0

simulation = abce.Simulation(name="Suppliers")

suppliers = simulation.build_agents(
    Supplier_Agent,  # agent class
    'supplier',      # name of the group
    agent_parameters = suppliers_list
    # no need to pass 'number' explicitly, because abce
    # calculates the length of the list automatically
)

# Run the simulation

for r in range(3):
  simulation.advance_round(r)
  suppliers.whether_to_sell()

