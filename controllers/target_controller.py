from flask import Blueprint, jsonify
from dictalchemy.utils import asdict
from returns.maybe import Some

from repository.terget_repository import find_all_targets, get_target_by_id

target_blueprint = Blueprint("target", __name__)


@target_blueprint.route("/", methods=['GET'])
def get_all():
    maybe_targets = find_all_targets()
    target_dicts = [asdict(target.unwrap()) for target in maybe_targets if isinstance(target, Some)]
    return jsonify(target_dicts), 200


@target_blueprint.route("/<int:t_id>", methods=['GET'])
def get_target(t_id: int):
    target = get_target_by_id(t_id)
    if target:
        return jsonify(target), 200
    return jsonify({}), 404




