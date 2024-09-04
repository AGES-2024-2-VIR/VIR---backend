from flask import Blueprint, request, jsonify
from models import db, User

bp = Blueprint('main', __name__)


@bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()

    new_user = User(
        name=data['name'],
        email=data['email'],
        password=data['password'],
        role=data['role']
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created!', 'id': new_user.id}), 201


@bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()

    return jsonify([{
        'id': user.id,
        'name': user.name,
        'email': user.email,
        'role': user.role,
        'created_at': user.created_at,
        'updated_at': user.updated_at
    } for user in users])


@bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)

    return jsonify({
        'id': user.id,
        'name': user.name,
        'email': user.email,
        'role': user.role,
        'created_at': user.created_at,
        'updated_at': user.updated_at
    })


@bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    user = User.query.get_or_404(id)

    user.name = data.get('name', user.name)
    user.email = data.get('email', user.email)
    user.password = data.get('password', user.password)
    user.role = data.get('role', user.role)

    db.session.commit()
    return jsonify({'message': 'User updated!'})


@bp.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()

    return jsonify({'message': 'User deleted!'})
