"""Illustrations for the Netoff site.

The screens are hand-inked versions of the real app: same sidebar, cards, switches, segmented controls and
labels, in the same arrangement. Only the styling is artistic (thick ink outlines, flat pastel fills, a few
doodles around them), and the sample apps and domains are made up. Colors come from CSS variables.
"""
import html

# ───────────────────────────── Labels (what the app shows) ─────────────────────────────

LABELS = {
    "en": dict(
        overview="Overview", activity="Activity", report="Privacy Report", rules="Rules", apps="Apps",
        hosts="Domains & IPs", settings="Settings", protected="Protected", blocklist="Blocklist",
        protection_on="Protection is on", mode_sub="Everything is allowed except the apps and addresses you block.",
        filter_mode="Filter Mode", m1="Blocklist", m2="App Allowlist", m3="Domain / IP Allowlist",
        speed_cap="Download / Upload", blocked="Blocked", procs="Processes online (10 min)",
        open_apps="Open Apps", view_all="View All Processes",
        a1="Photo Editor", a2="Browser", a3="Chat", a4="Notes",
        s_blocked="Network access blocked", s_a2="4 connections · example.com", s_a3="2 connections · chat.example.net",
        s_none="Not online yet",
        menu_status="Blocklist · 12 blocked", mode_s1="Blocklist", mode_s2="App Allowlist", mode_s3="Domain Allowlist",
        open_netoff="Open Netoff", quit="Quit",
        tab_report="Report", tab_log="Connection Log", last7="Last 7 Days", today="Today",
        apps_only="Apps Only", all_procs="All Processes",
        st1="Apps contacting the network", st2="Domains & IPs contacted", st3="Connections",
        h_apps="App Network Activity", h_apps_c="Apps ranked by how many domains they contacted.",
        h_doms="Most Contacted Domains", h_doms_c="Domains ranked by how many apps contacted them.",
        r_a1="11 domains · 116 connections", r_a2="6 domains · 48 connections", r_a3="3 domains · 21 connections",
        r_a4="2 domains · 9 connections", r_a5="1 domain · 3 connections",
        d1="cdn.example.com", d2="api.example.net", d3="stats.example.org", d4="fonts.example.com", d5="198.51.100.7",
        r_d1="4 apps · 62 connections", r_d2="3 apps · 41 connections", r_d3="2 apps · 17 connections",
        r_d4="2 apps · 12 connections", r_d5="1 app · 5 connections",
        p_title="“Browser” wants to connect to cdn.example.com", p_detail="93.184.216.34 · TCP 443",
        p_path="/Applications/Browser.app", p_scope="Scope", p_dur="Duration", p_forever="Forever", p_hour="1 Hour",
        p_once="Once", p_all="Allow All Connections from This App", p_deny="Deny", p_allow="Allow",
        p_count="Auto-deny in 98s", p_more="2 more requests",
        alt_hero="The Netoff window: sidebar, protection switch, three filter modes and the list of open apps",
        alt_menu="The Netoff menu bar panel: mode picker, open apps with switches, a blocked app pinned in red",
        alt_report="The Privacy Report: apps ranked by domains contacted, and the most contacted domains",
        alt_prompt="The approval window asking whether an app may connect to a domain",
        alt_local="A laptop with a padlock: data stays on this Mac",
    ),
    "zh": dict(
        overview="概览", activity="网络活动", report="隐私报告", rules="规则", apps="应用",
        hosts="域名与 IP", settings="设置", protected="保护中", blocklist="黑名单",
        protection_on="保护已开启", mode_sub="默认允许所有连接，只阻止选定的应用和地址。",
        filter_mode="过滤模式", m1="黑名单", m2="应用白名单", m3="域名 / IP 白名单",
        speed_cap="下载 / 上传", blocked="已阻止", procs="近 10 分钟联网进程",
        open_apps="已打开的应用", view_all="查看所有进程",
        a1="修图工具", a2="浏览器", a3="聊天", a4="备忘录",
        s_blocked="已禁止联网", s_a2="4 个连接 · example.com", s_a3="2 个连接 · chat.example.net",
        s_none="暂未联网",
        menu_status="黑名单 · 已阻止 12 次", mode_s1="黑名单", mode_s2="应用白名单", mode_s3="域名白名单",
        open_netoff="打开 Netoff", quit="退出",
        tab_report="报告", tab_log="连接日志", last7="过去 7 天", today="今天",
        apps_only="仅应用", all_procs="所有进程",
        st1="联网的应用", st2="联系过的域名和 IP", st3="连接次数",
        h_apps="应用网络活动", h_apps_c="按联系的域名数量排序。",
        h_doms="最常联系的域名", h_doms_c="按联系它们的应用数量排序。",
        r_a1="11 个域名 · 116 次连接", r_a2="6 个域名 · 48 次连接", r_a3="3 个域名 · 21 次连接",
        r_a4="2 个域名 · 9 次连接", r_a5="1 个域名 · 3 次连接",
        d1="cdn.example.com", d2="api.example.net", d3="stats.example.org", d4="fonts.example.com", d5="198.51.100.7",
        r_d1="4 个应用 · 62 次连接", r_d2="3 个应用 · 41 次连接", r_d3="2 个应用 · 17 次连接",
        r_d4="2 个应用 · 12 次连接", r_d5="1 个应用 · 5 次连接",
        p_title="“浏览器”想要连接 cdn.example.com", p_detail="93.184.216.34 · TCP 443",
        p_path="/Applications/Browser.app", p_scope="范围", p_dur="有效期", p_forever="永久", p_hour="1 小时",
        p_once="仅本次", p_all="允许该应用全部连接", p_deny="拒绝", p_allow="允许",
        p_count="98 秒后自动拒绝", p_more="还有 2 个请求",
        alt_hero="Netoff 主窗口：侧边栏、保护开关、三种过滤模式和已打开的应用列表",
        alt_menu="Netoff 菜单栏面板：模式切换、带开关的已打开应用，被禁止的应用以红色置顶",
        alt_report="隐私报告：按联系的域名数量排序的应用，以及最常联系的域名",
        alt_prompt="批准窗口：询问某个应用是否可以连接某个域名",
        alt_local="带挂锁的笔记本电脑：数据只保存在这台 Mac 上",
    ),
}

