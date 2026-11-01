# Lampa для LG webOS

Нативний застосунок-лаунчер [Lampa](http://lampa.mx) для телевізорів LG, для тих, у кого Lampa немає в LG Content Store.

Застосунок відкриває Lampa на весь екран із власною іконкою в меню телевізора. Кнопка «Назад» на пульті передається самій Lampa.

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

```bash
./scripts/build-ipk.sh      # без залежностей, результат у dist/
# або
ares-package app -o dist
```

## Змінити адресу Lampa

Якщо `lampa.mx` недоступний, зміни `LAMPA_URL` у [`app/index.html`](app/index.html), підвищ `version` в [`app/appinfo.json`](app/appinfo.json) і зроби push. Новий реліз збереться автоматично.
