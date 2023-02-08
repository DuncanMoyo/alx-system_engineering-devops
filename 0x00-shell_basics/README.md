List of scripts and what they do:

pwd :prints the absolute path name of the current working directory

ls :displays the contents list of your current directory

cd :changes the working directory to the user's home directory

ls -l :displays current directory on a long format

ls -la :displays current directory contents, including hidden files (starting with .).

ls -lna :displays current directory contents in long format, with user and group IDs displayed numerically and including hidden files (starting with .)

mkdir /tmp/my_first_directory :creates a directory named my_first_directory in the /tmp/ directory.

mv /tmp/betty /tmp/my_first_directory :move the file betty from /tmp/ to /tmp/my_first_directory

rm /tmp/my_first_directory/betty :delete the file betty

rm -r /tmp/my_first_directory :deletes the directory my_first_directory that is in the /tmp directory

cd - :changes the working directory to the previous one

ls -a . .. /boot : lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format.
