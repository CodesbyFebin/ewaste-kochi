const root = document.getElementById('ew-chat-root');

if (root && root.dataset.initialized !== 'true') {
  root.dataset.initialized = 'true';

  const contextKey = root.dataset.page || 'homepage';
  const phoneDisplay = root.dataset.phone || '+91 75005 55454';
  const phoneLink = root.dataset.phoneLink || 'tel:+917500555454';
  const whatsappNumber = root.dataset.whatsappNumber || '917500555454';
  const defaultWhatsApp = root.dataset.whatsappLink || `https://wa.me/${whatsappNumber}`;

  const contexts = {
    homepage: {
      label: 'General Enquiry',
      hook: 'Fast answers for pickup, pricing, and ITAD questions.',
      greeting:
        'Hi, I can help you with **pickup**, **ITAD**, **data destruction**, **battery recycling**, or **device buyback**. What are you trying to dispose or sell today?',
      quickReplies: ['Free pickup', 'Corporate ITAD', 'Sell laptop', 'Battery recycling'],
    },
    pickup: {
      label: 'Pickup',
      hook: 'Same-day slots open for bulk collections in Kochi.',
      greeting:
        'Need a pickup plan? Tell me your **area**, **approximate quantity**, and whether the load includes **laptops, batteries, or servers**.',
      quickReplies: ['Book pickup', 'Check my area', 'Office clearance', 'Residential drop-off'],
    },
    collection: {
      label: 'Collection',
      hook: 'Collection workflows for homes, schools, and offices.',
      greeting:
        'I can help you turn a mixed e-waste load into a clean collection plan. What items are you trying to hand over?',
      quickReplies: ['Mixed electronics', 'School collection', 'Corporate clearance', 'Need a quote'],
    },
    recycling: {
      label: 'Recycling',
      hook: 'Certified recycling, zero-landfill intent, and clear next steps.',
      greeting:
        'Looking for the right recycling path? I can explain **reuse vs recycling**, **battery handling**, and **what pickup includes**.',
      quickReplies: ['How recycling works', 'Office recycling drive', 'Battery handling', 'Zero-landfill'],
    },
    laptop: {
      label: 'Laptop Buyback',
      hook: 'Business laptops and MacBooks usually deserve a value check first.',
      greeting:
        'Tell me the **laptop model**, **condition**, and **quantity** and I will point you toward the best path: **buyback**, **secure wipe**, or **recycling**.',
      quickReplies: ['Sell MacBook', 'Bulk laptops', 'Secure wipe first', 'Damaged laptop'],
    },
    mobile: {
      label: 'Mobile Recycling',
      hook: 'Fast phone quotes with safer data and battery handling.',
      greeting:
        'Phone or tablet disposal is usually a resale-or-recycle decision. Share the **model** or the **fleet size** and I will narrow the next step.',
      quickReplies: ['Sell iPhone', 'Corporate mobile fleet', 'Tablet disposal', 'Swollen battery'],
    },
    corporate: {
      label: 'Corporate ITAD',
      hook: 'Audit-ready workflows for device refreshes and office exits.',
      greeting:
        'For corporate ITAD, the key details are **device count**, **location**, **timeline**, and whether you need **certificates** or **NIST-style wiping**.',
      quickReplies: ['ITAD quote', 'Need certificates', 'Asset recovery', 'Chain of custody'],
    },
    itad: {
      label: 'Data & ITAD',
      hook: 'Best fit for certificates, NIST workflows, and secure retirement.',
      greeting:
        'If the load contains storage devices, I can help you decide between **wiping**, **shredding**, and a full **ITAD workflow**.',
      quickReplies: ['Hard drive shredding', 'NIST wipe', 'Certificate of destruction', 'DPDP compliance'],
    },
    battery: {
      label: 'Battery Recycling',
      hook: 'Battery loads need safer packaging and pickup planning.',
      greeting:
        'Batteries are handled separately from general e-waste. Tell me whether you have **lithium-ion**, **lead-acid**, **UPS**, or a mixed battery load.',
      quickReplies: ['Laptop batteries', 'UPS batteries', 'Lithium safety', 'Battery pickup'],
    },
    scrap: {
      label: 'Scrap & Buyback',
      hook: 'Check value before selling everything as mixed scrap.',
      greeting:
        'If you are comparing scrap buyers, tell me the **device types** and whether anything is still working. That usually changes the quote a lot.',
      quickReplies: ['Scrap laptops', 'Office clearance', 'Server scrap', 'Need price range'],
    },
    compliance: {
      label: 'Compliance',
      hook: 'Strong for KSPCB, DPDP, and certificate-related questions.',
      greeting:
        'Need help with **DPDP**, **KSPCB authorization**, or **audit-ready disposal**? Tell me what the compliance question looks like and I will point you in the right direction.',
      quickReplies: ['DPDP disposal', 'Audit documents', 'Verify recycler', 'Bulk consumer rules'],
    },
  };

  const context = contexts[contextKey] || contexts.homepage;

  const replyCatalog = {
    pickup: {
      text:
        'For pickup planning, the fastest quote comes from three details: **area**, **quantity**, and whether the load includes **batteries or storage devices**. Once you have that, the team can usually confirm the best slot on WhatsApp very quickly.',
      replies: ['Share my area', 'Need same-day slot', 'Office clearance', 'WhatsApp quote'],
    },
    corporate: {
      text:
        'For corporate loads, start with **device count**, **pickup location**, and whether you need **certificates**, **chain of custody**, or **asset recovery**. That keeps the ITAD scope tight and avoids getting a generic scrap quote for a compliance-sensitive job.',
      replies: ['Need ITAD scope', 'Need certificates', 'Asset recovery', 'WhatsApp quote'],
    },
    laptop: {
      text:
        'Laptop projects usually split into two paths: **buyback** for working devices and **secure destruction + recycling** for retired assets with low value. If you share the model and condition, the team can tell you which side of that line you are on.',
      replies: ['Sell MacBook', 'Bulk laptops', 'Need secure wipe', 'WhatsApp quote'],
    },
    mobile: {
      text:
        'Phone and tablet jobs usually move fastest when you share the **model**, **condition**, and whether the battery is healthy. That helps separate **buyback**, **battery handling**, and **data wiping** before pickup is booked.',
      replies: ['Sell iPhone', 'Corporate mobiles', 'Damaged phone', 'WhatsApp quote'],
    },
    battery: {
      text:
        'Battery loads need a little extra care before pickup. The key questions are **battery type**, **approximate quantity**, and whether anything is swollen, damaged, or leaking. That changes how the job is staged and transported.',
      replies: ['Lithium batteries', 'UPS batteries', 'Need pickup', 'WhatsApp quote'],
    },
    data: {
      text:
        'If data is involved, the best next step is to decide whether you need **certified wiping**, **physical destruction**, or a full **certificate-backed workflow**. The team can scope that quickly once they know the device types and quantity.',
      replies: ['Hard drive shredding', 'Need certificate', 'NIST wipe', 'WhatsApp quote'],
    },
    compliance: {
      text:
        'Compliance questions usually come down to **authorization**, **documentation**, and the exact device mix. A cleaner vendor shortlist starts with asking for pickup records, destruction evidence, and the recycling path for the material after collection.',
      replies: ['DPDP question', 'Need audit docs', 'Verify recycler', 'WhatsApp quote'],
    },
    price: {
      text:
        'Pricing usually changes based on **working vs non-working devices**, **quantity**, and whether the load can move through **buyback** instead of pure recycling. If you share the item mix, the team can usually narrow the right range very quickly.',
      replies: ['Price my load', 'Sell laptops', 'Sell phones', 'WhatsApp quote'],
    },
    recycling: {
      text:
        'Recycling works best when the load is separated into **reusable devices**, **data-bearing assets**, **battery items**, and **pure scrap**. That is how you protect value and still keep the downstream route clean and documented.',
      replies: ['How recycling works', 'Need pickup', 'Battery handling', 'WhatsApp quote'],
    },
    general: {
      text:
        'The fastest way to move forward is to tell me the **item type**, **location**, and whether you care most about **pickup speed**, **compliance**, or **best value**. From there I can point you toward the right service path.',
      replies: context.quickReplies,
    },
  };

  const state = {
    isOpen: false,
    hasStarted: false,
    messageCount: 0,
  };

  const intentMatchers = [
    ['battery', /\bbattery|ups|inverter|lithium|lead acid|ev\b/i],
    ['data', /\bdata|wipe|wiping|destroy|destruction|shred|shredding|degauss|certificate\b/i],
    ['corporate', /\bitad|corporate|company|office|audit|procurement|bank|hospital|school|college|server room\b/i],
    ['laptop', /\blaptop|macbook|notebook|thinkpad|elitebook|latitude\b/i],
    ['mobile', /\bphone|iphone|mobile|tablet|ipad|samsung|oneplus\b/i],
    ['pickup', /\bpickup|pick up|collect|collection|slot|drop off|drop-off\b/i],
    ['price', /\bprice|quote|cost|value|buyers|buyback|sell|rate|scrap\b/i],
    ['compliance', /\bdpdp|kspcb|rule|rules|compliance|certificate|authorized|audit\b/i],
    ['recycling', /\brecycle|recycling|ewaste|e-waste|environment|zero landfill|circular\b/i],
  ];

  const escapeHtml = (value) =>
    value.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

  const formatMessage = (value) =>
    escapeHtml(value).replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>').replace(/\n/g, '<br>');

  const detectIntent = (value) => {
    for (const [intent, matcher] of intentMatchers) {
      if (matcher.test(value)) return intent;
    }
    return 'general';
  };

  const makeWhatsAppUrl = (value) => {
    const text = encodeURIComponent(value);
    return `https://wa.me/${whatsappNumber}?text=${text}`;
  };

  const buildWhatsAppMessage = (userText, intent) =>
    `Hi EWaste Kochi,\n\nI am on the ${context.label} page.\nIntent: ${intent}\nDetails: ${userText}\n\nPlease help me with the right next step.`;

  root.innerHTML = `
    <div class="ew-chat-launcher">
      <div class="ew-chat-tip" id="ew-chat-tip">
        <strong>${context.label}</strong>
        ${context.hook}
      </div>
      <button class="ew-chat-button" id="ew-chat-button" type="button" aria-label="Open chat">Chat</button>
    </div>
    <section class="ew-chat-window" id="ew-chat-window" aria-label="EWaste Kochi chat">
      <header class="ew-chat-header">
        <div class="ew-chat-header-row">
          <div>
            <div class="ew-chat-title">EWaste Kochi Chat</div>
            <div class="ew-chat-subtitle">${phoneDisplay} - reply-ready WhatsApp handoff</div>
          </div>
          <div class="ew-chat-header-row">
            <a class="ew-chat-link" href="${phoneLink}" aria-label="Call">Call</a>
            <a class="ew-chat-link" href="${defaultWhatsApp}" target="_blank" rel="noopener" aria-label="WhatsApp">WA</a>
            <button class="ew-chat-close" id="ew-chat-close" type="button" aria-label="Close">X</button>
          </div>
        </div>
        <div class="ew-chat-badge">${context.label}</div>
      </header>
      <div class="ew-chat-body">
        <div class="ew-chat-messages" id="ew-chat-messages"></div>
        <div class="ew-chat-quick-replies" id="ew-chat-quick-replies"></div>
        <a class="ew-chat-cta" id="ew-chat-cta" href="${defaultWhatsApp}" target="_blank" rel="noopener">
          <span id="ew-chat-cta-label">Continue on WhatsApp</span>
          <span>-&gt;</span>
        </a>
        <div class="ew-chat-input-row">
          <textarea class="ew-chat-input" id="ew-chat-input" rows="1" placeholder="Ask about pickup, pricing, ITAD, batteries, or secure disposal..."></textarea>
          <button class="ew-chat-send" id="ew-chat-send" type="button" aria-label="Send">-&gt;</button>
        </div>
      </div>
    </section>
  `;

  const launcherButton = document.getElementById('ew-chat-button');
  const closeButton = document.getElementById('ew-chat-close');
  const tip = document.getElementById('ew-chat-tip');
  const windowEl = document.getElementById('ew-chat-window');
  const messagesEl = document.getElementById('ew-chat-messages');
  const quickRepliesEl = document.getElementById('ew-chat-quick-replies');
  const ctaEl = document.getElementById('ew-chat-cta');
  const ctaLabelEl = document.getElementById('ew-chat-cta-label');
  const inputEl = document.getElementById('ew-chat-input');
  const sendButton = document.getElementById('ew-chat-send');

  const scrollToBottom = () => {
    messagesEl.scrollTop = messagesEl.scrollHeight;
  };

  const addMessage = (text, isUser = false) => {
    const wrapper = document.createElement('div');
    wrapper.className = `ew-chat-message${isUser ? ' is-user' : ''}`;
    const bubble = document.createElement('div');
    bubble.className = 'ew-chat-bubble';
    bubble.innerHTML = formatMessage(text);
    wrapper.appendChild(bubble);
    messagesEl.appendChild(wrapper);
    scrollToBottom();
  };

  const addTyping = () => {
    const wrapper = document.createElement('div');
    wrapper.className = 'ew-chat-message';
    wrapper.id = 'ew-chat-typing';
    const bubble = document.createElement('div');
    bubble.className = 'ew-chat-bubble';
    bubble.innerHTML = '<div class="ew-chat-typing"><span></span><span></span><span></span></div>';
    wrapper.appendChild(bubble);
    messagesEl.appendChild(wrapper);
    scrollToBottom();
  };

  const removeTyping = () => {
    const typing = document.getElementById('ew-chat-typing');
    if (typing) typing.remove();
  };

  const setQuickReplies = (replies) => {
    quickRepliesEl.innerHTML = '';
    replies.forEach((reply) => {
      const button = document.createElement('button');
      button.type = 'button';
      button.textContent = reply;
      button.addEventListener('click', () => sendMessage(reply));
      quickRepliesEl.appendChild(button);
    });
  };

  const showCta = (intent, userText) => {
    const label = intent === 'price' ? 'Get a quote on WhatsApp' : 'Continue on WhatsApp';
    ctaLabelEl.textContent = label;
    ctaEl.href = makeWhatsAppUrl(buildWhatsAppMessage(userText, intent));
    ctaEl.classList.add('is-visible');
  };

  const buildReply = (userText) => {
    const intent = detectIntent(userText);
    const catalogEntry = replyCatalog[intent] || replyCatalog.general;
    return {
      intent,
      text: catalogEntry.text,
      replies: catalogEntry.replies || context.quickReplies,
    };
  };

  const startConversation = () => {
    if (state.hasStarted) return;
    state.hasStarted = true;
    addMessage(context.greeting);
    setQuickReplies(context.quickReplies);
  };

  const openWidget = () => {
    windowEl.classList.add('is-open');
    state.isOpen = true;
    tip.style.display = 'none';
    startConversation();
    setTimeout(() => inputEl.focus(), 100);
  };

  const closeWidget = () => {
    windowEl.classList.remove('is-open');
    state.isOpen = false;
  };

  const sendMessage = (rawValue) => {
    const userText = rawValue.trim();
    if (!userText) return;

    addMessage(userText, true);
    inputEl.value = '';
    sendButton.disabled = true;
    addTyping();

    window.setTimeout(() => {
      removeTyping();
      const reply = buildReply(userText);
      addMessage(reply.text);
      setQuickReplies(reply.replies);
      showCta(reply.intent, userText);
      sendButton.disabled = false;
      inputEl.focus();
      state.messageCount += 1;

      if (window.dataLayer) {
        window.dataLayer.push({
          event: 'ew_chat_message',
          page_context: contextKey,
          intent: reply.intent,
        });
      }
    }, 520);
  };

  launcherButton.addEventListener('click', () => {
    if (state.isOpen) closeWidget();
    else openWidget();
  });

  closeButton.addEventListener('click', closeWidget);
  sendButton.addEventListener('click', () => sendMessage(inputEl.value));
  inputEl.addEventListener('keydown', (event) => {
    if (event.key === 'Enter' && !event.shiftKey) {
      event.preventDefault();
      sendMessage(inputEl.value);
    }
  });

  window.setTimeout(() => {
    if (!state.isOpen) {
      tip.style.display = 'block';
    }
  }, 1800);

  window.setTimeout(() => {
    if (!state.isOpen) openWidget();
  }, 3800);

  window.addEventListener(
    'scroll',
    () => {
      if (!state.isOpen && window.scrollY > 260) {
        openWidget();
      }
    },
    { passive: true },
  );
}
