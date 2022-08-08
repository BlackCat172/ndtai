import sqlite3

con=sqlite3.connect('/Users/nguyenductai/Library/Application Support/Google/Chrome/Default/History')
cursor = con.cursor()
cmd="SELECT url FROM urls where url like '%//dantri%' or url like '%//vnexpress%' or url like '%//baomoi%' or url like '%//vietnamnet%' or url like '%//thanhnien%' ;"
cursor.execute(cmd)
urls = cursor.fetchall()
result = '\n'.join('\n'.join(tup) for tup in urls)
print(result)