[English](README.en.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)

# Paper Revision Skill

سير عمل قائم على خطة مسبقة لمراجعة مقالات LaTeX، ورسائل الرد على المحكمين، وملفات redline، وتصحيحات البروفات.

> خطط أولا. حرر ثانيا. تحقق من ملف PDF. ثم احفظ حزمة العمل في git.

## ماذا يفعل

- ينشئ خطة markdown قبل التعديلات الكبيرة.
- يحافظ على `main.tex` و `sm.tex` كملفات العمل الحالية.
- يحفظ النسخ المرجعية مثل `original_main.tex` و `original_sm.tex`.
- يولد ملفات redline للتحقق الداخلي.
- يزامن response letter مع المواقع المؤكدة في PDF.

## ابدأ من هنا

- README الرئيسي: [../README.md](../README.md)
- ملف skill: [../SKILL.md](../SKILL.md)
- الدليل المرئي: [../docs/origin-chat.html](../docs/origin-chat.html)
- قالب خطة المراجعة: [../templates/revision_plan.md](../templates/revision_plan.md)

## القاعدة الأساسية

```text
خطة -> موافقة -> تحرير -> بناء -> فحص PDF -> redline -> commit
```
