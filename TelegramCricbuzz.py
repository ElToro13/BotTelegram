from pycricbuzz import Cricbuzz
c = Cricbuzz()

match = c.matches()


class Cricket:

    def __init__(self, hu=""):
        self.hu = hu

    def match(self):
        listo=[]
        num=[]
        
        try:
            for i in range(0,5):
                listo.append(match[i]['srs'])
                num.append(match[i]['id'])
        except:
            listo.append("No more matches")
            num.append("None")
    
        return listo, num


class sendID:

    def __init__(self, num=0):
        self.num = num

    def LiveScore(self):
        score = c.livescore(self.num)
        try:
            bowlerTwo = "{} // {} - {} - {} - {} \n".format(score['bowling']['bowler'][1]['name'], score['bowling']['bowler'][1]['overs'],
                                                            score['bowling']['bowler'][1]['maidens'], score['bowling']['bowler'][1]['runs'],
                                                            score['bowling']['bowler'][1]['wickets'])
            
            bowlerOne = "{} // {} - {} - {} - {} \n".format(score['bowling']['bowler'][0]['name'], score['bowling']['bowler'][0]['overs'],
                                                            score['bowling']['bowler'][0]['maidens'], score['bowling']['bowler'][0]['runs'],
                                                            score['bowling']['bowler'][0]['wickets'])
        except:
            bowlerOne = "{} // {} - {} - {} - {} \n".format(score['bowling']['bowler'][0]['name'], score['bowling']['bowler'][0]['overs'],
                                                            score['bowling']['bowler'][0]['maiden'], score['bowling']['bowler'][0]['runs'],
                                                            score['bowling']['bowler'][0]['wickets'])
            
        BatsmanOne = "{} - {}/{} // 4|{} 6|{} \n".format(score['batting']['batsman'][0]['name'],score['batting']['batsman'][0]['runs'],
                                                      score['batting']['batsman'][0]['balls'],score['batting']['batsman'][0]['fours'],
                                                      score['batting']['batsman'][0]['six'])
        try:
            BatsmanTwo = "{} - {}/{} // 4|{} 6|{} \n".format(score['batting']['batsman'][1]['name'],score['batting']['batsman'][1]['runs'],
                                                      score['batting']['batsman'][1]['balls'],score['batting']['batsman'][1]['fours'],
                                                      score['batting']['batsman'][1]['six'])
        except:
            BatsmanTwo = "Wicket!"

        scorecard = "{}: {} - {} / {} \n".format(score['batting']['team'],score['batting']['score'][0]['runs'], score['batting']['score'][0]['wickets'],
                                              score['batting']['score'][0]['overs'])

        return scorecard, BatsmanOne, BatsmanTwo, bowlerOne, bowlerTwo

            
            
            
        
