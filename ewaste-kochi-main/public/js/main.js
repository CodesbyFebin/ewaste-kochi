/* ============================================================
   EWASTEKOCHI.COM — SHARED JAVASCRIPT
   All pages include this script
   ============================================================ */

/* ── NAV ── */
function toggleMobileNav(){
  document.getElementById('mobile-nav').classList.toggle('open');
  const ov=document.getElementById('nav-overlay');
  ov.classList.toggle('show');
  document.body.style.overflow=document.getElementById('mobile-nav').classList.contains('open')?'hidden':'';
}
function closeMobileNav(){
  const mn=document.getElementById('mobile-nav');
  const ov=document.getElementById('nav-overlay');
  if(mn)mn.classList.remove('open');
  if(ov)ov.classList.remove('show');
  document.body.style.overflow='';
}
window.addEventListener('scroll',()=>{
  const nav=document.getElementById('main-nav');
  if(!nav)return;
  if(window.scrollY>60){nav.style.background='rgba(7,16,10,.98)';nav.style.boxShadow='0 4px 32px rgba(0,0,0,.4)';}
  else{nav.style.background='rgba(7,16,10,.93)';nav.style.boxShadow='none';}
},{passive:true});

/* ── FAQ ── */
function toggleFaq(btn){
  const item=btn.closest('.faq-item');
  const body=item.querySelector('.faq-body');
  const isOpen=item.classList.contains('open');
  const list=btn.closest('.faq-list')||btn.closest('.faq-section')||document.body;
  list.querySelectorAll('.faq-item.open').forEach(oi=>{
    if(oi!==item){
      oi.classList.remove('open');
      const ob=oi.querySelector('.faq-body');
      if(ob){ob.style.maxHeight='0';ob.style.padding='0 20px';}
    }
  });
  if(isOpen){item.classList.remove('open');body.style.maxHeight='0';body.style.padding='0 20px';}
  else{item.classList.add('open');body.style.maxHeight=body.scrollHeight+40+'px';body.style.padding='0 20px 16px';}
}

/* ── BUYBACK CALCULATOR ── */
const CALC_BASE={
  laptop:{apple:80000,dell:40000,hp:35000,lenovo:48000,samsung:22000,oneplus:0,other:18000},
  phone:{apple:70000,dell:0,hp:0,lenovo:20000,samsung:52000,oneplus:32000,other:14000},
  desktop:{apple:32000,dell:22000,hp:20000,lenovo:26000,samsung:14000,oneplus:0,other:12000},
  tablet:{apple:45000,dell:0,hp:18000,lenovo:22000,samsung:28000,oneplus:20000,other:10000},
  server:{apple:0,dell:60000,hp:55000,lenovo:58000,samsung:0,oneplus:0,other:30000}
};
const CALC_BRAND={apple:'Apple',dell:'Dell',hp:'HP',lenovo:'Lenovo',samsung:'Samsung',oneplus:'OnePlus',other:'Other'};
const CALC_COND={excellent:1.0,good:0.78,fair:0.55,damaged:0.28};
const CALC_AGE={1:.92,2:.75,3:.58,4:.42,5:.3,6:.2};
let calcType='laptop';

function calcSelectType(el,type){
  document.querySelectorAll('.calc-type-btn').forEach(b=>b.classList.remove('active'));
  el.classList.add('active');
  calcType=type;
  calcUpdate();
}

function calcUpdate(){
  const brand=document.getElementById('calc-brand')?.value||'apple';
  const age=parseInt(document.getElementById('calc-age')?.value||'2');
  const cond=document.getElementById('calc-cond')?.value||'good';
  const qty=parseInt(document.getElementById('calc-qty')?.value||'1');
  const base=(CALC_BASE[calcType]?.[brand]||15000);
  const condM=CALC_COND[cond]||.78;
  const ageM=CALC_AGE[age]||.3;
  const qtyBonus=qty>=100?1.07:qty>=25?1.04:qty>=5?1.02:1;
  const mid=Math.round(base*condM*ageM*qtyBonus/500)*500;
  const low=Math.max(mid-2500,500);
  const high=mid+3000;
  const res=document.getElementById('calc-result');
  const sub=document.getElementById('calc-sub');
  const bdwn=document.getElementById('calc-breakdown');
  const waLink=document.getElementById('wa-calc-link');
  const bulk=document.getElementById('calc-bulk');
  if(res)res.textContent=`₹${low.toLocaleString('en-IN')} – ₹${high.toLocaleString('en-IN')}`;
  if(sub)sub.textContent=`${CALC_BRAND[brand]||'Device'} ${calcType} · ${age}yr · ${cond.charAt(0).toUpperCase()+cond.slice(1)}`;
  if(bdwn)bdwn.innerHTML=`Base: ₹${base.toLocaleString('en-IN')} · Age ×${ageM} · Cond ×${condM}${qty>=5?' · Bulk ×'+qtyBonus:''}<br>→ <strong style="color:var(--green)">₹${low.toLocaleString('en-IN')} – ₹${high.toLocaleString('en-IN')}</strong>`;
  if(bulk)bulk.style.display=qty>=25?'flex':'none';
  if(waLink){
    const msg=encodeURIComponent(`Hi, I want to sell my ${CALC_BRAND[brand]||''} ${calcType}. Estimated price ₹${low.toLocaleString('en-IN')}–₹${high.toLocaleString('en-IN')}. Age: ${age}yr, Condition: ${cond}. Please confirm.`);
    waLink.href=`https://wa.me/919876543210?text=${msg}`;
  }
}

