# Dotfiles
A simple script to start backing up your dotfiles. Intended for Unix-like systems (Mac or Linux).

# How to set it up
1) Create a git repository anywhere (like your home directory and init and connect to remote repo.
2) Copy this file to the git repository.
3) Change the global variables below to match your configuration.
4) Add the files you want copied to the files dict.
5) chmod +x dotfiles.py
6) run `echo "alias dotfiles=<git-path>/dotfiles.py >> ~/.bash_profile` or similar
7) run `dotfiles`