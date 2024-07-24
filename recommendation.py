user_skills = {
    "user1": ["Python", "Data Analysis"],
    "user2": ["Web Development", "JavaScript"],
    "user3": ["Machine Learning", "Python"],
}


internships = {
    "Data Analyst": {
        "skills": ["Python", "SQL"],
        "rating": 4.2
        },
    "Web Development": {
        "skills": ["HTML", "JavaScript"],
        "rating": 4.0
        },
    "Machine Learning Engineer": {
        "skills": ["Machine Learning", "Python"],
        "rating": 4.8
        },
}

def recommend_internships(user_id):
    user_skills_list = user_skills[user_id]
    recommended = []
    for internship_title, details in internships.items():
        if any(skill in user_skills_list for skill in details["skills"]):
            recommended.append(internship_title)
    recommended.sort(key=lambda internship: internships[internship]["rating"], reverse=True)
    return recommended

# example usage
user_id = "user1"
print(f"Hi {user_id}, here are some internship recommendations for you:")
for internship in recommend_internships(user_id):
    print(f"- {internship}")
