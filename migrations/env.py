import subprocess
from pathlib import Path
from dotenv import load_dotenv
import typer
from rich import print

ENV_PATH = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=ENV_PATH)

app = typer.Typer(no_args_is_help=True)

@app.command()
def up():
    subprocess.run(["docker", "compose", "up", "-d"], check=True)

@app.command()
def migrate():
    subprocess.run(["alembic", "upgrade", "head"], check=True)

@app.command()
def seed():
    subprocess.run(["python", "tools/seed.py"], check=True)

@app.command()
def reset_db():
    print("[yellow]Resetting containers and volumes…[/yellow]")
    subprocess.run(["docker", "compose", "down", "-v"], check=True)
    subprocess.run(["docker", "compose", "up", "-d"], check=True)
    subprocess.run(["alembic", "upgrade", "head"], check=True)

@app.command()
def run_api():
    subprocess.run(["uvicorn", "app.main:app", "--reload"], check=True)

if __name__ == "__main__":
    app()

