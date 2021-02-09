from prettytable import PrettyTable

table = PrettyTable()

table.add_column('Student', ['Harry', 'Ron', 'Hermione', 'Neville', 'Draco'])
table.add_column('grade', ['Acceptable', 'Acceptable', 'Outstanding', 'Exeeds expectations', 'Troll'])

print(table)