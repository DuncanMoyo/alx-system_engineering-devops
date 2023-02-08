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

ls -al . .. /boot : lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format. {there is no difference between "ls -la" and "ls -al"}

file /tmp/iamafile :prints the type of the file named iamafile

ln -s /bin/ls __ls__ :creates a symbolic file

cp -u *.html ../ :copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory

mv [[:upper]]* /tmp/u :moves all files beginning with an uppercase letter to the directory /tmp/u

rm *~ :deletes all files in the current working directory that end with the character ~

mkdir -p welcome/to/school : creates directories in a tree

ls -amvp :lists all the files and directories of the current directory, separated by commas (,). Directory names should end with a slash (/). Files and directories starting with a dot (.) should be listed. The listing should be alpha ordered, except for the directories . and .. which should be listed at the very beginning. Only digits and letters are used to sort; Digits should come first, assuming that all the files we will test with will have at least one letter or one digit

0 string SCHOOL School data
!:mime School 
These two lines above can be used with the command file to detect School data files. School data files always contain the string SCHOOL at offset 0
