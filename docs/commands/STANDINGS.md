# Standings
    rinkrat standings [ sub-command ] { parameters }

The standings command retrieves standings data for the entire league. This data can be organized into different rankings by using the sub-commands.

|Sub-command   |Parameters   |Description   |
|---|---|---|
|`overall`  |   |The results are ranked by league.   |
|`conference`   |`eastern` `western`   |The results are ranked by conference.  |
|`division`   |`atlantic` `metropolitan` `central` `pacific`   |The results are ranked by division  |
|`wild`   |`eastern` `western`   |The results are ranked by wildcard position  |

You can supply more that one parameter at a time for the selected sub command:

    $ rinkrat standings division atlantic central

## Options
#### `-d`
You can get results for a specific date by passing the `-d` or `--date` flag with a date in the `YYYY-MM-DD` format.
