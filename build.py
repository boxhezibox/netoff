#!/usr/bin/env python3
"""Generates the static Netoff site (English at /, Simplified Chinese at /zh/). Run: python3 build.py"""
import os
import re
import doodles as d

SITE = "https://boxhezibox.github.io/netoff/"
ISSUES = "https://github.com/boxhezibox/netoff/issues"
UPDATED = {"en": "October 15, 2026", "zh": "2026 年 10 月 15 日"}
ROOT = os.path.dirname(os.path.abspath(__file__))

UI = {
    "en": dict(code="en", html_lang="en", other="zh", other_label="简体中文", home="Home", support="Support", privacy="Privacy",
               skip="Skip to content", tagline="Decide which apps get online.",
               footer_note="Netoff is an independent Mac app. Apple, Mac, macOS and the Mac App Store are trademarks of Apple Inc.",
               updated="Last updated"),
    "zh": dict(code="zh", html_lang="zh-Hans", other="en", other_label="English", home="首页", support="技术支持", privacy="隐私政策",
               skip="跳到正文", tagline="让哪些应用联网，由自己决定。",
               footer_note="Netoff 是独立开发的 Mac 应用。Apple、Mac、macOS 和 Mac App Store 是 Apple Inc. 的商标。",
               updated="最后更新"),
}

PAGES = ("index", "privacy", "support")


def path(lang, page):
    prefix = "" if lang == "en" else "zh/"
    return f"{prefix}{page}.html"


def layout(lang, page, title, desc, body):
    u = UI[lang]
    base = "" if lang == "en" else "../"
    other_href = ("zh/" if lang == "en" else "../") + (f"{page}.html" if page != "index" else "index.html")
    other_href = ("zh/" + f"{page}.html") if lang == "en" else ("../" + f"{page}.html")
    here = lambda p: ' aria-current="page"' if p == page else ""
    canon = SITE + path(lang, page).replace("index.html", "")
    alt_en = SITE + path("en", page).replace("index.html", "")
    alt_zh = SITE + path("zh", page).replace("index.html", "")
    return f'''<!doctype html>
<html lang="{u["html_lang"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="color-scheme" content="light dark">
<link rel="canonical" href="{canon}">
<link rel="alternate" hreflang="en" href="{alt_en}">
<link rel="alternate" hreflang="zh-Hans" href="{alt_zh}">
<link rel="alternate" hreflang="x-default" href="{alt_en}">
<link rel="icon" type="image/png" sizes="32x32" href="{base}assets/favicon-32.png">
<link rel="apple-touch-icon" href="{base}assets/icon-180.png">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE}assets/icon-512.png">
<meta name="twitter:card" content="summary">
<link rel="stylesheet" href="{base}assets/style.css">
</head>
<body>
<a class="skip" href="#main">{u["skip"]}</a>
<header class="nav"><div class="wrap">
  <a class="brand" href="{base or "./"}{"" if lang == "en" else "zh/"}" aria-label="Netoff"><img src="{base}assets/icon-180.png" alt="" width="30" height="30"><span>Netoff</span></a>
  <a class="link hide-sm" href="{"" if lang == "en" else ""}{"index.html" if lang == "en" else "index.html"}"{here("index")}>{u["home"]}</a>
  <a class="link" href="support.html"{here("support")}>{u["support"]}</a>
  <a class="link" href="privacy.html"{here("privacy")}>{u["privacy"]}</a>
  <a class="lang" href="{other_href}" hreflang="{"zh-Hans" if lang == "en" else "en"}" lang="{"zh-Hans" if lang == "en" else "en"}">{u["other_label"]}</a>
</div></header>
<main id="main">
{body}
</main>
<footer><div class="wrap">
  <span>© 2026 Netoff · {u["footer_note"]}</span>
  <span class="links"><a href="index.html">{u["home"]}</a><a href="support.html">{u["support"]}</a><a href="privacy.html">{u["privacy"]}</a><a href="{ISSUES}">GitHub</a></span>
</div></footer>
</body>
</html>
'''


# ───────────────────────────── Home ─────────────────────────────

