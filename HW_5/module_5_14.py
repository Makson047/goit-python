import re


def find_all_phones(text):
    result = re.findall(r"\+380\([0-9]{2}\)[0-9]{3}-[0-9]{1,2}-[0-9]{2,3}", text)
    res = []
    for r in result:
      if len(r)>17:
        r = r[:17]
      res.append(r)
    return res


print(find_all_phones("Irma +380(67)777-7-771 second +380(67)777-77-77 aloha a@test.com abc111@test.com.net "
                      "+380(67)111-777-777+380(67)777-77-787"))
