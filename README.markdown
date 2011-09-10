# ljout #

`ljout` is a command line tool for exporting a LiveJournal to local files.


## Installation ##

Install its dependencies from the `requirements.txt` file:

    $ pip install -r requirements.txt

Then you can install it as any other Python program:

    $ python setup.py install

If you don't want to install its dependencies system-wide, try installing it in a [virtual environment](http://www.virtualenv.org/).


## Configuring ##

The script uses your LiveJournal username and password to export your data. Run the `configure` command and enter the username you want to use:

    $ ljout configure
    Username: markpasc
    Password:
    Configured!

After saving your password, the export commands will be available. Note that your password is saved in the `~/.ljout` file – only you will be able to read that file, but take care with it!


## Usage ##

See `ljout --help` for supported commands.

    $ ljout -v events backup/
    INFO: Set log level to INFO

    $ ls backup/
    events/              events_lastsync.txt

    $ ls backup/events/ | head -10
    1.json
    10.json
    100.json
    101.json
    102.json
    103.json
    104.json
    105.json
    106.json
    107.json

    $ ljout -v comments backup/
    INFO: Set log level to INFO

    $ ls backup/
    comments/            events/              events_lastsync.txt  usermap.json

    $
