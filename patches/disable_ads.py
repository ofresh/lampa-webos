#!/usr/bin/env python3
"""
Вимикає рекламу у вихідному коді Lampa (https://github.com/yumata/lampa-source, GPL-2.0).

Що змінюється:
  1. src/interaction/advert/manager.js  - не запускаються рекламні модулі
     (прероли, банери в плеєрі, нагадування «Продовжіть CUB Premium»).
     Залишаються лише сповіщення про прем'єри фільмів.
  2. src/interaction/advert/preroll.js  - Preroll.show() одразу запускає відео без реклами.

Скрипт падає з помилкою, якщо upstream змінив код і патч не застосувався,
щоб не зібрати версію з рекламою непомітно.
"""
import re
import sys
from pathlib import Path

root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")

manager = root / "src/interaction/advert/manager.js"
manager.write_text(
    "import Premiere from './premiere'\n\n"
    "// lampa-webos: рекламні модулі вимкнено\n"
    "function init(){\n"
    "    Premiere.init()\n"
    "}\n\n"
    "export default {\n"
    "    init\n"
    "}\n",
    encoding="utf-8",
)
print("patched", manager)

preroll = root / "src/interaction/advert/preroll.js"
src = preroll.read_text(encoding="utf-8")
pattern = re.compile(r"(function\s+show\s*\(\s*(\w+)\s*,\s*(\w+)\s*\)\s*\{)")
m = pattern.search(src)
if not m:
    sys.exit("ERROR: function show(data, call) не знайдено в preroll.js, патч треба оновити")
cb = m.group(3)
src = src[: m.end()] + f"\n    // lampa-webos: без реклами\n    return {cb}()\n" + src[m.end():]
preroll.write_text(src, encoding="utf-8")
print("patched", preroll)
