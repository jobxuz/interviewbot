import requests

def userget():
    url = 'https://temur01.pythonanywhere.com/api/telegramuser/'
    #url = 'http://127.0.0.1:8000/api/telegramuser/'
    respons = requests.get(url)
    return respons.json()





def usercreate(first_name,username,user_id):
    url = 'https://temur01.pythonanywhere.com/api/telegramuser/'
    #url = 'http://127.0.0.1:8000/api/telegramuser/'
    re = requests.post(url,data={'first_name':first_name,'username':username,'user_id':user_id})
    return re.status_code


def user(user_id):
    url = 'https://temur01.pythonanywhere.com/api/user/'+ user_id + '/'
    #url = 'http://127.0.0.1:8000/api/user/'+ user_id + '/'
    respons = requests.get(url)
    return respons.json()



def reklama():
    url = 'https://temur01.pythonanywhere.com/api/reklama/'
    #url = 'http://127.0.0.1:8000/api/reklama/'
    respons = requests.get(url)
    return respons.json()




def interviewcategory():
    url = 'https://temur01.pythonanywhere.com/interview/category/'
    #url = 'http://127.0.0.1:8000/interview/category/'
    response = requests.get(url)
    return response.json()

#print(interviewcategory())


def interview_category_name(name):
    url = 'https://temur01.pythonanywhere.com/interview/question/'+name+'/'
    #url = 'http://127.0.0.1:8000/interview/question/'+name+'/'
    respons = requests.get(url)
    return respons.json()

#print(interview_category_name('java'))
#print(len(interview_category_name('jobinterview')))


def interview_answer(savol):
    answers = []
    javob_url = savol.replace(" ", "%20")
    url = 'https://temur01.pythonanywhere.com/interview/answer/'+javob_url+'/'
    #url = 'http://127.0.0.1:8000/interview/answer/'+javob_url+'/'
    respons = requests.get(url)
    javoblar = respons.json()
    for x in javoblar:
        answers.append(x['answer'])
    return answers




#print(interview_answer('PHP nima'))












