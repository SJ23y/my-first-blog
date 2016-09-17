
"""
Отыскивает наибольший файл с исходным программным кодом
на языке Python вдереве каталогов.
Поиск выполняется в каталоге стандартной библиотеки,
отображение результатов выполняется с помощью модуля pprint.

"""

import sys, os, pprint
trace = 0
if sys.platform.startswith('win'):
    dirname = r'F:\Python 3.5.1\Lib'     # windows
else:
    dirname = '/usr/lib/python'          # Unix, Linux, Cygwin

allsizes = []
for(thisDir, subsHere, filesHere) in os.walk(dirname):
    if trace: print(thisDir)
    for filename in filesHere:
        if filename[-3:] == '.py':
            if trace: print('...', filename)
            fullname = os.path.join(thisDir, filename)
            fullsize = os.path.getsize(fullname)
            allsizes.append((fullsize, fullname)


print(allsizes[:2])
print(allsizes[-2:])






