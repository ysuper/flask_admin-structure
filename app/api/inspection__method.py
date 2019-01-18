from app import app
from bson.json_util import dumps
from .connect import connect_mongoDB

@app.route('/iqc/get/inspection__method', methods=['GET'])
def get_INSPECTION__METHOD_all():
    """
    回傳 inspection__method 表格 所有資料
    ---
    tags:
      - IQC inspection__method API (GET ALL)
    responses:
      200:
        description: "回傳 inspection__method 表格 所有資料"
    """
    conn = connect_mongoDB()
    db = conn.test
    collection = db.inspection__method
    getData = collection.find()
    return dumps(getData)
