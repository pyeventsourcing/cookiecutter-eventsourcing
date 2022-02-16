# -*- coding: utf-8 -*-
from {{cookiecutter.project_slug}}.application import DogSchool


def test_application() -> None:
    # Construct application object.
    app = DogSchool()

    # Call application command methods.
    dog_id = app.register_dog("Fido")
    app.add_trick(dog_id, "roll over")
    app.add_trick(dog_id, "fetch ball")

    # Call application query method.
    assert app.get_dog(dog_id) == {
        "name": "Fido",
        "tricks": ("roll over", "fetch ball"),
    }
