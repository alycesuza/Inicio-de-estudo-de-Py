#!/bin/bash

GREEN='\033[32;1m'
YELLOW='\033[33;1m'
RED_BLINK='\033[31;5;1m'
END='\033[m'

trap __Ctrl_c__ INT

__Ctrl_c__() {
    printf "\n${RED_BLINK} [!] Ação abortada!${END}\n\n"
    exit 1
}

if [ "$1" == "" ] || [ "$2" == "" ]
then
	echo " "
	echo -e "${GREEN} [*] COMO USAR: ${END}"
	echo "     Especifique o site e a wordlist como argumento: "
	echo "     Exemplo: $0 site.com.br lista.txt"
else

    echo $1 >> temp_file
    site=$(cat temp_file | sed 's/www\.//')
    rm temp_file

    echo -e "${GREEN} [*] Realizando brute-force ... ${END}"
    echo "" > file.txt 
    i=$(cat $2 | wc -l)
    n=0
    echo -e "${YELLOW} Sente-se e me deixe trabalhar: ${END}"
    for prefix_sub in $(cat $2)
    do
        if [ "$prefix_sub" != "" ]
        then 
            sub_domain=$(host -t A $prefix_sub.$1 | grep -v "NXDOMAIN" | cut -d " " -f1) 
                
            if [ "$sub_domain" != "" ]
            then 
                ip_sub_domain=$(host -t A $sub_domain | cut -d " " -f4)
                echo "$sub_domain : $ip_sub_domain" >> file.txt
            fi
                
        fi
    
        ((n++))
        echo " carregando : [$n]de[$i] "
    done 
    echo " Fim!"
    echo " Obs. : Lista salva em file.txt"
fi