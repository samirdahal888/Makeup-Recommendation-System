from models.dry_skin_advisor import DrySkinAdvisor

a = DrySkinAdvisor('samir','oval','fair')
print(a.get_user_information())
print(a.general_tips())