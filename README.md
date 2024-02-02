# rinkrat
Rinkrat is a command line tool to query the NHL's public API for statistics.

## Install
You can install rinkrat from PyPi

    python -m pip install rinkrat

It is supported by python 3.8 and above.

## Usage

    rinkrat [ command ] [ sub-command ] { parameters }

Rinkrat uses the command line interface to get statistics from the public NHL api. With the current version you can access team standings data and rank it based on several criteria:

### Commands
Commands give you access to different data. Sub-commands determine how that data is organized and presented. For command snippits and descriptions, please see the [commands](docs/commands/README.md) directory.

#### Standings
The standings command retrieves standings data for the entire league. This data can be organized into different rankings by using the sub-commands.

|Sub-command   |Parameters   |Description   |
|---|---|---|
|`overall`  |none   |The results are ranked by league.   |
|`conference`   |`eastern` `western`   |The results are ranked by conference.  |
|`division`   |`atlantic` `metropolitan` `central` `pacific`   |The results are ranked by division  |
|`wild`   |`eastern` `western`   |The results are ranked by wildcard position  |

You can supply more that one parameter at a time for the selected sub command:

    $ rinkrat standings division atlantic central


