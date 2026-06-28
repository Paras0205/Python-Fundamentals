def group_by_dept(employees):

    dept={}

    for emp in employees:

        department=emp["dept"]

        if department not in dept:
            dept[department]=[]

        dept[department].append(emp["name"])

    return dept


employees=[
    {"name":"Paras","dept":"IT"},
    {"name":"Rahul","dept":"HR"},
    {"name":"Amit","dept":"IT"}
]

print(group_by_dept(employees))