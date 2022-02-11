# -*- coding: utf-8 -*-
import {{cookiecutter.project_slug}}


def test_{{cookiecutter.project_slug}}() -> None:
    assert {{cookiecutter.project_slug}}


def test_import_eventsourcing() -> None:
    import eventsourcing

    assert eventsourcing.__version__
