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


def get_lot_status(connection, id):

        cur = connection.cursor()
        string = "select " \
                    "DATE_FORMAT(SCAN_DATE, '%d-%b-%y at %r') as date ," \
                    "STUDENT_SPACES as student," \
                    "FACULTY_SPACES as faculty " \
                 "from PARKING_RECORDS  " \
                 "where " \
                    "LOT_ID = {} " \
                    "AND SCAN_DATE = (" \
                        "select MAX(SCAN_DATE) " \
                        "from PARKING_RECORDS " \
                        "WHERE LOT_ID = {}" \
                 ")".format(id, id)
        cur.execute(string)
        selected = cur.fetchone()
        result = dict.fromkeys(["date","student","faculty"])
        if selected:
            result["date"] = selected[0]
            result["student"] = selected[1]
            result["faculty"] = selected[2]
            return result
        else:
            return None

def update_lot(connection,student,staff,lot):
    cur = connection.cursor()
    string = "insert into PARKING_RECORDS( " \
                "LOT_ID,"\
                "SCAN_DATE," \
                "STUDENT_SPACES," \
                "FACULTY_SPACES) " \
             "values(" \
                "{}," \
                "SYSDATE()," \
                "{}," \
                "{}" \
             ")".format(lot,student,staff)

    cur.execute(string)
    connection.commit()
