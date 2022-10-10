# Set title on terminal
# Call script on either chpwd or precmd zsh hook
# Input should be current pwd
# If folder is a git project set the title root to project folder
# Else use current pwd
# Set terminal title


# Check if the current directory is in a Git repository.
function is_git() {
  [[ $(command git rev-parse --is-inside-work-tree 2>/dev/null) == true ]]
}


function is_git2() {
if [ -d .git ] ; then
  echo 'its a git yo'
  exit 0
fi
}

# helloWorld
if is_git
then
  echo "its a git"
else
  echo "no bueno"
fi

is_git
