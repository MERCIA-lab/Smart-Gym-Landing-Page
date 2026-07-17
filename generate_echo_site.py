from pathlib import Path

root = Path('.')
css_dir = root / 'css'
images_dir = root / 'images'
css_dir.mkdir(exist_ok=True)
images_dir.mkdir(exist_ok=True)

style = '''/* Echo Fitness stylesheet */
:root {
  --black: #000000;
  --white: #ffffff;
  --surface: #111111;
  --panel: #141414;
  --border: rgba(255,255,255,0.12);
  --accent: #ff0000;
  --text: #f5f5f5;
  --muted: #b3b3b3;
  --max-width: 1200px;
}

*, *::before, *::after {
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
}

body {
  margin: 0;
  min-height: 100%;
  background: var(--black);
  color: var(--text);
  font-family: Inter, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  line-height: 1.6;
}

img {
  display: block;
  width: 100%;
  height: auto;
}

a {
  color: inherit;
  text-decoration: none;
}

button,
input,
textarea,
select {
  font: inherit;
  color: inherit;
}

button,
a.button {
  background: transparent;
  border: 1px solid var(--white);
  color: var(--white);
  padding: 1rem 1.3rem;
  text-transform: uppercase;
  letter-spacing: 0.14em;
  font-weight: 700;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

button:hover,
button:focus,
a.button:hover,
a.button:focus {
  background: var(--white);
  color: var(--black);
}

body,
input,
textarea,
button,
select {
  outline: none;
}

.page-shell {
  padding-top: 100px;
  min-height: 100vh;
  overflow-x: hidden;
}

.navbar {
  position: fixed;
  inset: 0 auto auto 0;
  z-index: 50;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 24px 32px;
  width: 100%;
  background: rgba(0,0,0,0.72);
  border-bottom: 1px solid var(--border);
}

.logo {
  display: flex;
  align-items: center;
  gap: 1rem;
  text-transform: uppercase;
  letter-spacing: 0.25em;
  font-weight: 900;
}

.logo-mark {
  width: 44px;
  height: 44px;
}

.logo-text {
  display: grid;
  line-height: 1;
}

.logo-text span:first-child {
  font-size: 1.1rem;
}

.logo-text span:last-child {
  font-size: 0.7rem;
  letter-spacing: 0.35em;
  font-weight: 300;
}

.nav-links {
  display: flex;
  gap: 2rem;
  text-transform: uppercase;
  letter-spacing: 0.18em;
  font-size: 0.85rem;
}

.nav-links a {
  position: relative;
}

.nav-links a::after {
  content: "";
  position: absolute;
  left: 0;
  bottom: -6px;
  width: 0;
  height: 1px;
  background: var(--white);
  transition: width 0.25s ease;
}

.nav-links a:hover::after,
.nav-links a:focus::after {
  width: 100%;
}

.hero {
  min-height: calc(100vh - 100px);
  display: grid;
  place-items: center;
  text-align: center;
  padding: 0 32px;
  background: linear-gradient(180deg, rgba(0,0,0,0.35), rgba(0,0,0,0.95));
}

.hero-content {
  max-width: 920px;
  width: 100%;
  display: grid;
  gap: 1.5rem;
}

.hero-overline,
.section-heading,
.footer-note {
  text-transform: uppercase;
  letter-spacing: 0.35em;
  color: var(--muted);
  font-size: 0.75rem;
}

.hero-title {
  font-size: clamp(3rem, 8vw, 6.5rem);
  line-height: 0.9;
  font-weight: 900;
}

.hero-copy,
.section-copy,
.card p,
.contact-form p {
  color: var(--muted);
  max-width: 720px;
  margin: 0 auto;
  letter-spacing: 0.03em;
}

.heroflex {
  display: inline-flex;
  gap: 1rem;
  flex-wrap: wrap;
  justify-content: center;
}

.section {
  padding: 120px 32px;
}

.container {
  max-width: var(--max-width);
  margin: 0 auto;
  display: grid;
  gap: 2rem;
}

.section-title {
  font-size: clamp(2rem, 4vw, 3.5rem);
  font-weight: 900;
  text-transform: uppercase;
  letter-spacing: 0.08em;
}

.grid-3,
.coach-grid,
.program-grid,
.plan-grid,
.testimonial-grid,
.gallery-grid {
  display: grid;
  gap: 1.5rem;
}

.grid-3,
.program-grid,
.coach-grid,
.plan-grid,
.testimonial-grid,
.gallery-grid,
.stats-row {
  grid-template-columns: repeat(3, minmax(0, 1fr));
}

.stats-row {
  grid-template-columns: repeat(4, minmax(0, 1fr));
}

.card,
.program-card,
.trainer-card,
.plan-card,
.faq-item,
.contact-panel,
.dashboard-card {
  background: var(--surface);
  border: 1px solid var(--border);
  padding: 1.6rem;
}

.program-card img,
.trainer-card img,
.gallery-card img,
.placeholder-img,
.about-grid img,
.split-grid img {
  width: 100%;
  min-height: 220px;
  object-fit: cover;
}

.program-card h3,
.trainer-card h3,
.plan-card h3,
.faq-item h3,
.dashboard-card h3 {
  font-size: 1.25rem;
  margin: 1rem 0 0.75rem;
  text-transform: uppercase;
}

.program-card p,
.trainer-card p,
.plan-card p,
.gallery-card p,
.dashboard-card p,
.contact-panel p {
  color: var(--muted);
}

.stats-row strong {
  display: block;
  font-size: 2.5rem;
  font-weight: 900;
  margin-bottom: 0.75rem;
}

.stats-row span,
.plan-card span,
.card span,
.contact-panel span,
.dashboard-card span {
  display: block;
  color: var(--muted);
  text-transform: uppercase;
  letter-spacing: 0.25em;
}

.program-card a,
.section-action a,
.contact-form a,
.dashboard-actions a {
  display: inline-flex;
  margin-top: 1rem;
}

.about-grid,
.split-grid {
  display: grid;
  grid-template-columns: 1.2fr 0.8fr;
  gap: 1.5rem;
}

.contact-form,
.login-form,
.signup-form,
.accordion,
.dashboard-actions {
  display: grid;
  gap: 1rem;
}

input,
textarea,
select {
  width: 100%;
  padding: 1rem;
  background: transparent;
  border: 1px solid var(--border);
  color: var(--white);
}

textarea {
  resize: vertical;
}

input::placeholder,
textarea::placeholder {
  color: var(--muted);
}

.contact-panel {
  display: grid;
  gap: 1rem;
}

.contact-panel strong,
.contact-panel span {
  text-transform: uppercase;
  letter-spacing: 0.25em;
  color: var(--muted);
}

.accordion .faq-item {
  border: 1px solid var(--border);
}

.accordion input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.accordion label {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  cursor: pointer;
}

.accordion label::after {
  content: "+";
  font-size: 1.3rem;
}

.accordion input:checked + label::after {
  content: "–";
}

.accordion .panel {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.3s ease;
  padding: 0 1rem;
}

.accordion input:checked + label + .panel {
  max-height: 280px;
  padding: 1rem;
}

.plan-grid {
  grid-template-columns: repeat(3, minmax(0, 1fr));
}

.plan-card strong {
  display: block;
  font-size: 2rem;
  margin: 1rem 0;
}

.plan-card ul {
  list-style: none;
  margin: 1rem 0 0;
  padding: 0;
}

.plan-card li::before {
  content: "•";
  margin-right: 0.75rem;
  color: var(--accent);
}

.timetable {
  width: 100%;
  border-collapse: collapse;
}

.timetable th,
.timetable td {
  border: 1px solid var(--border);
  padding: 1rem;
  text-transform: uppercase;
  font-size: 0.85rem;
}

.timetable th {
  background: #111;
}

.footer {
  padding: 64px 32px;
  background: #090909;
  border-top: 1px solid var(--border);
}

.footer-grid {
  display: grid;
  gap: 1rem;
  max-width: var(--max-width);
  margin: 0 auto;
}

.footer-links {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
}

.footer-note {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 1rem;
  margin-top: 2rem;
  color: var(--muted);
}

@media (max-width: 1000px) {
  .nav-links {
    display: none;
  }

  .about-grid,
  .split-grid,
  .compare-grid,
  .grid-3,
  .plan-grid,
  .program-grid,
  .coach-grid,
  .testimonial-grid,
  .gallery-grid,
  .stats-row {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 640px) {
  .navbar {
    padding: 18px 20px;
  }

  .page-shell {
    padding-top: 92px;
  }

  .hero {
    padding: 0 18px;
  }

  .hero-title {
    font-size: 3rem;
  }

  .section {
    padding: 90px 18px;
  }
}
'''