/* ── LEAD FORM ── */
function submitLead(e){
  e.preventDefault();
  const btn=e.target.querySelector('button[type="submit"]');
  if(btn){btn.textContent='⏳ Sending...';btn.disabled=true;}
  setTimeout(()=>{
    const form=e.target;
    const success=document.getElementById('lead-success');
    if(form)form.style.display='none';
    if(success)success.style.display='block';
  },1200);
}

/* ── CONTACT FORM ── */
function submitContact(e){
  e.preventDefault();
  const btn=e.target.querySelector('button[type="submit"]');
  if(btn){btn.textContent='⏳ Sending...';btn.disabled=true;}
  setTimeout(()=>{
    const form=e.target;
    const success=document.getElementById('contact-success');
    if(form)form.style.display='none';
    if(success)success.style.display='block';
  },1200);
}

/* ── CHATBOT ENGINE ── */
const CHAT_TREE={
  start:{msg:"Hi! 👋 I'm the EWaste Kochi assistant. How can I help you today?",options:[
    {label:"💻 Sell a laptop or phone",next:'sell'},
    {label:"🏢 Corporate ITAD / bulk disposal",next:'itad'},
    {label:"🔒 Data destruction services",next:'data'},
    {label:"⚖️ DPDP Act compliance",next:'dpdp'},
    {label:"📋 Get free quote",next:'quote'}
  ]},
  sell:{msg:"Great! We offer Kochi's best buyback prices — 15–20% above Cashify for business laptops. What are you selling?",options:[
    {label:"💻 Laptop",next:'sell_laptop'},
    {label:"📱 Smartphone",next:'sell_phone'},
    {label:"🖥️ Desktop / Server",next:'sell_other'}
  ]},
  sell_laptop:{msg:"MacBook Pro M1/M2: up to ₹85,000. Dell/HP business laptops: up to ₹45,000. Lenovo ThinkPad: up to ₹50,000. Certificate of Data Destruction included. Same-day payment via UPI.",options:[
    {label:"💰 Use price estimator",next:'calc_link'},
    {label:"💬 WhatsApp for exact price",next:'wa'},
    {label:"📞 Call for instant quote",next:'call'}
  ]},
  sell_phone:{msg:"iPhone 14/15 Pro: up to ₹75,000. Samsung Galaxy S24: up to ₹55,000. OnePlus flagship: up to ₹35,000. Certified forensic wipe included — factory reset is not enough.",options:[
    {label:"💬 WhatsApp for price",next:'wa'},
    {label:"📞 Call us",next:'call'},
    {label:"⬅️ Back",next:'start'}
  ]},
  sell_other:{msg:"We buy desktops, servers, tablets, networking gear — working or not. Give us the details and we'll quote.",options:[
    {label:"💬 WhatsApp with details",next:'wa'},
    {label:"⬅️ Back",next:'start'}
  ]},
  itad:{msg:"We handle end-to-end ITAD for Kochi businesses. Free pickup for 50+ units. NIST 800-88 wipe, Certificate of Destruction per device, full DPDP Act documentation. How many devices?",options:[
    {label:"📦 Under 50 devices",next:'itad_small'},
    {label:"📦 50–200 devices",next:'itad_bulk'},
    {label:"📦 200+ devices",next:'itad_enterprise'}
  ]},
  itad_small:{msg:"For smaller lots: drop off at our Thrippunithura facility (free), or pickup can be arranged. CoD issued for every device.",options:[{label:"💬 Book via WhatsApp",next:'wa'},{label:"📋 Fill quote form",next:'form_link'},{label:"⬅️ Back",next:'itad'}]},
  itad_bulk:{msg:"For 50–200 units: free next-day pickup anywhere in Ernakulam. Full NIST wipe + CoD per device. Turnaround 48–72 hours from pickup to CoD delivery.",options:[{label:"💬 WhatsApp corporate team",next:'wa'},{label:"📞 Call for scheduling",next:'call'},{label:"⬅️ Back",next:'itad'}]},
  itad_enterprise:{msg:"For 200+ devices: dedicated account manager, on-site destruction option, custom reporting, RBI/ISO compliance documentation. Our team calls within 1 hour.",options:[{label:"📋 Submit enterprise request",next:'form_link'},{label:"📞 Call enterprise line",next:'call'}]},
  data:{msg:"We offer: NIST 800-88 Overwrite (₹200/drive), Degaussing (₹350/drive), Physical Shredding (₹500/drive). All include Certificate of Destruction.",options:[
    {label:"🔒 NIST overwrite",next:'data_nist'},
    {label:"🧲 Degaussing",next:'data_degauss'},
    {label:"⚙️ Physical shredding",next:'data_shred'},
    {label:"❓ Help me choose",next:'data_advice'}
  ]},
  data_nist:{msg:"NIST 800-88 overwrite: ₹200/drive (single), ₹150 (50+), ₹100 (500+). Drive remains functional but 100% unrecoverable. CoD included.",options:[{label:"💬 Book via WhatsApp",next:'wa'},{label:"⬅️ Back",next:'data'}]},
  data_degauss:{msg:"Degaussing: ₹350/drive (single), ₹280 (50+), ₹200 (500+). For HDDs and LTO tapes. Drive unusable after. Required by some RBI audits.",options:[{label:"💬 Book",next:'wa'},{label:"⬅️ Back",next:'data'}]},
  data_shred:{msg:"Physical shredding: ₹500/HDD, ₹600/SSD. Most definitive method. On-site service available for banks and hospitals. Shred certificate issued.",options:[{label:"💬 Book shredding",next:'wa'},{label:"⬅️ Back",next:'data'}]},
  data_advice:{msg:"Quick guide: Reuse the drive → NIST Overwrite. Magnetic media only → Degaussing. Maximum certainty (SSDs/high-security) → Physical Shredding. All options satisfy DPDP Act compliance when combined with our CoD.",options:[{label:"💬 Discuss with team",next:'wa'},{label:"📞 Call for advice",next:'call'}]},
  dpdp:{msg:"DPDP Act 2023 requires certified destruction documentation when disposing devices containing personal data. Penalty up to ₹250 Crore. You need: KSPCB-authorized recycler + CoD per device + vendor data processor contract. We provide all three.",options:[
    {label:"📋 Get DPDP-compliant ITAD",next:'form_link'},
    {label:"💬 Ask a specific question",next:'wa'},
    {label:"⬅️ Back",next:'start'}
  ]},
  quote:{msg:"Get your free quote via: (1) Quote form — 2-hour response, (2) WhatsApp — fastest, (3) Call — immediate scheduling.",options:[
    {label:"📋 Fill quote form",next:'form_link'},
    {label:"💬 WhatsApp fastest",next:'wa'},
    {label:"📞 Call us",next:'call'}
  ]},
  calc_link:{msg:"Scroll to our Buyback Estimator — select device type, brand, age, and condition for an instant price with a WhatsApp pre-fill link.",options:[{label:"⬅️ Back to menu",next:'start'}]},
  form_link:{msg:"Scroll to the 'Get Free Quote' section and fill the form. We respond within 2 hours. Or WhatsApp for faster response.",options:[{label:"💬 WhatsApp instead",next:'wa'},{label:"⬅️ Main menu",next:'start'}]},
  wa:{msg:"Opening WhatsApp — a pre-filled message will be ready.",options:[{label:"💬 Open WhatsApp →",next:'wa_open'},{label:"⬅️ Back",next:'start'}]},
  wa_open:{msg:"Opening WhatsApp now! 🚀",options:[{label:"⬅️ Main menu",next:'start'}],action:()=>window.open('https://wa.me/919876543210?text=Hi%2C+I+need+help+with+e-waste+services+in+Kochi','_blank')},
  call:{msg:"Call us: +91-9876-543-210. Mon–Sat 8AM–8PM. Corporate emergencies: 24/7.",options:[{label:"📞 Call Now",next:'call_now'},{label:"⬅️ Main menu",next:'start'}]},
  call_now:{msg:"Connecting...",options:[{label:"⬅️ Back",next:'start'}],action:()=>window.location.href='tel:+919876543210'}
};

