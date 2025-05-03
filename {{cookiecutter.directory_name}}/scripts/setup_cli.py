import subprocess
import click

@click.group()
def cli():
    """CLI tool to setup the Data Science Project Template"""
    pass

@cli.command()
@click.option('--env-name', prompt='Conda environment name', help='Name of the conda environment to create')
def create_env(env_name):
    """Create the conda environment from config/environment.yml"""
    click.echo(f"📦 Creating conda environment: {env_name}")
    subprocess.run(f"conda env create -f config/environment.yml -n {env_name}", shell=True, check=True)

@cli.command()
@click.option('--env-name', prompt='Conda environment name', help='Name of the conda environment to activate')
def activate(env_name):
    """Activate the environment and run make setup"""
    click.echo(f"⚙️ Running project setup for env: {env_name}")
    subprocess.run(f"conda activate {env_name} && make setup", shell=True, executable="/bin/bash")

@cli.command()
def install_precommit():
    """Manually installs pre-commit hooks"""
    click.echo("🔧 Installing pre-commit...")
    subprocess.run("pre-commit install", shell=True)

@cli.command()
def test():
    """Run unit tests using pytest"""
    click.echo("🧪 Running tests...")
    subprocess.run("make test", shell=True)

@cli.command()
def docs():
    """Generate documentation using pdoc"""
    click.echo("📚 Generating documentation...")
    subprocess.run("make docs", shell=True)

@cli.command()
@click.option('--env-name', prompt='Conda environment name', help='Name of the conda environment to use')
def all(env_name):
    """Run all setup steps in order"""
    create_env.invoke(click.Context(create_env), env_name=env_name)
    activate.invoke(click.Context(activate), env_name=env_name)
    install_precommit.invoke(click.Context(install_precommit))
    test.invoke(click.Context(test))
    docs.invoke(click.Context(docs))

if __name__ == '__main__':
    cli()
