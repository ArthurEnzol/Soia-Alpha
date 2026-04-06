import os
import sys
import typer
from dotenv import load_dotenv

from src.core.constants import SOIA_LOGO
from src.core.loader import load_project
from src.utils.directory import load_directory
from src.ui.display import center_txt
from src.ui.menu import menu
from src.ui.menu_area import menu_area
from src.ui.menu_config import json_config, json_config_reset
from src.auth.login import login
from src.ui.terminal import clear_lines

app = typer.Typer()
load_dotenv()

@app.command()
def config(reset: bool = typer.Option(False, "--reset", help="Reset your configs")):
    if reset:
        json_config_reset()
    else:
        json_config()


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    
    if ctx.invoked_subcommand is not None:
        return
    os.system('cls' if os.name == 'nt' else 'clear')
    
    center_txt(SOIA_LOGO)
    load_project(load_directory())

    print(f"Executando de: {sys.executable}")
    print("----------------------------------")
    while True:
        if menu():
            while True:
                if not menu_area():
                    break

    input("\nPressione ENTER para fechar o bot...")
    

if __name__ == "__main__":
    app()