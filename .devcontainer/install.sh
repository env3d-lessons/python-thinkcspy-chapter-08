#!/bin/bash

echo "Updating..."
sudo apt update

echo "Installing packages..."
sudo apt install -y xterm fluxbox novnc websockify x11vnc xvfb supervisor

echo "Setting up default redirect to vnc.html..."
sudo tee /usr/share/novnc/index.html > /dev/null <<EOF
<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="refresh" content="0; URL='vnc.html'" />
  </head>
  <body>
    <p>Redirecting to <a href="vnc.html?host=localhost&port=6080">vnc.html</a>...</p>
  </body>
</html>
EOF

pip install cs20-image