# ───────────────────────────── Drawing helpers ─────────────────────────────

def esc(s):
    return html.escape(s, quote=False)


def svg(w, h, body, label=""):
    aria = f'role="img" aria-label="{html.escape(label)}"' if label else 'aria-hidden="true"'
    return f'<svg class="doodle" viewBox="0 0 {w} {h}" {aria} xmlns="http://www.w3.org/2000/svg">{body}</svg>'


def T(x, y, s, size=12, cls="t", weight=None, anchor=None, mono=False):
    w = f' font-weight="{weight}"' if weight else ""
    a = f' text-anchor="{anchor}"' if anchor else ""
    m = " mono" if mono else ""
    return f'<text class="{cls}{m}" x="{x}" y="{y}" font-size="{size}"{w}{a}>{esc(s)}</text>'


def R(x, y, w, h, r=8, cls="ink k2 f-w"):
    return f'<rect class="{cls}" x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}"/>'


def toggle(x, y, on, w=48, h=26):
    r = h / 2
    kx = x + w - r if on else x + r
    return (f'<rect class="ink k2 {"f-a" if on else "f-gray"}" x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}"/>'
            f'<circle class="ink k2 f-w" cx="{kx}" cy="{y + r}" r="{r - 3.5}"/>')


def tile(x, y, s, fill):
    return R(x, y, s, s, s * 0.28, f"ink k2 f-{fill}")


def nosign(cx, cy, r=7):
    return (f'<circle class="ink k2 f-r" cx="{cx}" cy="{cy}" r="{r}"/>'
            f'<path class="ink k2" d="M{cx - r * .6} {cy + r * .6} L{cx + r * .6} {cy - r * .6}"/>')


def seg(x, y, widths, h, labels, sel, size=11):
    """Segmented control: a soft track with the selected segment raised."""
    total = sum(widths)
    out = [R(x, y, total, h, h * 0.3, "ink k2 f-s")]
    cx = x
    for i, (w, lab) in enumerate(zip(widths, labels)):
        if i == sel:
            out.append(R(cx + 2, y + 2, w - 4, h - 4, h * 0.25, "ink k2 f-w"))
        out.append(T(cx + w / 2, y + h / 2 + size * 0.36, lab, size, "t" if i == sel else "t2", 600 if i == sel else None, "middle"))
        cx += w
    return "".join(out)


