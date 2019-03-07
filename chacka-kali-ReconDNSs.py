#!/bin/bash

echo "
		 ██████╗██╗  ██╗ █████╗  ██████╗██╗  ██╗ █████╗
		██╔════╝██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔══██╗
		██║     ███████║███████║██║     █████╔╝ ███████║
		██║     ██╔══██║██╔══██║██║     ██╔═██╗ ██╔══██║
		╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗██║  ██║
		 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝
		 Colombia Hack Agent (CHackA)
[...]	Developer:		Jairo A. García H.		[...]
[...]	Version:		1.0.				[...]
[...]	Codename:		'KALI Recon DNSs'			[...]
[...]	Report bugs to:		chacka0101@gmail.com 		[...]
[...]	Homepage:		https://github.com/chacka0101/	[...]
"
PS3='# Enter option or pulse "Enter" to Menu: '
echo " "
echo "##############################################"
echo "#                  MENU                      #"
echo "##############################################"
echo " "
options=("Search DNSs in HTLM" "Quit")
select opt in "${options[@]}"
do
    case $opt in
        "Search DNSs in HTLM Domain")
echo "##############################################"
            echo "Enter Domain:"
            echo "Example: theeaglelabs.com, linux.com, hacking.com"
            echo "FOUND 1:"
            read var_domainvalue
            wget www.$var_domainvalue
            nano index.html |grep "href=" |cut -d"/" -f3 |grep "$var_domainvalue\.com"|cut -d'"' -f1 |sort-u |more
            echo "FOUND 2:"
            grep -o '[A-Za-z0-9_\.-]*\-*$var_domainvalue' index.html |sort-u |more
            ;;
        "Search HOST or IPs in DNSs")
echo "##############################################"
            echo "Enter Domain:"
            echo "Example: theeaglelabs.com, linux.com, hacking.com"
            echo "FOUND 1:"           
            read var_domainvalue
            host www.$var_domainvalue | grep "has address" |cut -d" " -f4 | more
            echo "FOUND 2:"
            host $var_domainvalue|grep "has address" |cut -d" " -f4 |more
            ;;
        "Quit")
echo " "
echo "#################################################"
echo "#                     BYE                       #"
echo "# The Matrix has you, follow the white rabbit.| #"
echo "#################################################"
            break
            ;;
        *) echo invalid option;;
    esac
done
# END
exit