(root / 'css' / 'style.css').write_text(style, encoding='utf-8')

logo_svg = '''<?xml version="1.0" encoding="UTF-8"?>
<svg width="120" height="120" viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
  <rect width="120" height="120" fill="#000"/>
  <path d="M24 96 L24 28 L38 14 L58 28 L74 14 L90 28 L90 96" fill="none" stroke="#fff" stroke-width="8"/>
  <line x1="12" y1="88" x2="108" y2="88" stroke="#fff" stroke-width="8"/>
</svg>
'''

placeholder_svg = '''<?xml version="1.0" encoding="UTF-8"?>
<svg width="400" height="260" viewBox="0 0 400 260" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="260" fill="#111"/>
  <line x1="0" y1="0" x2="400" y2="260" stroke="#555" stroke-width="4"/>
  <line x1="0" y1="260" x2="400" y2="0" stroke="#555" stroke-width="4"/>
  <text x="200" y="140" text-anchor="middle" fill="#888" font-size="24" font-family="Arial, Helvetica, sans-serif">IMAGE</text>
</svg>
'''

(images_dir / 'logo-echo.svg').write_text(logo_svg, encoding='utf-8')
(images_dir / 'placeholder.svg').write_text(placeholder_svg, encoding='utf-8')

nav_html = '''<nav class="navbar">
  <a href="index.html" class="logo">
    <img src="images/logo-echo.svg" alt="Echo Fitness" class="logo-mark">
    <span class="logo-text"><span>ECHO</span><span>FITNESS</span></span>
  </a>
  <div class="nav-links">
    <a href="index.html">Home</a>
    <a href="programs.html">Programs</a>
    <a href="trainers.html">Trainers</a>
    <a href="membership.html">Membership</a>
    <a href="contact.html">Contact</a>
  </div>
</nav>
'''

