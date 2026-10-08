'use strict';
const menuButton = document.querySelector('.menu-toggle');
const navigation = document.querySelector('#navigation');
function closeMenu() {
  navigation?.classList.remove('is-open');
  menuButton?.setAttribute('aria-expanded', 'false');
  menuButton?.setAttribute('aria-label', 'Mở menu');
}
menuButton?.addEventListener('click', () => {
  const open = navigation.classList.toggle('is-open');
  menuButton.setAttribute('aria-expanded', String(open));
  menuButton.setAttribute('aria-label', open ? 'Đóng menu' : 'Mở menu');
});
navigation?.querySelectorAll('a').forEach(link => link.addEventListener('click', closeMenu));
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && navigation?.classList.contains('is-open')) {
    closeMenu();
    menuButton.focus();
  }
});
document.addEventListener('click', event => {
  if (!event.target.closest('.nav')) closeMenu();
});
window.matchMedia('(min-width: 1101px)').addEventListener('change', event => {
  if (event.matches) closeMenu();
});
const filter = document.querySelector('#case-filter');
function filterCases() {
  const cards = [...document.querySelectorAll('[data-category]')];
  let visible = 0;
  cards.forEach(card => {
    card.hidden = filter.value !== 'all' && card.dataset.category !== filter.value;
    if (!card.hidden) visible += 1;
  });
  const status = document.querySelector('#case-status');
  status.textContent = cards.length === 0
    ? 'Chưa có Case Study được phê duyệt công bố. Danh sách sẽ cập nhật khi nội dung được duyệt.'
    : visible === 0 ? 'Không có dự án trong lĩnh vực đã chọn.' : `Hiển thị ${visible} dự án được phê duyệt.`;
}
if (filter) {
  filter.addEventListener('change', filterCases);
  filterCases();
}
const form = document.querySelector('#contact-form');
if (form) {
  const select = form.querySelector('#package');
  const requested = new URLSearchParams(window.location.search).get('goi');
  if ([...select.options].some(option => option.value === requested)) select.value = requested;
  form.addEventListener('submit', event => {
    event.preventDefault();
    if (!form.reportValidity()) return;
    const data = new FormData(form);
    const status = document.querySelector('#form-status');
    if (!String(data.get('name')).trim() || !String(data.get('message')).trim()) {
      status.textContent = 'Vui lòng nhập tên và nhu cầu tư vấn, không chỉ khoảng trắng.';
      return;
    }
    const text = ['YÊU CẦU TƯ VẤN — KHỞI HƯỚNG', '', `Họ tên: ${String(data.get('name')).trim()}`,
      `Email: ${String(data.get('email')).trim()}`, `Dự án: ${String(data.get('company')).trim()}`,
      `Gói: ${select.selectedOptions[0].textContent}`, '', 'Nhu cầu:', String(data.get('message')).trim(), '',
      'Phạm vi và điều kiện dịch vụ: Chờ phê duyệt.', 'Bản yêu cầu chưa được gửi tới đơn vị tư vấn.'].join('\n');
    const url = URL.createObjectURL(new Blob(['\uFEFF', text], {type: 'text/plain;charset=utf-8'}));
    const link = document.createElement('a');
    link.href = url;
    link.download = 'yeu-cau-tu-van.txt';
    document.body.append(link);
    link.click();
    link.remove();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
    status.textContent = 'Đã tạo tệp yêu cầu để tải về. Thông tin chưa được gửi hoặc lưu trên máy chủ.';
  });
}
