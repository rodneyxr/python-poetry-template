import logging

import click

from app.logger import get_logger

logger = get_logger(__name__)


@click.option("--debug", is_flag=True, help="Enable debug mode")
@click.group()
def cli(debug: bool):
    if debug:
        logger.setLevel(logging.DEBUG)


@cli.command()
@click.option("--world", is_flag=True, help="Include world in the greeting")
def hello(world: bool):
    """Sample command that prints hello (world).

    Example:
        $ app hello
        Hello!

        $ app hello --world
        Hello, world!

    Args:
        world (bool): Whether to include "world" in the greeting.
    """
    logger.debug("running in debug mode")
    click.echo("Hello, world!" if world else "Hello!")


if __name__ == "__main__":
    cli()
