student_details = {'id1':
    {'Name': 'Idhant',
     'Grade': 10,
     'si': ['English,maths, science']},
     'id2':
     {'Name': 'Bob',
      'Grade': 10,
      'si': ['English,maths, science']},
      'id3':
      {'Name': 'Bob',
      'Grade': 10,
      'si': ['English,maths, science']}
                         }

result = {}

for key,value in student_details.items():
    if value not in result.values():
        result[key] = value

print(result)