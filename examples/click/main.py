import click

@click.command()
@click.option('-j', '--jump', default='jump', help='I am jumping!')

def cli(jump):
    click.echo(jump)

if __name__ == '__main__':
    cli()
