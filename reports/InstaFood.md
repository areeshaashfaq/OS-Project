Subject: Possible exposed secret in your public repository

Hi,

While scanning public repositories for accidentally committed
secrets, an automated check flagged what looks like credential
material in this repository:

  https://github.com/Gourav-Sharma-dev/InstaFood

Flagged locations (secret values are not included):

  - InstaFood.App/bin/Debug/net8.0-android/com.companyname.instafood.app-Signed.apk:2347
    type: Box   preview: Dk*****************************w
    first seen in commit: ef40073c91ba
  - InstaFood.App/bin/Debug/net8.0-ios/iossimulator-x64/libxamarin-dotnet-debug.a:4
    type: Box   preview: VN*****************************t
    first seen in commit: ef40073c91ba
  - InstaFood.App/bin/Debug/net8.0-ios/iossimulator-x64/libxamarin-dotnet-debug.dylib:312
    type: Box   preview: VN*****************************t
    first seen in commit: ef40073c91ba
  - InstaFood.App/bin/Debug/net8.0-ios/iossimulator-x64/libxamarin-dotnet-nativeaot-debug.a:4
    type: Box   preview: VN*****************************t
    first seen in commit: ef40073c91ba
  - InstaFood.App/bin/Debug/net8.0-ios/iossimulator-x64/libxamarin-dotnet-nativeaot.a:6
    type: Box   preview: VN*****************************t
    first seen in commit: ef40073c91ba
  - InstaFood.App/bin/Debug/net8.0-ios/iossimulator-x64/libxamarin-dotnet.a:6
    type: Box   preview: VN*****************************t
    first seen in commit: ef40073c91ba
  - InstaFood.App/bin/Debug/net8.0-ios/iossimulator-x64/libxamarin-dotnet.dylib:174
    type: Box   preview: VN*****************************t
    first seen in commit: ef40073c91ba
  - InstaFood.App/bin/Debug/net8.0-maccatalyst/maccatalyst-x64/libxamarin-dotnet-debug.a:3
    type: Box   preview: VN*****************************t
    first seen in commit: ef40073c91ba
  - InstaFood.App/bin/Debug/net8.0-maccatalyst/maccatalyst-x64/libxamarin-dotnet-debug.dylib:318
    type: Box   preview: VN*****************************t
    first seen in commit: ef40073c91ba
  - InstaFood.App/bin/Debug/net8.0-maccatalyst/maccatalyst-x64/libxamarin-dotnet-nativeaot-debug.a:3
    type: Box   preview: VN*****************************t
    first seen in commit: ef40073c91ba
  - InstaFood.App/bin/Debug/net8.0-maccatalyst/maccatalyst-x64/libxamarin-dotnet-nativeaot.a:6
    type: Box   preview: VN*****************************t
    first seen in commit: ef40073c91ba
  - InstaFood.App/bin/Debug/net8.0-maccatalyst/maccatalyst-x64/libxamarin-dotnet.a:6
    type: Box   preview: VN*****************************t
    first seen in commit: ef40073c91ba
  - InstaFood.App/bin/Debug/net8.0-maccatalyst/maccatalyst-x64/libxamarin-dotnet.dylib:182
    type: Box   preview: VN*****************************t
    first seen in commit: ef40073c91ba
  - InstaFood.App/bin/Debug/net8.0-android/com.companyname.instafood.app-Signed.apk:2347
    type: Box   preview: Dk*****************************w
    first seen in commit: 415981624d28
  - InstaFood.App/bin/Debug/net8.0-android/com.companyname.instafood.app-Signed.apk:2347
    type: Box   preview: Dk*****************************w
    first seen in commit: 52585aedff96
  - InstaFood.App/bin/Debug/net8.0-ios/iossimulator-x64/libxamarin-dotnet-debug.a:4
    type: Box   preview: VN*****************************t
    first seen in commit: 52585aedff96
  - InstaFood.App/bin/Debug/net8.0-ios/iossimulator-x64/libxamarin-dotnet-debug.dylib:312
    type: Box   preview: VN*****************************t
    first seen in commit: 52585aedff96
  - InstaFood.App/bin/Debug/net8.0-ios/iossimulator-x64/libxamarin-dotnet-nativeaot-debug.a:4
    type: Box   preview: VN*****************************t
    first seen in commit: 52585aedff96
  - InstaFood.App/bin/Debug/net8.0-ios/iossimulator-x64/libxamarin-dotnet-nativeaot.a:6
    type: Box   preview: VN*****************************t
    first seen in commit: 52585aedff96
  - InstaFood.App/bin/Debug/net8.0-ios/iossimulator-x64/libxamarin-dotnet.a:6
    type: Box   preview: VN*****************************t
    first seen in commit: 52585aedff96
  - InstaFood.App/bin/Debug/net8.0-ios/iossimulator-x64/libxamarin-dotnet.dylib:174
    type: Box   preview: VN*****************************t
    first seen in commit: 52585aedff96
  - InstaFood.App/bin/Debug/net8.0-maccatalyst/maccatalyst-x64/libxamarin-dotnet-debug.a:3
    type: Box   preview: VN*****************************t
    first seen in commit: 52585aedff96
  - InstaFood.App/bin/Debug/net8.0-maccatalyst/maccatalyst-x64/libxamarin-dotnet-debug.dylib:318
    type: Box   preview: VN*****************************t
    first seen in commit: 52585aedff96
  - InstaFood.App/bin/Debug/net8.0-maccatalyst/maccatalyst-x64/libxamarin-dotnet-nativeaot-debug.a:3
    type: Box   preview: VN*****************************t
    first seen in commit: 52585aedff96
  - InstaFood.App/bin/Debug/net8.0-maccatalyst/maccatalyst-x64/libxamarin-dotnet-nativeaot.a:6
    type: Box   preview: VN*****************************t
    first seen in commit: 52585aedff96
  - InstaFood.App/bin/Debug/net8.0-maccatalyst/maccatalyst-x64/libxamarin-dotnet.a:6
    type: Box   preview: VN*****************************t
    first seen in commit: 52585aedff96
  - InstaFood.App/bin/Debug/net8.0-maccatalyst/maccatalyst-x64/libxamarin-dotnet.dylib:182
    type: Box   preview: VN*****************************t
    first seen in commit: 52585aedff96
  - InstaFood.Shared/Components/Account/LoginComponent.razor:29
    type: CustomRegex   preview: sa*****************************"
    first seen in commit: 52585aedff96
  - InstaFood.App/bin/Debug/net8.0-android/com.companyname.instafood.app-Signed.apk:2353
    type: Box   preview: Dk*****************************w
    first seen in commit: 3ff161f46f51
  - InstaFood.App/bin/Debug/net8.0-android/com.companyname.instafood.app-Signed.apk:2347
    type: Box   preview: Dk*****************************w
    first seen in commit: 22f35ca0003f
  - InstaFood.App/bin/Release/net8.0-ios/iossimulator-x64/libxamarin-dotnet-debug.a:4
    type: Box   preview: VN*****************************t
    first seen in commit: 22f35ca0003f
  - InstaFood.App/bin/Release/net8.0-ios/iossimulator-x64/libxamarin-dotnet-debug.dylib:312
    type: Box   preview: VN*****************************t
    first seen in commit: 22f35ca0003f
  - InstaFood.App/bin/Release/net8.0-ios/iossimulator-x64/libxamarin-dotnet-nativeaot-debug.a:4
    type: Box   preview: VN*****************************t
    first seen in commit: 22f35ca0003f
  - InstaFood.App/bin/Release/net8.0-ios/iossimulator-x64/libxamarin-dotnet-nativeaot.a:6
    type: Box   preview: VN*****************************t
    first seen in commit: 22f35ca0003f
  - InstaFood.App/bin/Release/net8.0-ios/iossimulator-x64/libxamarin-dotnet.a:6
    type: Box   preview: VN*****************************t
    first seen in commit: 22f35ca0003f
  - InstaFood.App/bin/Release/net8.0-ios/iossimulator-x64/libxamarin-dotnet.dylib:174
    type: Box   preview: VN*****************************t
    first seen in commit: 22f35ca0003f
  - InstaFood.App/bin/Release/net8.0-maccatalyst/maccatalyst-arm64/libxamarin-dotnet-debug.a:3
    type: Box   preview: VN*****************************t
    first seen in commit: 22f35ca0003f
  - InstaFood.App/bin/Release/net8.0-maccatalyst/maccatalyst-arm64/libxamarin-dotnet-debug.dylib:875
    type: Box   preview: VN*****************************t
    first seen in commit: 22f35ca0003f
  - InstaFood.App/bin/Release/net8.0-maccatalyst/maccatalyst-arm64/libxamarin-dotnet-nativeaot-debug.a:3
    type: Box   preview: VN*****************************t
    first seen in commit: 22f35ca0003f
  - InstaFood.App/bin/Release/net8.0-maccatalyst/maccatalyst-arm64/libxamarin-dotnet-nativeaot.a:4
    type: Box   preview: VN*****************************t
    first seen in commit: 22f35ca0003f
  - InstaFood.App/bin/Release/net8.0-maccatalyst/maccatalyst-arm64/libxamarin-dotnet.a:4
    type: Box   preview: VN*****************************t
    first seen in commit: 22f35ca0003f
  - InstaFood.App/bin/Release/net8.0-maccatalyst/maccatalyst-arm64/libxamarin-dotnet.dylib:174
    type: Box   preview: VN*****************************t
    first seen in commit: 22f35ca0003f
  - InstaFood.App/bin/Release/net8.0-maccatalyst/maccatalyst-x64/libxamarin-dotnet-debug.a:3
    type: Box   preview: VN*****************************t
    first seen in commit: 22f35ca0003f
  - InstaFood.App/bin/Release/net8.0-maccatalyst/maccatalyst-x64/libxamarin-dotnet-debug.dylib:318
    type: Box   preview: VN*****************************t
    first seen in commit: 22f35ca0003f
  - InstaFood.App/bin/Release/net8.0-maccatalyst/maccatalyst-x64/libxamarin-dotnet-nativeaot-debug.a:3
    type: Box   preview: VN*****************************t
    first seen in commit: 22f35ca0003f
  - InstaFood.App/bin/Release/net8.0-maccatalyst/maccatalyst-x64/libxamarin-dotnet-nativeaot.a:6
    type: Box   preview: VN*****************************t
    first seen in commit: 22f35ca0003f
  - InstaFood.App/bin/Release/net8.0-maccatalyst/maccatalyst-x64/libxamarin-dotnet.a:6
    type: Box   preview: VN*****************************t
    first seen in commit: 22f35ca0003f
  - InstaFood.App/bin/Release/net8.0-maccatalyst/maccatalyst-x64/libxamarin-dotnet.dylib:182
    type: Box   preview: VN*****************************t
    first seen in commit: 22f35ca0003f
  - InstaFood.Server/appsettings.json:11
    type: SQLServer   preview: ku*******f
    first seen in commit: 22f35ca0003f
  - InstaFood.Server/bin/Debug/net8.0/appsettings.json:11
    type: SQLServer   preview: ku*******f
    first seen in commit: 22f35ca0003f
  - InstaFood.App/bin/Debug/net8.0-android/com.companyname.instafood.app-Signed.apk:2347
    type: Box   preview: Dk*****************************w
    first seen in commit: 1cf38efb8759
  - InstaFood.Shared/Components/Account/SignupComponent.razor:50
    type: CustomRegex   preview: ab**************************"
    first seen in commit: 1cf38efb8759
  - InstaFood.WebApp/bin/Debug/net8.0/wwwroot/_framework/InstaFood.Shared.wasm:255
    type: CustomRegex   preview: mx*******************************************************************************************>
    first seen in commit: 1cf38efb8759
  - InstaFood.WebApp/bin/Debug/net8.0/wwwroot/_framework/InstaFood.Shared.wasm:259
    type: CustomRegex   preview: mx****************************************************************************************************************r
    first seen in commit: 1cf38efb8759
  - InstaFood.WebApp/bin/Debug/net8.0/wwwroot/_framework/InstaFood.Shared.wasm.gz:255
    type: CustomRegex   preview: mx*******************************************************************************************>
    first seen in commit: 1cf38efb8759
  - InstaFood.WebApp/bin/Debug/net8.0/wwwroot/_framework/InstaFood.Shared.wasm.gz:259
    type: CustomRegex   preview: mx****************************************************************************************************************r
    first seen in commit: 1cf38efb8759
  - InstaFood.WebApp/obj/Debug/net8.0/compressed/5f332bq5ri.gz:255
    type: CustomRegex   preview: mx*******************************************************************************************>
    first seen in commit: 1cf38efb8759
  - InstaFood.WebApp/obj/Debug/net8.0/compressed/5f332bq5ri.gz:259
    type: CustomRegex   preview: mx****************************************************************************************************************r
    first seen in commit: 1cf38efb8759
  - InstaFood.WebApp/obj/Debug/net8.0/tmp-webcil/InstaFood.Shared.wasm:259
    type: CustomRegex   preview: mx****************************************************************************************************************r
    first seen in commit: 1cf38efb8759
  - InstaFood.WebApp/obj/Debug/net8.0/tmp-webcil/InstaFood.Shared.wasm:255
    type: CustomRegex   preview: mx*******************************************************************************************>
    first seen in commit: 1cf38efb8759
  - InstaFood.WebApp/obj/Debug/net8.0/webcil/InstaFood.Shared.wasm:259
    type: CustomRegex   preview: mx****************************************************************************************************************r
    first seen in commit: 1cf38efb8759
  - InstaFood.WebApp/obj/Debug/net8.0/webcil/InstaFood.Shared.wasm:255
    type: CustomRegex   preview: mx*******************************************************************************************>
    first seen in commit: 1cf38efb8759
  - InstaFood.App/bin/Debug/net8.0-android/com.companyname.instafood.app-Signed.apk:2332
    type: Box   preview: Dk*****************************w
    first seen in commit: f3f7e3019af2
  - InstaFood.WebApp/bin/Debug/net8.0/wwwroot/_framework/InstaFood.Shared.wasm:287
    type: CustomRegex   preview: up******************************************************r
    first seen in commit: f3f7e3019af2
  - InstaFood.WebApp/bin/Debug/net8.0/wwwroot/_framework/InstaFood.Shared.wasm.gz:287
    type: CustomRegex   preview: up******************************************************r
    first seen in commit: f3f7e3019af2
  - InstaFood.WebApp/obj/Debug/net8.0/compressed/rjcchr3h9j.gz:287
    type: CustomRegex   preview: up******************************************************r
    first seen in commit: f3f7e3019af2
  - InstaFood.WebApp/obj/Debug/net8.0/compressed/zvz3itqmbm.gz:19677
    type: Circle   preview: 0f*************************************a
    first seen in commit: f3f7e3019af2
  - InstaFood.WebApp/obj/Debug/net8.0/tmp-webcil/InstaFood.Shared.wasm:287
    type: CustomRegex   preview: up******************************************************r
    first seen in commit: f3f7e3019af2
  - InstaFood.WebApp/obj/Debug/net8.0/webcil/InstaFood.Shared.wasm:287
    type: CustomRegex   preview: up******************************************************r
    first seen in commit: f3f7e3019af2
  - InstaFood.PhoneApp/bin/Debug/net8.0-android/com.companyname.instafood.phoneapp-Signed.apk:2359
    type: Box   preview: Dk*****************************w
    first seen in commit: 37eca6426fb1
  - InstaFood.PhoneApp/bin/Release/net8.0-ios/iossimulator-x64/libxamarin-dotnet-debug.a:4
    type: Box   preview: VN*****************************t
    first seen in commit: 37eca6426fb1
  - InstaFood.PhoneApp/bin/Release/net8.0-ios/iossimulator-x64/libxamarin-dotnet-debug.dylib:312
    type: Box   preview: VN*****************************t
    first seen in commit: 37eca6426fb1
  - InstaFood.PhoneApp/bin/Release/net8.0-ios/iossimulator-x64/libxamarin-dotnet-nativeaot-debug.a:4
    type: Box   preview: VN*****************************t
    first seen in commit: 37eca6426fb1
  - InstaFood.PhoneApp/bin/Release/net8.0-ios/iossimulator-x64/libxamarin-dotnet-nativeaot.a:6
    type: Box   preview: VN*****************************t
    first seen in commit: 37eca6426fb1
  - InstaFood.PhoneApp/bin/Release/net8.0-ios/iossimulator-x64/libxamarin-dotnet.a:6
    type: Box   preview: VN*****************************t
    first seen in commit: 37eca6426fb1
  - InstaFood.PhoneApp/bin/Release/net8.0-ios/iossimulator-x64/libxamarin-dotnet.dylib:174
    type: Box   preview: VN*****************************t
    first seen in commit: 37eca6426fb1
  - InstaFood.PhoneApp/bin/Release/net8.0-maccatalyst/maccatalyst-arm64/libxamarin-dotnet-debug.a:3
    type: Box   preview: VN*****************************t
    first seen in commit: 37eca6426fb1
  - InstaFood.PhoneApp/bin/Release/net8.0-maccatalyst/maccatalyst-arm64/libxamarin-dotnet-debug.dylib:875
    type: Box   preview: VN*****************************t
    first seen in commit: 37eca6426fb1
  - InstaFood.PhoneApp/bin/Release/net8.0-maccatalyst/maccatalyst-arm64/libxamarin-dotnet-nativeaot-debug.a:3
    type: Box   preview: VN*****************************t
    first seen in commit: 37eca6426fb1
  - InstaFood.PhoneApp/bin/Release/net8.0-maccatalyst/maccatalyst-arm64/libxamarin-dotnet-nativeaot.a:4
    type: Box   preview: VN*****************************t
    first seen in commit: 37eca6426fb1
  - InstaFood.PhoneApp/bin/Release/net8.0-maccatalyst/maccatalyst-arm64/libxamarin-dotnet.a:4
    type: Box   preview: VN*****************************t
    first seen in commit: 37eca6426fb1
  - InstaFood.PhoneApp/bin/Release/net8.0-maccatalyst/maccatalyst-arm64/libxamarin-dotnet.dylib:174
    type: Box   preview: VN*****************************t
    first seen in commit: 37eca6426fb1
  - InstaFood.PhoneApp/bin/Release/net8.0-maccatalyst/maccatalyst-x64/libxamarin-dotnet-debug.a:3
    type: Box   preview: VN*****************************t
    first seen in commit: 37eca6426fb1
  - InstaFood.PhoneApp/bin/Release/net8.0-maccatalyst/maccatalyst-x64/libxamarin-dotnet-debug.dylib:318
    type: Box   preview: VN*****************************t
    first seen in commit: 37eca6426fb1
  - InstaFood.PhoneApp/bin/Release/net8.0-maccatalyst/maccatalyst-x64/libxamarin-dotnet-nativeaot-debug.a:3
    type: Box   preview: VN*****************************t
    first seen in commit: 37eca6426fb1
  - InstaFood.PhoneApp/bin/Release/net8.0-maccatalyst/maccatalyst-x64/libxamarin-dotnet-nativeaot.a:6
    type: Box   preview: VN*****************************t
    first seen in commit: 37eca6426fb1
  - InstaFood.PhoneApp/bin/Release/net8.0-maccatalyst/maccatalyst-x64/libxamarin-dotnet.a:6
    type: Box   preview: VN*****************************t
    first seen in commit: 37eca6426fb1
  - InstaFood.PhoneApp/bin/Release/net8.0-maccatalyst/maccatalyst-x64/libxamarin-dotnet.dylib:182
    type: Box   preview: VN*****************************t
    first seen in commit: 37eca6426fb1
  - InstaFood.Server/appsettings.json:11
    type: SQLServer   preview: ku*******f
    first seen in commit: 37eca6426fb1
  - InstaFood.Server/bin/Debug/net8.0/appsettings.json:11
    type: SQLServer   preview: ku*******f
    first seen in commit: 37eca6426fb1
  - InstaFood.Server/bin/Release/net8.0/appsettings.json:11
    type: SQLServer   preview: ku*******f
    first seen in commit: 37eca6426fb1
  - InstaFood.Server/obj/Release/net8.0/PubTmp/Out/appsettings.json:11
    type: SQLServer   preview: ku*******f
    first seen in commit: 37eca6426fb1
  - InstaFood.WebApp/bin/Debug/net8.0/wwwroot/_framework/InstaFood.Shared.wasm:319
    type: CustomRegex   preview: up******************************************************r
    first seen in commit: 37eca6426fb1
  - InstaFood.WebApp/bin/Debug/net8.0/wwwroot/_framework/InstaFood.Shared.wasm.gz:319
    type: CustomRegex   preview: up******************************************************r
    first seen in commit: 37eca6426fb1
  - InstaFood.WebApp/bin/Release/net8.0/wwwroot/_framework/BlazorBootstrap.wasm:19677
    type: Circle   preview: 0f*************************************a
    first seen in commit: 37eca6426fb1
  - InstaFood.WebApp/bin/Release/net8.0/wwwroot/_framework/BlazorBootstrap.wasm.gz:19677
    type: Circle   preview: 0f*************************************a
    first seen in commit: 37eca6426fb1
  - InstaFood.WebApp/bin/Release/net8.0/wwwroot/_framework/InstaFood.Shared.wasm:321
    type: CustomRegex   preview: up******************************************************r
    first seen in commit: 37eca6426fb1
  - InstaFood.WebApp/bin/Release/net8.0/wwwroot/_framework/InstaFood.Shared.wasm.gz:321
    type: CustomRegex   preview: up******************************************************r
    first seen in commit: 37eca6426fb1
  - InstaFood.WebApp/obj/Debug/net8.0/compressed/2854sc7lec.gz:19677
    type: Circle   preview: 0f*************************************a
    first seen in commit: 37eca6426fb1
  - InstaFood.WebApp/obj/Debug/net8.0/compressed/929wbfhl9q.gz:319
    type: CustomRegex   preview: up******************************************************r
    first seen in commit: 37eca6426fb1
  - InstaFood.WebApp/obj/Debug/net8.0/tmp-webcil/InstaFood.Shared.wasm:319
    type: CustomRegex   preview: up******************************************************r
    first seen in commit: 37eca6426fb1
  - InstaFood.WebApp/obj/Debug/net8.0/webcil/InstaFood.Shared.wasm:319
    type: CustomRegex   preview: up******************************************************r
    first seen in commit: 37eca6426fb1
  - InstaFood.WebApp/obj/Release/net8.0/compressed/kfsbh45w9q.gz:321
    type: CustomRegex   preview: up******************************************************r
    first seen in commit: 37eca6426fb1
  - InstaFood.WebApp/obj/Release/net8.0/compressed/qe7zs4qzpq.gz:19677
    type: Circle   preview: 0f*************************************a
    first seen in commit: 37eca6426fb1
  - InstaFood.WebApp/obj/Release/net8.0/tmp-webcil/BlazorBootstrap.wasm:19677
    type: Circle   preview: 0f*************************************a
    first seen in commit: 37eca6426fb1
  - InstaFood.WebApp/obj/Release/net8.0/tmp-webcil/InstaFood.Shared.wasm:321
    type: CustomRegex   preview: up******************************************************r
    first seen in commit: 37eca6426fb1
  - InstaFood.WebApp/obj/Release/net8.0/webcil/BlazorBootstrap.wasm:19677
    type: Circle   preview: 0f*************************************a
    first seen in commit: 37eca6426fb1
  - InstaFood.WebApp/obj/Release/net8.0/webcil/InstaFood.Shared.wasm:321
    type: CustomRegex   preview: up******************************************************r
    first seen in commit: 37eca6426fb1
  - .vs/InstaFood/FileContentIndex/822111d0-eced-4c72-b9f9-54de888e87ab.vsidx:212
    type: Wit   preview: WJ*****************************N
    first seen in commit: 57323bf66a29
  - InstaFood.PhoneApp/Components/Pages/Account/Login.razor:40
    type: CustomRegex   preview: ad*******************************"
    first seen in commit: 57323bf66a29
  - InstaFood.PhoneApp/bin/Debug/net8.0-android/com.companyname.instafood.phoneapp-Signed.apk:2359
    type: Box   preview: Dk*****************************w
    first seen in commit: 57323bf66a29
  - InstaFood.Shared/Components/Account/LoginComponent.razor:37
    type: CustomRegex   preview: ad*****************************"
    first seen in commit: 57323bf66a29
  - InstaFood.WebApp/bin/Debug/net8.0/wwwroot/_framework/BlazorBootstrap.wasm:19677
    type: Circle   preview: 0f*************************************a
    first seen in commit: 57323bf66a29
  - InstaFood.WebApp/bin/Debug/net8.0/wwwroot/_framework/BlazorBootstrap.wasm.gz:19677
    type: Circle   preview: 0f*************************************a
    first seen in commit: 57323bf66a29
  - InstaFood.WebApp/bin/Debug/net8.0/wwwroot/_framework/InstaFood.Shared.wasm:319
    type: CustomRegex   preview: up******************************************************r
    first seen in commit: 57323bf66a29
  - InstaFood.WebApp/bin/Debug/net8.0/wwwroot/_framework/InstaFood.Shared.wasm.gz:319
    type: CustomRegex   preview: up******************************************************r
    first seen in commit: 57323bf66a29
  - InstaFood.WebApp/obj/Debug/net8.0/compressed/5f332bq5ri.gz:319
    type: CustomRegex   preview: up******************************************************r
    first seen in commit: 57323bf66a29
  - InstaFood.WebApp/obj/Debug/net8.0/compressed/klfcs8afz3.gz:19677
    type: Circle   preview: 0f*************************************a
    first seen in commit: 57323bf66a29
  - InstaFood.WebApp/obj/Debug/net8.0/tmp-webcil/BlazorBootstrap.wasm:19677
    type: Circle   preview: 0f*************************************a
    first seen in commit: 57323bf66a29
  - InstaFood.WebApp/obj/Debug/net8.0/tmp-webcil/InstaFood.Shared.wasm:319
    type: CustomRegex   preview: up******************************************************r
    first seen in commit: 57323bf66a29
  - InstaFood.WebApp/obj/Debug/net8.0/webcil/BlazorBootstrap.wasm:19677
    type: Circle   preview: 0f*************************************a
    first seen in commit: 57323bf66a29
  - InstaFood.WebApp/obj/Debug/net8.0/webcil/InstaFood.Shared.wasm:319
    type: CustomRegex   preview: up******************************************************r
    first seen in commit: 57323bf66a29
  - InstaFood.App/bin/Debug/net8.0-ios/iossimulator-x64/libxamarin-dotnet-debug.a:4
    type: Box   preview: VN*****************************t
    first seen in commit: b4e5ab53b55a
  - InstaFood.App/bin/Debug/net8.0-ios/iossimulator-x64/libxamarin-dotnet-debug.dylib:312
    type: Box   preview: VN*****************************t
    first seen in commit: b4e5ab53b55a
  - InstaFood.App/bin/Debug/net8.0-ios/iossimulator-x64/libxamarin-dotnet-nativeaot-debug.a:4
    type: Box   preview: VN*****************************t
    first seen in commit: b4e5ab53b55a
  - InstaFood.App/bin/Debug/net8.0-ios/iossimulator-x64/libxamarin-dotnet-nativeaot.a:6
    type: Box   preview: VN*****************************t
    first seen in commit: b4e5ab53b55a
  - InstaFood.App/bin/Debug/net8.0-ios/iossimulator-x64/libxamarin-dotnet.a:6
    type: Box   preview: VN*****************************t
    first seen in commit: b4e5ab53b55a
  - InstaFood.App/bin/Debug/net8.0-ios/iossimulator-x64/libxamarin-dotnet.dylib:174
    type: Box   preview: VN*****************************t
    first seen in commit: b4e5ab53b55a
  - InstaFood.App/bin/Debug/net8.0-maccatalyst/maccatalyst-x64/libxamarin-dotnet-debug.a:3
    type: Box   preview: VN*****************************t
    first seen in commit: b4e5ab53b55a
  - InstaFood.App/bin/Debug/net8.0-maccatalyst/maccatalyst-x64/libxamarin-dotnet-debug.dylib:318
    type: Box   preview: VN*****************************t
    first seen in commit: b4e5ab53b55a
  - InstaFood.App/bin/Debug/net8.0-maccatalyst/maccatalyst-x64/libxamarin-dotnet-nativeaot-debug.a:3
    type: Box   preview: VN*****************************t
    first seen in commit: b4e5ab53b55a
  - InstaFood.App/bin/Debug/net8.0-maccatalyst/maccatalyst-x64/libxamarin-dotnet-nativeaot.a:6
    type: Box   preview: VN*****************************t
    first seen in commit: b4e5ab53b55a
  - InstaFood.App/bin/Debug/net8.0-maccatalyst/maccatalyst-x64/libxamarin-dotnet.a:6
    type: Box   preview: VN*****************************t
    first seen in commit: b4e5ab53b55a
  - InstaFood.App/bin/Debug/net8.0-maccatalyst/maccatalyst-x64/libxamarin-dotnet.dylib:182
    type: Box   preview: VN*****************************t
    first seen in commit: b4e5ab53b55a

If these are real credentials, treat them as compromised:
  1. Rotate / revoke them now (a committed secret is public forever).
  2. Remove them from the repo and from git history
     (git filter-repo or BFG), then force-push.
  3. Move secrets into environment variables or a secrets manager.

This is an automated courtesy notice. No credentials were tested,
stored, or used.

