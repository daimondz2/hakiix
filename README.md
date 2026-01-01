# Hakiix

Hakiix เป็น **Python console logger module** สำหรับพิมพ์ log สีสันสดใสใน console  
เหมาะสำหรับงานสคริปต์, automation, หรือโปรเจกต์ Python ที่ต้องการ log อ่านง่ายและสวยงาม

สวัสดีครับ โมดูลนี้เป็น **โมดูลส่วนตัวที่เปิดให้ทุกคนใช้งานได้**  

---

## Installation

โมดูลสามารถติดตั้งได้ 2 วิธี

### 1️⃣ ติดตั้งผ่าน Git
ก่อนอื่นต้องติดตั้ง Git ก่อน  

**Windows:**  
[ดาวน์โหลด Git](https://git-scm.com/downloads)

**Linux:**  
```bash
sudo apt install git -y
```

**MacOS:**  
```bash
brew install git
```

ติดตั้งโมดูลผ่าน Git:
```bash
pip install git+https://github.com/daimondz2/hakiix.git
```

### 2️⃣ ติดตั้งผ่าน PyPI (ในอนาคต)
```bash
pip install hakiix
```

---

## Usage Example

### ใช้ console instance

```python
from hakiix import console

console.info("เริ่มทำงาน script")
console.suc("ทำงานสำเร็จ")
console.err("เกิดข้อผิดพลาด")
console.warn("เตือนความผิดพลาด")
console.dbg("Debug ข้อมูลตัวแปร x=123")
console.token("1234567890abcdefghijklmnopqrstuvwxyz")
```

### ใช้ shortcut แบบสั้น

```python
from hakiix.console import log_info, log_success, log_error

log_info("Info ผ่าน shortcut")
log_success("Success ผ่าน shortcut")
log_error("Error ผ่าน shortcut")
```

---

## Output ตัวอย่าง

```
[ INFO ] 12:34:56 | เริ่มทำงาน script
[ SUCC ] 12:34:56 | ทำงานสำเร็จ
[ ERRO ] 12:34:56 | เกิดข้อผิดพลาด
[ WARN ] 12:34:56 | เตือนความผิดพลาด
[ DEBG ] 12:34:56 | Debug ข้อมูลตัวแปร x=123
[ TOKN ] 12:34:56 | 1234567890abcdefghijklmn...
```

---

## ฟังก์ชัน clear

ล้างหน้าจอ console:
```python
console.clear()
```

---

## หมายเหตุ

- รองรับ Python 3.x  
- สี Neon ใช้งานได้บน terminal ที่รองรับ ANSI codes  
- สามารถใช้งานบน Windows, Linux, MacOS  
- Shortcut log ทำให้เรียกใช้ง่ายขึ้น  

---

## License

MIT License
