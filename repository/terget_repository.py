from typing import List
from returns.maybe import Maybe, Nothing
from returns.result import Success, Failure
from sqlalchemy import Result
from sqlalchemy.exc import SQLAlchemyError

from model import Target
from config.base import session_factory


def find_all_targets() -> List[Maybe(Target)]:
    with session_factory() as session:
        targets = session.query(Target).all()
        return [Maybe.from_optional(target) for target in targets]


def get_target_by_id(target_id: int):
    with session_factory() as session:
        target = session.query(Target).filter(Target.target_id == target_id).one_or_none()
        if target:
            return {
                "target_id": target.target_id,
                "target_priority": target.target_priority,
                "location": {
                    "latitude": target.location.latitude,
                    "longitude": target.location.longitude,
                    "city": {
                        "city_name": target.location.cities.city_name,
                        "country": target.location.cities.country.country_name,
                    }
                },
                "target_type": target.target_type.target_type_name if target.target_type else None,
                "industry": target.industry.industry_name if target.industry else None,
            }
        return None


def insert_target(target: Target) -> Success | Failure:
    with session_factory() as session:
        try:
            session.add(target)
            session.commit()
            session.refresh(target)
            return Success(target)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))


def update_target(t_id: int, target: Target) -> Failure | Success:
    with session_factory() as session:
        try:
            maybe_target = get_target_by_id(t_id)
            if maybe_target is Nothing:
                return Failure(f"No target by the id {t_id}")
            target_to_update = session.merge(maybe_target.unwrap())
            target_to_update.target_industry = target.target_industry
            target_to_update.target_priority = target.target_priority
            target_to_update.city_id = target.city_id
            target_to_update.target_type_id = target.target_type_id
            session.commit()
            session.refresh(target_to_update)
            return Success(target_to_update)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))


def delete_target(target_id: int) -> Failure | Success:
    with session_factory() as session:
        try:
            maybe_target = get_target_by_id(target_id)
            if maybe_target is Nothing:
                return Failure(f"No target found with id {target_id}")
            target_to_delete = maybe_target.unwrap()
            session.delete(target_to_delete)
            session.commit()
            return Success(target_to_delete)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))