footer_html = '''<footer class="footer">
  <div class="footer-grid container">
    <div>
      <p class="logo">ECHO FITNESS</p>
      <p class="hero-copy">Built for strength, speed, and relentless progress.</p>
    </div>
    <div class="footer-links">
      <a href="index.html">Home</a>
      <a href="programs.html">Programs</a>
      <a href="trainers.html">Trainers</a>
      <a href="membership.html">Membership</a>
      <a href="contact.html">Contact</a>
    </div>
  </div>
  <div class="footer-note container">
    <span>© 2026 ECHO FITNESS</span>
    <span><a href="about.html">About</a> | <a href="faq.html">FAQ</a> | <a href="contact.html">Support</a></span>
  </div>
</footer>
'''

head = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body class="page-shell">
'''

pages = {}

pages['index.html'] = ('Echo Fitness', f'''{nav_html}
  <section class="hero">
    <div class="hero-content">
      <div class="hero-overline">Black & White Training</div>
      <h1 class="hero-title">THE WEIGHT DOESN'T LIE</h1>
      <p class="hero-copy">Echo Fitness is a stripped-back gym for athletes who want hard training, sharp coaching, and performance that proves itself.</p>
      <div class="heroflex"><a class="button" href="membership.html">Join Now</a><a class="button" href="programs.html">View Programs</a></div>
    </div>
  </section>
  <section class="section">
    <div class="container stats-row">
      <article class="card"><strong>24/7</strong><span>Access</span></article>
      <article class="card"><strong>50+</strong><span>Weekly Classes</span></article>
      <article class="card"><strong>15</strong><span>Elite Coaches</span></article>
      <article class="card"><strong>2000+</strong><span>Members</span></article>
    </div>
  </section>
  <section class="section">
    <div class="container">
      <h2 class="section-title">Featured Programs</h2>
      <div class="program-grid">
        <article class="program-card"><img src="images/placeholder.svg" alt="Strength"><h3>Strength & Power</h3><p>Raw barbell programs for force, consistency, and grip strength.</p><a class="button" href="program-strength.html">Learn More</a></article>
        <article class="program-card"><img src="images/placeholder.svg" alt="HIIT"><h3>HIIT Cardio</h3><p>Metabolic intervals for capacity and grit.</p><a class="button" href="program-hiit.html">Learn More</a></article>
        <article class="program-card"><img src="images/placeholder.svg" alt="Mobility"><h3>Yoga & Mobility</h3><p>Recovery sessions focused on mobility, breathing, and resilience.</p><a class="button" href="program-yoga.html">Learn More</a></article>
      </div>
    </div>
  </section>
  <section class="section">
    <div class="container about-grid">
      <div>
        <div class="section-heading">Why Echo</div>
        <h2 class="section-title">Built for serious athletes.</h2>
        <p class="section-copy">No filters. No gimmicks. Just a training space where every rep, session, and coach matters.</p>
        <div class="heroflex"><a class="button" href="about.html">Our Story</a><a class="button" href="trainers.html">Meet Coaches</a></div>
      </div>
      <img src="images/placeholder.svg" alt="Gym interior">
    </div>
  </section>
  <section class="section">
    <div class="container plan-grid">
      <article class="plan-card"><h3>Basic</h3><strong>$39/mo</strong><ul><li>Gym access</li><li>4 classes</li></ul><a class="button" href="membership.html">Choose</a></article>
      <article class="plan-card"><h3>Pro</h3><strong>$79/mo</strong><ul><li>Unlimited classes</li><li>2 coach sessions</li></ul><a class="button" href="membership.html">Choose</a></article>
      <article class="plan-card"><h3>Elite</h3><strong>$129/mo</strong><ul><li>Unlimited access</li><li>4 coach sessions</li><li>Nutrition support</li></ul><a class="button" href="membership.html">Choose</a></article>
    </div>
  </section>
  <section class="section">
    <div class="container testimonial-grid">
      <article class="card"><p>"Every session pushes me harder than the last."</p></article>
      <article class="card"><p>"This gym keeps me accountable and consistent."</p></article>
      <article class="card"><p>"The coaches are precise and the facility is real."</p></article>
    </div>
  </section>
  {footer_html}
