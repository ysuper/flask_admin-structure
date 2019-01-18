from app import app 
from .connect import connect_sqlite

dbfile = "sample_db.sqlite"

@app.route('/sqlite/get/UserRegisters2', methods=['GET'])
def get_UserRegister2_all():
    """
    回傳 UserRegisters2 表格
    ---
    tags:
      - sqlite UserRegister2 API (GET All)
    responses:
      200:
        description: "回傳 UserRegisters2 表格"
    """
    sqlcmd = "SELECT * FROM UserRegisters2"
    return connect_sqlite(dbfile, sqlcmd)
