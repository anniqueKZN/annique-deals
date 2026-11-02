from flask import Flask, redirect, render_template_string, request

app = Flask(__name__)

# Complete portal HTML template with dynamic referral injection
PORTAL_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Annique Rooibos Black November Portal & Diagnostic Hub</title>
    <style>
        :root {
            --primary-red: #8B0000;
            --accent-gold: #D4AF37;
            --bg-light: #FDFBF7;
            --text-dark: #2C2C2C;
            --white: #FFFFFF;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: var(--bg-light);
            color: var(--text-dark);
            margin: 0;
            padding: 0;
        }
        .banner {
            background-color: #5c0000;
            color: #FFD700;
            text-align: center;
            padding: 0.6rem;
            font-weight: bold;
            font-size: 0.9rem;
        }
        header {
            background-color: var(--primary-red);
            color: var(--white);
            padding: 1rem 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
        }
        .nav-links a {
            color: var(--white);
            text-decoration: none;
            margin-left: 1.5rem;
            font-weight: 600;
        }
        .collection-nav {
            background-color: #f5efe6;
            padding: 0.75rem 2rem;
            display: flex;
            justify-content: center;
            gap: 2rem;
            border-bottom: 1px solid #e2d2a5;
            flex-wrap: wrap;
        }
        .collection-nav a {
            color: var(--primary-red);
            text-decoration: none;
            font-weight: 600;
            font-size: 0.95rem;
        }
        .collection-nav a:hover {
            text-decoration: underline;
        }
        .hero {
            padding: 3rem 2rem;
            text-align: center;
            background: linear-gradient(135deg, #fff5f5, #ffe6e6);
            border-bottom: 2px solid #ddd;
        }
        .hero h1 {
            font-size: 2.5rem;
            color: var(--primary-red);
            margin-bottom: 1rem;
        }
        .hero p {
            max-width: 700px;
            margin: 0 auto 1.5rem auto;
            line-height: 1.6;
            color: #555;
        }
        .quick-routes {
            display: flex;
            justify-content: center;
            gap: 1rem;
            flex-wrap: wrap;
            margin-top: 1.5rem;
        }
        .btn {
            background-color: var(--primary-red);
            color: var(--white);
            padding: 0.75rem 1.5rem;
            border-radius: 4px;
            text-decoration: none;
            font-weight: bold;
            transition: background 0.2s;
        }
        .btn:hover {
            background-color: #600;
        }
        .container {
            max-width: 1200px;
            margin: 2rem auto;
            padding: 0 1rem;
        }
        .section-title {
            font-size: 1.8rem;
            color: var(--primary-red);
            margin-bottom: 1.5rem;
            border-bottom: 2px solid var(--accent-gold);
            padding-bottom: 0.5rem;
        }
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 1.5rem;
        }
        .card {
            background: var(--white);
            border-radius: 8px;
            padding: 1.5rem;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
        .card-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 0.5rem;
        }
        .range-tag {
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            background: #eee;
            padding: 0.2rem 0.5rem;
            border-radius: 3px;
            font-weight: bold;
            color: #555;
        }
        .rating {
            color: #f39c12;
            font-size: 0.9rem;
        }
        .card h3 {
            font-size: 1.15rem;
            margin: 0.5rem 0;
            color: var(--text-dark);
        }
        .card p {
            font-size: 0.9rem;
            color: #666;
            flex-grow: 1;
            margin-bottom: 1rem;
        }
        .price-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 1rem;
            border-top: 1px solid #eee;
            padding-top: 1rem;
        }
        .price {
            font-size: 1.2rem;
            font-weight: bold;
            color: var(--primary-red);
        }
        footer {
            background-color: #222;
            color: #aaa;
            text-align: center;
            padding: 2rem;
            margin-top: 3rem;
            font-size: 0.9rem;
        }
    </style>