''')

pages['programs.html'] = ('Programs | Echo Fitness', f'''{nav_html}
  <section class="section">
    <div class="container">
      <h2 class="section-title">Programs</h2>
      <div class="program-grid">
        <article class="program-card"><img src="images/placeholder.svg" alt="Strength"><h3>Strength & Power</h3><p>Barbell progressions for strength and durability.</p><a class="button" href="program-strength.html">Open</a></article>
        <article class="program-card"><img src="images/placeholder.svg" alt="HIIT"><h3>HIIT Cardio</h3><p>Conditioning built around intervals and pace.</p><a class="button" href="program-hiit.html">Open</a></article>
        <article class="program-card"><img src="images/placeholder.svg" alt="Yoga"><h3>Yoga & Mobility</h3><p>Recovery tools for better movement and durability.</p><a class="button" href="program-yoga.html">Open</a></article>
        <article class="program-card"><img src="images/placeholder.svg" alt="Olympic"><h3>Olympic Lifting</h3><p>Technique-focused snatch and clean & jerk cycles.</p><a class="button" href="program-olympic.html">Open</a></article>
        <article class="program-card"><img src="images/placeholder.svg" alt="CrossFit"><h3>CrossFit WOD</h3><p>Functional workouts with strength and speed.</p><a class="button" href="program-crossfit.html">Open</a></article>
        <article class="program-card"><img src="images/placeholder.svg" alt="Hypertrophy"><h3>Hypertrophy</h3><p>Volume-focused sessions for muscle and mass.</p><a class="button" href="program-bodybuilding.html">Open</a></article>
        <article class="program-card"><img src="images/placeholder.svg" alt="Boxing"><h3>Boxing & MMA</h3><p>Conditioning and striking drills for athletes.</p><a class="button" href="program-boxing.html">Open</a></article>
        <article class="program-card"><img src="images/placeholder.svg" alt="Endurance"><h3>Endurance</h3><p>Longer effort training for capacity and recovery.</p><a class="button" href="program-endurance.html">Open</a></article>
      </div>
    </div>
  </section>
  {footer_html}