def spark(x, y, s=10):
    return f'<path class="ink" d="M{x} {y - s} Q{x} {y} {x + s} {y} Q{x} {y} {x} {y + s} Q{x} {y} {x - s} {y} Q{x} {y} {x} {y - s}Z"/>'


# Small glyphs in a 14×14 box, stroked (accent or white).
GLYPH = {
    "overview": "M7 1 L12 3 V7.5 C12 10.5 9.5 12.5 7 13 C4.5 12.5 2 10.5 2 7.5 V3Z",
    "activity": "M1 7 H4 L6 3 L8 11 L10 7 H13",
    "report": "M2.5 2.5 H11.5 V11.5 H2.5Z M5 5.5 H9 M5 8.5 H8",
    "apps": "M1.5 1.5 H5.5 V5.5 H1.5Z M8.5 1.5 H12.5 V5.5 H8.5Z M1.5 8.5 H5.5 V12.5 H1.5Z M8.5 8.5 H12.5 V12.5 H8.5Z",
    "hosts": "M7 1 A6 6 0 1 0 7.01 1Z M1 7 H13 M7 1 C4 4 4 10 7 13 M7 1 C10 4 10 10 7 13",
    "settings": "M7 4.8 A2.2 2.2 0 1 0 7.01 4.8Z M7 1 V2.6 M7 11.4 V13 M1 7 H2.6 M11.4 7 H13 M2.8 2.8 L3.9 3.9 M10.1 10.1 L11.2 11.2 M11.2 2.8 L10.1 3.9 M3.9 10.1 L2.8 11.2",
}


def glyph(name, x, y, white=False, scale=1.0):
    cls = "g gw" if white else "g ga"
    return f'<path class="{cls}" transform="translate({x} {y}) scale({scale})" d="{GLYPH[name]}"/>'


def mode_glyph(kind, x, y, white=False):
    """Mode symbols (hand / app with check / globe) in a 30×30 box, like the app's mode cards."""
    cls = "g gw" if white else "g ga"
    paths = {
        "block": "M9 15 V9.5 M13 15 V7 M17 15 V7.5 M21 15 V10 M9 15 C9 22 14 24.5 17 24.5 C21 24.5 22.5 20 21 15 M9 15 C6 14 5 15.2 6.2 17.2 L9 21",
        "app": "M6 8 Q6 6 8 6 H18 Q20 6 20 8 V18 Q20 20 18 20 H8 Q6 20 6 18Z M17 23 L20 26 L25 20",
        "host": "M15 5 A10 10 0 1 0 15.01 5Z M5 15 H25 M15 5 C10 10 10 20 15 25 M15 5 C20 10 20 20 15 25",
    }
    return f'<path class="{cls}" style="stroke-width:2" transform="translate({x} {y})" d="{paths[kind]}"/>'


def sidebar(L, sel, h):
    """The app's sidebar, in window-local coordinates (width 171)."""
    sw = 171
    out = [f'<path class="f-s" d="M22 0 H{sw} V{h} H22 A22 22 0 0 1 0 {h - 22} V22 A22 22 0 0 1 22 0Z"/>',
           f'<path class="ink k2 soft" d="M{sw} 0 V{h}"/>']
    rows = [("overview", 62, L["overview"]), ("activity", 94, L["activity"]), ("report", 126, L["report"]),
            ("apps", 190, L["apps"]), ("hosts", 222, L["hosts"]), ("settings", 262, L["settings"])]
    for key, y, label in rows:
        on = key == sel
        if on:
            out.append(R(12, y, 147, 28, 8, "f-a"))
        out.append(glyph(key, 24, y + 7, white=on))
        out.append(T(46, y + 19, label, 12.5, "tw" if on else "t"))
        if key == "apps":
            out.append(T(149, y + 19, "3", 11, "tw2" if on else "t2", anchor="end"))
        if key == "hosts":
            out.append(T(149, y + 19, "5", 11, "tw2" if on else "t2", anchor="end"))
    out.append(T(24, 182, L["rules"], 10.5, "t2", 600))
    out.append(f'<circle class="f-a" cx="22" cy="{h - 28}" r="4.5"/>')
    out.append(T(34, h - 24, L["protected"], 10.5, "t2"))
    out.append(T(159, h - 24, L["blocklist"], 10.5, "t2", anchor="end"))
    return "".join(out)


