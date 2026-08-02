[app]
title = Almanca Cekim Testi
package.name = almancacekim
package.domain = org.kullanici

source.dir = .
source.include_exts = py,kv,json
source.include_patterns = data/*.json

version = 0.1
requirements = python3,kivy==2.3.0,kivymd,pyjnius
orientation = portrait
fullscreen = 0

android.bootstrap = sdl2
android.api = 33
android.minapi = 21
android.ndk_api = 21
android.sdk = 33
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
