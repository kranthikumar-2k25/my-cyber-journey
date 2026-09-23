# Day 37: The Comeback Protocol

## Bandit Speed-Run (2 Levels)
- Level 16→17: Port scanning with nmap, SSL tunnel with openssl, SSH key extraction
- Level 17→18: File comparison with diff

## Natas Web Hacking (3 Levels)
- Level 6: PHP include file disclosure (secret.inc)
- Level 7: Path Traversal (../../../../etc/natas_webpass/natas8)
- Level 8: Reverse engineering encoded secrets (base64, strrev, bin2hex)

## Cyber Theory
- SQL Injection: The database killer (' OR 1=1 --)
- OWASP Top 10: Broken Access Control (IDOR)

## CCNA
- IPv4 Addressing: Network ID vs Host ID, Subnet Masks
- Episode 9: Home Network (SOHO router, NAT, DHCP, Switch/WAP)

## Python From Scratch
- Lists: Hacker's toolbelt, zero-based indexing
- Code: targets = ["10.0.0.1", "192.168.1.5", "172.16.0.10"]
- Code: print(targets[0]), print(targets[2])

## Key Learnings
- SSL/TLS tunnels require openssl s_client, not regular nc
- SSH keys must be chmod 600 or SSH rejects them
- Path Traversal escapes web directories using ../
- Broken Access Control is OWASP #1 vulnerability
