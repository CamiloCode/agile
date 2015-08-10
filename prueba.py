import os

index=os.listdir('./Images')

x=len(index)

for fname in index:
    while x>0:
        x=x-1
        index[x] = '<a href="./Images/' + index[x] + '">' + '<img src="./Images/' + index[x] + '" />' + '</a>'

listString='\n'.join(index)

title=os.getcwd()
title=title.split("/")
title=title.pop()

file = open("index.html", 'w')

file.write('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"' + '\n')
file.write('    "http://www.w3.org/TR/html4/loose.dtd">' + '\n')
file.write('<html>' + '\n')
file.write('<title>' + title + '</title>' + '\n')
file.write('<head>' + '\n')
file.write('<style>' + '\n')
file.write('body {padding:10px;background-color:black;margin-left:15%;margin-right:15%;font-family:"Lucida Grande",Verdana,Arial,Sans-Serif;color: white;}' + '\n')
file.write('img {border-style:solid;border-width:5px;border-color:white;}' + '\n')
file.write('</style>' + '\n')
file.write('</head>' + '\n')
file.write('<body>' + '\n')
file.write('<h1>' + title + '</h1>' + '\n')
file.write(listString + '\n')
file.write('</body>' + '\n')
file.write('</html>')

file.close()