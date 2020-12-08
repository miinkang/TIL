#!C:\Users\minju\AppData\Local\Programs\Python\Python39\python.exe
print("Content-Type: text/html")
print()
# print('Hello World')

import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
import cgi, os, view


form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId, 'r').read()

else:
    pageId = 'Welcome'
    description = 'Hello, AI'
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
<form action="process_update.py" method='post'>
    <input type="hidden" name="pageId" value="{form_default_title}">
  <p><input type="text" name="title" placeholder="title" value="{form_default_title}"></p>
  <p><textarea rows="4" name="description" placeholder="description">{form_default_description}</textarea></p>
  <p><input type="submit"></p>
</form>
  <h2>{title}</h2>
  <p>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/s0dMTAQM4cw" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
 </p>
  <p style="margin-top:80px;">{desc}</p>
</body>
</html>'''.format(title=pageId, desc=description, listStr=view.getList(), form_default_title=pageId, form_default_description=description))
