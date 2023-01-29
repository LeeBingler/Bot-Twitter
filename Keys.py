def getApi():
    import twitter
    return twitter.Api(consumer_key="your consumer key",
                  consumer_secret="your consumer secret key",
                  access_token_key="your access token key" ,
                  access_token_secret="your access token secret")
