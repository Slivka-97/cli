import click

# Command Group
@click.group()
def cli():
    pass

@cli.command(help='task publisher')
@click.pass_context
def task_publisher(ctx: click.Context) -> None:
    click.echo(f'task_publisher {ctx}')

@cli.command(name='task-consumer', help='task consumer')
@click.option('--value', default=None, help='test option')
def task_consumer(value):
    if value is not None:
        click.echo(f'task consumer {value}')
    else:
        click.echo(f'task consumer')


if __name__ == '__main__':
    cli()
