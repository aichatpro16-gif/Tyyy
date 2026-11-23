import json
import re
import os
from datetime import datetime

FILE = "requests.json"

def load_data():
    if os.path.exists(FILE):
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_data(data):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def main():
    print("\n================================")
    print("       TIKTOK VIEWS MANAGER")
    print("================================")

    data = load_data()

    while True:
        print("\n1. إضافة فيديو")
        print("2. عرض الطلبات")
        print("3. خروج")

        choice = input("\nاختيارك: ")

        if choice == "1":
            url = input("رابط الفيديو: ").strip()

            if not re.match(
                r"^https?://(www\.)?(vm\.tiktok\.com|vt\.tiktok\.com|tiktok\.com)/",
                url
            ):
                print("رابط غير صالح!")
                continue

            try:
                target = int(input("عدد المشاهدات المستهدف: "))
                if target <= 0:
                    raise ValueError
            except ValueError:
                print("العدد غير صالح!")
                continue

            data.append({
                "url": url,
                "target": target,
                "status": "بانتظار مصدر ترويج معتمد",
                "date": datetime.now().isoformat()
            })

            save_data(data)
            print("\nتم حفظ الطلب بنجاح.")

        elif choice == "2":
            for i, item in enumerate(data, 1):
                print(f"\nطلب رقم {i}")
                print("الرابط:", item["url"])
                print("الهدف:", item["target"])
                print("الحالة:", item["status"])

        elif choice == "3":
            print("إلى اللقاء!")
            break

        else:
            print("اختيار غير صحيح.")

if name == "main":
    main()
