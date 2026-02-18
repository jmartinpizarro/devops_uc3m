from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Sequence


@dataclass(frozen=True)
class User:
    id: int
    name: str
    email: str


@dataclass(frozen=True)
class Ticket:
    id: int
    author_id: int
    created_at: datetime
    title: str
    description: str
    tags: Sequence[str]