def traffic_lights(x=24, y=24):
    return (f'<circle class="ink f-r" cx="{x}" cy="{y}" r="6"/><circle class="ink f-y" cx="{x + 20}" cy="{y}" r="6"/>'
            f'<circle class="ink f-g" cx="{x + 40}" cy="{y}" r="6"/>')


def window(w, h, inner, sidebar_svg=""):
    return (f'<rect class="f-w" x="0" y="0" width="{w}" height="{h}" rx="22"/>{sidebar_svg}{inner}'
            f'<rect class="ink" x="0" y="0" width="{w}" height="{h}" rx="22"/>')


# ───────────────────────────── Screens ─────────────────────────────

def overview_content(L):
    s = []
    # toolbar: sidebar toggle + title
    s.append('<circle class="ink k2 f-w" cx="194" cy="26" r="14"/><rect class="ink k2" x="187" y="20.5" width="14" height="11" rx="3"/><path class="ink k2" d="M191.5 20.5 V31.5"/>')
    s.append(T(222, 31, L["overview"], 14, weight=700))
    # status card
    s.append(R(204, 60, 572, 74, 14, "ink k2 f-s"))
    s.append('<circle class="ink k2 f-a" cx="246" cy="97" r="24"/><path class="g gw" style="stroke-width:3" d="M236 98 L243 106 L257 90"/>')
    s.append(T(284, 93, L["protection_on"], 17, weight=700))
    s.append(T(284, 113, L["mode_sub"], 11, "t2"))
    s.append(toggle(718, 82, True, 52, 30))
    # filter mode
    s.append(T(204, 162, L["filter_mode"], 14, weight=700))
    for i, (key, name) in enumerate((("block", L["m1"]), ("app", L["m2"]), ("host", L["m3"]))):
        x = 204 + i * 196
        on = i == 0
        s.append(R(x, 172, 180, 96, 14, "ink k2 f-s sel" if on else "ink k2 f-s"))
        s.append(R(x + 12, 184, 30, 30, 9, "ink k2 f-a" if on else "ink k2 f-w"))
        s.append(mode_glyph(key, x + 12, 184, white=on))
        if on:
            s.append(f'<circle class="ink k2 f-a" cx="{x + 160}" cy="198" r="8"/><path class="g gw" style="stroke-width:2" d="M{x + 156} 198 L{x + 159} 201 L{x + 164} 195"/>')
        else:
            s.append(f'<circle class="ink k2 soft" cx="{x + 160}" cy="198" r="8"/>')
        s.append(T(x + 14, 236, name, 12.5, weight=700))
        s.append(f'<path class="ink k2 soft" d="M{x + 14} 249 h132 M{x + 14} 259 h92"/>')
    # stat tiles
    for i in range(3):
        s.append(R(204 + i * 196, 282, 180, 48, 12, "ink k2 f-s"))
    s.append('<circle class="ink k2 f-a" cx="224" cy="306" r="9"/><path class="g gw" d="M221 303 V309 M221 309 L219 307 M221 309 L223 307 M227 309 V303 M227 303 L225 305 M227 303 L229 305"/>')
    s.append(T(240, 304, "↓ 36 KB/s  ↑ 12 KB/s", 11, weight=700))
    s.append(T(240, 320, L["speed_cap"], 9, "t2"))
    s.append('<circle class="ink k2 f-r" cx="420" cy="306" r="9"/><path class="g" stroke="var(--ink)" d="M417 303 L423 309 M423 303 L417 309"/>')
    s.append(T(436, 311, "0", 16, weight=700))
    s.append(T(452, 311, L["blocked"], 9, "t2"))
    s.append('<circle class="ink k2 f-b" cx="616" cy="306" r="9"/><circle class="ink k2 f-w" cx="616" cy="306" r="3"/>')
    s.append(T(632, 304, "6", 14, weight=700))
    s.append(T(632, 320, L["procs"], 9, "t2"))
    # open apps
    s.append(T(204, 362, L["open_apps"], 14, weight=700))
    s.append(T(776, 362, L["view_all"], 11, "ta", anchor="end"))
    s.append(R(204, 372, 572, 124, 14, "ink k2 f-s"))
    # row 1: blocked, pinned in red
    s.append('<rect class="f-r" x="210" y="378" width="560" height="34" rx="9"/>')
    s.append(tile(220, 384, 22, "p") + nosign(240, 405))
    s.append(T(252, 393, L["a1"], 12, weight=700))
    s.append(T(252, 406, L["s_blocked"], 9.5, "tr"))
    s.append(toggle(718, 383, False, 44, 24))
    # rows 2 and 3
    for y, fill, name, sub, down, up in ((416, "b", L["a2"], L["s_a2"], "↓ 11 KB/s", "↑ 4 KB/s"),
                                         (454, "y", L["a3"], L["s_a3"], "↓ 0.9 KB/s", "↑ 0.4 KB/s")):
        s.append(tile(220, y + 6, 22, fill))
        s.append(T(252, y + 16, name, 12, weight=700))
        s.append(T(252, y + 29, sub, 9.5, "t2"))
        s.append(T(704, y + 15, down, 9, "t2", anchor="end"))
        s.append(T(704, y + 27, up, 9, "t2", anchor="end"))
        s.append(toggle(718, y + 5, True, 44, 24))
    return "".join(s)