''')

program_pages = [
    ('program-strength.html', 'Strength & Power', 'Barbell strength training for raw force and consistency.', 'Mon/Wed/Fri — 06:00 / 18:00', 'Coach Alex'),
    ('program-hiit.html', 'HIIT Cardio', 'High-intensity intervals designed for conditioning and grit.', 'Tue/Thu/Sat — 07:00 / 19:00', 'Coach Brooke'),
    ('program-yoga.html', 'Yoga & Mobility', 'Recovery, mobility, and breath work to support heavy training.', 'Mon/Wed/Fri — 08:00 / 20:00', 'Coach Maia'),
    ('program-olympic.html', 'Olympic Lifting', 'Technique-focused snatch and clean & jerk sessions.', 'Tue/Thu — 18:00 / 19:30', 'Coach Danny'),
    ('program-crossfit.html', 'CrossFit WOD', 'Functional workouts with strength, speed, and stamina.', 'Mon/Wed/Fri — 17:00 / 18:00', 'Coach Kate'),
    ('program-bodybuilding.html', 'Hypertrophy', 'Volume-driven muscle-building sessions.', 'Tue/Thu/Sat — 16:00 / 20:00', 'Coach Lucas'),
    ('program-boxing.html', 'Boxing & MMA', 'Striking and conditioning drills for combat-ready fitness.', 'Wed/Sat — 18:30 / 19:30', 'Coach Zara'),
    ('program-endurance.html', 'Endurance', 'Longer effort circuits for aerobic capacity and recovery.', 'Sat/Sun — 07:00 / 10:00', 'Coach Noah'),
]

for filename, title, summary, schedule, coach in program_pages:
    pages[filename] = (f'{title} | Echo Fitness', f'''{nav_html}
  <section class="section">
    <div class="container about-grid">
      <div>
        <div class="section-heading">Program</div>
        <h2 class="section-title">{title}</h2>
        <p class="section-copy">{summary}</p>
        <div class="section-copy"><strong>Schedule:</strong> {schedule}</div>
        <div class="section-copy"><strong>Coach:</strong> {coach}</div>
        <div class="heroflex"><a class="button" href="signup.html">Join This Program</a><a class="button" href="programs.html">Back to Programs</a></div>
      </div>
      <img src="images/placeholder.svg" alt="{title}">
    </div>
  </section>
  {footer_html}
''')

pages['trainers.html'] = ('Trainers | Echo Fitness', f'''{nav_html}
  <section class="section">
    <div class="container">
      <h2 class="section-title">Trainers</h2>
      <div class="coach-grid">
        <article class="trainer-card"><img src="images/placeholder.svg" alt="Coach Alex"><h3>ALEX</h3><p>Strength coach.</p></article>
        <article class="trainer-card"><img src="images/placeholder.svg" alt="Coach Brooke"><h3>BROOKE</h3><p>Conditioning coach.</p></article>
        <article class="trainer-card"><img src="images/placeholder.svg" alt="Coach Maia"><h3>MAIA</h3><p>Mobility coach.</p></article>
        <article class="trainer-card"><img src="images/placeholder.svg" alt="Coach Danny"><h3>DANNY</h3><p>Olympic lifting specialist.</p></article>
        <article class="trainer-card"><img src="images/placeholder.svg" alt="Coach Kate"><h3>KATE</h3><p>Functional fitness coach.</p></article>
        <article class="trainer-card"><img src="images/placeholder.svg" alt="Coach Zara"><h3>ZARA</h3><p>Boxing coach.</p></article>
      </div>
    </div>
  </section>
  {footer_html}
''')

pages['schedule.html'] = ('Schedule | Echo Fitness', f'''{nav_html}
  <section class="section">
    <div class="container">
      <h2 class="section-title">Weekly Schedule</h2>
      <div class="card">
        <p class="section-copy">Plan your week around strength, conditioning, and recovery sessions.</p>
        <table class="timetable">
          <thead><tr><th>Time</th><th>Mon</th><th>Tue</th><th>Wed</th><th>Thu</th><th>Fri</th><th>Sat</th><th>Sun</th></tr></thead>
          <tbody>
            <tr><td>06:00</td><td>Strength</td><td></td><td>Strength</td><td></td><td>Strength</td><td>Endurance</td><td></td></tr>
            <tr><td>08:00</td><td>Yoga</td><td></td><td>Yoga</td><td></td><td></td><td>Endurance</td><td></td></tr>
            <tr><td>17:00</td><td>CrossFit</td><td></td><td>CrossFit</td><td></td><td>Bodybuilding</td><td></td><td></td></tr>
            <tr><td>19:00</td><td></td><td>HIIT</td><td></td><td>Olympic</td><td></td><td>Boxing</td><td></td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>
  {footer_html}
