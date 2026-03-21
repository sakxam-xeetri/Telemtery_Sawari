# This temp file has been processed and can be safely deleted.
# To delete: del "d:\S.P.A.R.K\_tmp_write_landing.py"
$envFile = __DIR__ . '/.env';
$env = [];
if (file_exists($envFile)) {
  foreach (file($envFile, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES) as $line) {
    if (str_starts_with(trim($line), '#'))
      continue;
    if (strpos($line, '=') === false)
      continue;
    [$key, $value] = explode('=', $line, 2);
    $env[trim($key)] = trim($value);
  }
}
$groqApiKey = $env['GROQ_API_KEY'] ?? '';
?>
<!doctype html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Sawari — Kathmandu Valley Public Transit Navigator</title>
  <meta name="description" content="Navigate Kathmandu Valley's buses, tempos, and microbuses with real-time tracking, AI-powered route planning, and accurate fare estimates. No app download needed." />
  <meta name="keywords" content="Kathmandu bus, Nepal transit, public transport, bus routes, Sajha Yatayat, microbus, Lalitpur, Bhaktapur" />
  <meta property="og:title" content="Sawari — Kathmandu Valley Public Transit Navigator" />
  <meta property="og:description" content="Find the right bus, know the fare, and track your ride in real time across Kathmandu, Lalitpur, and Bhaktapur." />
  <meta property="og:type" content="website" />
  <meta property="og:image" content="logo/logo-transparent.png" />
  <meta name="theme-color" content="#0f1117" />
  <link rel="icon" type="image/png" href="logo/logo-icon.png" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" />
  <link rel="stylesheet" href="landing.css" />
</head>

