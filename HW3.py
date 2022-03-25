


class socialMedia:
  def __init__(self, name):
    self.name = name

  def getName(self):
    return self.name

class Instagram(socialMedia):
    def __init__(self, name):
        super().__init__(name)
        self.postList=[]  
    
    def GetPosts(self):
        return self.postList
    
    def PublishNewPost(self,body):
        if len(body) < 2200 :
            self.postList.append(body)
        else : print('larg size')
    
    

class Twitter(socialMedia):
    def __init__(self, name):
        super().__init__(name)
        self.tweetList=[]  
    
    def getTweets(self):
        return self.tweetList 
    
    def CreateNewTweet(self,body):
        if len(body) < 280 :
            self.tweetList.append(body)
        else : print('larg size')
        

insta = Instagram('instagram')
twitter = Twitter('Twitter')
twitter.CreateNewTweet('slam bar to')
twitter.CreateNewTweet('sal no mobarak omidvaram sale khobi dar kenar khanevade va dostanet dashte bashi va movafaghiat ha be samtet bian ...........................................................................................................................................................................')
twitter.CreateNewTweet('slm chetori ')
print('twitter :')
print(*twitter.getTweets(), sep = "\n")

insta.PublishNewPost('roze khobi dashte bashi')
insta.PublishNewPost('hale delet khob bahse')

print('\ninstagram :')
print(*insta.GetPosts(), sep = "\n")
