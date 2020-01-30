
# hosts manager

easily enable/disable named sections in your hosts file.
useful for switching from "distraction mode" into "non distraction mode". 
your excellence might find other usages.

## Install

    pip install hosts-manager

## Usage

Sudo is needed when not a superuser.

```
sudo hosts disable social  # disable section "social" 
sudo hosts enable news  # enable section "news" 
sudo hosts enable dev  # enable section "dev"
```

hosts manager will comment or uncomment the lines in the respective section.


## Section Definition

your hosts file:

``` 
basics, loopback, etc
.
.
.
# start: social
facebook.com    127.0.0.1
instagram.com    127.0.0.1
# end: social  
# end: would be enough as well! 

others.com      99.99.99.99
