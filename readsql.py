import sqlite3
 
conn = sqlite3.connect("2005-12.db")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

#sql = "SELECT coun FROM parent_reply"
#cursor.execute('PRAGMA table_info(parent_reply)')
cursor.execute("select * from parent_reply")
print cursor.fetchall()  # or use fetchone()
# =============================================================================
# def format_data(data):
#     data = data.replace("\n"," newlinechar ").replace("\r"," newlinechar ").replace('"',"'")
#     return data 
# print(format_data("I don\u00e2\u0080\u0099t know where they came up with this stuff, but Qube Web Search Client has taken the market by surprise. This is a cool concept that\u00e2\u0080\u0099s just beginning to blossom. You can save time by copying and pasting words and phrases."))
# =============================================================================
