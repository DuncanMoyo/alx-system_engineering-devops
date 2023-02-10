The following scripts can do the following:

su betty :script that switches the current user to the user betty

whoami :script that prints the effective username of the current user

groups :script that prints all the groups the current user is part of

sudo chown betty hello :script that changes the owner of the file hello to the user betty

touch hello :script that creates an empty file called hello

chmod 744 hello :script that adds execute permission to the owner of the file hello

chmod 754 hello :script that adds execute permission to the owner and the group owner, and read permission to other users, to the file hello

chmod ugo+x hello :script that adds execution permission to the owner, the group owner and the other users, to the file hello

chmod 007 hello :gives no permissions to the owner and the group, but all the permissions to other users

chmod 753 hello :shows all rights to the owner, read and execute to the groups and write and execute to the other users

chmod --reference=olleh hello :script that sets the mode of the file hello to be the same as olleh's mode

chmod -R ugo+X . :script that adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users

mkdir -m 751 my_dir :script that creates a directory called my_dir with permissions 751 in the working directory.

chgrp school hello :script that changes the group owner to school for the file hello

chown -R vincent:staff ./ :script that changes the owner to vincent and the group owner to staff for all the files and directories in the working directory.

chown -h vincent:staff _hello :script that changes the owner and the group owner of _hello to vincent and staff respectively

chown --from=guillaume betty hello :script that changes the owner of the file hello to betty only if it is owned by the user guillaume

telnet towel.blinkenlights.nl :script that will play the StarWars IV episode in the terminal
