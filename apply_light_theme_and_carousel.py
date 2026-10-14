# Run in the Joma Consulting repo root:  python apply_light_theme_and_carousel.py
# 1) light-theme override for the client dashboard  2) dual trust carousel inside <section id="trust">. Nothing else changes.
import re
CSS=r'''/* ===== Joma client dashboard: light theme override ===== */
#portal{background:var(--paper);color:var(--ink)}
.p-topbar{background:rgba(255,255,255,.92);border-bottom:1px solid var(--line)}.p-topbar .p-brand{color:var(--navy)}.portal-logo-img{border-color:var(--line)}.p-topbar .p-brand .name small{color:var(--green-deep)}
.p-link-back{color:var(--ink-soft)}.p-link-back:hover{color:var(--green-deep)}.p-user{border-left-color:var(--line)}.p-user .u-name{color:var(--navy)}.p-user .u-sub{color:var(--ink-soft)}
.p-signout{border-color:var(--line);color:var(--ink-soft)}.p-signout:hover{border-color:var(--green);color:var(--navy)}
.p-sidebar{background:var(--white);border-right-color:var(--line)}.p-sidebar .grp{color:var(--ink-faint)}.p-nav-item{color:var(--ink-soft)}.p-nav-item:hover{background:var(--mint-pale);color:var(--navy)}
.p-nav-item .cnt{background:var(--paper-deep);color:var(--ink-soft)}.p-nav-item.active{background:var(--mint-pale);color:var(--green-deep);border-color:rgba(30,138,76,.35)}.p-nav-item.active .cnt{background:var(--green);color:#fff}
@media(max-width:900px){.p-sidebar{border-bottom-color:var(--line)}}
.p-page-head h1,.p-stat-card .val,.p-card h3,.p-activity-row .txt b,.p-consult-date .info .t,.p-table .svc-name,.p-doc-row .n,.p-toggle-row .t,.p-dropzone h4{color:var(--navy)}
.p-page-head .sub,.p-card .p-card-sub,.p-stat-card .lbl,.p-consult-date .info .s,.p-doc-row .m,.p-table .svc-sub,.p-toggle-row .s,.p-dropzone p{color:var(--ink-soft)}
.p-glass{background:var(--white);border-color:var(--line);box-shadow:0 2px 8px -2px rgba(14,27,46,.06)}.p-glass-green{border-color:rgba(30,138,76,.35)}.p-stat-card .val small{color:var(--green-deep)}
.p-activity-row,.p-table th,.p-table td,.p-doc-row,.p-toggle-row{border-color:var(--line-soft)}.p-activity-row .txt{color:var(--ink)}.p-activity-row .time,.p-table th{color:var(--ink-faint)}.p-activity-dot{background:var(--green)}
.p-consult-date .d{background:var(--mint-pale);color:var(--green-deep);border-color:rgba(30,138,76,.35)}
.p-form .field label{color:var(--ink-soft)}.p-form .field input,.p-form .field select,.p-form .field textarea{background:var(--paper);border-color:var(--line);color:var(--navy)}
.p-chip-opt{border-color:var(--line);color:var(--ink-soft)}.p-chip-opt.sel{border-color:var(--green);background:var(--mint-pale);color:var(--green-deep)}
.p-chip.submitted{background:var(--mint-pale);color:var(--green-deep)}.p-chip.submitted::before{background:var(--green)}.p-chip.scheduled{background:#E6EFF7;color:#2662C9}.p-chip.scheduled::before{background:#2662C9}
.p-chip.progress{background:#FBF1DC;color:#B7791F}.p-chip.progress::before{background:#B7791F}.p-chip.done{background:#E4F5EA;color:var(--green-deep)}.p-chip.done::before{background:var(--green)}
.p-dropzone{border-color:var(--line)}.p-dropzone.drag{background:var(--mint-pale)}.p-doc-ic{background:var(--mint-pale);color:var(--green-deep)}.p-icon-btn{border-color:var(--line);color:var(--ink-soft)}.p-icon-btn:hover{color:var(--green-deep)}
.switch .track{background:var(--line)}#p-toast{background:var(--navy);color:#fff}
#portal .btn-ghost{border-color:var(--navy)!important;color:var(--navy)!important}#portal .btn-ghost:hover{background:var(--navy);color:#fff!important}
#portal [style*="#8FA098"]{color:var(--ink-soft)!important}
.trust-car{--tc-accent:var(--green-deep)}
'''
snip=open('trust-carousel-snippet.html',encoding='utf-8').read()
tcss=re.search(r'<style>(.*?)</style>',snip,re.S).group(1)
markup=snip.split('-->',1)[1].split('<script>',1)[0].strip()
js=re.search(r'<script>(.*?)</script>',snip,re.S).group(1)
s=open('index.html',encoding='utf-8').read()
assert 'trustCar' not in s,'already applied'
s=s.replace('</style>',tcss+CSS+'</style>',1)
i=s.index('<section id="trust">'); j=s.index('</section>',i)
s=s[:j]+'<div class="wrap" style="margin-top:72px">\n'+markup+'\n</div>\n'+s[j:]
k=s.rindex('</script>'); s=s[:k]+js+'\n'+s[k:]
open('index.html','w',encoding='utf-8').write(s); print('done')
