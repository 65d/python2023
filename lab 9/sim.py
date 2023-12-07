import random

class CafeSimulation:
    def __init__(self, num_tables, num_waiters):
        self.num_tables = num_tables
        self.num_waiters = num_waiters
        self.profit = 0
        self.hours_of_operation = 12
        self.time_slots = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]  
        self.table_slots = {i: None for i in range(1, num_tables + 1)}

    def simulate(self):
        for hour in range(1, self.hours_of_operation + 1):

            
            if hour in [7, 8, 12]:
                num_customers = random.randint(5, 10)
            else:
                num_customers = random.randint(1, 5)

            for one in range(num_customers):
                customer = Customer()
                self.handle_customer(customer)

            self.profit = self.profit - 15 * self.num_waiters


        self.analyze_results()

    def handle_customer(self, customer):

        available_tables = [table for table, occupant in self.table_slots.items() if occupant is None]
        
        if available_tables:
            selected_table = random.choice(available_tables)
            self.table_slots[selected_table] = customer
            customer.table_number = selected_table
            self.profit += customer.calculate_order_total(available_tables)



    def analyze_results(self):
        print(self.profit)

class Customer:
    def __init__(self):
        self.waiting_time = random.randint(5, 30)  
        self.time_spent = random.randint(30, 120)  
        self.table_number = None
        
    def calculate_order_total(self, available_tables):
        if self.table_number is not None:

            if self.time_spent > 0:
                self.time_spent -= 60
            else:
                available_tables[self.table_number] = None
                self.table_number = None

        return random.randint(10, 50)


if __name__ == "__main__":
    cafe_simulation = CafeSimulation(num_tables=35, num_waiters=5)
    cafe_simulation.simulate()
