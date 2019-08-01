import sqlite3

conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()

# cur.execute('''
# DROP TABLE IF EXISTS Counts''')

# cur.execute('''
# CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = 'tweets.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '):
        continue
    # if not line.startswith('To: ') : continue
    # if not line.startswith('From:') || line.contain('From:'): continue
    pieces = line.split()
    org = pieces[1]
    # print org
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES ( ?, 1 )''', (org, ))
    else:
        cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?',
                    (org, ))
    # This statement commits outstanding changes to disk each
    # time through the loop - the program can be made faster
    # by moving the commit so it runs only after the loop completes

# https://www.sqlite.org/lang_select.html
    conn.commit()
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

total = 0
print "Counts:"
for row in cur.execute(sqlstr):
    print str(row[0]), row[1]
    total += row[1]
print total

cur.close()
