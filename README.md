
# hosts manager

easily enable/disable named sections in your hosts file.
useful for switching from "distraction mode" into "non distraction mode". 
you might find other usages.

## Install

### Using pipx

    pipx install hosts-manager
    # or
    pipx install git+https://github.com/benzkji/hosts-manager.git

## Usage

```
Usage: hosts [OPTIONS] COMMAND SECTIONS...

  enable|disable named sections in your hosts file  
  filename.bak-YYYY-MM-DD--... is created by default

Options:
  --file FILENAME         if not /etc/hosts
  --dry-run               only pretend to
  -v, --verbose           output resulting file at the end
  --backup / --no-backup  default: true
  --help                  Show this message and exit.
```

### Examples

sudo is needed when not a superuser. If you don't use `$(which hosts)`, command
may fail with an importlib.metadata error.

```
sudo $(which hosts) disable social  # disable section "social", let's get distracted! 
sudo $(which hosts) enable news  # enable section "news" 
sudo $(which hosts) enable dev new social  # enable section dev, news and social
```

hosts manager will comment or uncomment the lines in the respective section. It's a good practice to 
first check results with the `--dry-run` option.


## Section Definition

your hosts file:

``` 
basics, loopback, etc
.
register.adobe.com  127.0.0.1
.
.
# start:social
facebook.com    127.0.0.1
instagram.com   127.0.0.1
twitter.com     127.0.0.1
# end  
# or end:social
# or endwhatever
# must start with "# end"

others.com      99.99.99.99
anothers.com    66.66.66.66