HOME = {
"en": dict(
    title="Netoff — Decide which apps get online",
    desc="Netoff for Mac blocks internet access app by app, or asks you to approve every app and every domain first. Live speeds, a privacy report and a connection log. Nothing leaves your Mac.",
    body=f'''
<div class="wrap hero">
  <span class="pill">🍎 Coming soon to the Mac App Store</span>
  <h1>Decide which apps get <span class="mark">online</span>.</h1>
  <p class="sub">Netoff cuts off the internet for any app on your Mac. Or flip it around: approve every app, and every domain, before it connects.</p>
  <div class="cta"><a class="btn primary" href="#how">See how it works</a><a class="btn ghost" href="support.html">Get support</a></div>
  <div class="art">{d.hero("en")}</div>
</div>

<section id="modes"><div class="wrap">
  <div class="center"><div class="eyebrow">Modes</div><h2 class="title">Three ways to stay in charge</h2>
  <p class="lead">Start relaxed and switch off only what you distrust, or start strict and let in only what you approve. Change modes any time from the menu bar.</p></div>
  <div class="cards">
    <div class="card bg-r"><div class="ic">{d.icon_blocklist()}</div><h3>Blocklist</h3><p>Everything works as usual. You switch off only the apps and addresses you don't trust.</p></div>
    <div class="card bg-b"><div class="ic">{d.icon_apps()}</div><h3>App allowlist</h3><p>Every app asks first. Approve it once, for an hour, or forever — or say no.</p></div>
    <div class="card bg-y"><div class="ic">{d.icon_domains()}</div><h3>Domain &amp; IP allowlist</h3><p>Go further: every unfamiliar domain or IP needs your OK. Or trust an app completely with one click.</p></div>
  </div>
</div></section>

<section><div class="wrap split rev">
  <div class="text">
    <div class="eyebrow">Approvals</div>
    <h2>Asked before it connects.</h2>
    <p>In an allowlist mode, a small window opens in the middle of your screen when an app wants to connect. Choose how long to allow it — once, for an hour, or forever — or say no.</p>
    <ul class="ticks">
      <li>In Domain / IP mode, allow just that address, its whole domain, or every connection from that app</li>
      <li>Requests queue up, and each one counts down for 120 seconds from the moment it is on screen</li>
      <li>No answer? That one connection is denied — no rule is created</li>
    </ul>
  </div>
  <div>{d.prompt("en")}</div>
</div></section>

<section><div class="wrap split">
  <div class="text">
    <div class="eyebrow">Menu bar</div>
    <h2>Always one click away.</h2>
    <p>The menu bar panel lists the apps you have open, with live download and upload speeds and a switch for each. Block one in a second.</p>
    <ul class="ticks">
      <li>Live speeds for your whole Mac and for each app</li>
      <li>Blocked apps are pinned to the top in red, so a switch flipped by accident can't hide</li>
      <li>Change the mode without opening the window</li>
    </ul>
  </div>
  <div>{d.menubar("en")}</div>
</div></section>

<section><div class="wrap split rev">
  <div class="text">
    <div class="eyebrow">Privacy report &amp; log</div>
    <h2>See who's talking to whom.</h2>
    <p>The Privacy Report ranks your apps by how many domains they contact, and domains by how many apps reach them. Tap an app to see every address it talked to over the last 7 days.</p>
    <ul class="ticks">
      <li>Activity shows connections that are open right now, plus the last 5 minutes</li>
      <li>Keep a full connection log for 7, 14 or 30 days — or cap it at 5, 10 or 200&nbsp;MB</li>
      <li>The size cap is a real ceiling: the oldest entries are trimmed so the log never grows past it</li>
      <li>Search it, export it as CSV, clear it whenever you like</li>
    </ul>
  </div>
  <div>{d.report("en")}</div>
</div></section>

<section><div class="wrap">
  <div class="center"><div class="eyebrow">Details</div><h2 class="title">Small things, done carefully</h2></div>
  <div class="grid6">
    <div><div class="emo">⚡</div><h3>Live speeds</h3><p>Download and upload speed for your Mac and for every app, updated every second.</p></div>
    <div><div class="emo">📌</div><h3>Nothing hides</h3><p>Blocked apps and blocked domains are always pinned to the top of their lists.</p></div>
    <div><div class="emo">🔔</div><h3>One gentle heads-up</h3><p>If a blocked app keeps trying to connect, you get a single notification. Turn it off any time.</p></div>
    <div><div class="emo">🪟</div><h3>Prompts that wait</h3><p>Approval requests open in the middle of the screen and queue up. The countdown starts only once a request is on screen.</p></div>
    <div><div class="emo">🌍</div><h3>Speaks your language</h3><p>English, 简体中文, 繁體中文, 日本語, 한국어, Français and Español.</p></div>
    <div><div class="emo">🌗</div><h3>Looks right everywhere</h3><p>Light and dark mode. Green when protected, soft green when the window is in the background, gray when protection is off.</p></div>
  </div>
</div></section>

<section><div class="wrap"><div class="band bg-g">
  <div>
    <div class="eyebrow">Private by design</div>
    <h2>Nothing leaves your Mac.</h2>
    <p>No account. No analytics. No ads. No servers. Netoff contains no code that sends data anywhere — it only watches what your other apps do. Your rules, logs and reports live on your Mac and nowhere else.</p>
    <a class="btn primary" href="privacy.html">Read the privacy policy</a>
  </div>
  <div>{d.local("en")}</div>
</div></div></section>

<section id="how"><div class="wrap">
  <div class="center"><div class="eyebrow">Getting started</div><h2 class="title">Up and running in a minute</h2></div>
  <div class="steps">
    <div class="step"><h3>Turn on protection</h3><p>Open Netoff and switch protection on. It installs a small network extension.</p></div>
    <div class="step"><h3>Allow the extension</h3><p>macOS asks for your approval once: System Settings › General › Login Items &amp; Extensions › Network Extensions.</p></div>
    <div class="step"><h3>Pick a mode</h3><p>Choose blocklist or one of the allowlists. Everything else is optional.</p></div>
  </div>
  <p class="note">Netoff uses Apple's Network Extension framework — a content filter that macOS itself runs and supervises. It looks at which app is connecting to where. It doesn't read your web pages, messages or files. Requires macOS 15 or later.</p>
</div></section>

<section><div class="wrap" style="max-width:820px">
  <div class="center" style="margin-bottom:28px"><div class="eyebrow">Questions</div><h2 class="title">Good to know</h2></div>
  <details><summary>Can Netoff see my passwords or messages?</summary><div class="a"><p>No. Netoff sees which app opens a connection, to which domain or IP address, on which port. It does not read the contents of your traffic. The only data it looks inside is plain DNS answers, in memory, to put a name next to an IP address.</p></div></details>
  <details><summary>What happens when Netoff isn't running?</summary><div class="a"><p>The filter lives in a system extension, so your rules keep working even when the Netoff window is closed. Connections that would need your approval are allowed or blocked — your choice in Settings — until Netoff is open again.</p></div></details>
  <details><summary>Is it a firewall or an antivirus?</summary><div class="a"><p>No. Netoff controls outgoing connections app by app. It isn't an inbound firewall and it doesn't scan for malware.</p></div></details>
  <details><summary>Where is my data stored?</summary><div class="a"><p>Only on your Mac. Rules, the privacy report and the connection log never leave it. See the <a href="privacy.html">privacy policy</a> for details, including how to delete everything.</p></div></details>
  <details><summary>How do I uninstall it?</summary><div class="a"><p>In Netoff, open Settings and choose “Uninstall Extension…”, then move the app to the Trash. Step by step on the <a href="support.html#uninstall">support page</a>.</p></div></details>
</div></section>

<section style="padding-top:20px"><div class="wrap center">
  <h2 class="title">Questions? Happy to help.</h2>
  <p class="lead">Setup, bugs or ideas — the support page has answers, and a place to ask.</p>
  <p style="margin-top:26px"><a class="btn primary" href="support.html">Go to support</a></p>
  {d.footer_squiggle()}
</div></section>
'''),
"zh": dict(
    title="Netoff — 让哪些应用联网，由自己决定",
    desc="Netoff 是一款 Mac 应用：按应用切断网络访问，或要求每个应用、每个域名联网前先获得批准。实时网速、隐私报告和连接日志。数据不会离开这台 Mac。",
    body=f'''
<div class="wrap hero">
  <span class="pill">🍎 即将登陆 Mac App Store</span>
  <h1><span class="nb">让哪些应用<span class="mark">联网</span>，</span><span class="nb">由自己决定。</span></h1>
  <p class="sub">Netoff 可以按应用切断 Mac 的网络访问；也可以反过来，让每个应用、每个域名在联网前都先获得批准。</p>
  <div class="cta"><a class="btn primary" href="#how">了解工作方式</a><a class="btn ghost" href="support.html">获取支持</a></div>
  <div class="art">{d.hero("zh")}</div>
</div>

<section id="modes"><div class="wrap">
  <div class="center"><div class="eyebrow">模式</div><h2 class="title">三种方式，掌控全局</h2>
  <p class="lead">可以先宽松，只关掉不信任的；也可以先严格，只放行批准的。随时可在菜单栏切换模式。</p></div>
  <div class="cards">
    <div class="card bg-r"><div class="ic">{d.icon_blocklist()}</div><h3>黑名单</h3><p>一切照常运行，只关掉不信任的应用和地址。</p></div>
    <div class="card bg-b"><div class="ic">{d.icon_apps()}</div><h3>应用白名单</h3><p>每个应用联网前都要先问一声。可以允许一次、一小时或永久，也可以拒绝。</p></div>
    <div class="card bg-y"><div class="ic">{d.icon_domains()}</div><h3>域名 / IP 白名单</h3><p>更进一步：每个陌生的域名或 IP 被访问前都需要批准。对信任的应用，一键放行它的全部连接。</p></div>
  </div>
</div></section>

<section><div class="wrap split rev">
  <div class="text">
    <div class="eyebrow">批准</div>
    <h2>联网之前，先问一声。</h2>
    <p>在白名单模式下，应用想要联网时，屏幕中央会弹出一个小窗口。可以选择允许一次、一小时或永久，也可以拒绝。</p>
    <ul class="ticks">
      <li>域名 / IP 模式下，可只允许该地址、允许整个域名，或放行该应用的全部连接</li>
      <li>请求依次排队，每个请求从显示在屏幕上起倒计时 120 秒</li>
      <li>没有回应则只拒绝这一次连接，不会生成规则</li>
    </ul>
  </div>
  <div>{d.prompt("zh")}</div>
</div></section>

<section><div class="wrap split">
  <div class="text">
    <div class="eyebrow">菜单栏</div>
    <h2>随时一键可达。</h2>
    <p>菜单栏面板列出当前打开的应用，实时显示下载和上传速度，每个应用一个开关。一秒钟就能断开某个应用的网络。</p>
    <ul class="ticks">
      <li>整台 Mac 和每个应用的实时网速</li>
      <li>被禁止的应用以红色置顶显示，误关的开关不会被遗忘</li>
      <li>不用打开主窗口，就能切换模式</li>
    </ul>
  </div>
  <div>{d.menubar("zh")}</div>
</div></section>

<section><div class="wrap split rev">
  <div class="text">
    <div class="eyebrow">隐私报告与日志</div>
    <h2>看清谁在和谁通信。</h2>
    <p>隐私报告按联系的域名数量给应用排名，也按联系它的应用数量给域名排名。点开任一应用，可查看它过去 7 天联系过的每个地址。</p>
    <ul class="ticks">
      <li>“网络活动”显示当前打开的连接，以及最近 5 分钟内的连接</li>
      <li>完整的连接日志可保留 7、14 或 30 天，也可限制在 5、10 或 200&nbsp;MB 以内</li>
      <li>大小上限是硬上限：Netoff 会删除最旧的记录，日志永远不会超过它</li>
      <li>可搜索、导出为 CSV，也可随时清除</li>
    </ul>
  </div>
  <div>{d.report("zh")}</div>
</div></section>

<section><div class="wrap">
  <div class="center"><div class="eyebrow">细节</div><h2 class="title">小地方，认真做</h2></div>
  <div class="grid6">
    <div><div class="emo">⚡</div><h3>实时网速</h3><p>整台 Mac 和每个应用的下载、上传速度，每秒更新。</p></div>
    <div><div class="emo">📌</div><h3>不会被遗漏</h3><p>被禁止的应用和域名，始终置顶显示在各自的列表里。</p></div>
    <div><div class="emo">🔔</div><h3>只提醒一次</h3><p>被禁止的应用频繁尝试联网时，只发送一条通知。可随时关闭。</p></div>
    <div><div class="emo">🪟</div><h3>等待批准的窗口</h3><p>批准请求出现在屏幕中央并依次排队，倒计时从请求显示在屏幕上时才开始。</p></div>
    <div><div class="emo">🌍</div><h3>多语言</h3><p>English、简体中文、繁體中文、日本語、한국어、Français、Español。</p></div>
    <div><div class="emo">🌗</div><h3>各种状态都清晰</h3><p>支持浅色和深色模式。保护开启为绿色，窗口在后台时为柔和的绿色，保护关闭时为灰色。</p></div>
  </div>
</div></section>

<section><div class="wrap"><div class="band bg-g">
  <div>
    <div class="eyebrow">隐私优先</div>
    <h2>数据不会离开这台 Mac。</h2>
    <p>没有账号，没有统计分析，没有广告，没有服务器。Netoff 不含任何向外发送数据的代码，只观察其他应用的联网行为。规则、日志和报告只保存在这台 Mac 上。</p>
    <a class="btn primary" href="privacy.html">阅读隐私政策</a>
  </div>
  <div>{d.local("zh")}</div>
</div></div></section>

<section id="how"><div class="wrap">
  <div class="center"><div class="eyebrow">开始使用</div><h2 class="title">一分钟即可上手</h2></div>
  <div class="steps">
    <div class="step"><h3>开启保护</h3><p>打开 Netoff 并开启保护，它会安装一个小型网络扩展。</p></div>
    <div class="step"><h3>允许网络扩展</h3><p>macOS 会请求一次批准：系统设置 › 通用 › 登录项与扩展 › 网络扩展。</p></div>
    <div class="step"><h3>选择模式</h3><p>选择黑名单或其中一种白名单即可，其余设置均为可选。</p></div>
  </div>
  <p class="note">Netoff 使用 Apple 的网络扩展（Network Extension）框架，这是由 macOS 自身运行并监管的内容过滤器。它只关注哪个应用在连接哪里，不会读取网页、消息或文件的内容。需要 macOS 15 或更高版本。</p>
</div></section>

<section><div class="wrap" style="max-width:820px">
  <div class="center" style="margin-bottom:28px"><div class="eyebrow">常见问题</div><h2 class="title">先了解一下</h2></div>
  <details><summary>Netoff 能看到密码或消息吗？</summary><div class="a"><p>不能。Netoff 只能看到哪个应用向哪个域名或 IP 地址、哪个端口发起了连接，不会读取流量内容。唯一会查看内容的是未加密的 DNS 应答，仅在内存中处理，用来在 IP 地址旁标注域名。</p></div></details>
  <details><summary>Netoff 没有运行时会怎样？</summary><div class="a"><p>过滤器运行在系统扩展中，所以即使关闭 Netoff 窗口，规则依然生效。需要批准的连接会按设置中的选择被允许或阻止，直到 Netoff 重新打开。</p></div></details>
  <details><summary>它是防火墙或杀毒软件吗？</summary><div class="a"><p>不是。Netoff 按应用控制出站连接，不是入站防火墙，也不扫描恶意软件。</p></div></details>
  <details><summary>数据保存在哪里？</summary><div class="a"><p>只保存在这台 Mac 上。规则、隐私报告和连接日志不会离开它。详情及如何删除全部数据，请见<a href="privacy.html">隐私政策</a>。</p></div></details>
  <details><summary>如何卸载？</summary><div class="a"><p>在 Netoff 的设置中选择“卸载扩展…”，然后把应用移到废纸篓。详细步骤见<a href="support.html#uninstall">技术支持页</a>。</p></div></details>
</div></section>

<section style="padding-top:20px"><div class="wrap center">
  <h2 class="title">有疑问？乐意帮忙。</h2>
  <p class="lead">设置、问题反馈或建议，技术支持页有解答，也有提问的地方。</p>
  <p style="margin-top:26px"><a class="btn primary" href="support.html">前往技术支持</a></p>
  {d.footer_squiggle()}
</div></section>
'''),
}

