#!/usr/bin/env python3
from mylib.calc import add, substract, multiply, divide, power, square_root
import click


@click.group()
def cli():
    """A calculator CLI"""


@cli.command("add")
@click.argument("x", type=float)
@click.argument("y", type=float)
def add_command(x, y):
    """Add two numbers

    Example:
    ./calCLI.py add 2 3
    """
    # use colored output to print the result
    click.echo(click.style(f"{add(x, y)}", fg="green"))


# build commands and arguments for all mylib.calc functions
@cli.command("substract")
@click.argument("x", type=float)
@click.argument("y", type=float)
def substract_command(x, y):
    """Substract two numbers

    Example:
    ./calCLI.py substract 2 3
    """
    click.echo(click.style(f"{substract(x, y)}", fg="green"))


@cli.command("multiply")
@click.argument("x", type=float)
@click.argument("y", type=float)
def multiply_command(x, y):
    """Multiply two numbers

    Example:
    ./calCLI.py multiply 2 3
    """
    click.echo(click.style(f"{multiply(x, y)}", fg="green"))


@cli.command("divide")
@click.argument("x", type=float)
@click.argument("y", type=float)
def divide_command(x, y):
    """Divide two numbers

    Example:
    ./calCLI.py divide 2 3
    """
    click.echo(click.style(f"{divide(x, y)}", fg="green"))


@cli.command("power")
@click.argument("x", type=float)
@click.argument("y", type=float)
def power_command(x, y):
    """Calculate the power of a number as x base y

    Example:
    ./calCLI.py power 2 3
    """
    click.echo(click.style(f"{power(x, y)}", fg="green"))


@cli.command("square_root")
@click.argument("x", type=float)
def square_root_command(x):
    """Calculate the square root of a number

    Example:
    ./calCLI.py square_root 2
    """
    click.echo(click.style(f"{square_root(x)}", fg="green"))


if __name__ == "__main__":
    cli()
