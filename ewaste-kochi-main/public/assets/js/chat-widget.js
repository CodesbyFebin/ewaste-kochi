/* ═══════════════════════════════════════════════════════════
   EWaste Kochi — AI Chat Widget
   ⚠  CONFIGURE: Replace ANTHROPIC_API_KEY below with your key.
      For production, proxy through a backend to keep the key secret.
   ═══════════════════════════════════════════════════════════ */
(function () {
  'use strict';

  // ── CONFIG ────────────────────────────────────────────────────
  const PHONE       = '+91-7500555454';
  const WA_NUM      = '917500555454';
  const WA_BASE     = 'https://wa.me/' + WA_NUM;
  // ⚠ IMPORTANT: Move this key to a backend proxy before going live!
  const ANTHROPIC_API_KEY = 'YOUR_ANTHROPIC_API_KEY_HERE';

  // ── STATE ─────────────────────────────────────────────────────
  let isOpen = false;
  let leadData = {};
  let conversationHistory = [];
  let awaitingInput = null;

  // ── HELPERS ───────────────────────────────────────────────────
  function esc(s) {
    return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
  }
  function nowTime() {
    return new Date().toLocaleTimeString('en-IN', { hour: '2-digit', minute: '2-digit', hour12: true });
  }
  function botAvatarSVG() {
    return `<svg viewBox="0 0 24 24"><path d="M21 16V8a2 2 0 00-1-1.73l-7-4a2 2 0 00-2 0l-7 4A2 2 0 003 8v8a2 2 0 001 1.73l7 4a2 2 0 002 0l7-4A2 2 0 0021 16z"/></svg>`;
  }

  // ── INJECT HTML ───────────────────────────────────────────────
  function injectMarkup() {
    const html = `
<!-- CHAT TRIGGER -->
<button class="chat-trigger" id="cwTrigger" aria-label="Chat with EWaste Kochi AI">
  <div class="trigger-icon">
    <svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12c0 1.85.5 3.58 1.37 5.06L2 22l4.94-1.37A9.95 9.95 0 0012 22c5.52 0 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg>
    <div class="trigger-badge" id="cwBadge">1</div>
  </div>
</button>

<!-- MINIMIZE PROMPT -->
<div class="chat-minimize" id="cwMinimize">
  <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="#00C896" stroke-width="2">
    <path d="M12 2a10 10 0 100 20 10 10 0 000-20z"/><path d="M12 16v-4M12 8h.01"/>
  </svg>
  <p>Need free e-waste pickup in Kochi? 🤖</p>
  <button class="cw-close-min" id="cwCloseMin" aria-label="Dismiss">✕</button>
</div>

<!-- CHAT WINDOW -->
<div class="chat-window" id="cwWindow" role="dialog" aria-modal="true" aria-label="EWaste Kochi AI Chat">
  <div class="chat-header">
    <div class="cw-bot-avatar">
      ${botAvatarSVG()}
      <div class="cw-bot-status"></div>
    </div>
    <div class="cw-bot-info">
      <h4>EWaste Kochi AI</h4>
      <span>● Online · Responds instantly</span>
    </div>
    <button class="chat-close" id="cwClose" aria-label="Close chat">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
        <path d="M18 6L6 18M6 6l12 12"/>
      </svg>
    </button>
  </div>
  <div class="chat-messages" id="cwMessages"></div>
  <div class="cw-quick-opts" id="cwOpts"></div>
  <div class="cw-ai-label">
    <div class="cw-ai-dot"></div>
    Powered by Claude AI · EWaste Kochi
  </div>
  <div class="cw-input-wrap">
    <input class="cw-input" id="cwInput" type="text" placeholder="Ask anything about e-waste in Kochi…" autocomplete="off" maxlength="300">
    <button class="cw-send-btn" id="cwSend" aria-label="Send message">
      <svg viewBox="0 0 24 24"><path d="M2 21l21-9L2 3v7l15 2-15 2v7z"/></svg>
    </button>
  </div>
</div>`;
    const div = document.createElement('div');
    div.id = 'ewkChatWidget';
    div.innerHTML = html;
    document.body.appendChild(div);
  }

  // ── DOM REFS (after inject) ───────────────────────────────────
  let $win, $msgs, $opts, $input, $badge, $minimize;

  function refs() {
    $win      = document.getElementById('cwWindow');
    $msgs     = document.getElementById('cwMessages');
    $opts     = document.getElementById('cwOpts');
    $input    = document.getElementById('cwInput');
    $badge    = document.getElementById('cwBadge');
    $minimize = document.getElementById('cwMinimize');
  }

  // ── OPEN / CLOSE ──────────────────────────────────────────────
  function openChat() {
    isOpen = true;
    $win.classList.add('open');
    $minimize.style.display = 'none';
    $badge.style.display = 'none';
    $input.focus();
    if ($msgs.children.length === 0) startConversation();
  }
  function closeChat() {
    isOpen = false;
    $win.classList.remove('open');
  }

  // ── MESSAGE RENDERING ─────────────────────────────────────────
  function addMsg(role, text, isHtml = false) {
    const wrap = document.createElement('div');
    wrap.className = `cw-msg ${role}`;
    if (role === 'bot') {
      wrap.innerHTML = `
        <div class="cw-msg-av">${botAvatarSVG()}</div>
        <div>
          <div class="cw-msg-bubble">${isHtml ? text : esc(text)}</div>
          <div class="cw-msg-time">${nowTime()}</div>
        </div>`;
    } else {
      wrap.innerHTML = `
        <div>
          <div class="cw-msg-bubble">${esc(text)}</div>
          <div class="cw-msg-time" style="text-align:right">${nowTime()}</div>
        </div>`;
    }
    $msgs.appendChild(wrap);
    $msgs.scrollTop = $msgs.scrollHeight;
    return wrap;
  }

  function addTypingIndicator() {
    const t = document.createElement('div');
    t.className = 'cw-msg bot';
    t.id = 'cwTyping';
    t.innerHTML = `
      <div class="cw-msg-av">${botAvatarSVG()}</div>
      <div class="cw-msg-bubble">
        <div class="cw-typing">
          <div class="cw-typing-dot"></div>
          <div class="cw-typing-dot"></div>
          <div class="cw-typing-dot"></div>
        </div>
      </div>`;
    $msgs.appendChild(t);
    $msgs.scrollTop = $msgs.scrollHeight;
  }
  function removeTyping() { document.getElementById('cwTyping')?.remove(); }

  function setOpts(opts) {
    $opts.innerHTML = '';
    opts.forEach(o => {
      const btn = document.createElement('button');
      btn.className = 'cw-qopt';
      btn.textContent = o.label;
      btn.addEventListener('click', o.action);
      $opts.appendChild(btn);
    });
  }

  function addWACard(waUrl, title, subtitle) {
    const waSVG = `<svg viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>`;
    const card = document.createElement('a');
    card.href = waUrl;
    card.target = '_blank';
    card.rel = 'noopener noreferrer';
    card.className = 'cw-wa-card';
    card.innerHTML = `
      <div class="cw-wa-card-ico">${waSVG}</div>
      <div class="cw-wa-card-text"><h5>${esc(title)}</h5><p>${esc(subtitle)}</p></div>
      <div class="cw-wa-card-arrow">→</div>`;
    const wrap = document.createElement('div');
    wrap.className = 'cw-msg bot';
    const inner = document.createElement('div');
    inner.appendChild(card);
    wrap.appendChild(inner);
    $msgs.appendChild(wrap);
    $msgs.scrollTop = $msgs.scrollHeight;
  }

  // ── BOT SAY (with typing delay) ───────────────────────────────
  function botSay(text, delay = 800, isHtml = false) {
    return new Promise(resolve => {
      addTypingIndicator();
      setTimeout(() => {
        removeTyping();
        addMsg('bot', text, isHtml);
        resolve();
      }, delay);
    });
  }

  // ── CONVERSATION FLOWS ────────────────────────────────────────
  async function startConversation() {
    leadData = {};
    conversationHistory = [];
    awaitingInput = null;
    await botSay("👋 Hi! I'm EWaste Kochi's AI assistant.", 600);
    await botSay("I can help you schedule <strong>free e-waste pickup</strong>, get price quotes, or handle <strong>corporate ITAD</strong> for your Kochi business. 🌿", 1200, true);
    setOpts([
      { label: '♻️ Schedule Pickup',   action: () => pickupFlow() },
      { label: '💰 Get Price Quote',   action: () => priceFlow() },
      { label: '🏢 Corporate ITAD',    action: () => corporateFlow() },
      { label: '🔐 Data Destruction',  action: () => dataDestrFlow() },
      { label: '❓ Ask a Question',    action: () => askFlow() },
    ]);
  }

  async function pickupFlow() {
    leadData.service = 'E-Waste Pickup';
    setOpts([]); addMsg('user', '♻️ Schedule Pickup');
    await botSay("Great! Let's schedule your <strong>free pickup</strong> in Kochi. 🚛", 700, true);
    await botSay("We cover all of Ernakulam — Infopark, Kakkanad, Edapally, Aluva, Marine Drive, and everywhere else.", 1200);
    await botSay("What items do you have? (laptops, servers, phones, printers…)", 1800);
    awaitingInput = 'items';
    $input.placeholder = 'e.g. 50 laptops, 3 servers…';
  }

  async function priceFlow() {
    leadData.service = 'Price Quote';
    setOpts([]); addMsg('user', '💰 Get Price Quote');
    await botSay("Happy to give you a quote! 📋", 700);
    await botSay("Quick info: working devices may have <strong>buyback value</strong> that offsets or eliminates your cost entirely.", 1200, true);
    await botSay("What type of equipment are you looking to dispose?", 1800);
    setOpts([
      { label: 'Laptops / Desktops',  action: () => handleItemSelect('Laptops/Desktops') },
      { label: 'Servers',             action: () => handleItemSelect('Servers') },
      { label: 'Hard Drives / SSDs',  action: () => handleItemSelect('Hard Drives/SSDs') },
      { label: 'Mobile Phones',       action: () => handleItemSelect('Mobile Phones') },
      { label: 'Mixed / Multiple',    action: () => handleItemSelect('Mixed equipment') },
    ]);
  }

  async function corporateFlow() {
    leadData.service = 'Corporate ITAD';
    setOpts([]); addMsg('user', '🏢 Corporate ITAD');
    await botSay("Our <strong>corporate ITAD team</strong> handles everything — certified data destruction, asset remarketing, PCB recycling, and full compliance documentation. 🏆", 800, true);
    await botSay("We specialize in Infopark companies, banks, hospitals, and government institutions in Kochi.", 1400);
    await botSay("What's your company name and industry?", 2000);
    awaitingInput = 'company';
    $input.placeholder = 'e.g. TechCorp Pvt Ltd, Banking, Healthcare…';
  }

  async function dataDestrFlow() {
    leadData.service = 'Data Destruction';
    setOpts([]); addMsg('user', '🔐 Data Destruction');
    await botSay("We provide <strong>NIST SP 800-88</strong> certified data destruction — software wipe, degaussing, or physical shredding to ≤2mm. 🔒", 800, true);
    await botSay("Every device gets a <strong>Certificate of Destruction</strong> (CoD) with serial number. DPDP Act 2023 compliant.", 1400, true);
    await botSay("What media needs to be destroyed?", 2000);
    setOpts([
      { label: 'Hard Drives (HDD)',   action: () => handleItemSelect('Hard Drives (HDD)') },
      { label: 'SSDs / NVMe',         action: () => handleItemSelect('SSDs/NVMe') },
      { label: 'Laptops (full)',       action: () => handleItemSelect('Full laptops') },
      { label: 'Tapes / USB / SD',    action: () => handleItemSelect('Tapes/USB/SD cards') },
      { label: 'Servers / Arrays',    action: () => handleItemSelect('Server storage') },
    ]);
  }

  async function askFlow() {
    setOpts([]); addMsg('user', '❓ Ask a Question');
    await botSay("Go ahead — ask me anything about e-waste recycling, ITAD, data destruction, or DPDP Act compliance in Kochi. 🤖", 700);
    $input.placeholder = 'Type your question…';
    awaitingInput = 'freeform';
  }

  // ── ITEM / QTY / AREA FLOWS ───────────────────────────────────
  async function handleItemSelect(item) {
    leadData.items = item;
    setOpts([]); addMsg('user', item);
    await botSay(`Got it — <strong>${esc(item)}</strong>. How many units approximately?`, 700, true);
    setOpts([
      { label: '1–10',   action: () => handleQtySelect('1–10') },
      { label: '10–50',  action: () => handleQtySelect('10–50') },
      { label: '50–200', action: () => handleQtySelect('50–200') },
      { label: '200+',   action: () => handleQtySelect('200+ (bulk)') },
    ]);
  }

  async function handleQtySelect(qty) {
    leadData.qty = qty;
    setOpts([]); addMsg('user', qty);
    if (qty === '200+ (bulk)') {
      await botSay("Excellent — that's a <strong>bulk order</strong>! 🏢 Our corporate team will prioritize this.", 700, true);
      leadData.service = 'Corporate ITAD (Bulk)';
    } else {
      await botSay(`Great — <strong>${esc(qty)} units</strong>. 👍`, 700, true);
    }
    await botSay("Which area in Kochi should we collect from?", 1200);
    setOpts([
      { label: 'Infopark / Kakkanad',      action: () => handleAreaSelect('Infopark/Kakkanad') },
      { label: 'Edapally / Kaloor',        action: () => handleAreaSelect('Edapally/Kaloor') },
      { label: 'Marine Drive / MG Road',   action: () => handleAreaSelect('Marine Drive/MG Road') },
      { label: 'Aluva / Angamaly',         action: () => handleAreaSelect('Aluva/Angamaly') },
      { label: 'Thrippunithura',           action: () => handleAreaSelect('Thrippunithura') },
      { label: 'Other area',               action: () => handleAreaSelect('Other Kochi area') },
    ]);
  }

  async function handleAreaSelect(area) {
    leadData.location = area;
    setOpts([]); addMsg('user', area);
    await botSay(`Perfect — <strong>${esc(area)}</strong> is fully covered. ✅`, 700, true);
    await botSay("Almost done! What's your name so I can personalize your quote?", 1200);
    awaitingInput = 'name';
    $input.placeholder = 'Your name…';
  }

  // ── INPUT HANDLER ─────────────────────────────────────────────
  async function handleUserInput() {
    const val = $input.value.trim();
    if (!val) return;
    $input.value = '';
    addMsg('user', val);

    if (awaitingInput === 'freeform') {
      await handleFreeform(val);
    } else if (awaitingInput === 'items') {
      leadData.items = val;
      awaitingInput = null;
      $input.placeholder = 'Ask anything about e-waste in Kochi…';
      await botSay(`Got it — <strong>${esc(val)}</strong>. 👍`, 600, true);
      await botSay("How many units approximately?", 1000);
      setOpts([
        { label: '1–10',   action: () => handleQtySelect('1–10') },
        { label: '10–50',  action: () => handleQtySelect('10–50') },
        { label: '50–200', action: () => handleQtySelect('50–200') },
        { label: '200+',   action: () => handleQtySelect('200+ (bulk)') },
      ]);
    } else if (awaitingInput === 'company') {
      leadData.company = val;
      awaitingInput = null;
      $input.placeholder = 'Ask anything…';
      await botSay(`Thanks! And approximately how many IT assets?`, 700);
      setOpts([
        { label: '50–200',  action: () => handleQtySelect('50–200') },
        { label: '200–500', action: () => handleQtySelect('200+') },
        { label: '500+',    action: () => handleQtySelect('200+ (bulk)') },
      ]);
    } else if (awaitingInput === 'name') {
      leadData.name = val;
      awaitingInput = 'phone';
      $input.placeholder = 'Your WhatsApp number…';
      await botSay(`Hi <strong>${esc(val)}</strong>! 👋 What's your WhatsApp number so our team can confirm your slot?`, 700, true);
    } else if (awaitingInput === 'phone') {
      leadData.phone = val;
      awaitingInput = null;
      $input.placeholder = 'Ask anything about e-waste in Kochi…';
      await showSummaryAndHandoff();
    } else {
      await handleFreeform(val);
    }
  }

  // ── AI FREEFORM ───────────────────────────────────────────────
  const SYSTEM_PROMPT = `You are EWaste Kochi's AI sales assistant. EWaste Kochi is Kerala's #1 certified ITAD and e-waste recycling company in Thrippunithura, Kochi (682301).

Services: Free e-waste pickup (all Ernakulam), NIST 800-88 data destruction, ITAD, hard drive shredding (≤2mm), SSD secure erasure, server recycling, laptop buyback, data centre decommissioning.
Phone: ${PHONE} | WhatsApp: wa.me/${WA_NUM}
Pricing: Data wipe from ₹150/device, shredding from ₹200/drive, ITAD free for bulk clients.
Key facts: Kerala PCB authorized, DPDP Act 2023 compliant, Certificate of Destruction every device, free bulk pickup, same-day available, 5000+ clients, 4.9★ Google.

Rules:
- Be warm, helpful, conversational. Use emojis occasionally.
- Keep replies SHORT (2–3 sentences max).
- Always aim to qualify the lead and move toward WhatsApp handoff or scheduling pickup.
- If asked something outside your knowledge, direct to WhatsApp: ${PHONE}.`;

  async function handleFreeform(question) {
    addTypingIndicator();
    conversationHistory.push({ role: 'user', content: question });

    // If no API key configured, fall back gracefully
    if (!ANTHROPIC_API_KEY || ANTHROPIC_API_KEY === 'YOUR_ANTHROPIC_API_KEY_HERE') {
      setTimeout(() => {
        removeTyping();
        addMsg('bot', answerLocally(question));
        conversationHistory.push({ role: 'assistant', content: 'local' });
        if (conversationHistory.length >= 4) setTimeout(() => offerWAHandoff(), 1200);
      }, 900);
      return;
    }

    try {
      const res = await fetch('https://api.anthropic.com/v1/messages', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'x-api-key': ANTHROPIC_API_KEY,
          'anthropic-version': '2023-06-01',
          'anthropic-dangerous-direct-browser-access': 'true'
        },
        body: JSON.stringify({
          model: 'claude-sonnet-4-20250514',
          max_tokens: 300,
          system: SYSTEM_PROMPT,
          messages: conversationHistory
        })
      });
      const data = await res.json();
      removeTyping();
      const reply = data.content?.[0]?.text || "For the fastest response, WhatsApp us directly at " + PHONE + " 📲";
      addMsg('bot', reply);
      conversationHistory.push({ role: 'assistant', content: reply });
      if (conversationHistory.length >= 4) setTimeout(() => offerWAHandoff(), 1200);
    } catch (e) {
      removeTyping();
      addMsg('bot', answerLocally(question));
      setTimeout(() => offerWAHandoff(), 1200);
    }
  }

  // Local FAQ fallback (no API needed)
  function answerLocally(q) {
    const lq = q.toLowerCase();
    if (lq.includes('free') && lq.includes('pickup'))
      return "Yes! Free doorstep pickup for bulk corporate clients across all of Ernakulam — Infopark, Kakkanad, Edapally, Aluva and more. Same-day available. 🚛";
    if (lq.includes('certificate') || lq.includes('cod'))
      return "Yes — every job gets a legally valid Certificate of Destruction (CoD) with device serial numbers, destruction method and date. Accepted by RBI and NABH auditors. 📜";
    if (lq.includes('nist') || lq.includes('dod') || lq.includes('data destruction'))
      return "We use NIST 800-88, DoD 5220.22-M, degaussing & physical shredding (≤2mm). 100% unrecoverable, even with forensic tools. CoD issued per device. 🔒";
    if (lq.includes('dpdp') || lq.includes('compliance') || lq.includes('legal'))
      return "We're fully DPDP Act 2023 and E-Waste Rules 2022 compliant, authorized by Kerala State PCB. Non-compliance fines can reach ₹250 crore. We keep you protected. ✅";
    if (lq.includes('price') || lq.includes('cost') || lq.includes('rate'))
      return "Data wipe from ₹150/device, shredding from ₹200/drive. Free pickup for bulk clients. Working laptops may earn you ₹8,000–₹25,000 each in buyback! 💰";
    if (lq.includes('infopark') || lq.includes('kakkanad') || lq.includes('edapally'))
      return "Yes! We're the preferred ITAD partner for IT companies in Infopark Kakkanad and Smart City Kochi. Free bulk pickup, NIST-compliant destruction and CoD included. 🏢";
    return `Great question! For the fastest and most accurate answer, WhatsApp our team directly at ${PHONE}. We respond instantly. 📲`;
  }

  function offerWAHandoff() {
    const waText = encodeURIComponent(`Hi! I was chatting with your AI assistant about: ${leadData.service || 'e-waste services'} in Kochi.`);
    addWACard(`${WA_BASE}?text=${waText}`, 'Continue on WhatsApp', 'Get instant reply from our team · Free quote');
  }

  // ── FINAL SUMMARY + HANDOFF ───────────────────────────────────
  async function showSummaryAndHandoff() {
    const s = leadData;
    await botSay(`Perfect, <strong>${esc(s.name)}</strong>! Here's your summary:`, 600, true);
    const summary = `
📋 <strong>Service:</strong> ${esc(s.service || 'E-Waste Pickup')}<br>
📦 <strong>Items:</strong> ${esc(s.items || 'E-Waste')}<br>
🔢 <strong>Quantity:</strong> ${esc(s.qty || 'To confirm')}<br>
📍 <strong>Location:</strong> ${esc(s.location || 'Kochi')}<br>
📱 <strong>WhatsApp:</strong> ${esc(s.phone)}`;
    addMsg('bot', summary, true);
    await botSay("✅ Our team will confirm your free pickup slot via WhatsApp shortly!", 1200);
    await botSay("Tap below to chat directly and get your <strong>exact time slot</strong>:", 2000, true);
    const waMsg = encodeURIComponent(`Hi EWaste Kochi! I'm ${s.name}, interested in ${s.service || 'e-waste pickup'} for ${s.items || 'equipment'} (${s.qty} units) from ${s.location}, Kochi. Please confirm my slot.`);
    addWACard(`${WA_BASE}?text=${waMsg}`, 'Confirm Slot on WhatsApp', `${s.name} · ${s.items} · ${s.location}`);
    setOpts([
      { label: '🔄 Start Over', action: () => { $msgs.innerHTML = ''; $opts.innerHTML = ''; leadData = {}; startConversation(); } }
    ]);
  }

  // ── INIT ──────────────────────────────────────────────────────
  function init() {
    injectMarkup();
    refs();

    document.getElementById('cwTrigger').addEventListener('click', openChat);
    document.getElementById('cwClose').addEventListener('click', closeChat);
    document.getElementById('cwMinimize').addEventListener('click', openChat);
    document.getElementById('cwCloseMin').addEventListener('click', e => {
      e.stopPropagation();
      $minimize.style.display = 'none';
    });
    document.getElementById('cwSend').addEventListener('click', handleUserInput);
    $input.addEventListener('keydown', e => { if (e.key === 'Enter') handleUserInput(); });

    // Show minimize prompt after 8 seconds if not opened
    setTimeout(() => { if (!isOpen) $minimize.style.display = 'flex'; }, 8000);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
