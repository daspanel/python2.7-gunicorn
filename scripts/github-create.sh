
#!/bin/bash
 
# This script create a new repo on github.com, then pushes the local repo from the current directory to the new remote.

# It is a fork of https://gist.github.com/robwierzbowski/5430952/.  Some of Rob's lines just didn't work for me, and to fix them I needed to make it more verbose so that a mere electrical engineer could understand it.

# This script gets a username from .gitconfig.  If it indicates that your default username is an empty string, you can set it with
# git config --add github.user YOUR_GIT_USERNAME

# Gather constant vars
PRIVATE_ANSWER=n
if [ "$PRIVATE_ANSWER" == "y" ]; then
  PRIVACYWORD=private
  PRIVATE_TF=true
else
  PRIVACYWORD=public
  PRIVATE_TF=false
fi

echo "Will create a new *$PRIVACYWORD* repo named python2.7-gunicorn"
echo "on github.com in:"
echo "    user account: admindaspanel"
echo "    organization: daspanel"
echo "with this description:"
echo Python 2.7 with Gunicorn app server running inside Docker container using Alpine Linux with S6 Overlay init system.
echo ""
echo "Type 'y' to proceed, any other character to cancel."
read OK
if [ "$OK" != "y" ]; then
  echo "User cancelled"
  exit
fi

# Curl some json to the github API oh damn we so fancy
curl -u admindaspanel https://api.github.com/orgs/daspanel/repos -d \
    "{\"name\": \"python2.7-gunicorn\", \"description\": \"Python 2.7 with Gunicorn app server running inside Docker container using Alpine Linux with S6 Overlay init system.\", \"private\": $PRIVATE_TF}"

