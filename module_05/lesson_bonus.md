# Относительные и абсолютные пути

Для того, чтобы обращаться к файловой системе, нам нужно указывать пути до файлов. Сделать это можно двумя способами - при помощи абсолютных и относительных путей.

Абсолютный путь - это полный адрес файла. Например, для Windows он может выглядеть так: `C:/Users/username/Documents/file.txt`.

Абсолютный путь можно использовать, чтобы обратиться к каким-то конфигурационным файлам, которые на всех компьютерах лежат в одном и том же месте. Во всех остальных случаях стоит использовать относительные пути.

Относительный путь - это способ задать адрес до файла относительно текущего местоположения. Абсолютный путь - это если бы вы спросили у человека на улице где он живет и он бы сказал название города, улицы и номер дома, а относительный путь - это если бы вы спросили как пройти до какого-то места и вам бы ответили, что нужно пройти 200 метров прямо, перейти дорогу и повернуть налево.

Относительный путь может выглядеть так: `Documents/file.txt`. Это будет означать, что из текущей папки мы зайдем в папку Documents и там будем  искать файл file.txt. Если в рамках одного проекта использовать относительные пути, то этот проект будет запускаться на любом компьютере без изменения путей.

А теперь представим такую ситуацию. Вы работаете в папке project, и в ней есть две папки - data и notebooks. В папке notebooks хранятся jupyter ноутбуки, из которых вам надо обращаться к файлам из папки data. Как это сделать при помощи относительных путей? Например, так: `../data/file.txt`. С помощью двух точек мы возвращаемся на уровень выше и можем зайти в любую папку на этом уровне.
