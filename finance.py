
class Finance:
    def __init__(self, salary, rent, current, mess):
        self.total = salary
        # Store initial expenses in a list of dictionaries
        self.expenses = [
            {'name': 'Rent', 'amount': rent},
            {'name': 'Current Bill', 'amount': current},
            {'name': 'Mess Bill', 'amount': mess}]
        self.calculate_balance()
        self.write_to_file('Initial setup')

    def calculate_balance(self):
        total_expenses = sum(i['amount'] for i in self.expenses)
        self.balance = self.total - total_expenses
        return  self.balance

    def write_to_file(self, note):
        with open('finance1.txt', 'a') as file:
            file.write(f'{note}\n')
            file.write(f'Total amount available: {self.total}\n\n')
            file.write('EXPENSES\n')
            for i in self.expenses:
                file.write(f"{i['name']}: {i['amount']}\n")
            file.write(f'Balance after expenses: {self.balance}\n\n')

    def new(self, newbill, amount):
        self.expenses.append({'name': newbill, 'amount': amount})
        self.calculate_balance()
        self.write_to_file(f'New expense added - {newbill}')

    def view(self):
        with open('finance1.txt', 'r') as file:
            content = file.read()
            print(content)


chart = Finance(40000, 5000, 1500, 2000)


def check(operation):
    if operation=='view':
        chart.view()
    elif operation == 'add':
        newbill = input('Enter the new expense: ')
        try:
            amount = int(input('Enter the amount: '))
            chart.new(newbill, amount)
            chart.view()
        except ValueError:
            print('Invalid amount. Please enter a valid number.')
    elif operation=='balance':
        chart.calculate_balance()
    else:
        print('invalid opertion')
        x=input('enter the  opertion to be done view/add/balance of expense: ')
        check(x)


operation=input('enter the  opertion to be done view/add/balance of expense: ')
check(operation)








