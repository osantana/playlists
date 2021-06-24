from pathlib import Path

import click

from prettyconf import config

from .storages import PropertyListStorage, JSONStorage, AppleMusicStorage


@click.group()
def cli():
    pass


@cli.command()
@click.argument('xml', type=click.Path(exists=True))
@click.argument('json', type=click.Path())
def convert(xml, json):
    """Convert Apple Music/iTunes XML exported playlists to Songshift JSON playlists"""

    src = PropertyListStorage(xml)
    dst = JSONStorage(json)

    playlists = src.get_playlists()
    dst.save(playlists)


@cli.command()
@click.option('--key-id', '-k',
              metavar='KEY',
              envvar='APPLE_KEY_ID',
              show_envvar=True,
              required=False)
@click.option('--key-file', '-kf',
              type=click.File('r'),
              metavar="FILENAME or `-' for stdin",
              envvar='APPLE_KEY_FILENAME',
              show_envvar=True,
              required=False)
@click.argument('playlist', type=click.Path(exists=True))
def upload(key_id, key_file, playlist):
    """Send a playlist to your Apple Music using MusicKit API"""

    if key_id is None:
        key_id = config('APPLE_KEY_ID', default='')

    if not key_id:
        raise click.NoSuchOption('--key-id')

    if key_file is None:
        key_file = config('APPLY_KEY_FILENAME', default='')

    if not key_file:
        raise click.NoSuchOption('--key-file')

    key_file = Path(key_file)

    if not key_file.exists():
        raise click.BadOptionUsage('--key-file', f"File `{key_file}' not found")

    playlist = Path(playlist)

    if playlist.suffix.lower() == '.xml':
        source = PropertyListStorage(playlist.absolute())
    elif playlist.suffix.lower() in ['.json', '.js']:
        source = JSONStorage(playlist.absolute())
    else:
        raise click.BadArgumentUsage('Invalid playlist format')

    destination = AppleMusicStorage(key_id, key_file)
    playlists = source.get_playlists()

    destination.save(playlists)
