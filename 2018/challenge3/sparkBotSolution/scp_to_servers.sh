#! /bin/bash
# bash script to scp files to multiple machines.

# list of digital ocean servers
declare -a server_ips=('188.166.150.229' '138.68.187.217' '138.68.183.3' '138.68.187.33' '138.68.181.12' '138.68.182.169' '138.68.177.138' '138.68.185.213' '138.68.183.18' '138.68.187.21')
#Files to transfer.
declare -a files=('test_futurama_handler.py' 'test_meaningoflife_handler.py' 'test_repeater_handler.py' 'test_vote_handler.py' 'test_eightball_handler.py' 'test_numbers_handler.py' 'test_trivia_handler.py')

# Passowrd for each server
passwd1="user1"
user1="user1"

#Files to transfer.
files="test_futurama_handler.py" 
path_to_dir="~/backup/sparkBotChallenge/"
port=8080

#Return values.
scp_code=0
ssh_code=0

scp_files(){
    for file in "${files[@]}"
    do
        echo "Transferring file \"$file\" to user \"$user1\"."
        sshpass -p "$passwd1" scp -P "$port" "$file" "$user1"@"$1":"$path_to_dir""$file"
        echo "Transferred \"$file\"."
    done
}


for ip in "${server_ips[@]}" 
do
    scp_files "$ip" 
done
