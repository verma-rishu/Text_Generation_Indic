
from googletrans import Translator
orgFile = open('test_quotes_english.txt', 'r')
orgFilesLines = orgFile.readlines()
translatorFile = open("test_quotes_punjabi.txt", "a", encoding="utf-8")

translator = Translator()
print("Starting Conversion")
# Strips the newline character
count = 0
for line in orgFilesLines:
    raw_trans = translator.translate(line, dest="pa", src="en")
    translation = raw_trans.text
    translatorFile.write(translation + '\n')
    count += 1

print(f'Number of lines converted {count}')