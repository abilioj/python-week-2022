from typer.testing import CliRunner

from beerlog.cli import main

# abre um terminaus
runner = CliRunner()


def test_add_beer():
    result = runner.invoke(
        main, ["add", "Skol", "KornPA", "--flavor=1", "--image=1", "--cost=2"]
    )
    assert result.exit_code == 0
    assert "Beer Added" in result.stdout
