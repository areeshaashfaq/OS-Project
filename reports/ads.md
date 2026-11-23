Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/chicomelo/ads

Flagged locations (secret values are not included):

  - wp-content/languages/plugins/easy-wp-smtp-pt_BR.po:4381
    type: CustomRegex   preview: em******************************s
    first seen in commit: dca08be730f3
  - wp-content/languages/plugins/easy-wp-smtp-pt_BR.po:4381
    type: CustomRegex   preview: em******************************g
    first seen in commit: dca08be730f3
  - wp-content/languages/plugins/easy-wp-smtp-pt_BR.po:4381
    type: CustomRegex   preview: em******************************s
    first seen in commit: dca08be730f3
  - wp-content/languages/plugins/easy-wp-smtp-pt_BR.po:4380
    type: CustomRegex   preview: em*****************************g
    first seen in commit: dca08be730f3
  - wp-content/languages/plugins/easy-wp-smtp-pt_BR.po:4381
    type: CustomRegex   preview: em******************************g
    first seen in commit: dca08be730f3
  - wp-content/languages/plugins/easy-wp-smtp-pt_BR.po:4380
    type: CustomRegex   preview: em*****************************s
    first seen in commit: dca08be730f3
  - wp-content/languages/plugins/easy-wp-smtp-pt_BR.po:4380
    type: CustomRegex   preview: em*****************************s
    first seen in commit: dca08be730f3
  - wp-content/languages/plugins/easy-wp-smtp-pt_BR.po:4380
    type: CustomRegex   preview: em*****************************g
    first seen in commit: dca08be730f3
  - wp-content/languages/plugins/easy-wp-smtp-pt_BR.l10n.php:2
    type: CustomRegex   preview: em******************************s
    first seen in commit: dca08be730f3
  - wp-content/languages/plugins/easy-wp-smtp-pt_BR.l10n.php:2
    type: CustomRegex   preview: em******************************s
    first seen in commit: dca08be730f3
  - wp-content/languages/plugins/easy-wp-smtp-pt_BR.l10n.php:2
    type: CustomRegex   preview: em*****************************g
    first seen in commit: dca08be730f3
  - wp-content/languages/plugins/easy-wp-smtp-pt_BR.l10n.php:2
    type: CustomRegex   preview: em*****************************g
    first seen in commit: dca08be730f3
  - wp-content/languages/plugins/easy-wp-smtp-pt_BR.l10n.php:2
    type: CustomRegex   preview: em******************************g
    first seen in commit: dca08be730f3
  - wp-content/languages/plugins/easy-wp-smtp-pt_BR.l10n.php:2
    type: CustomRegex   preview: em******************************g
    first seen in commit: dca08be730f3
  - wp-content/languages/plugins/easy-wp-smtp-pt_BR.l10n.php:2
    type: CustomRegex   preview: em*****************************s
    first seen in commit: dca08be730f3
  - wp-content/languages/plugins/easy-wp-smtp-pt_BR.l10n.php:2
    type: CustomRegex   preview: em*****************************s
    first seen in commit: dca08be730f3
  - wp-includes/SimplePie/src/Cache/MySQL.php:52
    type: CustomRegex   preview: my*********************************6
    first seen in commit: dca08be730f3
  - wp-content/plugins/duplicator-pro/aws/Guzzle/Http/Message/RequestFactoryInterface.php:98
    type: CustomRegex   preview: ht***************************************)
    first seen in commit: 4651563d9d9d
  - wp-content/plugins/duplicator-pro/aws/Guzzle/Http/Message/RequestFactoryInterface.php:98
    type: URI   preview: ht*************************************0
    first seen in commit: 4651563d9d9d
  - wp-content/plugins/duplicator-pro/classes/net/class.ftp.chunker.php:29
    type: CustomRegex   preview: an*************************************************,
    first seen in commit: 4651563d9d9d
  - wp-content/plugins/duplicator-pro/classes/net/class.ftp.chunker.php:29
    type: CustomRegex   preview: an*************************************;
    first seen in commit: 4651563d9d9d
  - wp-content/plugins/duplicator-pro/classes/net/class.u.s3.php:17
    type: AWS   preview: AK*****************Q
    first seen in commit: 4651563d9d9d
  - wp-content/plugins/duplicator-pro/lib/phpseclib/phpseclib/Crypt/Blowfish.php:30
    type: CustomRegex   preview: te********************************e
    first seen in commit: 4651563d9d9d
  - wp-content/plugins/duplicator-pro/lib/phpseclib/phpseclib/Crypt/Blowfish.php:31
    type: CustomRegex   preview: pe**************************************e
    first seen in commit: 4651563d9d9d
  - wp-content/plugins/duplicator-pro/lib/phpseclib/phpseclib/Crypt/RC4.php:38
    type: CustomRegex   preview: te********************************e
    first seen in commit: 4651563d9d9d
  - wp-content/plugins/duplicator-pro/lib/phpseclib/phpseclib/Crypt/Rijndael.php:62
    type: CustomRegex   preview: te********************************e
    first seen in commit: 4651563d9d9d
  - wp-content/plugins/duplicator-pro/lib/phpseclib/phpseclib/Crypt/Rijndael.php:48
    type: CustomRegex   preview: te********************************e
    first seen in commit: 4651563d9d9d
  - wp-content/updraft/backup_2024-08-05-1803_Positivo_ADS_e2e9c9d3d311-others.zip:2
    type: CustomRegex   preview: em******************************s
    first seen in commit: 4651563d9d9d
  - wp-content/updraft/backup_2024-08-05-1803_Positivo_ADS_e2e9c9d3d311-others.zip:2
    type: CustomRegex   preview: em******************************g
    first seen in commit: 4651563d9d9d
  - wp-content/updraft/backup_2024-08-05-1803_Positivo_ADS_e2e9c9d3d311-others.zip:2
    type: CustomRegex   preview: em******************************s
    first seen in commit: 4651563d9d9d
  - wp-content/updraft/backup_2024-08-05-1803_Positivo_ADS_e2e9c9d3d311-others.zip:2
    type: CustomRegex   preview: em*****************************s
    first seen in commit: 4651563d9d9d
  - wp-content/updraft/backup_2024-08-05-1803_Positivo_ADS_e2e9c9d3d311-others.zip:2
    type: CustomRegex   preview: em*****************************g
    first seen in commit: 4651563d9d9d
  - wp-content/updraft/backup_2024-08-05-1803_Positivo_ADS_e2e9c9d3d311-others.zip:2
    type: CustomRegex   preview: em*****************************s
    first seen in commit: 4651563d9d9d
  - wp-content/updraft/backup_2024-08-05-1803_Positivo_ADS_e2e9c9d3d311-others.zip:2
    type: CustomRegex   preview: em*****************************g
    first seen in commit: 4651563d9d9d
  - wp-content/updraft/backup_2024-08-05-1803_Positivo_ADS_e2e9c9d3d311-others.zip:2
    type: CustomRegex   preview: em******************************g
    first seen in commit: 4651563d9d9d
  - wp-content/updraft/backup_2024-08-05-1803_Positivo_ADS_e2e9c9d3d311-others.zip:3478
    type: CustomRegex   preview: em******************************g
    first seen in commit: 4651563d9d9d
  - wp-content/updraft/backup_2024-08-05-1803_Positivo_ADS_e2e9c9d3d311-others.zip:3477
    type: CustomRegex   preview: em*****************************s
    first seen in commit: 4651563d9d9d
  - wp-content/updraft/backup_2024-08-05-1803_Positivo_ADS_e2e9c9d3d311-others.zip:3477
    type: CustomRegex   preview: em*****************************s
    first seen in commit: 4651563d9d9d
  - wp-content/updraft/backup_2024-08-05-1803_Positivo_ADS_e2e9c9d3d311-others.zip:3478
    type: CustomRegex   preview: em******************************s
    first seen in commit: 4651563d9d9d
  - wp-content/updraft/backup_2024-08-05-1803_Positivo_ADS_e2e9c9d3d311-others.zip:3478
    type: CustomRegex   preview: em******************************s
    first seen in commit: 4651563d9d9d
  - wp-content/updraft/backup_2024-08-05-1803_Positivo_ADS_e2e9c9d3d311-others.zip:3477
    type: CustomRegex   preview: em*****************************g
    first seen in commit: 4651563d9d9d
  - wp-content/updraft/backup_2024-08-05-1803_Positivo_ADS_e2e9c9d3d311-others.zip:3477
    type: CustomRegex   preview: em*****************************g
    first seen in commit: 4651563d9d9d
  - wp-content/updraft/backup_2024-08-05-1803_Positivo_ADS_e2e9c9d3d311-others.zip:3478
    type: CustomRegex   preview: em******************************g
    first seen in commit: 4651563d9d9d
  - wp-content/updraft/backup_2024-08-05-1803_Positivo_ADS_e2e9c9d3d311-plugins.zip:98
    type: CustomRegex   preview: ht***************************************)
    first seen in commit: 4651563d9d9d
  - wp-content/updraft/backup_2024-08-05-1803_Positivo_ADS_e2e9c9d3d311-plugins.zip:98
    type: URI   preview: ht*************************************0
    first seen in commit: 4651563d9d9d
  - wp-content/updraft/backup_2024-08-05-1803_Positivo_ADS_e2e9c9d3d311-plugins.zip:17
    type: AWS   preview: AK*****************Q
    first seen in commit: 4651563d9d9d
  - wp-content/updraft/backup_2024-08-05-1803_Positivo_ADS_e2e9c9d3d311-plugins.zip:29
    type: CustomRegex   preview: an*************************************************,
    first seen in commit: 4651563d9d9d
  - wp-content/updraft/backup_2024-08-05-1803_Positivo_ADS_e2e9c9d3d311-plugins.zip:29
    type: CustomRegex   preview: an*************************************;
    first seen in commit: 4651563d9d9d
  - wp-content/updraft/backup_2024-08-05-1803_Positivo_ADS_e2e9c9d3d311-plugins.zip:30
    type: CustomRegex   preview: te********************************e
    first seen in commit: 4651563d9d9d
  - wp-content/updraft/backup_2024-08-05-1803_Positivo_ADS_e2e9c9d3d311-plugins.zip:31
    type: CustomRegex   preview: pe**************************************e
    first seen in commit: 4651563d9d9d
  - wp-content/updraft/backup_2024-08-05-1803_Positivo_ADS_e2e9c9d3d311-plugins.zip:62
    type: CustomRegex   preview: te********************************e
    first seen in commit: 4651563d9d9d
  - wp-content/updraft/backup_2024-08-05-1803_Positivo_ADS_e2e9c9d3d311-plugins.zip:48
    type: CustomRegex   preview: te********************************e
    first seen in commit: 4651563d9d9d
  - wp-content/updraft/backup_2024-08-05-1803_Positivo_ADS_e2e9c9d3d311-plugins.zip:38
    type: CustomRegex   preview: te********************************e
    first seen in commit: 4651563d9d9d
  - wp-content/updraft/backup_2024-08-05-1803_Positivo_ADS_e2e9c9d3d311-plugins.zip:1390
    type: CustomRegex   preview: em*****************************g
    first seen in commit: 4651563d9d9d
  - wp-content/updraft/backup_2024-08-05-1803_Positivo_ADS_e2e9c9d3d311-plugins.zip:1390
    type: CustomRegex   preview: em*****************************s
    first seen in commit: 4651563d9d9d
  - wp-content/updraft/backup_2024-08-05-1803_Positivo_ADS_e2e9c9d3d311-plugins.zip:1390
    type: CustomRegex   preview: em*****************************g
    first seen in commit: 4651563d9d9d
  - wp-content/updraft/backup_2024-08-05-1803_Positivo_ADS_e2e9c9d3d311-plugins.zip:1390
    type: CustomRegex   preview: em*****************************s
    first seen in commit: 4651563d9d9d
  - wp-content/updraft/backup_2024-08-05-1803_Positivo_ADS_e2e9c9d3d311-plugins.zip:350
    type: CustomRegex   preview: em*****************************s
    first seen in commit: 4651563d9d9d
  - wp-content/updraft/backup_2024-08-05-1803_Positivo_ADS_e2e9c9d3d311-plugins.zip:350
    type: CustomRegex   preview: em*****************************s
    first seen in commit: 4651563d9d9d
  - wp-content/updraft/backup_2024-08-05-1803_Positivo_ADS_e2e9c9d3d311-plugins.zip:350
    type: CustomRegex   preview: em*****************************g
    first seen in commit: 4651563d9d9d
  - wp-content/updraft/backup_2024-08-05-1803_Positivo_ADS_e2e9c9d3d311-plugins.zip:350
    type: CustomRegex   preview: em*****************************g
    first seen in commit: 4651563d9d9d
  - wp-content/updraft/backup_2024-08-05-1803_Positivo_ADS_e2e9c9d3d311-plugins.zip:27
    type: CustomRegex   preview: be***************************************'
    first seen in commit: 4651563d9d9d
  - wp-content/updraft/backup_2024-08-05-1803_Positivo_ADS_e2e9c9d3d311-plugins.zip:27
    type: CustomRegex   preview: be*******************************?
    first seen in commit: 4651563d9d9d
  - wp-content/updraft/backup_2024-08-05-1803_Positivo_ADS_e2e9c9d3d311-plugins.zip:97
    type: CustomRegex   preview: ht***************************************)
    first seen in commit: 4651563d9d9d
  - wp-content/updraft/backup_2024-08-05-1803_Positivo_ADS_e2e9c9d3d311-plugins.zip:97
    type: URI   preview: ht*************************************0
    first seen in commit: 4651563d9d9d
  - wp-content/updraft/backup_2024-08-05-1803_Positivo_ADS_e2e9c9d3d311-plugins.zip:736
    type: CustomRegex   preview: ne******************************)
    first seen in commit: 4651563d9d9d
  - wp-content/updraft/backup_2024-08-05-1803_Positivo_ADS_e2e9c9d3d311-plugins.zip:737
    type: CustomRegex   preview: ne********************************************;
    first seen in commit: 4651563d9d9d
  - wp-content/updraft/backup_2024-08-05-1803_Positivo_ADS_e2e9c9d3d311-plugins.zip:738
    type: CustomRegex   preview: ne********************************************;
    first seen in commit: 4651563d9d9d
  - wp-content/updraft/backup_2024-08-05-1803_Positivo_ADS_e2e9c9d3d311-plugins.zip:740
    type: CustomRegex   preview: ne********************************************;
    first seen in commit: 4651563d9d9d
  - wp-content/updraft/backup_2024-08-05-1803_Positivo_ADS_e2e9c9d3d311-plugins.zip:743
    type: CustomRegex   preview: ne********************************************;
    first seen in commit: 4651563d9d9d
  - wp-content/updraft/backup_2024-08-05-1803_Positivo_ADS_e2e9c9d3d311-plugins.zip:744
    type: CustomRegex   preview: ne******************************)
    first seen in commit: 4651563d9d9d
  - wp-content/updraft/backup_2024-08-05-1803_Positivo_ADS_e2e9c9d3d311-plugins.zip:745
    type: CustomRegex   preview: ne******************************)
    first seen in commit: 4651563d9d9d
  - wp-content/languages/plugins/easy-wp-smtp-pt_BR.po:3477
    type: CustomRegex   preview: em*****************************s
    first seen in commit: f30cafcd8e26
  - wp-content/languages/plugins/easy-wp-smtp-pt_BR.po:3477
    type: CustomRegex   preview: em*****************************s
    first seen in commit: f30cafcd8e26
  - wp-content/languages/plugins/easy-wp-smtp-pt_BR.po:3478
    type: CustomRegex   preview: em******************************g
    first seen in commit: f30cafcd8e26
  - wp-content/languages/plugins/easy-wp-smtp-pt_BR.po:3477
    type: CustomRegex   preview: em*****************************g
    first seen in commit: f30cafcd8e26
  - wp-content/languages/plugins/easy-wp-smtp-pt_BR.po:3478
    type: CustomRegex   preview: em******************************s
    first seen in commit: f30cafcd8e26
  - wp-content/languages/plugins/easy-wp-smtp-pt_BR.po:3478
    type: CustomRegex   preview: em******************************s
    first seen in commit: f30cafcd8e26
  - wp-content/languages/plugins/easy-wp-smtp-pt_BR.po:3477
    type: CustomRegex   preview: em*****************************g
    first seen in commit: f30cafcd8e26
  - wp-content/languages/plugins/easy-wp-smtp-pt_BR.po:3478
    type: CustomRegex   preview: em******************************g
    first seen in commit: f30cafcd8e26
  - wp-content/languages/plugins/easy-wp-smtp-pt_BR.l10n.php:2
    type: CustomRegex   preview: em******************************s
    first seen in commit: f30cafcd8e26
  - wp-content/languages/plugins/easy-wp-smtp-pt_BR.l10n.php:2
    type: CustomRegex   preview: em******************************g
    first seen in commit: f30cafcd8e26
  - wp-content/languages/plugins/easy-wp-smtp-pt_BR.l10n.php:2
    type: CustomRegex   preview: em*****************************g
    first seen in commit: f30cafcd8e26
  - wp-content/languages/plugins/easy-wp-smtp-pt_BR.l10n.php:2
    type: CustomRegex   preview: em*****************************s
    first seen in commit: f30cafcd8e26
  - wp-content/languages/plugins/easy-wp-smtp-pt_BR.l10n.php:2
    type: CustomRegex   preview: em******************************g
    first seen in commit: f30cafcd8e26
  - wp-content/languages/plugins/easy-wp-smtp-pt_BR.l10n.php:2
    type: CustomRegex   preview: em*****************************g
    first seen in commit: f30cafcd8e26
  - wp-content/languages/plugins/easy-wp-smtp-pt_BR.l10n.php:2
    type: CustomRegex   preview: em******************************s
    first seen in commit: f30cafcd8e26
  - wp-content/languages/plugins/easy-wp-smtp-pt_BR.l10n.php:2
    type: CustomRegex   preview: em*****************************s
    first seen in commit: f30cafcd8e26
  - wp-content/plugins/updraftplus/includes/Google/Signer/P12.php:27
    type: CustomRegex   preview: be***************************************'
    first seen in commit: f30cafcd8e26
  - wp-content/plugins/updraftplus/includes/Google/Signer/P12.php:27
    type: CustomRegex   preview: be*******************************?
    first seen in commit: f30cafcd8e26
  - wp-content/plugins/updraftplus/vendor/guzzle/guzzle/src/Guzzle/Http/Message/RequestFactoryInterface.php:97
    type: CustomRegex   preview: ht***************************************)
    first seen in commit: f30cafcd8e26
  - wp-content/plugins/updraftplus/vendor/guzzle/guzzle/src/Guzzle/Http/Message/RequestFactoryInterface.php:97
    type: URI   preview: ht*************************************0
    first seen in commit: f30cafcd8e26
  - wp-content/plugins/updraftplus/vendor/phpseclib/phpseclib/phpseclib/Net/SFTP.php:740
    type: CustomRegex   preview: ne********************************************;
    first seen in commit: f30cafcd8e26
  - wp-content/plugins/updraftplus/vendor/phpseclib/phpseclib/phpseclib/Net/SFTP.php:737
    type: CustomRegex   preview: ne********************************************;
    first seen in commit: f30cafcd8e26
  - wp-content/plugins/updraftplus/vendor/phpseclib/phpseclib/phpseclib/Net/SFTP.php:738
    type: CustomRegex   preview: ne******************************)
    first seen in commit: f30cafcd8e26
  - wp-content/plugins/updraftplus/vendor/phpseclib/phpseclib/phpseclib/Net/SFTP.php:744
    type: CustomRegex   preview: ne********************************************;
    first seen in commit: f30cafcd8e26
  - wp-content/plugins/updraftplus/vendor/phpseclib/phpseclib/phpseclib/Net/SFTP.php:736
    type: CustomRegex   preview: ne******************************)
    first seen in commit: f30cafcd8e26
  - wp-content/plugins/updraftplus/vendor/phpseclib/phpseclib/phpseclib/Net/SFTP.php:743
    type: CustomRegex   preview: ne******************************)
    first seen in commit: f30cafcd8e26
  - wp-content/plugins/updraftplus/vendor/phpseclib/phpseclib/phpseclib/Net/SFTP.php:745
    type: CustomRegex   preview: ne******************************)
    first seen in commit: f30cafcd8e26
  - wp-content/plugins/updraftplus/vendor/phpseclib/phpseclib/phpseclib/Net/SFTP.php:736
    type: CustomRegex   preview: ne********************************************;
    first seen in commit: f30cafcd8e26
  - wp-includes/http.php:544
    type: CustomRegex   preview: ht*************************m
    first seen in commit: f30cafcd8e26
  - wp-includes/http.php:544
    type: URI   preview: ht*************************m
    first seen in commit: f30cafcd8e26
  - wp-admin/includes/class-ftp.php:365
    type: CustomRegex   preview: an*************************;
    first seen in commit: 87e8fbbbb884
  - wp-admin/includes/class-ftp.php:365
    type: CustomRegex   preview: an***********************************;
    first seen in commit: 87e8fbbbb884
  - wp-admin/includes/class-ftp.php:147
    type: CustomRegex   preview: an*********************************;
    first seen in commit: 87e8fbbbb884
  - wp-admin/install.php:419
    type: CustomRegex   preview: us****************************************(
    first seen in commit: 87e8fbbbb884
  - wp-content/languages/plugins/all-in-one-wp-migration-pt_BR.mo:8
    type: CustomRegex   preview: su************************************************k
    first seen in commit: 87e8fbbbb884
  - wp-content/languages/plugins/all-in-one-wp-migration-pt_BR.mo:8
    type: CustomRegex   preview: su*********************************************k
    first seen in commit: 87e8fbbbb884
  - wp-content/plugins/easy-wp-smtp/assets/languages/easy-wp-smtp.pot:1498
    type: CustomRegex   preview: em*****************************s
    first seen in commit: 87e8fbbbb884
  - wp-content/plugins/easy-wp-smtp/assets/languages/easy-wp-smtp.pot:1498
    type: CustomRegex   preview: em*****************************s
    first seen in commit: 87e8fbbbb884
  - wp-content/plugins/easy-wp-smtp/assets/languages/easy-wp-smtp.pot:1498
    type: CustomRegex   preview: em*****************************g
    first seen in commit: 87e8fbbbb884
  - wp-content/plugins/easy-wp-smtp/assets/languages/easy-wp-smtp.pot:1498
    type: CustomRegex   preview: em*****************************g
    first seen in commit: 87e8fbbbb884
  - wp-includes/SimplePie/Cache/MySQL.php:49
    type: CustomRegex   preview: my*********************************6
    first seen in commit: 87e8fbbbb884
  - wp-includes/sodium_compat/composer.json:42
    type: CustomRegex   preview: se***********************************g
    first seen in commit: 87e8fbbbb884
  - wp-includes/sodium_compat/composer.json:46
    type: CustomRegex   preview: je**********************************g
    first seen in commit: 87e8fbbbb884

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