# ───────────────────────────── Privacy ─────────────────────────────

PRIVACY = {
"en": dict(
    title="Privacy Policy — Netoff",
    desc="Netoff doesn't collect, send or share any data. Everything it records stays on your Mac.",
    body=f'''
<div class="wrap doc">
  <div class="head"><div class="eyebrow">Privacy Policy</div><h1>Nothing leaves your Mac.</h1>
  <p class="meta">Last updated: {UPDATED["en"]}</p></div>
  <div class="summary"><p><strong>In short:</strong> Netoff does not collect, transmit, sell or share any personal data. There is no account, no analytics, no advertising and no server. The app contains no code that sends data anywhere. Everything Netoff records stays on your Mac, and you can delete it at any time.</p></div>
  <nav class="toc" aria-label="Contents"><a href="#processes">What Netoff looks at</a><a href="#stored">What is stored</a><a href="#sharing">Sharing</a><a href="#permissions">Permissions</a><a href="#delete">Deleting data</a><a href="#contact">Contact</a></nav>
  <article>
    <h2 id="processes">What Netoff looks at</h2>
    <p>To do its job — letting you allow or block internet access app by app — Netoff's network extension is told by macOS about every network connection that a program on your Mac opens. For each connection it handles:</p>
    <ul>
      <li>the name and location of the program that opened it;</li>
      <li>the destination domain name or IP address, the port and the protocol (TCP or UDP);</li>
      <li>whether the connection was allowed or blocked, and why;</li>
      <li>how many bytes were sent and received, to show speeds.</li>
    </ul>
    <p>Netoff does <strong>not</strong> read, record or modify the contents of your traffic — not web pages, messages, passwords or files. The one exception is plain (unencrypted) DNS answers: Netoff reads these in memory, only to show a domain name next to an IP address. They are not saved.</p>

    <h2 id="stored">What is stored, and where</h2>
    <p>Everything below is stored only on your Mac, in Netoff's own storage. None of it is uploaded.</p>
    <table>
      <tr><th>Data</th><th>Why</th><th>How long</th></tr>
      <tr><td>Your rules: blocked and allowed apps, domains and IP addresses, and your settings</td><td>To enforce your choices</td><td>Until you change or reset them</td></tr>
      <tr><td>Activity list (open connections and the last few minutes)</td><td>To show what is happening now</td><td>Kept in memory only; gone when you quit Netoff</td></tr>
      <tr><td>Privacy report: which apps contacted which domains, with counts</td><td>To show the Privacy Report</td><td>7 days, then removed automatically</td></tr>
      <tr><td>Connection log: one entry per connection</td><td>To let you review past connections</td><td>As you choose: off, 7, 14 or 30 days, or a size cap of 5, 10 or 200&nbsp;MB. The size cap is a hard limit — the oldest entries are removed so the log never exceeds it. Default: 7 days</td></tr>
      <tr><td>A few preferences, such as the notification setting</td><td>To remember your choices</td><td>Until you change them</td></tr>
    </table>
    <p>If you use “Export…”, Netoff writes a CSV file where you tell it to. That file is yours; Netoff doesn't track or upload it.</p>

    <h2 id="sharing">Sharing and third parties</h2>
    <p>Netoff doesn't share data with anyone, because it doesn't send data anywhere. It has no third-party software development kits, no advertising, no analytics and no crash reporting of its own.</p>
    <p>If you get Netoff from the Mac App Store, Apple may collect information about downloads and, if you've allowed it in your system settings, usage and crash data shared with developers. That is governed by <a href="https://www.apple.com/legal/privacy/">Apple's privacy policy</a>. Netoff does not receive personal data from it.</p>

    <h2 id="permissions">Permissions Netoff asks for</h2>
    <ul>
      <li><strong>Network extension (content filter).</strong> Required. This is how macOS lets Netoff see and control connections. You approve it in System Settings.</li>
      <li><strong>Notifications.</strong> Optional. Used for a single heads-up when a blocked app keeps trying to connect. You can turn it off in Netoff's Settings.</li>
      <li><strong>Open at login.</strong> Optional. Off unless you turn it on.</li>
    </ul>

    <h2 id="delete">Deleting your data</h2>
    <ul>
      <li><strong>Connection log:</strong> Privacy Report › Connection Log › Clear Log. Or set it to “Don’t Keep a Log”.</li>
      <li><strong>Privacy report:</strong> Privacy Report › Clear Report.</li>
      <li><strong>Activity list:</strong> Activity › Clear, or quit Netoff.</li>
      <li><strong>Rules:</strong> Settings › Reset All Rules…</li>
      <li><strong>Everything:</strong> do the above, then choose Settings › Uninstall Extension… and move Netoff to the Trash.</li>
    </ul>

    <h2>Children</h2>
    <p>Netoff doesn't collect personal data from anyone, including children.</p>

    <h2>Changes to this policy</h2>
    <p>If this policy changes, the new version will be posted on this page with a new “last updated” date. Because Netoff collects nothing, we don't expect that to change what the app does with your data.</p>

    <h2 id="contact">Contact</h2>
    <p>Questions about privacy? Open an issue on <a href="{ISSUES}">GitHub</a> — please don't include private information in it — or see the <a href="support.html">support page</a>.</p>
  </article>
</div>'''),
"zh": dict(
    title="隐私政策 — Netoff",
    desc="Netoff 不收集、不发送、不分享任何数据。它记录的一切都只保存在这台 Mac 上。",
    body=f'''
<div class="wrap doc">
  <div class="head"><div class="eyebrow">隐私政策</div><h1>数据不会离开这台 Mac。</h1>
  <p class="meta">最后更新：{UPDATED["zh"]}</p></div>
  <div class="summary"><p><strong>简而言之：</strong>Netoff 不收集、不传输、不出售、不分享任何个人数据。没有账号，没有统计分析，没有广告，也没有服务器。应用中不含任何向外发送数据的代码。Netoff 记录的一切都只保存在这台 Mac 上，随时可以删除。</p></div>
  <nav class="toc" aria-label="目录"><a href="#processes">Netoff 会查看什么</a><a href="#stored">保存了什么</a><a href="#sharing">数据分享</a><a href="#permissions">所需权限</a><a href="#delete">删除数据</a><a href="#contact">联系方式</a></nav>
  <article>
    <h2 id="processes">Netoff 会查看什么</h2>
    <p>为了实现“按应用允许或阻止互联网访问”，macOS 会把这台 Mac 上每个程序发起的网络连接告知 Netoff 的网络扩展。对于每个连接，Netoff 会处理：</p>
    <ul>
      <li>发起连接的程序的名称和位置；</li>
      <li>目标域名或 IP 地址、端口和协议（TCP 或 UDP）；</li>
      <li>连接被允许还是被阻止，以及原因；</li>
      <li>收发的字节数，用于显示网速。</li>
    </ul>
    <p>Netoff <strong>不会</strong>读取、记录或修改流量内容，包括网页、消息、密码和文件。唯一的例外是未加密的 DNS 应答：Netoff 只在内存中读取它们，用来在 IP 地址旁显示域名，不会保存。</p>

    <h2 id="stored">保存了什么，保存在哪里</h2>
    <p>以下内容全部只保存在这台 Mac 上 Netoff 自己的存储空间中，不会上传。</p>
    <table>
      <tr><th>数据</th><th>用途</th><th>保留时间</th></tr>
      <tr><td>规则：被阻止和被允许的应用、域名、IP 地址，以及设置</td><td>执行所做的选择</td><td>直到修改或重置</td></tr>
      <tr><td>网络活动列表（当前连接和最近几分钟）</td><td>显示此刻的情况</td><td>仅保存在内存中，退出 Netoff 后消失</td></tr>
      <tr><td>隐私报告：哪些应用联系了哪些域名及次数</td><td>用于显示隐私报告</td><td>7 天，之后自动删除</td></tr>
      <tr><td>连接日志：每个连接一条记录</td><td>方便回顾过去的连接</td><td>由用户选择：关闭、7、14 或 30 天，或限制为 5、10、200&nbsp;MB。大小上限是硬上限，会删除最旧的记录以确保日志不超过它。默认 7 天</td></tr>
      <tr><td>少量偏好设置，例如通知开关</td><td>记住所做的选择</td><td>直到修改</td></tr>
    </table>
    <p>如果使用“导出…”，Netoff 会把 CSV 文件写到指定的位置。该文件归用户所有，Netoff 不会追踪或上传。</p>

    <h2 id="sharing">数据分享与第三方</h2>
    <p>Netoff 不与任何人分享数据，因为它不会向任何地方发送数据。它没有第三方 SDK，没有广告，没有统计分析，也没有自己的崩溃报告。</p>
    <p>如果通过 Mac App Store 获取 Netoff，Apple 可能会收集下载信息；如果在系统设置中允许，还会向开发者共享使用情况和崩溃数据，这受 <a href="https://www.apple.com/legal/privacy/">Apple 隐私政策</a>约束。Netoff 不会从中获得个人数据。</p>

    <h2 id="permissions">所需权限</h2>
    <ul>
      <li><strong>网络扩展（内容过滤器）。</strong>必需。macOS 通过它让 Netoff 查看并控制连接，需要在系统设置中批准。</li>
      <li><strong>通知。</strong>可选。用于在被阻止的应用频繁尝试联网时发送一次提醒，可在 Netoff 设置中关闭。</li>
      <li><strong>登录时打开。</strong>可选。除非主动开启，否则保持关闭。</li>
    </ul>

    <h2 id="delete">删除数据</h2>
    <ul>
      <li><strong>连接日志：</strong>隐私报告 › 连接日志 › 清除日志；或设为“不记录日志”。</li>
      <li><strong>隐私报告：</strong>隐私报告 › 清除报告。</li>
      <li><strong>网络活动列表：</strong>网络活动 › 清除，或退出 Netoff。</li>
      <li><strong>规则：</strong>设置 › 重置所有规则…</li>
      <li><strong>全部数据：</strong>完成上述操作后，选择 设置 › 卸载扩展…，再把 Netoff 移到废纸篓。</li>
    </ul>

    <h2>儿童</h2>
    <p>Netoff 不会收集任何人的个人数据，包括儿童。</p>

    <h2>政策变更</h2>
    <p>如果本政策有变更，新版本会连同新的“最后更新”日期发布在此页面。由于 Netoff 不收集任何数据，预计不会影响应用对数据的处理方式。</p>

    <h2 id="contact">联系方式</h2>
    <p>对隐私有疑问？请在 <a href="{ISSUES}">GitHub</a> 上提交 issue（请勿在其中包含私人信息），或查看<a href="support.html">技术支持页</a>。</p>
  </article>
</div>'''),
}