</head>
<body>

    <div class="banner">
        🔥 ACTIVE CAMPAIGN: Black November Rooibos Specials Live | Consultant ID: {{ ref }}
    </div>

    <header>
        <div>
            <strong>ANNIQUE ROOIBOS</strong> <span style="font-size: 0.8rem; opacity: 0.8;">HERITAGE BEAUTY & HEALTH PORTAL</span>
        </div>
        <div class="nav-links">
            <a href="https://www.annique.com/?ref={{ ref }}">Main Storefront</a>
            <a href="https://www.annique.com/join?ref={{ ref }}">Join Consultant Team</a>
        </div>
    </header>

    <div class="collection-nav">
        <span>Quick Range Collections:</span>
        <a href="/collections/lucid?ref={{ ref }}">Lucid Collection →</a>
        <a href="/collections/forever-young?ref={{ ref }}">Forever Young Collection →</a>
        <a href="/collections/essense?ref={{ ref }}">Essense Collection →</a>
    </div>

    <section class="hero">
        <span class="range-tag" style="background: #e2d2a5; color: #333; margin-bottom: 1rem; display: inline-block;">OFFICIAL INDEPENDENT CONSULTANT PORTAL (#{{ ref }})</span>
        <h1>South Africa's Premier Rooibos Skincare & Wellness Hub</h1>
        <p>Explore high-performance organic Rooibos formulas, run automated skin diagnostic routines, calculate affiliate commissions, and access conversion-tested Black November media assets—all linked directly with active consultant tracking (?ref={{ ref }}).</p>
        
        <div class="quick-routes">
            <a href="https://www.annique.com/black-november?ref={{ ref }}" class="btn">🛍️ Black November Catalog</a>
            <a href="#diagnostic" class="btn" style="background-color: #444;">🧬 AI Skin Diagnostic Routine</a>
            <a href="#calculator" class="btn" style="background-color: #444;">📊 Affiliate Earnings Calculator</a>
        </div>
    </section>

    <main class="container">
        <h2 class="section-title">Annique Rooibos Product & Deal Showcase</h2>
        
        <div class="grid">
            <!-- Product 1 -->
            <div class="card">
                <div>
                    <div class="card-header">
                        <span class="range-tag">Lucid</span>
                        <span class="rating">★ 4.0</span>
                    </div>
                    <h3>Lucid Moisturiser for Dry Skin 50ml</h3>
                    <p>Deeply hydrating 50ml nourishment infused with organic Rooibos extract for dry and mature skin.</p>
                </div>
                <div class="price-row">
                    <span class="price">R 829.00</span>
                    <a href="https://www.annique.com/lucid-moisturiser-50ml?ref={{ ref }}" style="color: var(--primary-red); text-decoration: none; font-weight: bold; font-size: 0.9rem;">View Deal on Annique →</a>
                </div>
            </div>

            <!-- Product 2 -->
            <div class="card">
                <div>
                    <div class="card-header">
                        <span class="range-tag">Forever Young</span>
                        <span class="rating">★ 5.0</span>
                    </div>
                    <h3>Forever Young Revitalising Cream 50ml</h3>
                    <p>Flagship restorative cream targeting fine lines, wrinkles, and skin elasticity with concentrated Rooibos antioxidants.</p>
                </div>
                <div class="price-row">
                    <span class="price">R 1059.00</span>
                    <a href="https://www.annique.com/forever-young-revitalising-cream-50ml?ref={{ ref }}" style="color: var(--primary-red); text-decoration: none; font-weight: bold; font-size: 0.9rem;">View Deal on Annique →</a>
                </div>
            </div>

            <!-- Product 3 -->
            <div class="card">
                <div>
                    <div class="card-header">
                        <span class="range-tag">Essense</span>
                        <span class="rating">★ 5.0</span>
                    </div>
                    <h3>Essense Hyaluronic Acid³ Serum 30ml</h3>
                    <p>Multi-layer hydration serum boosting moisture retention, skin elasticity, and immediate plumpness.</p>
                </div>
                <div class="price-row">
                    <span class="price">R 699.00</span>
                    <a href="https://www.annique.com/essense-hyaluronic-acid-serum-30ml?ref={{ ref }}" style="color: var(--primary-red); text-decoration: none; font-weight: bold; font-size: 0.9rem;">View Deal on Annique →</a>
                </div>
            </div>

            <!-- Product 4 -->
            <div class="card">
                <div>
                    <div class="card-header">
                        <span class="range-tag">Forever Young</span>
                        <span class="rating">★ 4.4</span>
                    </div>
                    <h3>Forever Young Crème de Nuit 50ml</h3>
                    <p>Rich anti-ageing night cream nourishing and repairing the skin overnight.</p>
                </div>
                <div class="price-row">
                    <span class="price">R 749.00</span>
                    <a href="https://www.annique.com/forever-young-creme-de-nuit-50ml?ref={{ ref }}" style="color: var(--primary-red); text-decoration: none; font-weight: bold; font-size: 0.9rem;">View Deal on Annique →</a>
                </div>
            </div>

            <!-- Product 5 -->
            <div class="card">
                <div>
                    <div class="card-header">
                        <span class="range-tag">Lucid</span>
                        <span class="rating">★ 4.7</span>
                    </div>
                    <h3>Lucid Crème Cleanser 200ml</h3>
                    <p>Gently removes impurities while maintaining vital moisture balance in dry skin types.</p>
                </div>
                <div class="price-row">
                    <span class="price">R 319.00</span>
                    <a href="https://www.annique.com/lucid-creme-cleanser-200ml?ref={{ ref }}" style="color: var(--primary-red); text-decoration: none; font-weight: bold; font-size: 0.9rem;">View Deal on Annique →</a>
                </div>
            </div>

            <!-- Product 6 -->
            <div class="card">
                <div>
                    <div class="card-header">
                        <span class="range-tag">Essense</span>
                        <span class="rating">★ 5.0</span>
                    </div>
                    <h3>Essense Sensi Crème 50ml</h3>
                    <p>Soothing treatment specifically formulated to calm sensitive, red, or irritated skin.</p>
                </div>
                <div class="price-row">
                    <span class="price">R 219.00</span>
                    <a href="https://www.annique.com/essense-sensi-creme-50ml?ref={{ ref }}" style="color: var(--primary-red); text-decoration: none; font-weight: bold; font-size: 0.9rem;">View Deal on Annique →</a>
                </div>
            </div>

            <!-- Product 7 -->
            <div class="card">
                <div>
                    <div class="card-header">
                        <span class="range-tag">Face Facts</span>
                        <span class="rating">★ 4.5</span>
                    </div>
                    <h3>Face Facts Gel Cleanser 200ml</h3>
                    <p>Refreshing deep cleanser formulated for normal, oily, or acne-prone skin.</p>
                </div>
                <div class="price-row">
                    <span class="price">R 239.00</span>
                    <a href="https://www.annique.com/face-facts-gel-cleanser-200ml?ref={{ ref }}" style="color: var(--primary-red); text-decoration: none; font-weight: bold; font-size: 0.9rem;">View Deal on Annique →</a>
                </div>
            </div>

            <!-- Product 8 -->
            <div class="card">
                <div>
                    <div class="card-header">
                        <span class="range-tag">Forever Healthy</span>
                        <span class="rating">★ 5.0</span>
                    </div>
                    <h3>Forever Healthy Collagen with Rooibos 150g</h3>
                    <p>Nutraceutical supplement supporting inner skin elasticity, hair growth, and joint health.</p>
                </div>
                <div class="price-row">
                    <span class="price">R 399.00</span>
                    <a href="https://www.annique.com/forever-healthy-collagen-with-rooibos-150g?ref={{ ref }}" style="color: var(--primary-red); text-decoration: none; font-weight: bold; font-size: 0.9rem;">View Deal on Annique →</a>
                </div>
            </div>

            <!-- Product 9 -->
            <div class="card">
                <div>
                    <div class="card-header">
                        <span class="range-tag">Tea</span>
                        <span class="rating">★ 4.9</span>
                    </div>
                    <h3>Rooibos & Ginger Tea 50g</h3>
                    <p>Calming herbal tea blend promoting digestive comfort and immune resilience.</p>
                </div>
                <div class="price-row">
                    <span class="price">R 72.00</span>
                    <a href="https://www.annique.com/rooibos-ginger-tea-50g?ref={{ ref }}" style="color: var(--primary-red); text-decoration: none; font-weight: bold; font-size: 0.9rem;">View Deal on Annique →</a>
                </div>
            </div>
        </div>
    </main>

    <footer>
        <p>Annique Rooibos Independent Consultant Pipeline | Consultant Reference ID: {{ ref }}</p>
    </footer>

</body>
</html>
"""


@app.route("/")
def home():
  ref = request.args.get("ref", "527160")
  return render_template_string(PORTAL_HTML, ref=ref)


@app.route("/collections/<collection_name>")
def redirect_collection(collection_name):
  ref = request.args.get("ref", "527160")
  # Safely forward collection requests directly to Annique with tracking
  target_url = (
      f"https://www.annique.com/collections/{collection_name}?ref={ref}"
  )
  return redirect(target_url)


if __name__ == "__main__":
  app.run(debug=True, port=5000)
