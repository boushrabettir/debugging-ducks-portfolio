#/bin/bash

tmux kill-server
cd $HOME/etc/systemd/system
sudo systemctl start myportfolio
sudo systemctl daemon-reload
sudo systemctl enable myportfolio
sudo systemctl restart myportfolio

echo "Flask server has started."
