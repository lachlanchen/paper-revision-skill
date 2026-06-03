[English](README.en.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)

# Paper Revision Skill

Quy trình sửa bài theo cơ chế plan-gated cho bản thảo LaTeX, thư trả lời phản biện, redline và proof correction.

> Lập kế hoạch trước. Chỉnh sửa sau. Kiểm tra bằng PDF. Commit từng gói công việc.

## Công Dụng

- Tạo kế hoạch markdown trước các sửa đổi quan trọng.
- Giữ `main.tex` và `sm.tex` là các tệp hiện hành có thể chỉnh sửa.
- Lưu các bản gốc như `original_main.tex` và `original_sm.tex`.
- Tạo redline để kiểm tra nội bộ.
- Đồng bộ response letter với vị trí đã xác minh trong PDF.

## Bắt Đầu

- README chính: [../README.md](../README.md)
- Skill đang dùng: [../SKILL.md](../SKILL.md)
- Hướng dẫn trực quan: [../docs/origin-chat.html](../docs/origin-chat.html)
- Mẫu kế hoạch: [../templates/revision_plan.md](../templates/revision_plan.md)

## Quy Tắc Cốt Lõi

```text
kế hoạch -> phê duyệt -> chỉnh sửa -> build -> kiểm tra PDF -> redline -> commit
```
