#!/usr/bin/env python

# 1) Create a git repository anywhere (like your home directory and init and connect to remote repo.
# 2) Add this file to the git repository.
# 3) Change the global variables below to match your configuration.
# 4) Add the files you want copied to the files dict.
# 5) chmod +x dotfiles.py
# 6) run `echo "alias dotfiles=<git-path>/dotfiles.py" >> ~/.bash_profile` or similar
# 7) run `dotfiles`

import os
import shutil
import subprocess
from datetime import datetime

files = {
  '/Users/js': [
    '.zshenv',
    '.zshrc',
    '.bash_profile',
    '.vimrc',
  ]
}

gitPath = '/Users/js/.dotfiles'

def main():
  # check for git folder
  if not os.path.isdir(gitPath):
    print('git directory {} does not exists'.format(gitPath))
    exit(1)
  elif not os.path.isdir(os.path.join(gitPath, '.git')):
    print('directory {} is not a git repository'.format(gitPath))

  global files
  for dir, files in files.items():
    for file in files:
      copyToGit(os.path.join(dir, file))

  subprocess_cmd('cd {} && git add . && git commit -m "{}"; git push'
                 .format(gitPath, datetime.now()))

def copyToGit(src):
  filename = os.path.split(src)[-1]

  try:
    shutil.copy(src, os.path.join(gitPath, filename))
  except shutil.Error as e:
    print('Error: %s' % e)
  except IOError as e:
    print('Error: %s' % e.strerror)

def subprocess_cmd(command):
    process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    print(proc_stdout)

if __name__ == "__main__":
  main()