<body>
  <!-- Page Loader -->
  <div class="page-loader" id="pageLoader">
    <div class="loader-inner">
      <div class="loader-logo"><img src="logo/logo-white.png" alt="Sawari" width="120" height="40" /></div>
      <div class="loader-bar"><div class="loader-bar-fill"></div></div>
    </div>
  </div>

  <!-- Navbar -->
  <header class="navbar" id="top">
    <div class="navbar-inner">
      <a href="#top" class="logo" aria-label="Sawari Home">
        <img src="logo/logo-white.png" alt="Sawari" class="logo-white" width="110" height="36" />
        <img src="logo/logo-black.png" alt="Sawari" class="logo-black" width="110" height="36" />
      </a>
      <nav class="nav-links" id="nav-links" aria-label="Main navigation">
        <a href="#about">About</a>
        <a href="#how">How It Works</a>
        <a href="#features">Features</a>
        <a href="#gallery">Gallery</a>
        <a href="#ask">Ask AI</a>
        <a href="#contribute">Contribute</a>
      </nav>
      <a href="index.php" class="btn-cta-nav">Open Navigator <i class="fa-solid fa-arrow-right"></i></a>
      <button class="mobile-toggle" id="mobile-toggle" aria-label="Toggle menu">
        <i class="fa-solid fa-bars"></i>
      </button>
    </div>
  </header>

  <main>
    <!-- Hero -->
    <section class="hero" id="hero">
      <div class="hero-bg">
        <img src="gallery/landing.jpg" alt="Kathmandu Valley transit" width="1920" height="1080" />
      </div>
      <div class="hero-overlay"></div>
      <div class="hero-content">
        <span class="hero-badge"><i class="fa-solid fa-sparkles"></i> AI-Powered Transit Navigator</span>
        <h1>Navigate Kathmandu Valley<br><em>with confidence.</em></h1>
        <p class="hero-desc">Find the right bus, know the fare, and track your ride in real time. Sawari brings smart route planning to Kathmandu, Lalitpur, and Bhaktapur — no app download needed.</p>
        <div class="hero-actions">
          <a class="btn-hero" href="index.php"><i class="fa-solid fa-compass"></i> Start Your Journey</a>
          <a class="btn-hero-outline" href="#how"><i class="fa-solid fa-play"></i> See How It Works</a>
        </div>
        <div class="hero-trust">
          <div class="hero-trust-item">
            <i class="fa-solid fa-check-circle"></i>
            <span>100% Free</span>
          </div>
          <div class="hero-trust-item">
            <i class="fa-solid fa-check-circle"></i>
            <span>No Sign-up Required</span>
          </div>
          <div class="hero-trust-item">
            <i class="fa-solid fa-check-circle"></i>
            <span>Works on Any Device</span>
          </div>
        </div>
      </div>
    </section>

    <!-- Stats Bar -->
    <section class="stats-strip" aria-label="Platform statistics">
      <div class="stats-strip-inner">
        <div class="stat-item">
          <span class="stat-number" data-target="50">0</span>
          <span class="stat-label">Bus Routes</span>
        </div>
        <div class="stat-divider"></div>
        <div class="stat-item">
          <span class="stat-number" data-target="200">0</span>
          <span class="stat-label">Stops Covered</span>
        </div>
        <div class="stat-divider"></div>
        <div class="stat-item">
          <span class="stat-number" data-target="15">0</span>
          <span class="stat-label">Transit Operators</span>
        </div>
        <div class="stat-divider"></div>
        <div class="stat-item">
          <span class="stat-number" data-target="3">0</span>
          <span class="stat-label">Districts Covered</span>
        </div>
      </div>
    </section>

    <!-- About -->
    <section id="about" class="section">
      <div class="container">
        <div class="section-header reveal">
          <span class="section-tag">About Sawari</span>
          <h2>Built for real commuters</h2>
          <p class="section-subtitle">Getting around Kathmandu by bus is confusing — dozens of routes, no official app, and you're stuck asking strangers. Sawari fixes that.</p>
        </div>
        <div class="about-grid">
          <article class="about-card reveal">
            <div class="about-card-img">
              <img src="gallery/routes.jpg" alt="Kathmandu bus routes" loading="lazy" width="600" height="400" />
            </div>
            <div class="about-card-body">
              <div class="about-icon"><i class="fa-solid fa-map-location-dot"></i></div>
              <h3>Tailored for the Valley</h3>
              <p>Understands local route names, stop landmarks, and transit patterns across Kathmandu, Lalitpur, and Bhaktapur — search the way you actually speak.</p>
            </div>
          </article>
          <article class="about-card reveal">
            <div class="about-card-img">
              <img src="gallery/high-tech-buses.jpg" alt="Modern electric buses" loading="lazy" width="600" height="400" />
            </div>
            <div class="about-card-body">
              <div class="about-icon"><i class="fa-solid fa-globe"></i></div>
              <h3>Works in Your Browser</h3>
              <p>No downloads, no sign-ups. Open Sawari in any browser, type where you're going, and get moving instantly.</p>
            </div>
          </article>
          <article class="about-card reveal">
            <div class="about-card-img">
              <img src="gallery/nepal.jpg" alt="Nepal public transit" loading="lazy" width="600" height="400" />
            </div>
            <div class="about-card-body">
              <div class="about-icon"><i class="fa-solid fa-users"></i></div>
              <h3>Community Powered</h3>
              <p>Riders report missing stops and route changes — every suggestion is reviewed and merged to keep data accurate for everyone.</p>
            </div>
          </article>
        </div>
      </div>
    </section>

    <!-- How It Works -->
    <section id="how" class="section section-dark">
      <div class="container">
        <div class="section-header section-header-light reveal">
          <span class="section-tag">How It Works</span>
          <h2>Four steps to your destination</h2>
          <p class="section-subtitle">From opening the app to catching your bus — it's simple and fast.</p>
        </div>
        <div class="steps-grid">
          <article class="step-card reveal">
            <div class="step-number">01</div>
            <div class="step-img">
              <img src="gallery/SajhaBus_20220707134627.jpg" alt="Enter destination" loading="lazy" width="600" height="400" />
            </div>
            <h3>Tell us where you're going</h3>
            <p>Type your destination in plain language — "Ratnapark to Lagankhel" or drop a pin on the map.</p>
          </article>
          <article class="step-card reveal">
            <div class="step-number">02</div>
            <div class="step-img">
              <img src="gallery/sajha-yatayat-kathmandu-narayangadh-shuttle-service-1758693554.jpg" alt="See routes" loading="lazy" width="600" height="400" />
            </div>
            <h3>Explore route options</h3>
            <p>See direct buses and smart transfer combos ranked by speed and convenience.</p>
          </article>
          <article class="step-card reveal">
            <div class="step-number">03</div>
            <div class="step-img">
              <img src="gallery/samakhusi-yatayat-1729569860.jpg" alt="Check fare" loading="lazy" width="600" height="400" />
            </div>
            <h3>Know your fare upfront</h3>
            <p>Get fare estimates based on official DoTM tariff rates — no surprises at the conductor's window.</p>
          </article>
          <article class="step-card reveal">
            <div class="step-number">04</div>
            <div class="step-img">
              <img src="gallery/sajha1.jpg" alt="Track live buses" loading="lazy" width="600" height="400" />
            </div>
            <h3>Catch your bus</h3>
            <p>Live tracking shows approaching buses so you can time your arrival at the stop perfectly.</p>
          </article>
        </div>
      </div>
    </section>

    <!-- Features -->
    <section id="features" class="section">
      <div class="container">
        <div class="section-header reveal">
          <span class="section-tag">Features</span>
          <h2>Everything you need to ride</h2>
          <p class="section-subtitle">A powerful toolkit built for real-world public transit in Nepal.</p>
        </div>
        <div class="features-grid">
          <article class="feature-card reveal">
            <div class="feature-icon"><i class="fa-solid fa-route"></i></div>
            <h3>Smart Route Planning</h3>
            <p>Find direct rides or multi-bus transfers with stop-level precision across the entire valley.</p>
          </article>
          <article class="feature-card reveal">
            <div class="feature-icon"><i class="fa-solid fa-ticket"></i></div>
            <h3>Accurate Fare Estimates</h3>
            <p>Know what you'll pay before you board — based on real Nepal DoTM tariff rates in Rs 5 increments.</p>
          </article>
          <article class="feature-card feature-card-highlight reveal">
            <div class="feature-icon"><i class="fa-solid fa-wand-magic-sparkles"></i></div>
            <h3>AI-Powered Search</h3>
            <p>Type naturally — "Kalanki bata Chabahil" or "bus from Ratnapark to Lagankhel" — both just work.</p>
          </article>
          <article class="feature-card reveal">
            <div class="feature-icon"><i class="fa-solid fa-location-arrow"></i></div>
            <h3>GPS &amp; Nearby Stops</h3>
            <p>Instantly discover the closest stops and which buses pass through them using your location.</p>
          </article>
          <article class="feature-card reveal">
            <div class="feature-icon"><i class="fa-solid fa-satellite-dish"></i></div>
            <h3>Live Vehicle Tracking</h3>
            <p>See buses on the map in real time with passenger counts, ETAs, and capacity indicators.</p>
          </article>
          <article class="feature-card reveal">
            <div class="feature-icon"><i class="fa-solid fa-leaf"></i></div>
            <h3>Eco Impact Tracker</h3>
            <p>See how much CO₂ you save by choosing the bus over a private vehicle on every trip.</p>
          </article>
          <article class="feature-card reveal">
            <div class="feature-icon"><i class="fa-solid fa-road-barrier"></i></div>
            <h3>Obstruction Awareness</h3>
            <p>Routes automatically adjust around road blockages and protests for uninterrupted navigation.</p>
          </article>
          <article class="feature-card reveal">
            <div class="feature-icon"><i class="fa-solid fa-circle-half-stroke"></i></div>
            <h3>Dark &amp; Light Mode</h3>
            <p>Switch themes to match your surroundings — bright daylight or late-night trip planning.</p>
          </article>
        </div>
      </div>
    </section>

    <!-- Benefits -->
    <section class="section section-accent">
      <div class="container">
        <div class="benefits-grid reveal">
          <div class="benefits-content">
            <span class="section-tag">Why Sawari</span>
            <h2>The smartest way to navigate Kathmandu's transit</h2>
            <p>Built by locals who understand the valley's transit challenges. Sawari combines real route data, AI intelligence, and community feedback to give you the most reliable transit experience.</p>
            <ul class="benefits-list">
              <li><i class="fa-solid fa-circle-check"></i> Covers major operators: Nepal Yatayat, Mahanagar, Sajha Yatayat, and more</li>
              <li><i class="fa-solid fa-circle-check"></i> Routes span Thankot to Dhulikhel, Lagankhel to Budhanilkantha</li>
              <li><i class="fa-solid fa-circle-check"></i> Student and elderly fare discounts shown automatically</li>
              <li><i class="fa-solid fa-circle-check"></i> Works offline for stop search — online for live tracking</li>
            </ul>
            <a href="index.php" class="btn-benefits">Try It Now <i class="fa-solid fa-arrow-right"></i></a>
          </div>
          <div class="benefits-visual">
            <img src="gallery/sajha-bus-EV.jpg" alt="Modern Sajha Yatayat electric bus" loading="lazy" width="600" height="400" />
            <div class="benefits-badge">
              <i class="fa-solid fa-bolt"></i>
              <span>Real-time Data</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Gallery -->
    <section id="gallery" class="section">
      <div class="container">
        <div class="section-header reveal">
          <span class="section-tag">Gallery</span>
          <h2>Transit life in the Valley</h2>
          <p class="section-subtitle">The buses, the roads, and the riders that keep Kathmandu moving every day.</p>
        </div>
        <div class="gallery-grid reveal">
          <div class="gallery-item gallery-item-lg">
            <img src="gallery/1594641445.jpg" alt="Kathmandu road transit" loading="lazy" width="800" height="600" />
          </div>
          <div class="gallery-item">
            <img src="gallery/473749570_1355280112583010_593412764911101796_n.jpg" alt="Public bus" loading="lazy" width="600" height="400" />
          </div>
          <div class="gallery-item">
            <img src="gallery/302216934_482557370551393_6475660738973236802_n.jpg" alt="Bus service" loading="lazy" width="600" height="400" />
          </div>
          <div class="gallery-item">
            <img src="gallery/IMG-1.jpeg" alt="Transit Kathmandu" loading="lazy" width="600" height="400" />
          </div>
          <div class="gallery-item gallery-item-lg">
            <img src="gallery/high-tech-buses.jpg" alt="Modern high-tech buses" loading="lazy" width="800" height="600" />
          </div>
          <div class="gallery-item">
            <img src="gallery/mahanagar-yatayat.png" alt="Mahanagar Yatayat" loading="lazy" width="600" height="400" />
          </div>
          <div class="gallery-item">
            <img src="gallery/481820024_656265493582501_1243983797300762177_n.jpg" alt="Modern local bus" loading="lazy" width="600" height="400" />
          </div>
          <div class="gallery-item">
            <img src="gallery/mayur.jpg" alt="Mayur Yatayat bus" loading="lazy" width="600" height="400" />
          </div>
          <div class="gallery-item">
            <img src="gallery/sajha.jpg" alt="Sajha Yatayat" loading="lazy" width="600" height="400" />
          </div>
          <div class="gallery-item">
            <img src="gallery/nilo-micro.jpg" alt="Blue microbus" loading="lazy" width="600" height="400" />
          </div>
          <div class="gallery-item">
            <img src="gallery/tempo.jpg" alt="Safa tempo" loading="lazy" width="600" height="400" />
          </div>
          <div class="gallery-item">
            <img src="gallery/digo-yatayat.jpg" alt="Digo Yatayat" loading="lazy" width="600" height="400" />
          </div>
        </div>
      </div>
    </section>

    <!-- Ask AI -->
    <section id="ask" class="section section-dark">
      <div class="container">
        <div class="section-header section-header-light reveal">
          <span class="section-tag">AI Assistant</span>
          <h2>Ask Sawari anything</h2>
          <p class="section-subtitle">Got a transit question? Our AI gives you clear, instant answers about routes, fares, and stops.</p>
        </div>
        <div class="ask-layout reveal">
          <div class="ask-sidebar">
            <div class="ask-info-card">
              <img src="gallery/mayur_yatayat_XWhLImWBJm.jpg" alt="Mayur Yatayat bus" loading="lazy" width="600" height="400" />
              <div class="ask-info-overlay">
                <h3>Your Personal Transit Guide</h3>
                <p>Ask about routes, fares, schedules, or nearby stops — get instant, helpful answers.</p>
              </div>
            </div>
            <div class="ask-chips">
              <button class="ask-example" data-query="How do I get from Kalanki to Chabahil?">Kalanki → Chabahil</button>
              <button class="ask-example" data-query="What is the bus fare from Ratnapark to Lagankhel?">Ratnapark fare</button>
              <button class="ask-example" data-query="Which buses pass through Balaju?">Buses through Balaju</button>
              <button class="ask-example" data-query="How to reach Bhaktapur from Koteshwor?">Koteshwor → Bhaktapur</button>
            </div>
          </div>
          <div class="chat-shell">
            <div class="chat-header">
              <div class="chat-header-dot"></div>
              <span>Sawari AI</span>
            </div>
            <div class="chat-log" id="chat-log">
              <div class="chat-msg assistant">
                <div class="chat-avatar"><i class="fa-solid fa-bus"></i></div>
                <div class="chat-bubble">Namaste! Ask me about routes, fares, or nearby stops in Kathmandu Valley.</div>
              </div>
            </div>
            <form id="chat-form" class="chat-form" autocomplete="off">
              <input type="text" id="chat-input" placeholder="e.g. Kalanki to Chabahil by bus" autocomplete="off" />
              <button type="submit" id="chat-send" aria-label="Send message"><i class="fa-solid fa-paper-plane"></i></button>
            </form>
          </div>
        </div>
      </div>
    </section>

    <!-- Contribute -->
    <section id="contribute" class="section">
      <div class="container">
        <div class="contribute-wrapper">
          <div class="section-header reveal">
            <span class="section-tag">Community</span>
            <h2>Help improve Sawari</h2>
            <p class="section-subtitle">Spotted a missing stop, wrong fare, or a new route? Your local knowledge keeps Sawari accurate for every rider.</p>
          </div>
          <div class="contribute-layout">
            <form id="suggest-form" class="suggest-form reveal">
              <div class="form-group">
                <label for="suggest-name">Your Name <span class="label-hint">(optional)</span></label>
                <input id="suggest-name" type="text" maxlength="50" placeholder="Anonymous" />
              </div>
              <div class="form-group">
                <label for="suggest-category">Category</label>
                <select id="suggest-category">
                  <option value="route_correction">Route Correction</option>
                  <option value="missing_stop">Missing Stop</option>
                  <option value="fare_issue">Fare Issue</option>
                  <option value="new_route">New Route Suggestion</option>
                  <option value="general" selected>General Feedback</option>
                </select>
              </div>
              <div class="form-group">
                <label for="suggest-message">Your Suggestion</label>
                <textarea id="suggest-message" rows="4" maxlength="1000" placeholder="Describe what needs to be added or corrected…" required></textarea>
                <div class="char-count"><span id="suggest-chars">0</span> / 1000</div>
              </div>
              <button id="suggest-submit" type="submit"><i class="fa-solid fa-paper-plane"></i> Submit Suggestion</button>
              <div id="suggest-feedback" class="suggest-feedback" style="display:none"></div>
            </form>
            <aside class="contribute-aside reveal">
              <div class="contribute-aside-img">
                <img src="gallery/mahanagar.jpg" alt="Transit in Kathmandu" loading="lazy" width="600" height="400" />
              </div>
              <div class="contribute-aside-body">
                <h3>How your suggestion is reviewed</h3>
                <div class="review-steps">
                  <div class="review-step">
                    <span class="review-step-icon"><i class="fa-solid fa-paper-plane"></i></span>
                    <div>
                      <strong>Submit</strong>
                      <p>Your suggestion is sent to the admin dashboard for review.</p>
                    </div>
                  </div>
                  <div class="review-step">
                    <span class="review-step-icon"><i class="fa-solid fa-robot"></i></span>
                    <div>
                      <strong>AI Analysis</strong>
                      <p>AI extracts actionable tasks from your feedback automatically.</p>
                    </div>
                  </div>
                  <div class="review-step">
                    <span class="review-step-icon"><i class="fa-solid fa-check-double"></i></span>
                    <div>
                      <strong>Review &amp; Deploy</strong>
                      <p>Admin approves and changes go live instantly.</p>
                    </div>
                  </div>
                </div>
                <p class="contribute-note"><i class="fa-solid fa-lock"></i> No account or email required. Your privacy is respected.</p>
              </div>
            </aside>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA -->
    <section class="section-cta">
      <div class="container">
        <div class="cta-content reveal">
          <img src="logo/logo-white.png" alt="Sawari" class="cta-logo" width="140" height="46" />
          <h2>Ready to navigate smarter?</h2>
          <p>Join thousands of riders using Sawari to get around Kathmandu Valley with confidence.</p>
          <div class="cta-actions">
            <a href="index.php" class="btn-cta"><i class="fa-solid fa-compass"></i> Open Navigator</a>
            <a href="#ask" class="btn-cta-outline"><i class="fa-solid fa-message"></i> Ask a Question</a>
          </div>
        </div>
      </div>
    </section>
  </main>

  <!-- Footer -->
  <footer class="footer">
    <div class="container">
      <div class="footer-top">
        <div class="footer-brand">
          <a href="#top" class="footer-logo">
            <img src="logo/logo-white.png" alt="Sawari" width="110" height="36" />
          </a>
          <p>Your smart companion for navigating Kathmandu Valley's public transit — buses, tempos, and microbuses.</p>
          <div class="footer-social">
            <a href="#" aria-label="GitHub"><i class="fa-brands fa-github"></i></a>
            <a href="#" aria-label="Facebook"><i class="fa-brands fa-facebook-f"></i></a>
            <a href="#" aria-label="Instagram"><i class="fa-brands fa-instagram"></i></a>
          </div>
        </div>
        <div class="footer-col">
          <h4>Platform</h4>
          <a href="index.php">Open Navigator</a>
          <a href="#features">Features</a>
          <a href="#how">How It Works</a>
          <a href="#ask">Ask AI</a>
        </div>
        <div class="footer-col">
          <h4>Community</h4>
          <a href="#contribute">Submit Suggestion</a>
          <a href="#gallery">Gallery</a>
          <a href="#about">About Sawari</a>
          <a href="admin/">Admin Panel</a>
        </div>
        <div class="footer-col">
          <h4>Team Spark</h4>
          <a href="https://zenithkandel.com.np" target="_blank" rel="noopener">Zenith Kandel</a>
          <span class="footer-text">Sakhyam Bastakoti</span>
          <span class="footer-text">Sakshyam Upadhaya</span>
          <p class="footer-text footer-tagline">Built for the AI Hackathon, designed for every commuter in the valley.</p>
        </div>
      </div>
      <div class="footer-divider"></div>
      <div class="footer-bottom">
        <p>&copy; <?= date('Y') ?> Sawari by Team Spark. All rights reserved.</p>
        <p class="footer-made">Made with <i class="fa-solid fa-heart"></i> at Embbarg College</p>
      </div>
    </div>
  </footer>

  <script>const GROQ_API_KEY = <?= json_encode($groqApiKey) ?>;</script>
  <script src="landing.js"></script>
</body>

</html>"""

# Write the file with UTF-8 encoding and Unix line endings (LF)
with open(r'd:\S.P.A.R.K\landing.php', 'w', encoding='utf-8', newline='') as f:
    # Replace CRLF with LF to ensure Unix-style line endings
    content = content.replace('\r\n', '\n')
    f.write(content)

print("✓ landing.php written successfully with UTF-8 encoding and LF line endings")
