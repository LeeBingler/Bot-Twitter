from Keys import getApi
import time
api = getApi()

def finishWith(sentence, keyword):
    return  sentence.endswith(keyword)

def dontStartsWith (sentence, keyword):
    return not sentence.startswith(keyword)

def postStatus(update, inReplyTo, media):
    api.PostUpdate(update,media=media, in_reply_to_status_id=inReplyTo)

def search(research, Howmany):
    searchResult = api.GetSearch(raw_query="q="+research+"&result_type=recent&count="+Howmany)
    for search in searchResult :
        if finishWith(search.text,"Quoi") or finishWith(search.text,"quoi") or finishWith(search.text,"quoi!") or finishWith(search.text,"quoi?") or finishWith(search.text,"quoi !") or finishWith(search.text,"quoi ?") or finishWith(search.text,"quoi ???") or finishWith(search.text,"quoi???"):
            if dontStartsWith(search.text,"RT"):
                print(search.text)
                time.sleep(3)
                postStatus("@"+search.user.screen_name+" Feur",search.id, "quoifeur.jpeg")

search("quoi","40")
