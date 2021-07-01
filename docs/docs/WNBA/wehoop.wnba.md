# wehoop.wnba package

## Module contents


### wehoop.wnba.load_wnba_pbp(seasons: List[int])
Load WNBA play by play data going back to 2002

Ex:

    wnba_df = wehoop.wnba.load_wnba_pbp(seasons=[range(2002,2022)])

Args:

    seasons (list): Used to define different seasons. 2002 is the earliest available season.

Returns:

    pd.DataFrame: Pandas dataframe containing the
    play-by-plays available for the requested seasons.

Raises:

    ValueError: If season is less than 2002.


### wehoop.wnba.load_wnba_player_boxscore(seasons: List[int])
Load WNBA player boxscore data

Ex:

    wnba_df = wehoop.wnba.load_wnba_player_boxscore(seasons=[range(2002,2022)])

Args:

    seasons (list): Used to define different seasons. 2002 is the earliest available season.

Returns:

    pd.DataFrame: Pandas dataframe containing the
    player boxscores available for the requested seasons.

Raises:

    ValueError: If season is less than 2002.


### wehoop.wnba.load_wnba_schedule(seasons: List[int])
Load WNBA schedule data

Ex:

    wnba_df = wehoop.wnba.load_wnba_schedule(seasons=[range(2002,2022)])

Args:

    seasons (list): Used to define different seasons. 2002 is the earliest available season.

Returns:

    pd.DataFrame: Pandas dataframe containing the
    schedule for  the requested seasons.

Raises:

    ValueError: If season is less than 2002.


### wehoop.wnba.load_wnba_team_boxscore(seasons: List[int])
Load WNBA team boxscore data

Ex:

    wnba_df = wehoop.wnba.load_wnba_team_boxscore(seasons=[range(2002,2022)])

Args:

    seasons (list): Used to define different seasons. 2002 is the earliest available season.

Returns:

    pd.DataFrame: Pandas dataframe containing the
    team boxscores available for the requested seasons.

Raises:

    ValueError: If season is less than 2002.


### wehoop.wnba.wnba_calendar(season: int)
wbb_calendar - look up the WNBA calendar for a given season

Args:

    season (int): Used to define different seasons. 2002 is the earliest available season.

Returns:

    pd.DataFrame: Pandas dataframe containing
    calendar dates for the requested season.

Raises:

    ValueError: If season is less than 2002.
