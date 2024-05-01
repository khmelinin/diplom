import sqlite3

db = sqlite3.connect('policlinic_tg_bot.db')

# Курсор sql
c = db.cursor()

# c.execute('drop table spheres')
# c.execute('drop table complaints')
# c.execute('drop table sessions')
# c.execute('drop table complaints_sessions')
# c.execute('drop table journal')
# c.execute('drop table experts')

db.commit()
c.close()
db.close()