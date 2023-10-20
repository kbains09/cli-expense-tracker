import csv
import os
import click
from babel.numbers import format_currency

# Define the filename for the expense data
expense_file = 'expenses.csv'
categories_file = 'categories.csv'

# Create the CSV files if they don't exist
if not os.path.exists(expense_file):
    with open(expense_file, 'w', newline='') as csvfile:
        fieldnames = ['Date', 'Description', 'Amount', 'Category']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

if not os.path.exists(categories_file):
    with open(categories_file, 'w', newline='') as csvfile:
        fieldnames = ['Category']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

@click.group()
def cli():
    pass

@cli.command()
@click.option('--date', prompt='Date (YYYY-MM-DD)', help='Expense date')
@click.option('--description', prompt='Description', help='Expense description')
@click.option('--amount', prompt='Amount', type=float, help='Expense amount')
@click.option('--category', prompt='Category', help='Expense category')
def add(date, description, amount, category):
    """Add a new expense"""
    with open(expense_file, 'a', newline='') as csvfile:
        fieldnames = ['Date', 'Description', 'Amount', 'Category']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'Date': date, 'Description': description, 'Amount': amount, 'Category': category})
    click.echo(f'Expense added: Date: {date}, Description: {description}, Amount: {format_currency(amount, "USD", locale="en_US")}, Category: {category}')

@cli.command()
@click.option('--date', prompt='Date to edit (YYYY-MM-DD)', help='Date of the expense to edit')
@click.option('--description', prompt='New description', help='New description')
@click.option('--amount', prompt='New amount', type=float, help='New amount')
@click.option('--category', prompt='New category', help='New category')
def edit(date, description, amount, category):
    """Edit an existing expense"""
    expenses = []
    with open(expense_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            expenses.append(row)

    for expense in expenses:
        if expense['Date'] == date:
            expense['Description'] = description
            expense['Amount'] = amount
            expense['Category'] = category
            break

    with open(expense_file, 'w', newline='') as csvfile:
        fieldnames = ['Date', 'Description', 'Amount', 'Category']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for expense in expenses:
            writer.writerow(expense)
    click.echo(f'Expense updated: Date: {date}, Description: {description}, Amount: {format_currency(amount, "USD", locale="en_US")}, Category: {category}')

if __name__ == '__main__':
    cli()
