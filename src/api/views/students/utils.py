def sqliteRowToDict(row):
    if (len(row) != 0):
        return dict(row[0])
    return {}