def cloud_and_plug():
    return ('<path class="ink f-w" d="M862 96 C842 96 834 74 852 64 C852 38 890 30 904 50 C922 32 958 46 954 72 C976 74 978 100 954 102 Z"/>'
            '<path class="ink" d="M880 84 q8 6 16 0 M924 84 q8 6 16 0"/>'
            '<path class="ink" d="M846 330 C920 330 880 296 906 270 C922 254 918 238 918 238"/>'
            '<rect class="ink f-b" x="904" y="196" width="28" height="42" rx="8"/>'
            '<path class="ink" d="M912 196 V184 M924 196 V184"/>'
            '<path class="ink" d="M896 164 l-8 -9 M918 158 V144 M940 164 l8 -9"/>')


def hero(lang):
    L = LABELS[lang]
    body = (
        '<path class="f-y" d="M20 330 C-10 190 120 60 300 74 C470 36 700 70 780 210 C860 360 740 560 520 556 C320 596 60 540 20 330Z"/>'
        '<g transform="translate(50 70) rotate(-1 400 260)">'
        + window(800, 520, traffic_lights() + overview_content(L), sidebar(L, "overview", 520)) +
        '</g>'
        + cloud_and_plug() + spark(30, 90, 12) + spark(900, 420, 10) + spark(70, 610, 8)
    )
    return svg(980, 640, body, L["alt_hero"])


