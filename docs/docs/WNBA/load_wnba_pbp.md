---
title: Load WNBA PBP
sidebar_label: Load WNBA PBP
---

### wehoop.wnba.load_wnba_pbp(seasons: List[int])
Load WNBA play by play data going back to 2002

Ex:

    wnba_df = wehoop.wnba.load_wnba_pbp(seasons=range(2002,2022))

Args:

    seasons (list): Used to define different seasons. 2002 is the earliest available season.

Returns:

    pd.DataFrame: Pandas dataframe containing the
    play-by-plays available for the requested seasons.

Raises:

    ValueError: If season is less than 2002.
