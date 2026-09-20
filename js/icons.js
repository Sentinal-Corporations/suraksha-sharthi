// Real SVG icon set — stroke style, offline, no emoji. Usage: icon('home', 18)
window.ICONS = {
home: '<path d="M3 10.5 12 3l9 7.5"/><path d="M5 9.5V21h5v-6h4v6h5V9.5"/>',
scan: '<rect x="3" y="7" width="18" height="13" rx="2"/><circle cx="12" cy="13" r="4"/><path d="M8 7l1.5-3h5L16 7"/>',
chart: '<path d="M4 20V10M10 20V4M16 20v-8M22 20H2"/>',
help: '<circle cx="12" cy="12" r="9"/><path d="M9.5 9.5a2.5 2.5 0 1 1 3.4 2.3c-.8.3-.9 1-.9 1.7"/><circle cx="12" cy="17" r=".5" fill="currentColor"/>',
menu: '<path d="M4 7h16M4 12h16M4 17h16"/>',
moon: '<path d="M20 14.5A8 8 0 0 1 9.5 4 8 8 0 1 0 20 14.5Z"/>',
sun: '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>',
phone: '<rect x="7" y="2" width="10" height="20" rx="2"/><path d="M11 18.5h2"/>',
monitor: '<rect x="2" y="4" width="20" height="13" rx="2"/><path d="M8 21h8M12 17v4"/>',
x: '<path d="M6 6l12 12M18 6 6 18"/>',
camera: '<rect x="2" y="7" width="20" height="14" rx="2"/><circle cx="12" cy="14" r="4"/><path d="M8 7l1.5-3h5L16 7"/>',
volume: '<path d="M4 9v6h4l5 4V5L8 9H4Z"/><path d="M16.5 8.5a5 5 0 0 1 0 7M19 6a8.5 8.5 0 0 1 0 12"/>',
save: '<path d="M5 3h11l3 3v15H5Z"/><path d="M8 3v5h7V3M8 21v-7h8v7"/>',
trash: '<path d="M4 7h16M9 7V4h6v3M6 7l1 14h10l1-14"/>',
bell: '<path d="M6 9a6 6 0 0 1 12 0c0 5 2 6 2 6H4s2-1 2-6"/><path d="M10 20a2 2 0 0 0 4 0"/>',
alert: '<path d="M12 3 2 20h20L12 3Z"/><path d="M12 10v4M12 17.5v.5"/>',
check: '<path d="M4 12.5 9.5 18 20 6.5"/>',
pill: '<rect x="3" y="8" width="18" height="8" rx="4" transform="rotate(-45 12 12)"/><path d="M8.5 15.5l7-7"/>',
globe: '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.5 3 14 0 18M12 3c-3 3.5-3 14 0 18"/>',
user: '<circle cx="12" cy="8" r="4"/><path d="M4 21c1.5-3.5 4.5-5 8-5s6.5 1.5 8 5"/>',
lock: '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>',
doc: '<path d="M6 2h8l4 4v16H6Z"/><path d="M14 2v4h4M9 12h6M9 16h6"/>',
info: '<circle cx="12" cy="12" r="9"/><path d="M12 11v5"/><circle cx="12" cy="8" r=".6" fill="currentColor"/>',
tool: '<path d="M14.5 6.5a4.5 4.5 0 0 0-6 6L3 18l3 3 5.5-5.5a4.5 4.5 0 0 0 6-6L14 13l-3-3 3.5-3.5Z"/>',
clock: '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
rupee: '<path d="M6 4h12M6 8.5h12M6 4c6 0 9 1.5 9 4.5S12 13 8.5 13L18 21"/>',
hospital: '<path d="M4 21V7l8-4 8 4v14"/><path d="M4 21h16M12 8v6M9 11h6"/>',
cloud: '<path d="M7 18a4 4 0 1 1 .5-7.97A5.5 5.5 0 0 1 18.3 12H18a3 3 0 0 1 0 6H7Z"/>'
};
window.icon = function (name, size) {
  size = size || 18;
  const p = window.ICONS[name] || window.ICONS.info;
  return `<svg class="ic" width="${size}" height="${size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${p}</svg>`;
};
