

alias env-init="python -m venv venv"
alias env-enter="source venv/bin/activate"
alias env-show="pip3 freeze --local"
alias env-install="sudo pip3 install -r" 
​
alias env-help='echo "
env-init= python -m venv venv - initialize env
env-enter=source venv/bin/activate - enter to the env
env-show=pip3 freeze --local - show dependencies in this env
env-install=sudo pip3 inastall -r - install files from file" '