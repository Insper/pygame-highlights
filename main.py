import os
from pathlib import Path

import click

HERE = Path(__file__).parent
RUN_GAME = 'run_game.py'
PROJECT_PATHS = {
    dirpath.name: dirpath
    for dirpath in HERE.iterdir()
    if dirpath.is_dir() and (dirpath / RUN_GAME).is_file()
}
PROJECT_NAMES = sorted(list(PROJECT_PATHS), key=lambda x: x.lower())
PROJECT_OPTIONS = '\n'.join(f'{i}) {name}' for i, name in enumerate(PROJECT_NAMES, 1))


def validate_project(ctx, param, value):
    if value is None or value <= 0 or value > len(PROJECT_NAMES):
        raise click.BadParameter(f"Opção inválida.")
    return value


@click.command()
@click.option('--project', prompt=f'\nProjetos disponíveis:\n{PROJECT_OPTIONS}\nDigite o número do projeto', help='Nome do projeto', callback=validate_project, type=int)
def main(project):
    project_name = PROJECT_NAMES[project - 1]
    project_path = PROJECT_PATHS[project_name]
    os.chdir(project_path)
    try:
        os.system(f'python {RUN_GAME}')
    finally:
        os.chdir(HERE)


if __name__ == "__main__":
    main()
