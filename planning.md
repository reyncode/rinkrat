# rinkrat
A command line interface designed to fetch NHL stats and output the results in the requested order. It should have a similar feel to the ps command for linux users who would like to inspect active processes on their system.

## SoC

### Data Acquisition
Fetching the data, caching the results and handling of any errors.

- API requests can be made with the requests module. To cache those results we can use the install_cache method provided by requests-cache[^1].
- If an error arises we can catch it from the RequestsException[^2] class.
- There is limited documentation on the NHL API but similar API's recommend updating the results every 5 minutes.

### Data Manipulation
How the fetched data is restructured to provide a result that matches the request.

### Result Delivery
What the user sees after their request has been processed.

- We can specify a string width with formatting methods to make the results easy to read.

An ideal result would look like:

```
$ rinkrat -td

Atlantic Division
Team                    GP  W   L   OT  P   ...
Boston Bruins           29  19  5   5   43
Toronto Maple Leafs     28  16  6   6   38
Florida Panthers        30  18  10  2   38
...

Metropolitan Division
Team                    GP  W   L   OT  P   ... 
New York Rangers        29  21  7   1   43
Philadelphia Flyers     30  17  10  3   37
New York Islandes       30  14  8   8   36
...
```

### User Requests
Providing an interface for the user to make a request on the structure of fetched data.

- We can use the argparse package to handle program options and option arguments.
- Requires a mapping of exclusive commands.
- The options should allow for scalability of additional options as the project grows.

- POSIX has its own standards for utility arguments which describes things like providing options as a hyphen + letter (-a) and option arguments (-a option_argument). GNU has Standards for Command Line Interfaces which extends POSIX with long options (--long_option) and the inclusion of a --help and --version option[^3][^4].
    - The arguments that consist of <hyphen-minus> characters and single letters or digits, such as 'a', are known as "options" (or, historically, "flags").
    - Certain options are followed by an "option-argument", as shown with [ -c option_argument].
    - Option-arguments are shown separated from their options by <blank> characters, except when the option-argument is enclosed in the '[' and ']' notation to indicate that it is optional, as shown with [-f[option_argument].
    - Frequently, names of parameters that require substitution by actual values can be shown with <parameter name>.
    - Arguments separated by the '|' ( <vertical-line>) bar notation are mutually-exclusive. Mutually-exclusive means they are separate and very different from each other, so that it is impossible for them to exist or happen together. 

#### High-level Overview:
```
rinkrat
├── team
│   ├── league
│   ├── conference
│   ├── division
│   └── wild-card
└── player
    └── ?
```
#### Lower-level Overview:

**Base Data Options:**

-t, --team: 
Default option. Usage unlocks subset options that apply to NHL Team data. Providing a team abbreviation fetches results for just one team (untested)

-p, --players:
Usage unlocks subset of options that apply to searching NHL player stats.

**Team Options:**

-o, --league:
Default Option. Groups teams in overall league ranking (1-32).

-c, --conference:
Groups teams by their conference in ranked order (1-16 east, 1-16 west).

-d, --division:
Groups teams by their division in ranked order (1-8 atlantic, 1-8 metropolitan, 1-8 central, 1-8 pacific).

-w, --wild-card:
Groups teams by their conference/division in ranked order with the wild-card cut line (1-3 atlantic + 1-3 metropolitan + 1-8 wild-card-east, ...)

#### Example Help Page:
```
Usage:
 rinkrat [options]

Selection options:
 -t, --teams                        selects nhl team data
                                    default option

 -p, --players                      [v2] selects nhl player data
                                    default option

Team based options:
 -o, --league                       group results by conference,
                                    default option

 -c, --conference <conference>      group results by conference,
                                    limit to <conference> if specified

 -d, --division <division>          group results by division,
                                    limit to <division> if specified

 -w, --wild-card <conference>       insert the wild card cut line,
                                    limit to <conference> if specified

Player based options:
 -?, --? <name>                     [v2] query player results by name

 -?, --? <category>                 [v2] group results by leaders of 
                                    <category>, use C to see all categories

Output formats:
 -f, --format <format>  user-defined format,
                        use L to see all options
                        
 -F                     all extra columns

 -s, --sort <col>       sort the results by data
                        in col

 -n, --lines <num>      limit the results to lines

 -r, --reverse          show in reverse order

Miscellaneous options:
  L                     show format specifiers

  A                     show team abbreviations

  C                     [v2] show leaders categories

 --help                 Print usage and this help message and exit

 --version              Print version and exit 
```

## User Stories
- As a user, I want to be able to view NHL teams by their rank in the standings.
    - A user shall be able to group their results by league, conference or division.
    - A user shall be given the option to show wild card rankings

- As a user, I want to be able to search only my favorite team.
    - A user shall be given an option to list accepted keywords if they are confused.

- As a user, I only want to see the first 3 teams in each grouping.

## Sample flow
1. On the command line I type `rinkrat -td` to list all teams ranked by their division.
2. The program makes an API request to ../v1/standings/now to get the current rankings.
3. The results are cached in a database provided by the requests-cache package and expire after 5 minutes.
4. Raw data is passed to a function and parsed by looking at the value for the 'divisionName' key. A data structure similar to the input is returned but with new keys for each division. Ranked team data is inserted into a new dict that is found under the divisional key name.
5. The manipulated results are displayed to the users terminal.

## Resources
[^1]:[basic-usage-with-patching](https://requests-cache.readthedocs.io/en/stable/examples.html#basic-usage-with-patching)
[^2]:[requests.RequestException](https://requests.readthedocs.io/en/latest/api/#requests.RequestException)
[^3]:[12.1 Utility Argument Syntax](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap12.html)
[^4]:[4.8 Standards for Command Line Interfaces](https://www.gnu.org/prep/standards/standards.html#Command_002dLine-Interfaces)

- [NHL-API-Reference](https://github.com/Zmalski/NHL-API-Reference)
