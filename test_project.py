from mylib.calc import substract, multiply, divide, power, square_root
from calCLI import cli
from click.testing import CliRunner

# write the testing using click.testing.CliRunner and a pytest fixture
import pytest


@pytest.fixture
def runner():
    return CliRunner()


# write a command line test for each function
def test_substract_command(runner):
    result = runner.invoke(cli, ["substract", "2", "3"])
    assert result.exit_code == 0
    assert "1.0" in result.output


def test_multiply_command(runner):
    result = runner.invoke(cli, ["multiply", "2", "3"])
    assert result.exit_code == 0
    assert "6.0" in result.output


def test_divide_command(runner):
    result = runner.invoke(cli, ["divide", "2", "3"])
    assert result.exit_code == 0
    assert "0.6666666666666666" in result.output


def test_power_command(runner):
    result = runner.invoke(cli, ["power", "2", "3"])
    assert result.exit_code == 0
    assert "8.0" in result.output


def test_square_root_command(runner):
    result = runner.invoke(cli, ["square_root", "4"])
    assert result.exit_code == 0
    assert "2.0" in result.output


# write a test function for each function that asserts the correct output for a given input
def test_substract():
    assert substract(2, 3) == -1


def test_multiply():
    assert multiply(2, 3) == 6


def test_divide():
    assert divide(2, 3) == 0.6666666666666666


def test_power():
    assert power(2, 3) == 8


def test_square_root():
    assert square_root(4) == 2
