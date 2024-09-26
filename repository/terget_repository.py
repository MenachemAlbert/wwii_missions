from typing import List
from returns.maybe import Maybe
from model import Target
from config.base import session_factory


def find_all_targets() -> List[Maybe(Target)]:
    with session_factory() as session:
        targets = session.query(Target).all()
        return [Maybe.from_optional(target) for target in targets]
