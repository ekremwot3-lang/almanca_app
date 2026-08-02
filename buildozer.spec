[app]
title = Almanca Cekim Testi
package.name = almancacekim
package.domain = org.kullanici

source.dir = .
source.include_exts = py,kv,json
source.include_patterns = data/*.json

version = 0.1
requirements = python3,kivy==2.3.0,kivymd
orientation = portrait
fullscreen = 0

# Android özel ayarları
android.bootstrap = sdl2
android.api = 30
android.minapi = 21
# android.ndk = 23b  <--- BUNU SİL veya YORUM SATIRI YAP
android.ndk_api = 21
android.sdk = 30
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
