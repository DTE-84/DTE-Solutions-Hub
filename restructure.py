import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We need to extract the product cards and re-group them.
# The products section starts at <section class="section" id="products"> and ends at the next </section>

start_idx = content.find('<section class="section" id="products">')
end_idx = content.find('</section>', start_idx) + len('</section>')

if start_idx == -1 or end_idx == -1:
    print("Could not find products section")
    exit(1)

products_section = content[start_idx:end_idx]

# Let's extract all the cards by regex or just define the new HTML directly since we know what's in there.
# I will just write the new HTML and replace the old block.

new_products_html = """<section class="section" id="products">
    <div class="inner">
        <div style="text-align:center;margin-bottom:60px;">
            <div class="section-label" style="justify-content:center;margin:0 auto 16px;">Ecosystem</div>
            <h2 class="section-title">All products in one place</h2>
            <p class="section-sub" style="margin:12px auto 0;">Every tool in the DTE ecosystem is purpose-built, production-grade, and live.</p>
        </div>

        <!-- TIER 1: LIVE CORE PRODUCTS -->
        <h3 style="font-size:20px;font-weight:900;letter-spacing:-0.5px;margin-bottom:24px;border-bottom:1px solid rgba(255,255,255,0.1);padding-bottom:12px;">Live Core Products</h3>
        <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(320px, 1fr));gap:20px;margin-bottom:60px;">
            
            <!-- Pulse -->
            <div class="card" style="padding:32px;background:linear-gradient(135deg, rgba(0,255,204,0.05), transparent);border-color:rgba(0,255,204,0.1);">
                <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:16px;">
                    <div>
                        <h4 style="font-size:22px;font-weight:900;letter-spacing:-.5px;margin-bottom:4px;color:#fff;">Pulse-AI</h4>
                        <p style="font-size:11px;color:rgba(0,255,204,0.5);text-transform:uppercase;letter-spacing:.08em;">Behavioral Finance &middot; Plaid &middot; ML</p>
                    </div>
                    <div class="icon-box" style="background:rgba(0,255,204,0.1);border-color:rgba(0,255,204,0.2);"><i data-lucide="activity" style="color:var(--green);"></i></div>
                </div>
                <p style="font-size:13px;color:var(--text-muted);line-height:1.7;margin-bottom:20px;">Behavioral finance SaaS with Nova AI coaching, real-time Plaid telemetry, stress indexing, and predictive capital forecasting.</p>
                <a href="https://pulse.dte-solutions.icu" target="_blank" style="font-size:12px;font-weight:700;color:var(--green);display:flex;align-items:center;gap:6px;">View Plans <i data-lucide="arrow-right" style="width:12px;height:12px;"></i></a>
            </div>

            <!-- LockboxIQ -->
            <div class="card" style="padding:32px;background:linear-gradient(135deg, rgba(0,255,204,0.05), transparent);border-color:rgba(0,255,204,0.1);">
                <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:16px;">
                    <div>
                        <h4 style="font-size:22px;font-weight:900;letter-spacing:-.5px;margin-bottom:4px;color:#fff;">LockboxIQ</h4>
                        <p style="font-size:11px;color:rgba(0,255,204,0.5);text-transform:uppercase;letter-spacing:.08em;">Pulse Add-On &middot; Subscriptions</p>
                    </div>
                    <div class="icon-box" style="background:rgba(0,255,204,0.1);border-color:rgba(0,255,204,0.2);"><i data-lucide="lock" style="color:var(--green);"></i></div>
                </div>
                <p style="font-size:13px;color:var(--text-muted);line-height:1.7;margin-bottom:20px;">Seamless subscription tracking and behavioral logic bundled directly into the Pulse ecosystem to stop subscription bleed.</p>
                <a href="lockboxiq-breakdown.html" target="_blank" style="font-size:12px;font-weight:700;color:var(--green);display:flex;align-items:center;gap:6px;">View Case Study <i data-lucide="arrow-right" style="width:12px;height:12px;"></i></a>
            </div>

            <!-- PCSP Pro -->
            <div class="card" style="padding:32px;background:linear-gradient(135deg, rgba(0,255,204,0.05), transparent);border-color:rgba(0,255,204,0.1);">
                <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:16px;">
                    <div>
                        <h4 style="font-size:22px;font-weight:900;letter-spacing:-.5px;margin-bottom:4px;color:#fff;">PCSP Pro</h4>
                        <p style="font-size:11px;color:rgba(0,255,204,0.5);text-transform:uppercase;letter-spacing:.08em;">Compliance &middot; HIPAA</p>
                    </div>
                    <div class="icon-box" style="background:rgba(0,255,204,0.1);border-color:rgba(0,255,204,0.2);"><i data-lucide="shield-check" style="color:var(--green);"></i></div>
                </div>
                <p style="font-size:13px;color:var(--text-muted);line-height:1.7;margin-bottom:20px;">HIPAA-compliant documentation engine for state-mandated healthcare reporting with 87% DMH threshold accuracy.</p>
                <a href="https://dte-84.github.io/DTE-Portfolio/case-study-pcsp/" target="_blank" style="font-size:12px;font-weight:700;color:var(--green);display:flex;align-items:center;gap:6px;">View Case Study <i data-lucide="external-link" style="width:12px;height:12px;"></i></a>
            </div>

            <!-- ResaleIQ Neural -->
            <div class="card" style="padding:32px;background:linear-gradient(135deg, rgba(0,255,204,0.05), transparent);border-color:rgba(0,255,204,0.1);">
                <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:16px;">
                    <div>
                        <h4 style="font-size:22px;font-weight:900;letter-spacing:-.5px;margin-bottom:4px;color:#fff;">ResaleIQ Neural</h4>
                        <p style="font-size:11px;color:rgba(0,255,204,0.5);text-transform:uppercase;letter-spacing:.08em;">Anthropic &middot; Claude 3.5 &middot; React</p>
                    </div>
                    <div class="icon-box" style="background:rgba(0,255,204,0.1);border-color:rgba(0,255,204,0.2);"><i data-lucide="zap" style="color:var(--green);"></i></div>
                </div>
                <p style="font-size:13px;color:var(--text-muted);line-height:1.7;margin-bottom:20px;">Luxury boutique intelligence suite for elite resellers. Powered by Anthropic's Claude 3.5 for high-conversion SEO listings and neural market analytics.</p>
                <a href="resaleiq-breakdown.html" target="_blank" style="font-size:12px;font-weight:700;color:var(--green);display:flex;align-items:center;gap:6px;">View Case Study <i data-lucide="arrow-right" style="width:12px;height:12px;"></i></a>
            </div>

            <!-- Spark Analyzer -->
            <div class="card" style="padding:32px;background:linear-gradient(135deg, rgba(0,255,204,0.05), transparent);border-color:rgba(0,255,204,0.1);">
                <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:16px;">
                    <div>
                        <h4 style="font-size:22px;font-weight:900;letter-spacing:-.5px;margin-bottom:4px;color:#fff;">Spark Analyzer</h4>
                        <p style="font-size:11px;color:rgba(0,255,204,0.5);text-transform:uppercase;letter-spacing:.08em;">Analytics &middot; Dashboard</p>
                    </div>
                    <div class="icon-box" style="background:rgba(0,255,204,0.1);border-color:rgba(0,255,204,0.2);"><i data-lucide="bar-chart" style="color:var(--green);"></i></div>
                </div>
                <p style="font-size:13px;color:var(--text-muted);line-height:1.7;margin-bottom:20px;">High-fidelity analytics dashboard and data visualization engine for business intelligence.</p>
                <a href="sparkiq-breakdown.html" target="_blank" style="font-size:12px;font-weight:700;color:var(--green);display:flex;align-items:center;gap:6px;">View Case Study <i data-lucide="arrow-right" style="width:12px;height:12px;"></i></a>
            </div>

        </div>

        <!-- TIER 2: CLIENT WORK & PORTALS -->
        <h3 style="font-size:20px;font-weight:900;letter-spacing:-0.5px;margin-bottom:24px;border-bottom:1px solid rgba(255,255,255,0.1);padding-bottom:12px;">Client Work & Portals</h3>
        <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(320px, 1fr));gap:20px;margin-bottom:60px;">
            
            <!-- MW Properties -->
            <div class="card" style="padding:32px;background:linear-gradient(135deg, rgba(212,175,55,0.05), transparent);border-color:rgba(212,175,55,0.1);">
                <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:16px;">
                    <div>
                        <h4 style="font-size:22px;font-weight:900;letter-spacing:-.5px;margin-bottom:4px;color:#fff;">MW Properties</h4>
                        <p style="font-size:11px;color:rgba(212,175,55,0.5);text-transform:uppercase;letter-spacing:.08em;">React &middot; Vite &middot; GitHub Pages</p>
                    </div>
                    <div class="icon-box" style="background:rgba(212,175,55,0.1);border-color:rgba(212,175,55,0.2);"><i data-lucide="home" style="color:#D4AF37;"></i></div>
                </div>
                <p style="font-size:13px;color:var(--text-muted);line-height:1.7;margin-bottom:20px;">Real estate restoration and investor relations portal. Showcases interactive Before/After sliders, underwriting ledgers, and a validated stateful lead capture pipeline.</p>
                <a href="mwproperties-breakdown.html" target="_blank" style="font-size:12px;font-weight:700;color:#D4AF37;display:flex;align-items:center;gap:6px;">Case Study <i data-lucide="arrow-right" style="width:12px;height:12px;"></i></a>
            </div>

            <!-- Tony's Landscaping -->
            <div class="card" style="padding:32px;background:linear-gradient(135deg, rgba(212,175,55,0.05), transparent);border-color:rgba(212,175,55,0.1);">
                <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:16px;">
                    <div>
                        <h4 style="font-size:22px;font-weight:900;letter-spacing:-.5px;margin-bottom:4px;color:#fff;">Tony's Landscaping</h4>
                        <p style="font-size:11px;color:rgba(212,175,55,0.5);text-transform:uppercase;letter-spacing:.08em;">Local Business &middot; React &middot; Lead Gen</p>
                    </div>
                    <div class="icon-box" style="background:rgba(212,175,55,0.1);border-color:rgba(212,175,55,0.2);"><i data-lucide="leaf" style="color:#D4AF37;"></i></div>
                </div>
                <p style="font-size:13px;color:var(--text-muted);line-height:1.7;margin-bottom:20px;">Digital storefront and lead generation portal for a premier local landscaping and outdoor design business.</p>
                <a href="https://www.tonyslandscapingllc.com/" target="_blank" style="font-size:12px;font-weight:700;color:#D4AF37;display:flex;align-items:center;gap:6px;">View Site <i data-lucide="external-link" style="width:12px;height:12px;"></i></a>
            </div>

            <!-- PRO DIP -->
            <div class="card" style="padding:32px;background:linear-gradient(135deg, rgba(212,175,55,0.05), transparent);border-color:rgba(212,175,55,0.1);">
                <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:16px;">
                    <div>
                        <h4 style="font-size:22px;font-weight:900;letter-spacing:-.5px;margin-bottom:4px;color:#fff;">PRO DIP</h4>
                        <p style="font-size:11px;color:rgba(212,175,55,0.5);text-transform:uppercase;letter-spacing:.08em;">Local Business &middot; Next.js &middot; Lead Gen</p>
                    </div>
                    <div class="icon-box" style="background:rgba(212,175,55,0.1);border-color:rgba(212,175,55,0.2);"><i data-lucide="car" style="color:#D4AF37;"></i></div>
                </div>
                <p style="font-size:13px;color:var(--text-muted);line-height:1.7;margin-bottom:20px;">Digital storefront for a local custom car wrap and tinting business, engineered for localized SEO and streamlined quote generation.</p>
                <a href="https://dte-84.github.io/ProDip/" target="_blank" style="font-size:12px;font-weight:700;color:#D4AF37;display:flex;align-items:center;gap:6px;">View Site <i data-lucide="external-link" style="width:12px;height:12px;"></i></a>
            </div>

            <!-- MCSDD-Quarterly -->
            <div class="card" style="padding:32px;background:linear-gradient(135deg, rgba(212,175,55,0.05), transparent);border-color:rgba(212,175,55,0.1);">
                <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:16px;">
                    <div>
                        <h4 style="font-size:22px;font-weight:900;letter-spacing:-.5px;margin-bottom:4px;color:#fff;">MCSDD-Quarterly</h4>
                        <p style="font-size:11px;color:rgba(212,175,55,0.5);text-transform:uppercase;letter-spacing:.08em;">Government &middot; Reporting</p>
                    </div>
                    <div class="icon-box" style="background:rgba(212,175,55,0.1);border-color:rgba(212,175,55,0.2);"><i data-lucide="clipboard-list" style="color:#D4AF37;"></i></div>
                </div>
                <p style="font-size:13px;color:var(--text-muted);line-height:1.7;margin-bottom:20px;">Automated quarterly reporting and compliance tracking for MCSDD, ensuring data integrity and precision for government organizations.</p>
                <span style="font-size:12px;font-weight:700;color:rgba(212,175,55,0.3);display:flex;align-items:center;gap:6px;cursor:default;">Case Study Coming Soon <i data-lucide="clock" style="width:12px;height:12px;"></i></span>
            </div>

        </div>

        <!-- TIER 3: LABS & CONCEPTS -->
        <h3 style="font-size:20px;font-weight:900;letter-spacing:-0.5px;margin-bottom:24px;border-bottom:1px solid rgba(255,255,255,0.1);padding-bottom:12px;">Labs & Technical Concepts</h3>
        <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(320px, 1fr));gap:20px;">
            
            <!-- Fluff -->
            <div class="card" style="padding:32px;background:linear-gradient(135deg, rgba(255,255,255,0.02), transparent);border-color:rgba(255,255,255,0.05);">
                <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:16px;">
                    <div>
                        <h4 style="font-size:22px;font-weight:900;letter-spacing:-.5px;margin-bottom:4px;color:#fff;">Fluff</h4>
                        <p style="font-size:11px;color:rgba(255,255,255,0.3);text-transform:uppercase;letter-spacing:.08em;">Computer Vision &middot; Biomechanics</p>
                    </div>
                    <div class="icon-box" style="background:rgba(255,255,255,0.05);border-color:rgba(255,255,255,0.1);"><i data-lucide="eye" style="color:#aaa;"></i></div>
                </div>
                <p style="font-size:13px;color:var(--text-muted);line-height:1.7;margin-bottom:20px;">Computer-vision golf analysis platform with biomechanical motion tracking, swing feedback, and performance tools for players and coaches.</p>
                <a href="fluff-breakdown.html" target="_blank" style="font-size:12px;font-weight:700;color:#aaa;display:flex;align-items:center;gap:6px;">Explore <i data-lucide="arrow-right" style="width:12px;height:12px;"></i></a>
            </div>

            <!-- Keys Beats -->
            <div class="card" style="padding:32px;background:linear-gradient(135deg, rgba(255,255,255,0.02), transparent);border-color:rgba(255,255,255,0.05);">
                <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:16px;">
                    <div>
                        <h4 style="font-size:22px;font-weight:900;letter-spacing:-.5px;margin-bottom:4px;color:#fff;">Keys Beats</h4>
                        <p style="font-size:11px;color:rgba(255,255,255,0.3);text-transform:uppercase;letter-spacing:.08em;">React &middot; Audio Engine &middot; Portfolio</p>
                    </div>
                    <div class="icon-box" style="background:rgba(255,255,255,0.05);border-color:rgba(255,255,255,0.1);"><i data-lucide="music" style="color:#aaa;"></i></div>
                </div>
                <p style="font-size:13px;color:var(--text-muted);line-height:1.7;margin-bottom:20px;">A high-fidelity music portfolio showcasing interactive audio streaming, beat catalogs, and immersive artist branding.</p>
                <a href="https://keys-beats.vercel.app/" target="_blank" style="font-size:12px;font-weight:700;color:#aaa;display:flex;align-items:center;gap:6px;">Launch Portfolio <i data-lucide="external-link" style="width:12px;height:12px;"></i></a>
            </div>

            <!-- SiKnight GameHub -->
            <div class="card" style="padding:32px;background:linear-gradient(135deg, rgba(255,255,255,0.02), transparent);border-color:rgba(255,255,255,0.05);">
                <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:16px;">
                    <div>
                        <h4 style="font-size:22px;font-weight:900;letter-spacing:-.5px;margin-bottom:4px;color:#fff;">SiKnight GameHub</h4>
                        <p style="font-size:11px;color:rgba(255,255,255,0.3);text-transform:uppercase;letter-spacing:.08em;">Gaming Portal &middot; Interactive</p>
                    </div>
                    <div class="icon-box" style="background:rgba(255,255,255,0.05);border-color:rgba(255,255,255,0.1);"><i data-lucide="gamepad-2" style="color:#aaa;"></i></div>
                </div>
                <p style="font-size:13px;color:var(--text-muted);line-height:1.7;margin-bottom:20px;">Interactive gaming hub featuring custom game modes, community leaderboards, and real-time multiplayer logic.</p>
                <a href="https://dte-84.github.io/SiKnight/" target="_blank" style="font-size:12px;font-weight:700;color:#aaa;display:flex;align-items:center;gap:6px;">Launch Hub <i data-lucide="external-link" style="width:12px;height:12px;"></i></a>
            </div>

            <!-- E-Commerce Intelligence -->
            <div class="card" style="padding:32px;background:linear-gradient(135deg, rgba(255,255,255,0.02), transparent);border-color:rgba(255,255,255,0.05);">
                <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:16px;">
                    <div>
                        <h4 style="font-size:22px;font-weight:900;letter-spacing:-.5px;margin-bottom:4px;color:#fff;">E-Commerce Intelligence</h4>
                        <p style="font-size:11px;color:rgba(255,255,255,0.3);text-transform:uppercase;letter-spacing:.08em;">Pandas &middot; Jest &middot; Data Integrity</p>
                    </div>
                    <div class="icon-box" style="background:rgba(255,255,255,0.05);border-color:rgba(255,255,255,0.1);"><i data-lucide="shopping-bag" style="color:#aaa;"></i></div>
                </div>
                <p style="font-size:13px;color:var(--text-muted);line-height:1.7;margin-bottom:20px;">Full-stack analytics workflow to process e-commerce data, validate outputs, and surface cleaner reporting for business decisions.</p>
                <a href="https://ecomm-505qtlvsc-dte-solutions.vercel.app/" target="_blank" style="font-size:12px;font-weight:700;color:#aaa;display:flex;align-items:center;gap:6px;">View Archive <i data-lucide="arrow-right" style="width:12px;height:12px;"></i></a>
            </div>

            <!-- PDF Integrity Editor -->
            <div class="card" style="padding:32px;background:linear-gradient(135deg, rgba(255,255,255,0.02), transparent);border-color:rgba(255,255,255,0.05);">
                <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:16px;">
                    <div>
                        <h4 style="font-size:22px;font-weight:900;letter-spacing:-.5px;margin-bottom:4px;color:#fff;">PDF Integrity Editor</h4>
                        <p style="font-size:11px;color:rgba(255,255,255,0.3);text-transform:uppercase;letter-spacing:.08em;">Zero-Server &middot; Local Storage</p>
                    </div>
                    <div class="icon-box" style="background:rgba(255,255,255,0.05);border-color:rgba(255,255,255,0.1);"><i data-lucide="file-text" style="color:#aaa;"></i></div>
                </div>
                <p style="font-size:13px;color:var(--text-muted);line-height:1.7;margin-bottom:20px;">Zero-server document editor free to the community. Annotate, markup, and finalize PDFs with all processing handled locally.</p>
                <a href="pdf-editor.html" target="_blank" style="font-size:12px;font-weight:700;color:#aaa;display:flex;align-items:center;gap:6px;">Access Tool <i data-lucide="arrow-right" style="width:12px;height:12px;"></i></a>
            </div>

            <!-- SetLogic -->
            <div class="card" style="padding:32px;background:linear-gradient(135deg, rgba(255,255,255,0.02), transparent);border-color:rgba(255,255,255,0.05);">
                <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:16px;">
                    <div>
                        <h4 style="font-size:22px;font-weight:900;letter-spacing:-.5px;margin-bottom:4px;color:#fff;">SetLogic</h4>
                        <p style="font-size:11px;color:rgba(255,255,255,0.3);text-transform:uppercase;letter-spacing:.08em;">AI Fitness &middot; Telemetry &middot; React</p>
                    </div>
                    <div class="icon-box" style="background:rgba(255,255,255,0.05);border-color:rgba(255,255,255,0.1);"><i data-lucide="dumbbell" style="color:#aaa;"></i></div>
                </div>
                <p style="font-size:13px;color:var(--text-muted);line-height:1.7;margin-bottom:20px;">AI fitness coaching platform with guided training flows, performance tracking, and data-driven feedback for athletes and coaches.</p>
                <a href="setlogic-breakdown.html" target="_blank" style="font-size:12px;font-weight:700;color:#aaa;display:flex;align-items:center;gap:6px;">Explore <i data-lucide="arrow-right" style="width:12px;height:12px;"></i></a>
            </div>

        </div>
    </div>
</section>"""

new_content = content[:start_idx] + new_products_html + content[end_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Restructured Products grid successfully!")
