'use strict';
const menuButton = document.querySelector('.menu-toggle');
const navigation = document.querySelector('#navigation');
function closeMenu() {
  navigation.classList.remove('is-open');
  menuButton.setAttribute('aria-expanded', 'false');
  menuButton.setAttribute('aria-label', 'Mở menu');
}
menuButton.addEventListener('click', () => {
  const open = navigation.classList.toggle('is-open');
  menuButton.setAttribute('aria-expanded', String(open));
  menuButton.setAttribute('aria-label', open ? 'Đóng menu' : 'Mở menu');
});
navigation.querySelectorAll('a').forEach(link => link.addEventListener('click', closeMenu));
document.addEventListener('keydown', event => { if (event.key === 'Escape') closeMenu(); });
window.matchMedia('(min-width: 761px)').addEventListener('change', event => { if (event.matches) closeMenu(); });
const dialog = document.querySelector('#contact-dialog');
const form = document.querySelector('#contact-form');
const status = document.querySelector('#form-status');
document.querySelectorAll('[data-contact]').forEach(button => {
  button.addEventListener('click', () => {
    closeMenu();
    document.querySelector('#package').value = button.dataset.package || 'Chưa xác định — cần tư vấn';
    status.textContent = '';
    dialog.showModal();
    document.body.classList.add('dialog-open');
  });
});
document.querySelector('.dialog-close').addEventListener('click', () => dialog.close());
dialog.addEventListener('close', () => document.body.classList.remove('dialog-open'));
dialog.addEventListener('click', event => {
  const rect = dialog.getBoundingClientRect();
  if (event.target === dialog && (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom)) dialog.close();
});
form.addEventListener('submit', event => {
  event.preventDefault();
  if (!form.reportValidity()) return;
  const data = new FormData(form);
  if (!String(data.get('name')).trim() || !String(data.get('message')).trim()) {
    status.textContent = 'Vui lòng điền tên và nhu cầu tư vấn, không chỉ nhập khoảng trắng.';
    return;
  }
  const text = ['YÊU CẦU TƯ VẤN — KHỞI HƯỚNG', '', `Họ tên: ${String(data.get('name')).trim()}`, `Email: ${String(data.get('email')).trim()}`, `Gói: ${data.get('package')}`, '', 'Nhu cầu:', String(data.get('message')).trim(), '', 'Bản yêu cầu được tạo trên thiết bị, chưa được gửi tới đơn vị tư vấn.'].join('\n');
  const url = URL.createObjectURL(new Blob(['\uFEFF', text], { type: 'text/plain;charset=utf-8' }));
  const link = document.createElement('a');
  link.href = url;
  link.download = 'yeu-cau-tu-van.txt';
  document.body.append(link);
  link.click();
  link.remove();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
  status.textContent = 'Đã tạo bản yêu cầu để tải về. Thông tin chưa được gửi và không được lưu trên máy chủ.';
});
document.querySelector('#year').textContent = new Date().getFullYear();
