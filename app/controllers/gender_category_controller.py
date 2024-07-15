from flask import jsonify, request
from sqlalchemy.orm import joinedload
from app.models.gender import Gender
from app.models.gender_category import Gender_category
from app.connectors.sql_connector import Session
from app.utils.api_response import api_response

# def get_gender():
#     response_data = dict()
#     session = Session()
#     session.begin()

#     try:
#         gender_query = session.query(Gender)
#         if request.args.get('query') != None:
#             search_query = request.args.get('query')
#             gender_query = gender_query.filter(Gender.name.like(f"%{search_query}%"))

#         gender = gender_query.all()
#         response_data['gender'] = [gender.serialize(full=False) for gender in gender]
#         return jsonify(response_data)
#     except Exception as e:
#         session.rollback()
#         return jsonify(f"error occured: {e}"), 400
#     finally:
#         session.close()

def get_gender_category():
    try:
        session = Session()

        gender_categories = session.query(Gender_category).all()
        serialized_gender_categories = [gc.serialize() for gc in gender_categories]

        return jsonify(serialized_gender_categories), 200
    except Exception as e:
        return jsonify({"error": f"Failed to fetch gender categories: {str(e)}"}), 400
    finally:
        session.close()
