# Assignment_ARP-Spoofing

Name: Killian Munt-Buron & Naji ullah abbasi

## Installation of packages

First, install packages with this : 

`./install.sh`

## Attack

Use two VM (for us, we use Ubuntu VM). One simulates the victim and the other the attacker.

Install the package with the files on two VM.

With this command `ip a `, take these: 
* Target_ip
* Target_mac
* gateway_ip
* attacker_mac

Complete the informations get in the script for the VM attacker.

In the victim VM, launch this command : `arp -a`

We see the arp table before the attack.

Launch the attack with the `script.py` with the attacker VM.

Wait 5 seconds.

After, relaunch `arp -a` to see the changes mades by the attacker.

So see the traffic by the victim, the attacker can use Wireshark (ens33).



