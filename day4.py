# a = [26, "ghorahi","sudan"]

# a = {
#     "address":"ghorahi",
#     "age":26,
#     "name":"sudan",
# }

# print (type(a))

# print(a['address'])
# print(a['age'])
# print(a['name'])

# # print(a['asd'])
# print(len(a))


# print(a.keys())


# print(a.values())

# print(a.get('age','No data found'))

# print(a.get('age'))


user_info = {
    "name":"suman",
    "phone":[
        {
            "name":"Jio",
            "no":"985678"
        },
        {
            "name":"Ncell",
            "no":"980"
        }

    ]
}

print(f'Phone no of Suman {user_info['name'][0]['name']}')

print("Phone number JIO of suman", )





user_info = {
    "name":"suman",
    "phone":[
        {
            "name":"JIO",
            "no":"985678"
        },
        {
            "name":"Ncell",
            "no":"980"
        }

    ]
}
# Phone number JIO of suman: 98213
# Phone number NCell of suman: 98213


phone_identifier =user_info['phone']
print("-------->",phone_identifier)
phone_identifier_0 = phone_identifier[0]
phone_identifier_0_name = phone_identifier_0['name']
phone_identifier_0_no =
phone_identifier_0['no']


phone_identifier_1 = phone_identifier[1]
phone_identifier_1_name = phone_identifier_1['name']
phone_identifier_1_no = phone_identifier_1['no']
print("-<", phone_identifier_1_no)

user_name = user_info['name']

# print(f'Phone number {user_info['phone'][0]['name']} of {user_info['name']}: {user_info['phone'][0]['no']} ')
# print(f'Phone number {user_info['phone'][1]['name']} of {user_info['name']}: {user_info['phone'][1]['no']} ')

print(f'Phone number {phone_identifier_0_name} of {user_name}: {phone_identifier_0_no} ')


