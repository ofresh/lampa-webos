# Lampa для LG webOS

Нативний застосунок-лаунчер [Lampa](http://lampa.mx) для телевізорів LG, для тих, у кого Lampa немає в LG Content Store.

Lampa збирається з [вихідного коду](https://github.com/yumata/lampa-source) **без реклами**: без прероликів перед відео, банерів у плеєрі та нагадувань про CUB Premium. Увесь код Lampa лежить усередині `.ipk` і не підвантажується з інтернету, тому реклама не повернеться оновленням із сервера.

Що саме змінено, видно в [`patches/disable_ads.py`](patches/disable_ads.py). Lampa поширюється за ліцензією GPL-2.0, вихідний код є в upstream-репо, а зміни лежать тут.

> Якщо хочеш підтримати автора Lampa, оформи [CUB Premium](https://cub.red/premium): він також прибирає рекламу й відкриває додаткові функції.

## Оновлення Lampa

Відкрий **Actions → Build IPK → Run workflow**. Збереться остання версія Lampa, вийде новий реліз, і його `.ipk` треба встановити поверх старого. Налаштування й закладки збережуться.

## Завантажити

Готовий файл `.ipk` лежить у [**Releases**](../../releases/latest). GitHub Actions збирає його автоматично після кожного push у `main`.

## Встановлення на телевізор

### Спосіб 1: Developer Mode (без root)

1. Зареєструйся на [webostv.developer.lge.com](https://webostv.developer.lge.com) (безкоштовно).
2. На телевізорі встанови з LG Content Store застосунок **Developer Mode**, увійди в акаунт.
3. Увімкни **Dev Mode Status**, а також **Key Server**. Телевізор перезавантажиться.
4. На ПК (Windows/macOS/Linux) встанови [**webOS Dev Manager**](https://github.com/webosbrew/dev-manager-desktop/releases).
5. Додай телевізор (IP можна подивитися в Developer Mode), введи Passphrase з екрана телевізора.
6. На вкладці **Apps** натисни **Install** і вибери завантажений `.ipk`.
7. Lampa з'явиться в списку застосунків.

> Режим розробника діє 50 днів. Продовжити можна кнопкою **Extend** у Developer Mode або в Dev Manager. Якщо термін мине, встановлені застосунки зникнуть.

### Автопродовження Developer Mode

У репо є workflow, який щодня продовжує режим розробника, тому застосунки не зникають.

1. Дізнайся токен телевізора (режим розробника має бути увімкнений):
   - **webOS Dev Manager**: відкрий телевізор → **Info** (або **Device Info**) → там є Dev Mode token / Renew script. Скопіюй значення `sessionToken`.
   - або командою: `ares-novacom --device tv --run "cat /var/luna/preferences/devsecret"`
2. Додай його в GitHub: **Settings → Secrets and variables → Actions → New repository secret**, назва `DEVMODE_TOKEN`.
3. Перейди в **Actions → Renew LG Dev Mode → Run workflow**, щоб перевірити. У Developer Mode на телевізорі таймер має знову показати ~50 днів (999:xx годин).

Далі продовження йде автоматично щодня. Якщо LG відхилить токен, GitHub надішле лист про помилку.

### Спосіб 2: Homebrew Channel (root)

Якщо на телевізорі є root і [Homebrew Channel](https://github.com/webosbrew/webos-homebrew-channel), просто встанови `.ipk` через Dev Manager. Тоді нічого не злітає через 50 днів.

Перевірити, чи можна зробити root на твоїй моделі: [canirootmytv.org](https://canirootmytv.org).

### Спосіб 3: через командний рядок

```bash
npm install -g @webos-tools/cli
ares-setup-device            # додати телевізор
ares-novacom --device tv --getkey   # ввести Passphrase з екрана ТВ
ares-install --device tv com.ofresh.lampa_1.0.0_all.ipk
```

## Самостійна збірка

Дивись кроки в [`.github/workflows/build.yml`](.github/workflows/build.yml): клон `lampa-source`, `patches/disable_ads.py`, `gulp`, потім `ares-package pkg` (або `./scripts/build-ipk.sh pkg`).
