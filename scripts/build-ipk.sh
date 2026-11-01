#!/usr/bin/env bash
# Збирає .ipk без додаткових інструментів (потрібні лише tar, ar, python3).
set -euo pipefail
cd "$(dirname "$0")/.."
SRC="${1:-pkg}"  # папка з готовим застосунком (див. workflow)
ID=$(python3 -c "import json;print(json.load(open('$SRC/appinfo.json'))['id'])")
VER=$(python3 -c "import json;print(json.load(open('$SRC/appinfo.json'))['version'])")
OUT="dist/${ID}_${VER}_all.ipk"
TMP=$(mktemp -d)
mkdir -p "$TMP/data/usr/palm/applications/$ID" "$TMP/control" dist
cp -r "$SRC"/. "$TMP/data/usr/palm/applications/$ID/"
SIZE=$(du -sk "$TMP/data" | cut -f1)
cat > "$TMP/control/control" <<CTRL
Package: $ID
Version: $VER
Section: misc
Priority: optional
Architecture: all
Installed-Size: $SIZE
Maintainer: ofresh
Description: Lampa launcher for LG webOS
webOS-Package-Format-Version: 2
webOS-Packager-Version: x.y.x
CTRL
echo "2.0" > "$TMP/debian-binary"
TAROPTS="--owner=0 --group=0 --numeric-owner --format=gnu"
tar $TAROPTS -czf "$TMP/control.tar.gz" -C "$TMP/control" .
tar $TAROPTS -czf "$TMP/data.tar.gz" -C "$TMP/data" .
rm -f "$OUT"
(cd "$TMP" && ar rc "$OLDPWD/$OUT" debian-binary control.tar.gz data.tar.gz)
rm -rf "$TMP"
echo "Готово: $OUT"
