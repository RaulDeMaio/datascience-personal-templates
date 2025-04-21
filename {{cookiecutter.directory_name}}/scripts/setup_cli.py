import subprocess
import click

@click.group()
def cli():
    """CLI tool for setting up and managing the Data Science Project Template using uv."""
    pass

@cli.command()
def create_env():
    """Create a new virtual environment using uv"""
    click.echo("📦 Creating virtual environment with uv...")
    subprocess.run("uv venv", shell=True, check=True)

@cli.command()
def install():
    """Install project dependencies using uv"""
    click.echo("📚 Installing project dependencies...")
    subprocess.run("uv pip install -e .", shell=True, check=True)
    subprocess.run("pre-commit install", shell=True, check=True)

@cli.command()
def test():
    """Run unit tests using pytest"""
    click.echo("🧪 Running tests...")
    subprocess.run("pytest tests/", shell=True, check=True)

@cli.command()
def docs():
    """Generate documentation using pdoc"""
    click.echo("📖 Generating documentation...")
    subprocess.run("make docs", shell=True, check=True)

@cli.command()
def all():
    """Run all setup steps in order: create env, install deps, pre-commit, test, docs"""
    click.echo("🚀 Running full setup with uv...")
    create_env.invoke(click.Context(create_env))
    install.invoke(click.Context(install))
    test.invoke(click.Context(test))
    docs.invoke(click.Context(docs))

if __name__ == '__main__':
    cli()