def menubar(lang):
    L = LABELS[lang]
    x0, y0 = 100, 70   # panel origin
    s = []
    # menu bar strip with the app's status item highlighted
    s.append(R(0, 20, 440, 30, 8, "ink k2 f-w"))
    s.append('<path class="ink k2 soft" d="M18 35 h34 M66 35 h26 M106 35 h20"/>')
    s.append(R(384, 24, 32, 22, 6, "ink k2 f-a"))
    s.append('<path class="g gw" style="stroke-width:1.6" d="M400 29 L405 31 V35.5 C405 38.5 402.5 40.5 400 41 C397.5 40.5 395 38.5 395 35.5 V31Z"/>')
    p = []
    p.append(R(0, 0, 340, 420, 18, "ink f-w"))
    # header
    p.append('<circle class="ink k2 f-a" cx="30" cy="32" r="15"/><path class="g gw" style="stroke-width:2.4" d="M23 33 L28 38 L37 27"/>')
    p.append(T(54, 30, "Netoff", 15, weight=700))
    p.append(T(54, 45, L["menu_status"], 10.5, "t2"))
    p.append(toggle(272, 18, True, 52, 28))
    # speeds
    p.append(T(16, 82, "↓ 1.2 MB/s", 12, "t2"))
    p.append(T(112, 82, "↑ 86 KB/s", 12, "t2"))
    # mode picker
    p.append(seg(14, 96, [100, 106, 106], 28, [L["mode_s1"], L["mode_s2"], L["mode_s3"]], 0, 11))
    p.append('<path class="ink k2 soft" d="M0 140 H340"/>')
    p.append(T(16, 162, L["open_apps"], 10.5, "t2", 600))
    rows = [("p", L["a1"], L["s_blocked"], None, False, True),
            ("b", L["a2"], L["s_a2"], ("↓ 11 KB/s", "↑ 4 KB/s"), True, False),
            ("y", L["a3"], L["s_a3"], ("↓ 0.9 KB/s", "↑ 0.4 KB/s"), True, False),
            ("g", L["a4"], L["s_none"], None, True, False)]
    for i, (fill, name, sub, speeds, on, red) in enumerate(rows):
        y = 172 + i * 46
        if red:
            p.append(f'<rect class="f-r" x="8" y="{y - 4}" width="324" height="42" rx="10"/>')
        p.append(tile(18, y + 3, 26, fill))
        if red:
            p.append(nosign(42, y + 28, 7.5))
        p.append(T(54, y + 15, name, 13, weight=700))
        p.append(T(54, y + 29, sub, 10, "tr" if red else "t2"))
        if speeds:
            p.append(T(270, y + 13, speeds[0], 9, "t2", anchor="end"))
            p.append(T(270, y + 25, speeds[1], 9, "t2", anchor="end"))
        p.append(toggle(278, y + 5, on, 44, 24))
    p.append('<path class="ink k2 soft" d="M0 362 H340"/>')
    p.append('<rect class="ink k2" x="16" y="381" width="16" height="12" rx="3"/><path class="ink k2" d="M16 385 H32"/>')
    p.append(T(40, 391, L["open_netoff"], 12.5, "t"))
    p.append(T(324, 391, L["quit"], 12.5, "t", anchor="end"))
    body = (
        '<path class="f-b" d="M110 280 C90 160 190 70 330 78 C470 66 560 150 548 290 C540 420 420 500 300 492 C180 500 124 400 110 280Z"/>'
        + "".join(s) + f'<g transform="translate({x0} {y0})">' + "".join(p) + '</g>'
        + spark(60, 150, 11) + spark(40, 330, 8) + spark(520, 470, 9)
    )
    return svg(560, 520, body, L["alt_menu"])


