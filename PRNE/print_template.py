template = "{0:19} {1:20} {2:15}"
    print(template.format("TENANT", "APP_PROFILE", "EPG"))
    print(template.format("------", "-----------", "---"))
    for rec in data:
        print(template.format(*rec))