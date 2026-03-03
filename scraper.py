import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import os
import re # أضفنا هذه المكتبة للتنظيف الاحترافي

def get_gold_price():
    url = "https://www.goldpriceindia.com/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            price_element = soup.find('td', class_='p-2 align-center nte-day-low')
            
            if price_element:
                rate_raw = price_element.text.strip()
                
                # --- خطوة التنظيف الجديدة ---
                # نقوم بإزالة أي شيء ليس رقماً (مثل ₹، الفواصل، والرموز)
                rate_clean = re.sub(r'[^\d.]', '', rate_raw)
                # تحويله إلى رقم حقيقي (float)
                rate_number = float(rate_clean)
                
                print(f"✅ تم بنجاح! السعر الخام: {rate_raw} -> السعر المنظف: {rate_number}")
                
                data = {
                    'Date': [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
                    'Gold Price': [rate_number] # نحفظ الرقم المنظف هنا
                }
                
                df = pd.DataFrame(data)
                file_path = 'gold_rates_history.csv'
                header_condition = not os.path.exists(file_path)
                
                df.to_csv(file_path, mode='a', index=False, header=header_condition)
                print(f"📂 تم التحديث في ملف CSV.")
            else:
                print("❌ لم يتم العثور على عنصر السعر.")
        else:
            print(f"⚠️ فشل الاتصال بالموقع. كود: {response.status_code}")

    except Exception as e:
        print(f"🛑 حدث خطأ: {e}")

if __name__ == "__main__":
    get_gold_price()