def report(lang):
    L = LABELS[lang]
    w, h = 620, 470
    s = [traffic_lights()]
    s.append('<circle class="ink k2 f-w" cx="74" cy="24" r="12"/><rect class="ink k2" x="68" y="19.5" width="12" height="9" rx="2.5"/><path class="ink k2" d="M72 19.5 V28.5"/>')
    s.append(seg(w / 2 - 125, 10, [96, 154], 28, [L["tab_report"], L["tab_log"]], 0, 11))
    s.append('<circle class="ink k2 f-w" cx="594" cy="24" r="12"/><path class="g" stroke="var(--ink)" d="M588 21 H600 M590 21 L591 30 H597 L598 21 M592 18.5 H596"/>')
    s.append('<path class="ink k2 soft" d="M0 48 H620"/>')
    # controls
    s.append(seg(24, 62, [92, 70], 26, [L["last7"], L["today"]], 0, 10.5))
    s.append(seg(w - 24 - 200, 62, [90, 110], 26, [L["apps_only"], L["all_procs"]], 0, 10.5))
    # stat cards
    stats = [(L["st1"], "9", "app"), (L["st2"], "24", "host"), (L["st3"], "199", "arrows")]
    for i, (cap, val, ic) in enumerate(stats):
        x = 24 + i * 192
        s.append(R(x, 102, 180, 48, 12, "ink k2 f-s"))
        s.append(f'<circle class="ink k2 f-a" cx="{x + 22}" cy="126" r="10"/>')
        s.append(T(x + 40, 130, val, 16, weight=700))
        s.append(T(x + 40, 143, cap, 8.5, "t2"))
    # two ranked lists
    def column(x, title, cap, rows, kind):
        out = [T(x, 178, title, 12.5, weight=700), T(x, 192, cap, 8.8, "t2"), R(x, 202, 284, 250, 14, "ink k2 f-s")]
        top = rows[0][3]
        for i, (name, det, fill, frac) in enumerate(rows):
            y = 212 + i * 48
            if i:
                out.append(f'<path class="ink k2 soft" d="M{x + 46} {y - 5} H{x + 270}"/>')
            if kind == "app":
                out.append(tile(x + 12, y + 6, 24, fill))
            else:
                out.append(f'<rect class="ink k2 f-{fill}" x="{x + 12}" y="{y + 6}" width="24" height="24" rx="7"/><path class="g ga" style="stroke-width:1.4" transform="translate({x + 17} {y + 11})" d="{GLYPH["hosts"]}"/>')
            out.append(T(x + 46, y + 14, name, 11.5, weight=600))
            out.append(f'<rect class="f-a" opacity=".75" x="{x + 46}" y="{y + 19}" width="{max(8, 196 * frac)}" height="5" rx="2.5"/>')
            out.append(T(x + 46, y + 38, det, 9, "t2"))
            out.append(f'<path class="g" stroke="var(--ink-2)" d="M{x + 268} {y + 14} l5 5 l-5 5"/>')
        return "".join(out)
    app_rows = [(L["a1"], L["r_a1"], "p", 1.0), (L["a2"], L["r_a2"], "b", .55), (L["a3"], L["r_a3"], "y", .3),
                (L["a4"], L["r_a4"], "g", .2), ("Mail", L["r_a5"], "b", .1)]
    dom_rows = [(L["d1"], L["r_d1"], "b", 1.0), (L["d2"], L["r_d2"], "y", .75), (L["d3"], L["r_d3"], "g", .5),
                (L["d4"], L["r_d4"], "p", .5), (L["d5"], L["r_d5"], "b", .25)]
    s.append(column(24, L["h_apps"], L["h_apps_c"], app_rows, "app"))
    s.append(column(312, L["h_doms"], L["h_doms_c"], dom_rows, "dom"))
    body = (
        '<path class="f-p" d="M-10 260 C-30 120 120 20 320 30 C520 10 700 90 690 260 C684 410 540 500 330 492 C130 506 0 410 -10 260Z"/>'
        '<g transform="translate(40 52) rotate(1 310 235)">' + window(w, h, "".join(s)) + '</g>'
        # a magnifying glass on top, as a nod to "see who's talking to whom"
        '<circle class="ink f-w" cx="610" cy="430" r="46" fill-opacity=".9"/><circle class="ink f-b" cx="610" cy="430" r="34" fill-opacity=".55"/>'
        '<path class="ink" style="stroke-width:9" d="M642 464 L690 512"/>'
        + spark(30, 40, 11) + spark(700, 110, 9) + spark(60, 540, 8)
    )
    return svg(740, 570, body, L["alt_report"])


