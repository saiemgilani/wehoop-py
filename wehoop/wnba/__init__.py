import pyarrow.parquet as pq
import pandas as pd
import json
from typing import List, Callable, Iterator, Union, Optional
from wehoop.config import WNBA_BASE_URL, WNBA_TEAM_BOX_URL, WNBA_PLAYER_BOX_URL, WNBA_TEAM_SCHEDULE_URL
from wehoop.errors import SeasonNotFoundError
from wehoop.dl_utils import download

def load_wnba_pbp(seasons: List[int]) -> pd.DataFrame:
    """Load WNBA play by play data going back to 2002

    Example:
        `wnba_df = wehoop.wnba.load_wnba_pbp(seasons=range(2002,2022))`

    Args:
        seasons (list): Used to define different seasons. 2002 is the earliest available season.

    Returns:
        pd.DataFrame: Pandas dataframe containing the
        play-by-plays available for the requested seasons.

    Raises:
        ValueError: If `season` is less than 2002.
    """
    data = pd.DataFrame()
    if type(seasons) is int:
        seasons = [seasons]
    for i in seasons:
        if int(i) < 2002:
            raise SeasonNotFoundError("season cannot be less than 2002")
        i_data = pd.read_parquet(WNBA_BASE_URL.format(season=i), engine='auto', columns=None)
        data = data.append(i_data)
    #Give each row a unique index
    data.reset_index(drop=True, inplace=True)
    return data

def load_wnba_team_boxscore(seasons: List[int]) -> pd.DataFrame:
    """Load WNBA team boxscore data

    Example:
        `wnba_df = wehoop.wnba.load_wnba_team_boxscore(seasons=range(2002,2022))`

    Args:
        seasons (list): Used to define different seasons. 2002 is the earliest available season.

    Returns:
        pd.DataFrame: Pandas dataframe containing the
        team boxscores available for the requested seasons.

    Raises:
        ValueError: If `season` is less than 2002.
    """
    data = pd.DataFrame()
    if type(seasons) is int:
        seasons = [seasons]
    for i in seasons:
        if int(i) < 2002:
            raise ValueError("season cannot be less than 2002")
        i_data = pd.read_parquet(WNBA_TEAM_BOX_URL.format(season = i), engine='auto', columns=None)
        data = data.append(i_data)
    #Give each row a unique index
    data.reset_index(drop=True, inplace=True)

    return data

def load_wnba_player_boxscore(seasons: List[int]) -> pd.DataFrame:
    """Load WNBA player boxscore data

    Example:
        `wnba_df = wehoop.wnba.load_wnba_player_boxscore(seasons=range(2002,2022))`

    Args:
        seasons (list): Used to define different seasons. 2002 is the earliest available season.

    Returns:
        pd.DataFrame: Pandas dataframe containing the
        player boxscores available for the requested seasons.

    Raises:
        ValueError: If `season` is less than 2002.
    """
    data = pd.DataFrame()
    if type(seasons) is int:
        seasons = [seasons]
    for i in seasons:
        if int(i) < 2002:
            raise ValueError("season cannot be less than 2002")
        i_data = pd.read_parquet(WNBA_PLAYER_BOX_URL.format(season = i), engine='auto', columns=None)
        data = data.append(i_data)
    #Give each row a unique index
    data.reset_index(drop=True, inplace=True)

    return data

def load_wnba_schedule(seasons: List[int]) -> pd.DataFrame:
    """Load WNBA schedule data

    Example:
        `wnba_df = wehoop.wnba.load_wnba_schedule(seasons=range(2002,2022))`

    Args:
        seasons (list): Used to define different seasons. 2002 is the earliest available season.

    Returns:
        pd.DataFrame: Pandas dataframe containing the
        schedule for  the requested seasons.

    Raises:
        ValueError: If `season` is less than 2002.
    """
    data = pd.DataFrame()
    if type(seasons) is int:
        seasons = [seasons]
    for i in seasons:
        if int(i) < 2002:
            raise ValueError("season cannot be less than 2002")
        i_data = pd.read_parquet(WNBA_TEAM_SCHEDULE_URL.format(season = i), engine='auto', columns=None)
        data = data.append(i_data)
    #Give each row a unique index
    data.reset_index(drop=True, inplace=True)

    return data

def wnba_calendar(season: int) -> pd.DataFrame:
    """wnba_calendar - look up the WNBA calendar for a given season

    Args:
        season (int): Used to define different seasons. 2002 is the earliest available season.

    Returns:
        pd.DataFrame: Pandas dataframe containing
        calendar dates for the requested season.

    Raises:
        ValueError: If `season` is less than 2002.
    """
    if int(season) < 2002:
        raise SeasonNotFoundError("season cannot be less than 2002")
    url = "http://site.api.espn.com/apis/site/v2/sports/basketball/wnba/scoreboard?dates={}".format(season)
    resp = download(url=url)
    txt = json.loads(resp)['leagues'][0]['calendar']
    datenum = list(map(lambda x: x[:10].replace("-",""),txt))
    date = list(map(lambda x: x[:10],txt))

    year = list(map(lambda x: x[:4],txt))
    month = list(map(lambda x: x[5:7],txt))
    day = list(map(lambda x: x[8:10],txt))

    data = {"season": season,
            "datetime" : txt,
            "date" : date,
            "year": year,
            "month": month,
            "day": day,
            "dateURL": datenum
    }
    df = pd.DataFrame(data)
    df['url']="http://site.api.espn.com/apis/site/v2/sports/basketball/wnba/scoreboard?dates="
    df['url']= df['url'] + df['dateURL']
    return df
