import csv
import os
import click

# Define the filename for the expense data
expense_file = 'expenses.csv'

# Create the CSV file if it doesn't exist
if not os.path.exists(expense_file):
    with open(expense_file, 'w', newline='') as csvfile:
        fieldnames = ['Date', 'Description', 'Amount']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

@click.group()
def cli():
    pass

@cli.command()
@click.option('--date', prompt='Date (YYYY-MM-DD)', help='Expense date')
@click.option('--description', prompt='Description', help='Expense description')
@click.option('--amount', prompt='Amount', type=float, help='Expense amount')
def add(date, description, amount):
    """Add a new expense"""
    with open(expense_file, 'a', newline='') as csvfile:
        fieldnames = ['Date', 'Description', 'Amount']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'Date': date, 'Description': description, 'Amount': amount})
    click.echo(f'Expense added: Date: {date}, Description: {description}, Amount: {amount}')

@cli.command()
def list():
    """List all expenses"""
    with open(expense_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        click.echo("Expense List:")
        for row in reader:
            click.echo(f'Date: {row["Date"]}, Description: {row["Description"]}, Amount: {row["Amount"]}')

if __name__ == '__main__':
    cli()