let chatOpen=false;

function addBotMsg(text,delay=0){
  setTimeout(()=>{
    document.querySelector('.chat-typing-indicator')?.remove();
    const msgs=document.getElementById('chat-messages');
    if(!msgs)return;
    const div=document.createElement('div');
    div.className='chat-msg bot';
    div.innerHTML=`<div class="chat-msg-avatar">🤖</div><div class="chat-bubble">${text}</div>`;
    msgs.appendChild(div);
    msgs.scrollTop=msgs.scrollHeight;
  },delay);
}
function showTyping(){
  const msgs=document.getElementById('chat-messages');
  if(!msgs)return;
  const div=document.createElement('div');
  div.className='chat-msg bot chat-typing-indicator';
  div.innerHTML=`<div class="chat-msg-avatar">🤖</div><div class="chat-bubble"><div class="typing"><span></span><span></span><span></span></div></div>`;
  msgs.appendChild(div);
  msgs.scrollTop=msgs.scrollHeight;
}
function addUserMsg(text){
  const msgs=document.getElementById('chat-messages');
  if(!msgs)return;
  const div=document.createElement('div');
  div.className='chat-msg user';
  div.innerHTML=`<div class="chat-bubble">${text}</div>`;
  msgs.appendChild(div);
  msgs.scrollTop=msgs.scrollHeight;
}
function showOptions(node){
  const opts=document.getElementById('chat-options');
  if(!opts||!node.options)return;
  opts.innerHTML='';
  node.options.forEach(opt=>{
    const btn=document.createElement('button');
    btn.className='chat-opt';
    btn.textContent=opt.label;
    btn.onclick=()=>selectChatOption(opt);
    opts.appendChild(btn);
  });
}
function selectChatOption(opt){
  document.getElementById('chat-options').innerHTML='';
  addUserMsg(opt.label);
  const nextNode=CHAT_TREE[opt.next];
  if(!nextNode)return;
  if(nextNode.action)nextNode.action();
  showTyping();
  addBotMsg(nextNode.msg,700);
  setTimeout(()=>showOptions(nextNode),900);
}
function sendChatMsg(){
  const input=document.getElementById('chat-input');
  if(!input)return;
  const text=input.value.trim();
  if(!text)return;
  input.value='';
  addUserMsg(text);
  const lower=text.toLowerCase();
  let nextNode=CHAT_TREE.start;
  if(/laptop|macbook|dell|hp|lenovo|sell|buyback/.test(lower))nextNode=CHAT_TREE.sell_laptop;
  else if(/phone|iphone|samsung|oneplus|mobile/.test(lower))nextNode=CHAT_TREE.sell_phone;
  else if(/dpdp|compliance|certificate|cod|penalty/.test(lower))nextNode=CHAT_TREE.dpdp;
  else if(/shred|destroy|nist|degauss|data|wipe/.test(lower))nextNode=CHAT_TREE.data;
  else if(/price|cost|how much|quote|rate/.test(lower))nextNode=CHAT_TREE.quote;
  else if(/itad|corporate|bulk|office|business/.test(lower))nextNode=CHAT_TREE.itad;
  showTyping();
  addBotMsg(nextNode.msg,700);
  setTimeout(()=>showOptions(nextNode),900);
}
function openChat(){if(!chatOpen)toggleChat();}
function toggleChat(){
  chatOpen=!chatOpen;
  const win=document.getElementById('chat-window');
  const btn=document.getElementById('chat-toggle-btn');
  const badge=document.getElementById('chat-badge');
  if(!win)return;
  if(chatOpen){
    win.classList.add('open');
    if(btn)btn.textContent='✕';
    if(badge)badge.style.display='none';
    if(document.getElementById('chat-messages')?.children.length===0){
      showTyping();
      addBotMsg(CHAT_TREE.start.msg,800);
      setTimeout(()=>showOptions(CHAT_TREE.start),1000);
    }
  }else{
    win.classList.remove('open');
    if(btn)btn.innerHTML='💬';
  }
}

/* ── ANIMATED COUNTERS ── */
function animateCounters(){
  document.querySelectorAll('[data-count]').forEach(el=>{
    const target=parseInt(el.dataset.count);
    const suffix=el.dataset.suffix||'';
    let cur=0;const step=target/60;
    const timer=setInterval(()=>{
      cur=Math.min(cur+step,target);
      el.textContent=Math.floor(cur).toLocaleString('en-IN')+suffix;
      if(cur>=target)clearInterval(timer);
    },16);
  });
}

/* ── INTERSECTION OBSERVER FOR COUNTERS ── */
function initCounterObserver(){
  const el=document.querySelector('[data-count]');
  if(!el)return;
  const io=new IntersectionObserver(entries=>{
    if(entries[0].isIntersecting){animateCounters();io.disconnect();}
  },{threshold:.5});
  io.observe(el.closest('section')||el);
}

/* ── INIT ── */
document.addEventListener('DOMContentLoaded',()=>{
  calcUpdate();
  initCounterObserver();
  // Show chat badge after delay
  setTimeout(()=>{
    const badge=document.getElementById('chat-badge');
    if(badge&&!chatOpen)badge.style.display='flex';
  },6000);
});
