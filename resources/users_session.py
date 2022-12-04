from flask_restful import Resource, reqparse
from models.user import UserModel
from flask_jwt_extended import create_access_token

minha_requisicao = reqparse.RequestParser()
minha_requisicao.add_argument('email', type=str, required=True, help="email is required")
minha_requisicao.add_argument('password', type=str, required=True, help="password is required")

class UserSession(Resource):
    @classmethod
    def post(cls):
        dados = minha_requisicao.parse_args()
        user = UserModel.find_user_by_email(dados['email'])

        if user and user.password == dados['password']:
            token_acesso = create_access_token(identity=user.id)
            return {'access_token': token_acesso}, 200
        return {'message': 'User or password is not correct.'}

