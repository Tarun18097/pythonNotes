sapid = "123,1234,345,456"
sapid = sapid.strip().replace("'","").replace('"',"").split(",")


def generate_email_list(sapid):
    str = "@stu.upes.ac.in"
    email_list = []
    for i in sapid:
        email_list.append(f"'{i.strip() + str}'")
    return "[" + ",".join(email_list) + "]"

email_list = generate_email_list(sapid)
print(email_list)

