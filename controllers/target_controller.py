from flask import Blueprint, jsonify
from dictalchemy.utils import asdict
from repository.terget_repository import find_all_targets

target_blueprint = Blueprint("target", __name__)


@target_blueprint.route("/", methods=['GET'])
def get_all():
    maybe_targets = find_all_targets()
    target_dicts = [asdict(target.value) for target in maybe_targets if target.is_present()]
    return jsonify(target_dicts), 200
