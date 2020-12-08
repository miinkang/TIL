#!C:\Users\minju\AppData\Local\Programs\Python\Python39\python.exe
print("Content-Type: text/html")
print()
# print('Hello World')

import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
import cgi, os, view, html_sanitizer
sanitizer = html_sanitizer.Sanitizer()


form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId, 'r').read()
    description = description.replace('<', '&lt')
    description = description.replace('>', '&gt')
    description = sanitizer.sanitize(description)
    update_link = '<a href="update.py?id={}">update</a>'.format(pageId)
    delete_action = '''
        <form action="process_delete.py" method="post">
            <input type="hidden" name="pageId" value="{}">
            <input type="submit" value="delete">
        </form>
    '''.format(pageId)

else:
    pageId = "Welcome"
    description = "Hello, AI"
    update_link = ""
    delete_action = " "
# print(pageId)

print('''<!doctype html>
<html>
<head>
  <title>learning page</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">AI</a></h1>
  <ol>
    {listStr}
  </ol>
<a href="create.py">create</a>
{update_link}
{delete_action}
  <h2>{title}</h2>
  <p>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/s0dMTAQM4cw" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
 </p>
  <p style="margin-top:80px;">{desc}</p>
</body>
</html>'''.format(
            title=pageId,
            desc=description,
            listStr=view.getList(),
            update_link=update_link,
            delete_action=delete_action))
