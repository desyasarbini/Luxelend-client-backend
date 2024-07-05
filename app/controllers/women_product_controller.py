from flask import jsonify, request
from app.models.women import Women
from app.connectors.sql_connector import Session
from app.utils.api_response import api_response

def create_women_product():
    session = Session()
    session.begin()

    category = request.json.get("category"),
    product_name = request.json.get("product_name"),
    product_brand = request.json.get("product_brand"),
    image_url = request.json.get("image_url"),
    rent_price = request.json.get("rent_price"),
    retail_price = request.json.get("retail_price"),
    size = request.json.get("size"),
    color = request.json.get("color"),
    style = request.json.get("style"),
    material = request.json.get("material"),
    fit_note = request.json.get("fit_note")
    
    women_new_product = Women(
        category = category,
        product_name = product_name,
        product_brand = product_brand,
        image_url = image_url,
        rent_price = rent_price,
        retail_price = retail_price,
        size = size,
        color = color,
        style = style,
        material = material,
        fit_note = fit_note
    )
    
    try:
        session.add(women_new_product)
        session.commit()        
    except Exception as e:
        session.rollback()
        return jsonify(f"add new product for women section failed: {e}")
    finally:
        session.close()
        return api_response(
            status_code = 201,
            message = "Add new product in women section success!!!",
            data = {
                "id": women_new_product.id,
                "category": women_new_product.id,
                "product_name": women_new_product.product_name,
                "product_brand": women_new_product.product_brand,
                "image_url": women_new_product.image_url,
                "rent_price": women_new_product.rent_price,
                "retail_price": women_new_product.retail_price,
                "size": women_new_product.size
            }
        )