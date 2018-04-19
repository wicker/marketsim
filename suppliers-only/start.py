import abce
import csv

# supplier object contains:
#   id: integer
#   county: string
#   marg_cost: float
#   marg_qty: float

class Supplier():

  id = 0
  county = ''
  marg_cost = 0.0
  marg_qty = 0.0

  def __init__(self, id, county, marg_cost, marg_qty):
    self.id = id
    self.county = county
    self.marg_cost = marg_cost
    self.marg_qty = marg_qty

  def print_info(self):
    print(self.id, self.county, self.marg_cost, self.marg_qty)

# Create a queue of suppliers from CSV file
# Verify by printing info

suppliers_csv_filename = 'crc_supply.csv'
suppliers_queue = []

with open(suppliers_csv_filename, 'r') as csvfile:
  suppliers_csv = csv.reader(csvfile, delimiter=',', quotechar='"')
  for line in suppliers_csv:

    s = Supplier(line[0], line[1], line[2], line[3])
    suppliers_queue.append(s)

  for supplier in suppliers_queue:
    supplier.print_info()


