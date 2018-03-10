# -*- coding: utf-8 -*-

import click
import os
import sys
from paper.librarian import Librarian


@click.group()
def cmd():
    pass


@cmd.command()
def init():
    librarian = Librarian()
    librarian.init()


@cmd.command()
@click.argument('keywords', nargs=-1)
def search(keywords):
    librarian = Librarian()

    if not os.path.isfile('.paperconfig'):
        librarian.init()

    papers = librarian.search(keywords)
    for index, paper in enumerate(papers):
        print('- ' + str(index) + '. ' + paper['title'])
    user_input = librarian.get_user_input()
    librarian.save(papers[user_input])
    return 0


def main():
    cmd()


if __name__ == "__main__":
    sys.exit(main())
