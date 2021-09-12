import re
from pprint import pprint

# читаем адресную книгу в формате CSV в список contacts_list
import csv

with open("phonebook_raw.csv", encoding='UTF8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

# TODO 1: выполните пункты 1-3 ДЗ
for row in contacts_list[1:]:
  fio = (' '.join(row[:3])).split(' ')[:3]
  for i in range(0, 3):
    row[i] = fio[i]

  phone_mask = re.compile("((\+7|8)\s?\(?(\d{,3})\)?\s?[-]?(\d{,3})[-]?(\d{,2})[-]?(\d+)(\s\(?(доб.(\s\d+)?)\)?)?)")
  row[5] = re.sub(phone_mask, r"+7(\3)\4-\5-\6 \8", row[5])

contacts_list.sort()

new_contact_list = []
for contact in contacts_list:
  for new_contact in new_contact_list:
    if contact[0] in new_contact:
      for i, n in enumerate(new_contact):
        if new_contact[i] == "":
          new_contact[i] = contact[i]
      break
  else:
    new_contact_list.append(contact)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding='UTF8') as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(new_contact_list)
