import click

from .storages import PropertyListStorage, JSONStorage


@click.command()
@click.argument('xml', type=click.Path(exists=True))
@click.argument('json', type=click.Path())
def run(xml, json):
    """Convert Apple Music/iTunes XML exported playlists to Songshift JSON playlists"""

    src = PropertyListStorage(xml)
    dst = JSONStorage(json)

    playlists = src.get_playlists()
    dst.save(playlists)