''')

pages['membership.html'] = ('Membership | Echo Fitness', f'''{nav_html}
  <section class="section">
    <div class="container">
      <h2 class="section-title">Membership</h2>
      <div class="plan-grid">
        <article class="plan-card"><h3>Basic</h3><strong>$39/mo</strong><ul><li>Gym access</li><li>4 classes</li></ul><a class="button" href="signup.html">Select</a></article>
        <article class="plan-card"><h3>Pro</h3><strong>$79/mo</strong><ul><li>Unlimited classes</li><li>2 coach sessions</li></ul><a class="button" href="signup.html">Select</a></article>
        <article class="plan-card"><h3>Elite</h3><strong>$129/mo</strong><ul><li>Unlimited access</li><li>4 coach sessions</li><li>Nutrition support</li></ul><a class="button" href="signup.html">Select</a></article>
      </div>
      <div class="card"><p class="section-copy">Membership includes facility access, class booking, and coach support. Elite members receive extra recovery and nutrition guidance.</p></div>
    </div>
  </section>
  {footer_html}
''')

pages['about.html'] = ('About | Echo Fitness', f'''{nav_html}
  <section class="section">
    <div class="container split-grid">
      <div>
        <div class="section-heading">About</div>
        <h2 class="section-title">A gym for athletes that train with intent.</h2>
        <p class="section-copy">Echo Fitness is built around real programming, expert coaching, and a culture that values consistency over trends.</p>
        <a class="button" href="membership.html">Join the Team</a>
      </div>
      <img src="images/placeholder.svg" alt="Gym interior">
    </div>
  </section>
  {footer_html}
''')

pages['nutrition.html'] = ('Nutrition | Echo Fitness', f'''{nav_html}
  <section class="section">
    <div class="container about-grid">
      <div>
        <div class="section-heading">Nutrition</div>
        <h2 class="section-title">Fuel performance with purpose.</h2>
        <p class="section-copy">We keep nutrition simple: protein, carbs, and fats aligned to your training goals.</p>
      </div>
      <img src="images/placeholder.svg" alt="Nutrition planning">
    </div>
  </section>
  <section class="section">
    <div class="container card">
      <h3>Macro Guidance</h3>
      <p class="section-copy">Choose a plan based on your goal: cut, maintain, or build. Adjust calories around training and recovery sessions.</p>
    </div>
  </section>
  {footer_html}
''')

pages['success-stories.html'] = ('Success Stories | Echo Fitness', f'''{nav_html}
  <section class="section">
    <div class="container">
      <h2 class="section-title">Success Stories</h2>
      <div class="gallery-grid">
        <article class="card"><img src="images/placeholder.svg" alt="Transformation"><p>"Strength and confidence gained in 12 weeks."</p></article>
        <article class="card"><img src="images/placeholder.svg" alt="Transformation"><p>"Consistent work gave me better results than shortcuts."</p></article>
        <article class="card"><img src="images/placeholder.svg" alt="Transformation"><p>"The coaches kept my training honest and effective."</p></article>
      </div>
    </div>
  </section>
  {footer_html}
''')

pages['blog.html'] = ('Blog | Echo Fitness', f'''{nav_html}
  <section class="section">
    <div class="container">
      <h2 class="section-title">Blog</h2>
      <div class="program-grid">
        <article class="program-card"><h3>Deadlift Setup</h3><p>Improve your pull with a stronger base.</p><a class="button" href="blog.html">Read</a></article>
        <article class="program-card"><h3>Recovery Routine</h3><p>Train harder through better recovery habits.</p><a class="button" href="blog.html">Read</a></article>
        <article class="program-card"><h3>Training Blocks</h3><p>Structure load and rest for long-term progress.</p><a class="button" href="blog.html">Read</a></article>
      </div>
    </div>
  </section>
  {footer_html}
