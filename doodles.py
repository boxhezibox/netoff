"""Hand-drawn style SVG illustrations: thick ink outlines + flat pastel fills (colors come from CSS variables)."""

def svg(w, h, body, label=""):
    aria = f'role="img" aria-label="{label}"' if label else 'aria-hidden="true"'
    return f'<svg class="doodle" viewBox="0 0 {w} {h}" {aria} xmlns="http://www.w3.org/2000/svg">{body}</svg>'

SPARK = lambda x, y, s=10: f'<path class="ink" d="M{x} {y-s} Q{x} {y} {x+s} {y} Q{x} {y} {x} {y+s} Q{x} {y} {x-s} {y} Q{x} {y} {x} {y-s}Z"/>'

def toggle(x, y, on, fill):
    knob_x = x + 38 if on else x + 14
    f = f"f-{fill}" if on else "f-gray"
    return (f'<rect class="ink {f}" x="{x}" y="{y}" width="52" height="28" rx="14"/>'
            f'<circle class="ink f-w" cx="{knob_x}" cy="{y+14}" r="9"/>')

def app_row(y, appfill, name_w, on, toggle_fill="g", blocked=False):
    badge = ''
    if blocked:
        badge = ('<circle class="ink f-r" cx="222" cy="%d" r="11"/><path class="ink" d="M214 %d L230 %d"/>' % (y + 4, y + 12, y - 4))
    return (f'<rect class="ink f-{appfill}" x="194" y="{y}" width="36" height="36" rx="10"/>'
            f'<path class="ink" d="M246 {y+12} q{name_w/4} -4 {name_w/2} 0 t{name_w/2} 0"/>'
            f'<path class="ink soft" d="M246 {y+27} q{name_w/6} -3 {name_w/3} 0 t{name_w/3} 0"/>'
            + toggle(478, y + 4, on, toggle_fill) + badge)

HERO = svg(720, 440, f'''
  <path class="f-y" d="M70 250 C48 140 160 56 300 64 C440 36 610 80 660 190 C710 300 610 410 440 408 C300 436 92 396 70 250Z"/>
  <rect class="ink f-w" x="170" y="92" width="400" height="270" rx="20"/>
  <path class="ink" d="M170 134 H570"/>
  <circle class="ink f-r" cx="196" cy="113" r="6"/><circle class="ink f-y" cx="217" cy="113" r="6"/><circle class="ink f-g" cx="238" cy="113" r="6"/>
  {app_row(158, "b", 150, True)}
  {app_row(214, "p", 120, False, blocked=True)}
  {app_row(270, "g", 170, True)}
  <path class="ink soft" d="M194 322 q60 -8 120 0 t120 0"/>
  <path class="ink f-w" d="M572 112 C552 112 544 90 562 80 C562 54 600 46 614 66 C632 48 668 62 664 88 C686 90 688 116 664 118 Z"/>
  <path class="ink" d="M590 100 q8 6 16 0 M634 100 q8 6 16 0"/>
  <path class="ink" d="M570 250 C640 250 600 214 624 196 C636 188 634 184 634 184"/>
  <rect class="ink f-b" x="620" y="150" width="28" height="36" rx="7" transform="rotate(0)"/>
  <path class="ink" d="M628 150 V138 M640 150 V138"/>
  <path class="ink" d="M612 126 l-8 -8 M634 122 V108 M656 126 l8 -8"/>
  {SPARK(112, 126, 11)}{SPARK(650, 350, 9)}{SPARK(130, 330, 7)}
''', "A Mac window with three apps, one switched off, and a cable unplugged from the cloud")

def icon_blocklist():
    return svg(120, 120, '''
  <circle class="ink f-w" cx="60" cy="60" r="46"/>
  <rect class="ink f-r" x="38" y="38" width="44" height="44" rx="12"/>
  <path class="ink" d="M26 94 L94 26"/>
''', "")

def icon_apps():
    return svg(120, 120, '''
  <rect class="ink f-w" x="22" y="22" width="64" height="64" rx="18"/>
  <path class="ink" d="M40 54 q6 -2 12 0 t12 0"/>
  <circle class="ink f-g" cx="86" cy="86" r="20"/>
  <path class="ink" d="M76 86 l7 8 l13 -16"/>
''', "")

def icon_domains():
    return svg(120, 120, '''
  <circle class="ink f-w" cx="56" cy="56" r="38"/>
  <path class="ink" d="M18 56 H94 M56 18 C36 38 36 74 56 94 M56 18 C76 38 76 74 56 94"/>
  <rect class="ink f-y" x="64" y="68" width="44" height="30" rx="9"/>
  <path class="ink" d="M74 83 l7 8 l16 -16"/>
''', "")

