import youtube_assistant as ya

user_input = "What are the characteristics of life?"
url = "https://youtu.be/tZE_fQFK8EY?si=cjPlr3k3nuYbo0xj"

db = ya.create_vector_db_from_youtube(url)
#cprint(db)
response = ya.youtube_assistant(user_input,db)
print(response)