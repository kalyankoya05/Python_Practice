DevOps = ["AWS", "Ansible", "Terraform", "Jenkins","K8s"]
Dev = ("Java", "Python", ".Net", "JS")

emp1 = {"name":"Kalyan","Skill":"DevOps","ID":1234}
emp2 = {"Name":"Nani","Skill":"Python","Id":2345}

usr_data = input("Enter your skill: ")

if usr_data in DevOps:
    print(f"Your skill {usr_data} in DevOps team")
elif usr_data in Dev:
    print(f"Your Skill {usr_data} in Dev team")
elif usr_data in emp1.values() or usr_data in emp2.values():
    print(f"your data {usr_data} in employee details")
else:
    print("Not found")