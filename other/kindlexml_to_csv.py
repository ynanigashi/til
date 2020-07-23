#kindle Pc cashe file => kindle book list csv
import xml.etree.ElementTree as ET
import csv

input_file_str = "./KindleSyncMetadataCache.xml"
output_file_str = "./kindle_book_list.csv"
header = ["ASIN", "title", "authors", "publishers",
            "publication_date", "purchase_date",
            "textbook_type", "cde_contenttype",
            "content_type"]
nary = [header]
tree = ET.parse(input_file_str)
root = tree.getroot()
for book_info in root[2]:
    ary = []
    for info in book_info:
        #authers publishers are nested
        if len(info) == 0:
            ary.append(info.text)
        else:
            info_list = [ s.text for s in info ]
            ary.append(';'.join(info_list))
    nary.append(ary)

with open(output_file_str, 'w') as f:
    writer = csv.writer(f)
    writer.writerows(nary)



