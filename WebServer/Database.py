def get_lot_info(connection):
    try:
        cur = connection.cursor()
        string = "select LOT_ID, LOT_NAME from PARKING_LOTS"
        cur.execute(string)
        result = cur.fetchall()
        if result:
            return result
        return -1
    except:
        return "exception"
