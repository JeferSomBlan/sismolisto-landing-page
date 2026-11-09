/* Acceptance scenarios HU-003, 005, 006, 009, 014, 016, 018.
   Academic demo only: no actual auth, verified testimonials or external services. */
(() => {
  'use strict';
  const $ = selector => document.querySelector(selector);
  const escapeHTML = text => String(text ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const ACCOUNT_KEY = 'sismolisto_demo_account_v1';
  const SESSION_KEY = 'sismolisto_demo_session_v1';
  const accountDialog = $('#account-dialog');
  let account = null;
  try { const raw = localStorage.getItem(ACCOUNT_KEY); if (raw) account = JSON.parse(raw); } catch { account = null; }
  const clearFeedback = selector => { const el = $(selector); el.textContent = ''; };
  const fieldProblem = (input, message, feedback) => {
    input.classList.add('is-invalid'); input.setAttribute('aria-invalid', 'true');
    $(feedback).textContent = message;
    input.focus();
  };
  const clearProblems = form => form.querySelectorAll('.is-invalid').forEach(el => {
    el.classList.remove('is-invalid'); el.removeAttribute('aria-invalid');
  });
  // Only a demonstrative verifier: not cryptographic security, never use real credentials.
  const demoVerifier = value => {
    let n = 2166136261;
    for (const char of `academic-demo-only:${value}`) { n ^= char.charCodeAt(0); n = Math.imul(n, 16777619); }
    return (n >>> 0).toString(16);
  };
  function switchAccount(mode) {
    const register = mode === 'register';
    $('#register-form').hidden = !register;
    $('#login-form').hidden = register;
    $('#account-register-tab').setAttribute('aria-pressed', String(register));
    $('#account-login-tab').setAttribute('aria-pressed', String(!register));
    $('#account-title').textContent = register ? 'Crear cuenta de demostración' : 'Iniciar sesión de demostración';
    clearFeedback('#register-feedback'); clearFeedback('#login-feedback');
  }
  function openAccount(mode = null) {
    switchAccount(mode || (account ? 'login' : 'register'));
    if (!accountDialog.open) accountDialog.showModal();
  }
  $('#account-register-tab').addEventListener('click', () => switchAccount('register'));
  $('#account-login-tab').addEventListener('click', () => switchAccount('login'));
  $('#account-close').addEventListener('click', () => accountDialog.close());
  $('#register-policy').addEventListener('click', () => $('#privacy-dialog').showModal());
  document.addEventListener('sismolisto:open-account', () => openAccount('register'));
  for (const a of document.querySelectorAll('.nav-cta, .hero-content .actions .btn-primary, .section-next-action .btn-primary')) {
    a.addEventListener('click', event => {
      event.preventDefault();
      history.replaceState(null, '', '#experiencia');
      $('#experiencia').scrollIntoView({block:'start', behavior:'instant'});
      openAccount();
    });
  }
  const jumpToApp = tab => {
    accountDialog.close();
    const btn = document.querySelector(`#app-tabs [data-tab="${tab}"]`);
    if (btn) btn.click();
  };
  $('#register-form').addEventListener('submit', event => {
    event.preventDefault();
    const form = event.currentTarget; clearProblems(form); clearFeedback('#register-feedback');
    const name = $('#register-name').value.trim();
    const email = $('#register-email').value.trim().toLowerCase();
    const password = $('#register-password').value;
    if (name.length < 2) return fieldProblem($('#register-name'), 'Ingresa un nombre de ejemplo con al menos dos letras.', '#register-feedback');
    if (!$('#register-email').validity.valid || !email) return fieldProblem($('#register-email'), 'Ingresa un correo de ejemplo válido.', '#register-feedback');
    if (account?.email === email) return fieldProblem($('#register-email'), 'Ese correo ya está registrado en esta demostración.', '#register-feedback');
    if (password.length < 8) return fieldProblem($('#register-password'), 'La contraseña ficticia debe tener al menos 8 caracteres.', '#register-feedback');
    if (!$('#register-privacy-check').checked) return fieldProblem($('#register-privacy-check'), 'Debes aceptar la política de privacidad de esta demostración.', '#register-feedback');
    const role = $('#register-role').value;
    account = { name, email, role, verifier: demoVerifier(password), demo: true };
    try { localStorage.setItem(ACCOUNT_KEY, JSON.stringify(account)); }
    catch { $('#register-feedback').textContent = 'No fue posible guardar la cuenta demostrativa en este navegador.'; return; }
    try { sessionStorage.setItem(SESSION_KEY, '1'); } catch { /* blocked in some sandboxed local test contexts */ }
    form.reset();
    jumpToApp('progreso');
    const select = $('#profile-role');
    if (select) select.value = role;
    $('#profile-settings')?.scrollIntoView({behavior:'instant',block:'start'});
    select?.focus();
  });
  $('#login-form').addEventListener('submit', event => {
    event.preventDefault();
    clearProblems(event.currentTarget);clearFeedback('#login-feedback');
    const email = $('#login-email').value.trim().toLowerCase();
    const password = $('#login-password').value;
    if (!account || email !== account.email || demoVerifier(password) !== account.verifier) {
      $('#login-email').classList.add('is-invalid');$('#login-password').classList.add('is-invalid');
      $('#login-email').setAttribute('aria-invalid','true');$('#login-password').setAttribute('aria-invalid','true');
      $('#login-feedback').textContent = 'Correo o contraseña incorrectos';return;
    }
    try { sessionStorage.setItem(SESSION_KEY, '1'); } catch {}
    $('#login-password').value = '';
    jumpToApp('inicio');
  });
  $('#forgot-demo').addEventListener('click', () => {
    $('#login-feedback').textContent = 'Recuperación simulada: vuelve a crear tu cuenta ficticia. No se enviará ningún correo.';
  });
  for (const id of ['register-name','register-email','register-password','login-email','login-password']) {
    $(`#${id}`).addEventListener('input', event => { event.target.classList.remove('is-invalid'); event.target.removeAttribute('aria-invalid'); });
  }

  // HU-003: images are traceable crops of existing TB1 mobile mockups (pp. 106 y 113).
  const steps = [
    ['Elige tu espacio', 'Selecciona un ambiente ficticio en el que estudiar o trabajar antes de evaluar riesgos.', 'paso-espacio-tb1.webp'],
    ['Evalúa riesgos y zonas', 'Responde las preguntas de evaluación y comprueba las zonas señalizadas de ejemplo.', 'paso-riesgos-tb1.webp'],
    ['Practica con micro-simulacros', 'Elige una respuesta a un imprevisto ficticio y recibe retroalimentación.', 'paso-simulacro-tb1.webp'],
    ['Revisa tu progreso', 'Consulta actividades realizadas, checklist e historial guardados en este navegador.', 'paso-progreso-tb1.webp']
  ];
  $('#step-view').addEventListener('click', () => {
    const n = Number($('#step-select').value), step = steps[n];
    if (!step) return;
    $('#step-detail-title').textContent = step[0];$('#step-detail-text').textContent = step[1];
    $('#step-detail-image').src = `assets/images/screenshots/${step[2]}`;
    $('#step-detail-image').alt = `Mockup móvil de referencia para ${step[0]}, tomado de SismoListo TB1, pp. 106 y 113`;
    $('#step-detail').hidden = false;$('#step-detail-title').focus?.();
  });

  // HU-009: intentionally fictional people, never misattributed to real users.
  const testimonials = [
    { name:'Andrea (personaje ficticio)', role:'Estudiante universitaria', quote:'Puedo practicar decisiones para un aula de ejemplo sin esperar a un simulacro.' },
    { name:'Luis (personaje ficticio)', role:'Trabajador de oficina', quote:'La demostración me ayuda a reconocer riesgos que habría pasado por alto.' },
    { name:'Camila (personaje ficticio)', role:'Estudiante universitaria', quote:'Es útil ver qué actividad practiqué y qué me falta revisar.' }
  ];
  let testimonialIndex = 0;
  function showTestimonial() {
    const item = testimonials[testimonialIndex];
    $('#testimonial-quote').textContent = `“${item.quote}”`;
    $('#testimonial-name').textContent = item.name;
    $('#testimonial-role').textContent = item.role;
    $('#testimonial-counter').textContent = `${testimonialIndex+1} de ${testimonials.length}`;
  }
  $('#testimonial-prev').addEventListener('click', () => { testimonialIndex = (testimonialIndex+testimonials.length-1)%testimonials.length;showTestimonial(); });
  $('#testimonial-next').addEventListener('click', () => { testimonialIndex = (testimonialIndex+1)%testimonials.length;showTestimonial(); });
  showTestimonial();
})();
