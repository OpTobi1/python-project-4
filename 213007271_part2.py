# Name: David Haim Liav Lugasi ID: 213007271


class Employee:
    def __init__(self, employee_id, name, monthly_hours, hourly_wage):
        self.employee_id = employee_id
        self.name = name
        self.monthly_hours = monthly_hours
        self.hourly_wage = hourly_wage
        self.monthly_salary = 0

    def get_salary(self):
        self.monthly_salary = self.monthly_hours * self.hourly_wage
        return self.monthly_salary

    def __repr__(self):
        return f"Employee(ID: {self.employee_id}, Name: {self.name}, Monthly Hours: {self.monthly_hours}, Hourly Wage: {self.hourly_wage}, Monthly Salary: {self.monthly_salary})"

class Manager(Employee):
    def __init__(self, employee_id, name, monthly_hours, hourly_wage, bonus, management_level):
        super().__init__(employee_id, name, monthly_hours, hourly_wage)
        self.bonus = bonus
        self.management_level = management_level

    def get_salary(self):
        self.monthly_salary = (self.monthly_hours * self.hourly_wage + self.bonus) * self.management_level
        return self.monthly_salary

    def __repr__(self):
        return f"Manager(ID: {self.employee_id}, Name: {self.name}, Monthly Hours: {self.monthly_hours}, Hourly Wage: {self.hourly_wage}, Bonus: {self.bonus}, Management Level: {self.management_level}, Monthly Salary: {self.monthly_salary})"

class Factory:
    def __init__(self, factory_name):
        self.factory_name = factory_name
        self.workers = []

    def add_worker(self, worker):
        self.workers.append(worker)

    def get_best_worker(self):
        best_worker = max(self.workers, key=lambda worker: worker.monthly_hours)
        return best_worker.employee_id, best_worker.name

    def promote(self):
        promoted_workers = []
        for worker in self.workers:
            if worker.monthly_hours > 160:
                worker.hourly_wage *= 1.1
                worker.get_salary()
                promoted_workers.append((worker.name, worker.monthly_salary))
        return promoted_workers

    def best_managers(self):
        return [manager for manager in self.workers if isinstance(manager, Manager) and manager.management_level >= 2 and manager.monthly_hours > 120]

    def __repr__(self):
        return f"Factory(Name: {self.factory_name}, Workers: {self.workers})"



factory1 = Factory("Liav's Factory")
employee1 = Employee(1, "David", 160, 10)
empolyee2 = Employee(2, "Haim", 180, 10)
manager1 = Manager(3, "Liav", 200, 10, 1000, 2)
manager2 = Manager(4, "Lugasi", 180, 10, 1000, 3)

factory1.add_worker(employee1)
factory1.add_worker(empolyee2)
factory1.add_worker(manager1)
factory1.add_worker(manager2)

print(factory1.get_best_worker())
print(factory1.promote())
print(factory1.best_managers())
print(factory1)

