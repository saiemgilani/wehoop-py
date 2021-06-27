import pandas as pd
import json
from wehoop.dl_utils import download



def wbb_calendar(season: int) -> pd.DataFrame:
    url = "http://site.api.espn.com/apis/site/v2/sports/basketball/womens-college-basketball/scoreboard?dates={}".format(season)
    resp = download(url=url)
    txt = json.loads(resp)['leagues'][0]['calendar']
    reg = pd.DataFrame(txt[0]['entries'])
    post = pd.DataFrame(txt[1]['entries'])
    full_schedule = pd.concat([reg,post], ignore_index=True)
    full_schedule['season']=season
    return full_schedule

def wnba_calendar(season: int) -> pd.DataFrame:
    url = "http://site.api.espn.com/apis/site/v2/sports/basketball/wnba/scoreboard?dates={}".format(season)
    resp = download(url=url)
    txt = json.loads(resp)['leagues'][0]['calendar']
    reg = pd.DataFrame(txt[0]['entries'])
    post = pd.DataFrame(txt[1]['entries'])
    full_schedule = pd.concat([reg,post], ignore_index=True)
    full_schedule['season']=season
    return full_schedule
