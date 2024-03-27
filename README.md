# How to use it


Place your OVPN certificate in the "/var/snap/simple-openvpn-client/common/" folder
named "client.ovpn" then restart the app. The device will be connected at boot
the command is:

    sudo cp yourfile.ovpn  /var/snap/simple-openvpn-client-gui/common/client.ovpn

# The app needs to have the right interfaces

The command to connect an interface is:

            sudo snap connect <snap>:<plug interface>

So basically:

            sudo snap connect simple-openvpn-client-gui:network-control
            sudo snap connect simple-openvpn-client-gui:firewall-control

The apps starts at boot and connects the VPN server automatically. 

