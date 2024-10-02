# PyGame Highlights

Neste repositório você encontrará alguns projetos desenvolvidos por alunos do primeiro semestre dos cursos de engenharia, na disciplina Design de Software, e ciência da computação, na disciplina Vida de Desenvolvedor de Software. Os alunos devem implementar um jogo utilizando a linguagem Python e a biblioteca PyGame.

## Executando os jogos

As dependências estão no arquivo `requirements.txt`. Caso você adicione um projeto a este repositório que possua dependências adicionais, lembre-se de adicioná-las nesse arquivo.

    python -m venv env --prompt .
    . env/bin/activate
    pip install -r requirements.txt

Todos os jogos podem ser executados a partir do script `main.py`:

    python main.py

Para que um projeto seja executável por esse script, ele precisa conter um arquivo chamado `run_game.py` em sua raiz. Esse arquivo é responsável por executar o jogo. Assim, provavelmente será necessário adicioná-lo e importar o arquivo do jogo ou renomear o arquivo principal do jogo para `run_game.py`.

## Créditos

### TugWar 2016

- **Autores:** Lucas Cardoso Fontenla, Frederico Vilela Curti e Guilherme Schoueri Moraes
- **Semestre:** 1o semestre de 2016
- **Curso:** Engenharias
- **Repositório:** https://github.com/lucasfontenla/Projeto_Final_CaboDeGuerra
