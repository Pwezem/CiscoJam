#! /bin/bash
# bash script to scp files to multiple machines.

# list of digital ocean servers
declare -a server_ips=('138.68.191.171')
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
