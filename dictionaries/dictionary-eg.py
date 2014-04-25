student = {
    'id':'123',
    'name':'hugo',
    'scores':{
        'maths':100,
        'english':99
    },
    'hobby':['reading','sports']
}

print student['name']
print student['hobby'][0]
print student['scores']['maths']

student['age'] = 21
print len(student) # the number of key-value pairs

del student['id']
student['age'] += 1
print student