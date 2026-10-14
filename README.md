# Netoff website

Source of the static site for **Netoff**, a Mac app that blocks internet access app by app.

- Live site: https://boxhezibox.github.io/netoff/
- Pages: home, [privacy policy](https://boxhezibox.github.io/netoff/privacy.html), [support](https://boxhezibox.github.io/netoff/support.html) — in English and 简体中文 (`/zh/`).
- Questions or bug reports: [open an issue](https://github.com/boxhezibox/netoff/issues).

The HTML files are generated: edit the copy in `build.py` (and illustrations in `doodles.py`, styles in `assets/style.css`), then run

```sh
python3 build.py
```

No other tooling is needed. GitHub Pages serves the repository root from `main`.
