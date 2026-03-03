import pandas as pd
import matplotlib.pyplot as plt

# 1. قراءة البيانات من ملفك الذي أنشأته
try:
    df = pd.read_csv('gold_rates_history.csv')
    
    # تحويل عمود التاريخ لنوع "تاريخ" ليسهل ترتيبه
    df['Date'] = pd.to_datetime(df['Date'])

    # 2. إنشاء الرسم البياني
    plt.figure(figsize=(10, 5))
    plt.plot(df['Date'], df['Gold Price'], marker='o', linestyle='-', color='gold', linewidth=2)

    # 3. إضافة اللمسات الجمالية
    plt.title('Gold Price Trend | حركة سعر الذهب', fontsize=14)
    plt.xlabel('Date & Time', fontsize=12)
    plt.ylabel('Price (INR)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.xticks(rotation=45) # تدوير التاريخ ليكون واضحاً
    
    plt.tight_layout()
    
    # 4. عرض الرسم وحفظه كصورة
    plt.savefig('gold_trend.png') # سيحفظ صورة الرسم في مجلدك
    plt.show()
    
    print("✅ تم إنشاء الرسم البياني وحفظه كصورة (gold_trend.png)")

except Exception as e:
    print(f"🛑 تأكد من وجود بيانات في الملف أولاً: {e}")