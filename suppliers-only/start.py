import abce
import csv

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

# Preparation step! Nothing in here requires abce
# Create a list of suppliers from CSV file
# Verify by printing info

suppliers_csv_filename = 'crc_supply.csv'
suppliers_list = []

with open(suppliers_csv_filename, 'r') as csvfile:
  suppliers_csv = csv.reader(csvfile, delimiter=',', quotechar='"')
  for line in suppliers_csv:

    s = {
      'id': line[0],
      'county': line[1],
      'marg_cost': line[2],
      'marg_qty': line[3]
    }
    suppliers_list.append(s)

# Create simulation

simulation = abce.Simulation(name="Suppliers")

suppliers = simulation.build_agents(
    Supplier_Agent,  # agent class
    'supplier',      # name of the group
    agent_parameters = suppliers_list
    # no need to pass 'number' explicitly, because abce
    # calculates the length of the list automatically
)

# Run the simulation

for r in range(1):
  simulation.advance_round(r)
  suppliers.print_info()

