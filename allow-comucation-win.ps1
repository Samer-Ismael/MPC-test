# Allow ICMP (ping) requests through Windows Firewall
New-NetFirewallRule -DisplayName "Allow ICMP" -Protocol ICMPv4 -Action Allow -Enabled True -Direction Inbound

# Allow TCP communication on port 7070
New-NetFirewallRule -DisplayName "Allow TCP 7070" -Protocol TCP -LocalPort 7070 -Action Allow -Enabled True -Direction Inbound

Write-Host "Firewall rules updated successfully to allow ping and TCP communication on port 7070."