MENUBAR = svg(560, 400, f'''
  <path class="f-b" d="M170 220 C160 120 250 50 380 54 C490 46 552 124 540 232 C534 330 450 378 350 372 C240 380 180 330 170 220Z"/>
  <rect class="ink f-w" x="196" y="46" width="324" height="30" rx="8"/>
  <path class="ink soft" d="M216 61 h40 M274 61 h30 M322 61 h24"/>
  <circle class="ink f-g" cx="480" cy="61" r="8"/>
  <path class="ink" d="M480 84 V92" />
  <rect class="ink f-w" x="250" y="92" width="270" height="270" rx="18"/>
  <rect class="ink f-g" x="268" y="110" width="30" height="30" rx="9"/>
  <path class="ink" d="M308 118 q10 -4 20 0 t20 0 M308 132 q8 -3 16 0 t16 0"/>
  {toggle(448, 112, True, "g")}
  <path class="ink soft" d="M268 156 H502"/>
  <rect class="ink f-r" x="262" y="172" width="246" height="56" rx="12"/>
  <rect class="ink f-p" x="276" y="185" width="30" height="30" rx="9"/>
  <circle class="ink f-r" cx="304" cy="213" r="9"/><path class="ink" d="M298 219 L310 207"/>
  <path class="ink" d="M320 192 q10 -4 20 0 t20 0 M320 206 q8 -3 16 0 t16 0"/>
  {toggle(442, 186, False, "g")}
  <rect class="ink f-y" x="268" y="242" width="30" height="30" rx="9"/>
  <path class="ink" d="M308 250 q10 -4 20 0 t20 0 M308 264 q8 -3 16 0 t16 0"/>
  {toggle(448, 244, True, "g")}
  <rect class="ink f-b" x="268" y="292" width="30" height="30" rx="9"/>
  <path class="ink" d="M308 300 q10 -4 20 0 t20 0 M308 314 q8 -3 16 0 t16 0"/>
  {toggle(448, 294, True, "g")}
  <path class="ink" d="M196 250 C170 250 150 230 150 200 C150 176 164 160 190 156" /><path class="ink" d="M178 144 l14 12 l-18 10"/>
  {SPARK(212, 330, 10)}{SPARK(232, 392, 7)}
''', "A menu bar panel listing apps with switches, a blocked app pinned at the top in red")

REPORT = svg(560, 400, f'''
  <path class="f-p" d="M40 200 C30 110 140 40 280 46 C430 40 540 120 520 240 C510 330 390 376 270 368 C140 376 50 310 40 200Z"/>
  <rect class="ink f-w" x="70" y="70" width="330" height="260" rx="18"/>
  <path class="ink" d="M70 112 H400"/>
  <circle class="ink f-r" cx="92" cy="91" r="6"/><circle class="ink f-y" cx="112" cy="91" r="6"/><circle class="ink f-g" cx="132" cy="91" r="6"/>
  <rect class="ink f-b" x="98" y="146" width="36" height="36" rx="10"/>
  <rect class="ink f-b" x="150" y="152" width="190" height="24" rx="12"/>
  <rect class="ink f-g" x="98" y="200" width="36" height="36" rx="10"/>
  <rect class="ink f-g" x="150" y="206" width="136" height="24" rx="12"/>
  <rect class="ink f-y" x="98" y="254" width="36" height="36" rx="10"/>
  <rect class="ink f-y" x="150" y="260" width="84" height="24" rx="12"/>
  <circle class="ink f-w" cx="372" cy="262" r="52" fill-opacity=".85"/>
  <circle class="ink f-b" cx="372" cy="262" r="40" fill-opacity=".5"/>
  <path class="ink" d="M410 300 L468 358" stroke-width="9"/>
  <path class="ink" d="M352 262 h40 M372 242 v40" stroke-width="3"/>
  {SPARK(470, 100, 12)}{SPARK(448, 190, 8)}
''', "A report window with ranked bars and a magnifying glass")

LOCAL = svg(560, 400, f'''
  <path class="f-g" d="M40 210 C34 110 140 44 280 48 C430 40 534 120 520 236 C512 330 392 376 270 368 C140 376 50 320 40 210Z"/>
  <rect class="ink f-w" x="150" y="96" width="260" height="170" rx="16"/>
  <rect class="ink f-b" x="170" y="116" width="220" height="130" rx="8"/>
  <path class="ink f-w" d="M110 266 H450 L430 300 H130 Z"/>
  <rect class="ink f-y" x="236" y="168" width="88" height="68" rx="14"/>
  <path class="ink" d="M254 168 v-18 a26 26 0 0 1 52 0 v18"/>
  <circle class="ink f-w" cx="280" cy="198" r="8"/><path class="ink" d="M280 206 v14"/>
  <path class="ink soft" d="M60 330 q18 -14 36 0 t36 0 M440 90 q18 -14 36 0 t36 0"/>
  {SPARK(100, 150, 11)}{SPARK(468, 230, 9)}
''', "A laptop with a padlock: data stays on this Mac")

STEP = svg(0,0,"")  # placeholder, not used

def footer_squiggle():
    return '<svg class="squiggle" viewBox="0 0 400 14" preserveAspectRatio="none" aria-hidden="true"><path class="ink" d="M2 8 C40 0 60 14 100 7 S160 1 200 8 S280 14 320 6 S380 4 398 8"/></svg>'