''')

pages['faq.html'] = ('FAQ | Echo Fitness', f'''{nav_html}
  <section class="section">
    <div class="container">
      <h2 class="section-title">FAQ</h2>
      <div class="accordion">
        <div class="faq-item"><input type="checkbox" id="faq-a"><label for="faq-a">Can I try the gym first?</label><div class="panel"><p>Yes. New members can claim a one-week trial.</p></div></div>
        <div class="faq-item"><input type="checkbox" id="faq-b"><label for="faq-b">What should I bring?</label><div class="panel"><p>Bring gym shoes, a towel, water, and chalk for heavy lifts.</p></div></div>
        <div class="faq-item"><input type="checkbox" id="faq-c"><label for="faq-c">Can I freeze my membership?</label><div class="panel"><p>Membership holds are available for medical reasons and extended travel.</p></div></div>
      </div>
    </div>
  </section>
  {footer_html}
''')

pages['contact.html'] = ('Contact | Echo Fitness', f'''{nav_html}
  <section class="section">
    <div class="container split-grid">
      <div class="contact-panel">
        <div class="section-heading">Contact</div>
        <h2 class="section-title">Get in touch.</h2>
        <p class="section-copy">Questions, booking, or membership help. Reach out and we’ll respond quickly.</p>
        <div><strong>Phone</strong><p>(123) 456-7890</p><strong>Email</strong><p>hello@echofitness.com</p></div>
      </div>
      <form class="contact-form">
        <input type="text" placeholder="Name">
        <input type="email" placeholder="Email">
        <textarea rows="5" placeholder="Message"></textarea>
        <a class="button" href="signup.html">Send Message</a>
      </form>
    </div>
  </section>
  {footer_html}
''')

pages['login.html'] = ('Login | Echo Fitness', f'''{nav_html}
  <section class="section">
    <div class="container contact-form">
      <div class="section-heading">Member Login</div>
      <h2 class="section-title">Access your account.</h2>
      <input type="email" placeholder="Email">
      <input type="password" placeholder="Password">
      <button type="button">Sign In</button>
      <a class="button" href="signup.html">New? Create account</a>
    </div>
  </section>
  {footer_html}
''')

pages['signup.html'] = ('Sign Up | Echo Fitness', f'''{nav_html}
  <section class="section">
    <div class="container contact-form">
      <div class="section-heading">Sign Up</div>
      <h2 class="section-title">Start training today.</h2>
      <input type="text" placeholder="Full Name">
      <input type="email" placeholder="Email">
      <input type="text" placeholder="Phone">
      <input type="password" placeholder="Password">
      <input type="password" placeholder="Confirm Password">
      <button type="button">Create Account</button>
      <a class="button" href="login.html">Already a member? Login</a>
    </div>
  </section>
  {footer_html}
''')

pages['dashboard.html'] = ('Dashboard | Echo Fitness', f'''{nav_html}
  <section class="section">
    <div class="container">
      <h2 class="section-title">Dashboard</h2>
      <div class="stats-row">
        <article class="dashboard-card"><span>Membership</span><h3>Elite active</h3><p>Renew in 30 days</p></article>
        <article class="dashboard-card"><span>Next Class</span><h3>Strength</h3><p>Today 18:00</p></article>
      </div>
      <div class="grid-3">
        <article class="dashboard-card"><h3>Progress</h3><p>4 of 5 sessions completed this week.</p></article>
        <article class="dashboard-card"><h3>Upcoming</h3><p>Wed — HIIT • Fri — Olympic</p></article>
        <article class="dashboard-card"><h3>Notes</h3><p>Continue to load, recover, and hit consistency.</p></article>
      </div>
      <div class="dashboard-actions">
        <a class="button" href="membership.html">Manage Plan</a>
        <a class="button" href="contact.html">Contact Coach</a>
      </div>
    </div>
  </section>
  {footer_html}
''')

for filename, (title, content) in pages.items():
    (root / filename).write_text(head.format(title=title) + content + '\n</body>\n</html>\n', encoding='utf-8')

print(f'Wrote {len(pages)} pages to {root.resolve()}')