# ───────────────────────────── Support ─────────────────────────────

SUPPORT = {
"en": dict(
    title="Support — Netoff",
    desc="Help for Netoff: getting started, approving the network extension, troubleshooting, uninstalling, and how to reach us.",
    body=f'''
<div class="wrap doc">
  <div class="head"><div class="eyebrow">Support</div><h1>How can we help?</h1>
  <p class="meta">Netoff for Mac · requires macOS 15 or later</p></div>
  <div class="support-cards">
    <a class="card bg-b" href="#start"><div class="emo" style="font-size:28px">🚀</div><h3>Getting started</h3><p>Turn on protection and approve the extension.</p></a>
    <a class="card bg-y" href="#trouble"><div class="emo" style="font-size:28px">🛠</div><h3>Troubleshooting</h3><p>Stuck on “Connecting…”, or nothing is blocked?</p></a>
    <a class="card bg-p" href="#contact"><div class="emo" style="font-size:28px">💬</div><h3>Contact</h3><p>Report a bug or ask a question.</p></a>
  </div>
  <article>
    <h2 id="start">Getting started</h2>
    <ol>
      <li>Open Netoff and switch <strong>protection</strong> on.</li>
      <li>macOS asks you to allow the network extension. Open <strong>System Settings › General › Login Items &amp; Extensions › Network Extensions</strong> and switch Netoff on. If macOS shows a prompt about filtering network content, choose Allow.</li>
      <li>Come back to Netoff. The status reads “Protection is on”. Choose a mode on the Overview page.</li>
    </ol>
    <h3>The three modes</h3>
    <ul>
      <li><strong>Blocklist</strong> — everything is allowed except the apps and addresses you block. On the Apps page, set an app to “Block”.</li>
      <li><strong>App allowlist</strong> — each app must be approved before it first connects. A prompt appears; choose how long to allow it.</li>
      <li><strong>Domain / IP allowlist</strong> — every unfamiliar domain or IP needs approval. In the prompt, allow just that address, its whole domain, or all connections of that app. Setting an app to “Allow” on the Apps page trusts it fully, so it is never asked about again.</li>
    </ul>
    <div class="callout"><span class="emo">💡</span><p>Approval prompts count down for 120 seconds, starting when the prompt appears. If you don't answer, that one connection is denied — no rule is created.</p></div>

    <h2 id="trouble">Troubleshooting</h2>
    <details open><summary>The status stays on “Connecting…” or protection won't turn on</summary><div class="a"><p>Check that Netoff is switched on under System Settings › General › Login Items &amp; Extensions › Network Extensions. Then turn protection off and on again in Netoff. If that doesn't help, open Settings › Network Extension › <strong>Reinstall Extension</strong>, and restart your Mac if macOS asks you to.</p></div></details>
    <details><summary>An app isn't being blocked</summary><div class="a"><p>Make sure protection is on (green) and that the app is set to “Block” on the Apps page — or switched off in the menu bar panel. A block applies to new connections; a connection that was already open may stay open until the app closes it. Some apps keep a connection alive for a long time.</p></div></details>
    <details><summary>Everything stopped working after I changed a mode</summary><div class="a"><p>In the allowlist modes, anything not yet approved waits for your answer. Open Netoff and answer the prompt, or switch back to Blocklist mode from the menu bar. Tip: set your browser and other must-have apps to “Allow” on the Apps page first.</p></div></details>
    <details><summary>I see “Unknown process” or “Exited process”</summary><div class="a"><p>A program opened a connection and quit before macOS could tell Netoff who it was. This is normal for very short-lived processes.</p></div></details>
    <details><summary>The connection log says it's unavailable</summary><div class="a"><p>The log is kept by the network extension, so protection must be on to read it. Turn protection on and reopen the Connection Log tab.</p></div></details>
    <details><summary>I'm not getting notifications</summary><div class="a"><p>Check Settings › Notifications in Netoff, and that Netoff is allowed to send notifications in System Settings › Notifications. Each blocked app triggers one notification; allowing and blocking it again resets that.</p></div></details>
    <details><summary>Does it work with a VPN or proxy app?</summary><div class="a"><p>Netoff filters connections app by app on your Mac. If you use a VPN or proxy app, its own connections show up under that app's name. Other filtering tools can interact in unexpected ways; if something looks wrong, turn the others off and tell us what you saw.</p></div></details>

    <h2 id="uninstall">Uninstalling</h2>
    <ol>
      <li>In Netoff, open <strong>Settings › Network Extension › Uninstall Extension…</strong>.</li>
      <li>If you want to remove your data too, first use <strong>Clear Log</strong>, <strong>Clear Report</strong> and <strong>Reset All Rules…</strong> (see the <a href="privacy.html#delete">privacy policy</a>).</li>
      <li>Quit Netoff and move it to the Trash.</li>
    </ol>

    <h2 id="contact">Contact us</h2>
    <p>Found a bug, or have an idea? Please <a href="{ISSUES}"><strong>open an issue on GitHub</strong></a>. A good report says:</p>
    <ul>
      <li>your macOS version and Netoff version (shown in the Netoff menu › About);</li>
      <li>what you did, what you expected, and what happened instead;</li>
      <li>a screenshot, if it helps.</li>
    </ul>
    <div class="callout"><span class="emo">🔒</span><p>Issues on GitHub are public. Please don't include private information — such as the names of sites you visit, or your connection log — in a report.</p></div>
  </article>
</div>'''),
"zh": dict(
    title="技术支持 — Netoff",
    desc="Netoff 使用帮助：快速上手、批准网络扩展、疑难解答、卸载方法，以及联系方式。",
    body=f'''
<div class="wrap doc">
  <div class="head"><div class="eyebrow">技术支持</div><h1>需要什么帮助？</h1>
  <p class="meta">Netoff for Mac · 需要 macOS 15 或更高版本</p></div>
  <div class="support-cards">
    <a class="card bg-b" href="#start"><div class="emo" style="font-size:28px">🚀</div><h3>快速上手</h3><p>开启保护并批准网络扩展。</p></a>
    <a class="card bg-y" href="#trouble"><div class="emo" style="font-size:28px">🛠</div><h3>疑难解答</h3><p>一直显示“正在连接…”，或什么都没被阻止？</p></a>
    <a class="card bg-p" href="#contact"><div class="emo" style="font-size:28px">💬</div><h3>联系方式</h3><p>反馈问题或提问。</p></a>
  </div>
  <article>
    <h2 id="start">快速上手</h2>
    <ol>
      <li>打开 Netoff，开启<strong>保护</strong>。</li>
      <li>macOS 会请求允许网络扩展。打开<strong>系统设置 › 通用 › 登录项与扩展 › 网络扩展</strong>，打开 Netoff 的开关。如果 macOS 弹出关于过滤网络内容的提示，选择“允许”。</li>
      <li>回到 Netoff，状态显示“保护已开启”。在“概览”页选择一种模式。</li>
    </ol>
    <h3>三种模式</h3>
    <ul>
      <li><strong>黑名单</strong>：除了被阻止的应用和地址，其余一律允许。在“应用”页把某个应用设为“阻止”。</li>
      <li><strong>应用白名单</strong>：每个应用第一次联网前都需要批准。出现提示时，选择允许多久。</li>
      <li><strong>域名 / IP 白名单</strong>：每个陌生的域名或 IP 都需要批准。在提示中可以只允许该地址、允许整个域名，或允许该应用的全部连接。在“应用”页把某个应用设为“允许”，表示完全信任，之后不再询问。</li>
    </ul>
    <div class="callout"><span class="emo">💡</span><p>批准提示从出现时开始倒计时 120 秒。如果没有回应，只会拒绝这一次连接，不会生成规则。</p></div>

    <h2 id="trouble">疑难解答</h2>
    <details open><summary>状态一直显示“正在连接…”，或保护无法开启</summary><div class="a"><p>请确认在 系统设置 › 通用 › 登录项与扩展 › 网络扩展 中，Netoff 的开关已打开。然后在 Netoff 中关闭再重新开启保护。如果仍无效，打开 设置 › 网络扩展 › <strong>重新安装扩展</strong>，若 macOS 提示，请重启 Mac。</p></div></details>
    <details><summary>某个应用没有被阻止</summary><div class="a"><p>请确认保护已开启（绿色），并且该应用在“应用”页被设为“阻止”，或在菜单栏面板中被关闭。阻止针对新的连接；已经建立的连接可能会保持到应用自己关闭它。有些应用会长时间保持连接。</p></div></details>
    <details><summary>切换模式后所有东西都连不上了</summary><div class="a"><p>在白名单模式下，尚未批准的连接会等待回应。打开 Netoff 回应提示，或在菜单栏中切回黑名单模式。建议：先在“应用”页把浏览器等必需的应用设为“允许”。</p></div></details>
    <details><summary>看到“未知进程”或“已退出的进程”</summary><div class="a"><p>某个程序发起连接后，在 macOS 告知 Netoff 它是谁之前就退出了。这对存活时间极短的进程来说是正常现象。</p></div></details>
    <details><summary>连接日志提示不可用</summary><div class="a"><p>日志由网络扩展保存，因此需要开启保护才能查看。开启保护后重新打开“连接日志”标签页即可。</p></div></details>
    <details><summary>收不到通知</summary><div class="a"><p>请检查 Netoff 设置中的“通知”，以及 系统设置 › 通知 中是否允许 Netoff 发送通知。每个被阻止的应用只会触发一次通知，重新允许再阻止后会再次提醒。</p></div></details>
    <details><summary>能和 VPN 或代理应用一起使用吗？</summary><div class="a"><p>Netoff 在这台 Mac 上按应用过滤连接。使用 VPN 或代理应用时，它们自己的连接会显示在该应用名下。其他过滤工具可能产生意料之外的相互影响；如果发现异常，请先关闭其他工具，并告诉我们观察到的情况。</p></div></details>

    <h2 id="uninstall">卸载</h2>
    <ol>
      <li>在 Netoff 中打开<strong>设置 › 网络扩展 › 卸载扩展…</strong>。</li>
      <li>如果还想删除数据，请先使用<strong>清除日志</strong>、<strong>清除报告</strong>和<strong>重置所有规则…</strong>（见<a href="privacy.html#delete">隐私政策</a>）。</li>
      <li>退出 Netoff，把它移到废纸篓。</li>
    </ol>

    <h2 id="contact">联系我们</h2>
    <p>发现问题或有好点子？请<a href="{ISSUES}"><strong>在 GitHub 上提交 issue</strong></a>。一份好的反馈包含：</p>
    <ul>
      <li>macOS 版本和 Netoff 版本（在 Netoff 菜单 › 关于 中查看）；</li>
      <li>做了什么、期望发生什么、实际发生了什么；</li>
      <li>如有帮助，附上截图。</li>
    </ul>
    <div class="callout"><span class="emo">🔒</span><p>GitHub 上的 issue 是公开的。请勿在反馈中包含私人信息，例如访问过的网站名称或连接日志。</p></div>
  </article>
</div>'''),
}

CONTENT = {"index": HOME, "privacy": PRIVACY, "support": SUPPORT}


def write(rel, text):
    full = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(full) or ROOT, exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    for lang in ("en", "zh"):
        for page in PAGES:
            c = CONTENT[page][lang]
            write(path(lang, page), layout(lang, page, c["title"], c["desc"], c["body"]))
    write(".nojekyll", "")
    write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n")
    urls = "".join(f"<url><loc>{SITE}{path(l, p).replace('index.html', '')}</loc></url>" for l in ("en", "zh") for p in PAGES)
    write("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    page404 = layout("en", "index", "Page not found — Netoff", "This page doesn't exist.",
          '<div class="wrap hero"><h1>Nothing here.</h1><p class="sub">That page doesn\'t exist — but the rest of the site does.</p><div class="cta"><a class="btn primary" href="index.html">Back to home</a></div></div>')
    # Served from any path, so every relative link must be absolute.
    page404 = re.sub(r'(href|src)="(?!https?:|#|/)([^"]*)"', lambda m: f'{m.group(1)}="/netoff/{m.group(2)}"', page404)
    write("404.html", page404)
    print("built", len(PAGES) * 2, "pages")


if __name__ == "__main__":
    main()
