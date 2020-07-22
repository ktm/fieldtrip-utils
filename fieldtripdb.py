import sqlite3


def get_location(dbfile, location_id):
    conn = sqlite3.connect(dbfile)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    t = (location_id,)
    c.execute('SELECT * FROM location where id = ?', t)
    retval = c.fetchall()
    conn.close()
    return retval

def get_locations(dbfile):
    conn = sqlite3.connect(dbfile)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT * FROM location')
    retval = c.fetchall()
    conn.close()
    return retval


def get_fieldtrips(dbfile):
    conn = sqlite3.connect(dbfile)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT * FROM field_trip')
    retval = c.fetchall()
    conn.close()
    return retval


def get_fieldtrips_at_location(dbfile, location_id):
    conn = sqlite3.connect(dbfile)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT * FROM field_trip where locationId = ?', location_id)
    retval = c.fetchall()
    conn.close()
    return retval


def create_artifact(dbfile, fieldtrip, latitude, longitude, file, description):
    conn = sqlite3.connect(dbfile)
    c = conn.cursor()
    c.execute('INSERT INTO field_trip_artifact(fieldTripid, artifactUrl, latitude, longitude, description) '
              'VALUES (?, ?, ?, ?, ?)', (fieldtrip, file, latitude, longitude, description))
    conn.commit()
    conn.close()
