Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/araguaci/aspnetboilerplate

Flagged locations (secret values are not included):

  - doc/WebSite/EF-Core-Oracle-Integration.md:43
    type: SQLServer   preview: 12***e
    first seen in commit: 19f1b3f93aa4
  - test/Abp.ZeroCore.Tests/Zero/Sessions/Session_Override_Tests.cs:33
    type: CustomRegex   preview: jo**********************************"
    first seen in commit: f5c85b8094f8
  - test/Abp.ZeroCore.Tests/Zero/Sessions/Session_Override_Tests.cs:34
    type: CustomRegex   preview: JO**********************************"
    first seen in commit: f5c85b8094f8
  - doc/WebSite/Zero/Startup-Template-Core.md:131
    type: SQLServer   preview: 12***e
    first seen in commit: 98472dcf9f38
  - doc/WebSite/Zero/Startup-Template-Angular.md:177
    type: SQLServer   preview: 12***e
    first seen in commit: 98472dcf9f38
  - src/Abp.ZeroCore.NHibernate/Zero/FluentMigrator/Migrations/_20140323_03_CreateAbpUsersTable.cs:44
    type: CustomRegex   preview: ad*********************************************************************************************************"
    first seen in commit: 94f85483dd14
  - src/Abp.ZeroCore.NHibernate/Zero/FluentMigrator/Migrations/_20140323_03_CreateAbpUsersTable.cs:57
    type: CustomRegex   preview: ad*********************************************************************************************************"
    first seen in commit: 94f85483dd14
  - src/Abp.ZeroCore.NHibernate/Zero/FluentMigrator/Migrations/_20140323_03_CreateAbpUsersTable.cs:44
    type: CustomRegex   preview: ad*********************************************************************************************************"
    first seen in commit: e29a196855d8
  - src/Abp.ZeroCore.NHibernate/Zero/FluentMigrator/Migrations/_20140323_03_CreateAbpUsersTable.cs:57
    type: CustomRegex   preview: ad*********************************************************************************************************"
    first seen in commit: e29a196855d8
  - (unknown file):2
    type: CustomRegex   preview: m_***********************************h
    first seen in commit: 142478ea5c18
  - (unknown file):1
    type: CustomRegex   preview: m_***********************************h
    first seen in commit: 142478ea5c18
  - test/Abp.Zero.SampleApp.Tests/Users/UserManager_DeleteUser_Tests.cs:22
    type: CustomRegex   preview: us**********************************************************************************************************,
    first seen in commit: f83b4b4e41c8
  - test/Abp.ZeroCore.Tests/Zero/Users/UserManager_DeleteUser_Tests.cs:22
    type: CustomRegex   preview: us**********************************************************************************************************,
    first seen in commit: f83b4b4e41c8
  - test/Abp.ZeroCore.SampleApp/EntityFramework/Seed/Host/HostRoleAndUserCreator.cs:50
    type: CustomRegex   preview: ad**************************************************************************************************"
    first seen in commit: 4e0d0b9f0cbe
  - (unknown file):2
    type: CustomRegex   preview: is*************************************d
    first seen in commit: 7a86978975b9
  - (unknown file):1
    type: CustomRegex   preview: is*************************************d
    first seen in commit: 7a86978975b9
  - nupkg/create-push_new.ps1:2
    type: NuGetApiKey   preview: oy*******************************************y
    first seen in commit: 2f0169e27eda
  - test/Abp.Zero.SampleApp.Tests/Users/UserManager_SecurityStamp_Tests.cs:90
    type: CustomRegex   preview: te*************************************;
    first seen in commit: b0287f77c123
  - test/Abp.Zero.SampleApp.Tests/Users/UserManager_SecurityStamp_Tests.cs:85
    type: CustomRegex   preview: te*************************************;
    first seen in commit: b0287f77c123
  - test/Abp.Zero.SampleApp.Tests/Users/UserManager_SecurityStamp_Tests.cs:49
    type: CustomRegex   preview: se***************************************;
    first seen in commit: b0287f77c123
  - test/Abp.Zero.SampleApp.Tests/Users/UserAppService_Tests.cs:127
    type: CustomRegex   preview: te*************************************;
    first seen in commit: f55f06e18bbd
  - test/Abp.Zero.SampleApp.Tests/Users/UserAppService_Tests.cs:122
    type: CustomRegex   preview: te*************************************;
    first seen in commit: f55f06e18bbd
  - test/Abp.Zero.SampleApp.Tests/Users/UserAppService_Tests.cs:86
    type: CustomRegex   preview: se***************************************;
    first seen in commit: f55f06e18bbd
  - test/Abp.Zero.SampleApp.Tests/Users/UserAccountSynchronizer_Tests.cs:107
    type: CustomRegex   preview: Te***************************************************************************************************"
    first seen in commit: 0c3cb7ef5398
  - test/Abp.ZeroCore.Tests/Zero/Users/UserManager_Permission_Tests.cs:92
    type: CustomRegex   preview: us**********************************************************************************************************,
    first seen in commit: 05d7d2dc6a74
  - test/Abp.ZeroCore.Tests/Zero/Users/UserManager_AddToRole_Tests.cs:26
    type: CustomRegex   preview: us**********************************************************************************************************,
    first seen in commit: 3c15e2cbc761
  - test/Abp.Zero.SampleApp.Tests/Users/UserRole_Tests.cs:31
    type: CustomRegex   preview: us************************************************************************************************************"
    first seen in commit: b56d661d34b3
  - test/Abp.Zero.SampleApp.Tests/Users/UserRole_Tests.cs:33
    type: CustomRegex   preview: us************************************************************************************************************"
    first seen in commit: eff841b3c10d
  - test/Abp.Zero.SampleApp.Tests/Users/UserManager_Lockout_Tests.cs:132
    type: CustomRegex   preview: us**********************************************************************************************************,
    first seen in commit: e5410cf73904
  - test/Abp.ZeroCore.Tests/Zero/Users/UserManager_Lockout_Tests.cs:47
    type: CustomRegex   preview: us**********************************************************************************************************,
    first seen in commit: 1961d3834996
  - test/Abp.ZeroCore.Tests/Zero/Users/UserManager_Lockout_Tests.cs:69
    type: CustomRegex   preview: us**********************************************************************************************************,
    first seen in commit: e5410cf73904
  - test/Abp.Zero.SampleApp.Tests/Users/UserManager_Lockout_Tests.cs:93
    type: CustomRegex   preview: us**********************************************************************************************************,
    first seen in commit: af38d05c9a12
  - doc/WebSite/Articles/Running-in-Docker-Containers-and-Building-a-Web-Farm-Load-Balancer-Scenario/index.html:118
    type: SQLServer   preview: ***
    first seen in commit: efc1e33eaf60
  - doc/WebSite/EF-Core-PostgreSql-Integration.md:21
    type: SQLServer   preview: ***
    first seen in commit: 1e4659184a91
  - doc/WebSite/MySql-Integration.md:33
    type: SQLServer   preview: ****
    first seen in commit: b5116e8e928f
  - doc/WebSite/Download/EventCloudSource.zip:47
    type: CustomRegex   preview: ad**********************************************************************************************************,
    first seen in commit: 9e4d7ba7bc38
  - doc/WebSite/Download/EventCloudSource.zip:121
    type: Box   preview: qK*****************************e
    first seen in commit: 9e4d7ba7bc38
  - doc/WebSite/Download/EventCloudSource.zip:20931
    type: CustomRegex   preview: ht**********************************0
    first seen in commit: 9e4d7ba7bc38
  - doc/WebSite/Download/EventCloudSource.zip:20931
    type: URI   preview: ht**********************************0
    first seen in commit: 9e4d7ba7bc38
  - doc/WebSite/Download/EventCloudSource.zip:11739
    type: CustomRegex   preview: ht**********************************0
    first seen in commit: 9e4d7ba7bc38
  - doc/WebSite/Download/EventCloudSource.zip:11739
    type: URI   preview: ht**********************************0
    first seen in commit: 9e4d7ba7bc38
  - doc/WebSite/Download/InterceptionDemo.zip:21001
    type: URI   preview: ht**********************************0
    first seen in commit: 7af284fc0589
  - doc/WebSite/Download/InterceptionDemo.zip:21001
    type: CustomRegex   preview: ht**********************************0
    first seen in commit: 7af284fc0589
  - doc/WebSite/Download/InterceptionDemo.zip:11809
    type: URI   preview: ht**********************************0
    first seen in commit: 7af284fc0589
  - doc/WebSite/Download/InterceptionDemo.zip:11809
    type: CustomRegex   preview: ht**********************************0
    first seen in commit: 7af284fc0589
  - doc/WebSite/Articles/dockerize-aspnetboilerplate-projects/index.html:109
    type: SQLServer   preview: ***
    first seen in commit: 059c15f57695
  - doc/WebSite/EF-MySql-Integration.md:32
    type: SQLServer   preview: ***
    first seen in commit: 66556235616a
  - doc/WebSite/Zero/Installation.md:352
    type: CustomRegex   preview: ad*********************************************************************************************************"
    first seen in commit: 66556235616a
  - doc/WebSite/Zero/Installation.md:310
    type: CustomRegex   preview: ad*********************************************************************************************************"
    first seen in commit: 66556235616a
  - test/Abp.ZeroCore.IdentityServer4.Tests/IdentityServer4/DependencyInjection_Tests.cs:29
    type: CustomRegex   preview: ad*******************************;
    first seen in commit: c79092b28073
  - src/Abp.Zero.NHibernate/Zero/FluentMigrator/Migrations/_20140323_03_CreateAbpUsersTable.cs:44
    type: CustomRegex   preview: ad*********************************************************************************************************"
    first seen in commit: bc266e3503fc
  - src/Abp.Zero.NHibernate/Zero/FluentMigrator/Migrations/_20140323_03_CreateAbpUsersTable.cs:57
    type: CustomRegex   preview: ad*********************************************************************************************************"
    first seen in commit: bc266e3503fc
  - test/Abp.Zero.SampleApp.Tests/Users/UserRepository_Tests.cs:28
    type: CustomRegex   preview: ad*********************************************************************************************************"
    first seen in commit: bc266e3503fc
  - test/Abp.Zero.SampleApp.Tests/Users/UserRepository_Tests.cs:15
    type: CustomRegex   preview: ad*********************************************************************************************************"
    first seen in commit: bc266e3503fc
  - test/Abp.Zero.SampleApp.Tests/Users/UserRepository_Tests.cs:23
    type: CustomRegex   preview: ad*********************************************************************************************************"
    first seen in commit: bc266e3503fc
  - test/Abp.Zero.SampleApp.Tests/Users/UserOrganizationUnit_Tests.cs:128
    type: CustomRegex   preview: em********************************************************************************************************"
    first seen in commit: bc266e3503fc
  - test/Abp.Zero.SampleApp.Tests/Users/UserRole_Tests.cs:31
    type: CustomRegex   preview: us************************************************************************************************************"
    first seen in commit: bc266e3503fc
  - test/Abp.Zero.SampleApp.Tests/Users/UserLoginHelper.cs:32
    type: CustomRegex   preview: us************************************************************************************************************"
    first seen in commit: bc266e3503fc
  - test/Abp.Zero.SampleApp.Tests/Users/UserLoginHelper.cs:20
    type: CustomRegex   preview: ow*********************************************************************************************************"
    first seen in commit: bc266e3503fc
  - test/Abp.Zero.SampleApp.Tests/Users/UserLogin_ExternalAuthenticationSources_Test.cs:28
    type: CustomRegex   preview: fa**************************************"
    first seen in commit: bc266e3503fc
  - test/Abp.ZeroCore.SampleApp/EntityFramework/Seed/Host/HostRoleAndUserCreator.cs:47
    type: CustomRegex   preview: ad**************************************************************************************************"
    first seen in commit: bc266e3503fc
  - doc/WebSite/EF-MySql-Integration.html:31
    type: SQLServer   preview: ***
    first seen in commit: 299a1b896e83
  - doc/WebSite/zero/installation.html:297
    type: CustomRegex   preview: ad*********************************************************************************************************"
    first seen in commit: 3e3ec6ba7e52
  - doc/WebSite/zero/installation.html:339
    type: CustomRegex   preview: ad*********************************************************************************************************"
    first seen in commit: 3e3ec6ba7e52
  - doc/WebSite/zero/installation.html:297
    type: CustomRegex   preview: ad*******************************************************************************************************************;
    first seen in commit: 3e3ec6ba7e52
  - doc/WebSiteContents/zero/installation.html:232
    type: CustomRegex   preview: ad*********************************************************************************************************"
    first seen in commit: e0c6d7dbcb6d
  - doc/WebSiteContents/zero/installation.html:274
    type: CustomRegex   preview: ad*********************************************************************************************************"
    first seen in commit: e0c6d7dbcb6d
  - doc/WebSiteContents/zero/installation.html:232
    type: CustomRegex   preview: ad*******************************************************************************************************************;
    first seen in commit: e0c6d7dbcb6d
  - src/Tests/Abp.EntityFramework.Tests/Repositories/EntityFrameworkConventionalRegisterer_Test.cs:34
    type: SQLServer   preview: ***
    first seen in commit: 9a20d1f272de
  - src/Abp/Modules/Zero/Abp.Zero.NHibernate/Zero/DbMigrations/V20140323/_20140323_03_CreateAbpUsersTable.cs:53
    type: CustomRegex   preview: ad*********************************************************************************************************"
    first seen in commit: f49715d687a8
  - src/Abp/Modules/Core/Abp.Modules.Core.Infrastructure.NHibernate/Modules/Core/Data/Migrations/V20140323/_20140323_03_CreateAbpUsersTable.cs:53
    type: CustomRegex   preview: ad*********************************************************************************************************"
    first seen in commit: f205b8c6a745
  - src/Abp/Modules/Core/Abp.Modules.Core.Infrastructure.NHibernate/Data/Migrations/V20130824/_02_CreateAbpUsersTable.cs:24
    type: CustomRegex   preview: hi*************************************************************************************************"
    first seen in commit: d9c847b431fa

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

