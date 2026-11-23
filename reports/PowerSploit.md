Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/pentestbr/PowerSploit

Flagged locations (secret values are not included):

  - docs/Recon/Convert-ADName.md:71
    type: CustomRegex   preview: pf*************************************************g
    first seen in commit: 0aaa23cd8656
  - docs/Recon/Convert-ADName.md:67
    type: CustomRegex   preview: pf*************************************************g
    first seen in commit: 0aaa23cd8656
  - docs/Recon/Convert-ADName.md:69
    type: CustomRegex   preview: pf*************************************************g
    first seen in commit: 0aaa23cd8656
  - Recon/PowerView.ps1:1417
    type: CustomRegex   preview: ha***************************************************g
    first seen in commit: 7c32bf69f334
  - Exfiltration/Invoke-Mimikatz.ps1:2729
    type: VirusTotal   preview: be*************************************************************9
    first seen in commit: 926979ad1ace
  - Exfiltration/Invoke-Mimikatz.ps1:2725
    type: VirusTotal   preview: c3*************************************************************8
    first seen in commit: 926979ad1ace
  - Exfiltration/Invoke-Mimikatz.ps1:2727
    type: Box   preview: xV*****************************M
    first seen in commit: 66c93f9317ff
  - Exfiltration/Invoke-Mimikatz.ps1:2724
    type: Box   preview: wA*****************************9
    first seen in commit: 66c93f9317ff
  - Privesc/PowerUp.ps1:2173
    type: CustomRegex   preview: je**************************************************************************************=
    first seen in commit: 83305c5243ab
  - Privesc/PowerUp.ps1:2173
    type: CustomRegex   preview: je***********************************************!
    first seen in commit: 83305c5243ab
  - (unknown file):2
    type: CustomRegex   preview: wi****************************s
    first seen in commit: 6de1d78af875
  - (unknown file):1
    type: CustomRegex   preview: wi****************************s
    first seen in commit: 6de1d78af875
  - Privesc/Get-SiteListPassword.ps1:63
    type: CustomRegex   preview: je***********************************************!
    first seen in commit: 2e6b301170e6
  - Privesc/Get-SiteListPassword.ps1:63
    type: CustomRegex   preview: je**************************************************************************************=
    first seen in commit: 2e6b301170e6
  - Exfiltration/Invoke-Mimikatz.ps1:2726
    type: VirusTotal   preview: 1e*************************************************************0
    first seen in commit: e144be7f292f
  - Exfiltration/Invoke-Mimikatz.ps1:2729
    type: VirusTotal   preview: c2*************************************************************e
    first seen in commit: e144be7f292f
  - Exfiltration/Invoke-Mimikatz.ps1:2732
    type: Box   preview: xW*****************************M
    first seen in commit: e144be7f292f

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

