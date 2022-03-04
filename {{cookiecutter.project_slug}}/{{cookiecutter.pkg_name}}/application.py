# -*- coding: utf-8 -*-
from typing import Any, Dict, cast
from uuid import UUID

from eventsourcing.application import Application

from {{cookiecutter.pkg_name}}.domainmodel import Dog


class DogSchool(Application):
    def register_dog(self, name: str) -> UUID:
        dog = Dog(name)
        self.save(dog)
        return dog.id

    def add_trick(self, dog_id: UUID, trick: str) -> None:
        dog = cast(Dog, self.repository.get(dog_id))
        dog.add_trick(trick)
        self.save(dog)

    def get_dog(self, dog_id: UUID) -> Dict[str, Any]:
        dog = cast(Dog, self.repository.get(dog_id))
        return {"name": dog.name, "tricks": tuple(dog.tricks)}