def prompt(lang):
    L = LABELS[lang]
    w, h = 460, 276
    s = []
    s.append(f'<rect class="f-y" x="10" y="14" width="{w}" height="{h}" rx="22"/>')   # offset shadow block
    s.append(R(0, 0, w, h, 22, "ink f-w"))
    s.append(T(w - 18, 22, L["p_count"] + " · " + L["p_more"], 9.5, "t2", anchor="end"))
    # header: app icon + title
    s.append(R(24, 38, 56, 56, 15, "ink k2 f-b"))
    s.append(R(38, 52, 28, 28, 8, "ink k2 f-w"))
    s.append(T(94, 56, L["p_title"], 14 if lang == "en" else 15, weight=700))
    s.append(T(94, 74, L["p_detail"], 11.5, "t2", mono=True))
    s.append(T(94, 90, L["p_path"], 9.5, "t2"))
    # options box
    s.append(R(24, 108, w - 48, 82, 12, "ink k2 f-s"))
    s.append(T(40, 134, L["p_scope"], 11.5, "t2"))
    s.append(R(130, 118, 200, 26, 7, "ink k2 f-w"))
    s.append(T(142, 135, "cdn.example.com", 11.5, mono=True))
    s.append('<path class="g" stroke="var(--ink-2)" d="M312 128 l4 4 l4 -4"/>')
    s.append(T(40, 170, L["p_dur"], 11.5, "t2"))
    s.append(seg(130, 156, [92, 92, 92], 26, [L["p_forever"], L["p_hour"], L["p_once"]], 0, 11))
    # buttons
    bw = 226 if lang == "en" else 150
    s.append(R(24, 216, bw, 32, 9, "ink k2 f-w"))
    s.append(T(24 + bw / 2, 236, L["p_all"], 11.5, anchor="middle"))
    s.append(R(w - 24 - 74 - 12 - 74, 216, 74, 32, 9, "ink k2 f-w"))
    s.append(T(w - 24 - 74 - 12 - 37, 236, L["p_deny"], 12.5, anchor="middle"))
    s.append(R(w - 24 - 74, 216, 74, 32, 9, "ink k2 f-a"))
    s.append(T(w - 24 - 37, 236, L["p_allow"], 12.5, "tw", 600, "middle"))
    body = (
        '<path class="f-g" d="M-20 150 C-30 40 110 -20 260 -14 C420 -22 520 50 508 160 C500 270 380 330 250 322 C100 330 -10 260 -20 150Z" transform="translate(0 6)"/>'
        '<g transform="translate(36 40) rotate(-1.2 230 138)">' + "".join(s) + '</g>'
        + spark(16, 330, 10) + spark(520, 40, 9)
    )
    return svg(560, 400, body, L["alt_prompt"])


# ───────────────────────────── Icons for the three mode cards (same symbols as the app) ─────────────────────────────

def _icon(kind):
    paths = {
        "block": '<path class="ink" d="M36 62 V34 M52 62 V22 M68 62 V24 M84 62 V34"/><path class="ink f-w" d="M32 60 C32 90 50 100 62 100 C78 100 88 84 84 60 L84 60 M32 60 C20 56 16 62 22 70 L34 86"/>',
        "app": '<rect class="ink f-w" x="22" y="22" width="64" height="64" rx="18"/><path class="ink" d="M40 54 q6 -2 12 0 t12 0"/><circle class="ink f-g" cx="86" cy="86" r="20"/><path class="ink" d="M76 86 l7 8 l13 -16"/>',
        "host": '<circle class="ink f-w" cx="56" cy="56" r="38"/><path class="ink" d="M18 56 H94 M56 18 C36 38 36 74 56 94 M56 18 C76 38 76 74 56 94"/><rect class="ink f-y" x="64" y="68" width="44" height="30" rx="9"/><path class="ink" d="M74 83 l7 8 l16 -16"/>',
    }
    return svg(120, 120, paths[kind])


def icon_blocklist():
    return _icon("block")


def icon_apps():
    return _icon("app")


def icon_domains():
    return _icon("host")


def local(lang):
    L = LABELS[lang]
    return svg(560, 400, '''
  <path class="f-g" d="M40 210 C34 110 140 44 280 48 C430 40 534 120 520 236 C512 330 392 376 270 368 C140 376 50 320 40 210Z"/>
  <rect class="ink f-w" x="150" y="96" width="260" height="170" rx="16"/>
  <rect class="ink f-b" x="170" y="116" width="220" height="130" rx="8"/>
  <path class="ink f-w" d="M110 266 H450 L430 300 H130 Z"/>
  <rect class="ink f-y" x="236" y="168" width="88" height="68" rx="14"/>
  <path class="ink" d="M254 168 v-18 a26 26 0 0 1 52 0 v18"/>
  <circle class="ink f-w" cx="280" cy="198" r="8"/><path class="ink" d="M280 206 v14"/>
  <path class="ink soft" d="M60 330 q18 -14 36 0 t36 0 M440 90 q18 -14 36 0 t36 0"/>
''' + spark(100, 150, 11) + spark(468, 230, 9), L["alt_local"])


def footer_squiggle():
    return '<svg class="squiggle" viewBox="0 0 400 14" preserveAspectRatio="none" aria-hidden="true"><path class="ink" d="M2 8 C40 0 60 14 100 7 S160 1 200 8 S280 14 320 6 S380 4 398 8"/></svg>'
