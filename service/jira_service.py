
def find_summary_and_description(jira_id):
    return "", ""


def find_top_similar_jira(user_input):

    similar_jiras = []
    for i in range(5):
        similar_jira = dict()
        similar_jira["summary"] = "here is summary 1" + str(i)
        similar_jira["description"] = "here is desciption herhe ,ere  \n adaf  here is desciption herhe , 1" + str(i)
        similar_jira["score"] = 67-i
        similar_jira['created_time'] = "2024-07-03"
        similar_jira['pk_jira_data_id'] = "12"+ str(i)
        similar_jiras.append(similar_jira)

    return similar_jiras