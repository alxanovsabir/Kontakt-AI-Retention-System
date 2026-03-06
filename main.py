# Kontakt AI - Müştəri İtki Riski (Churn Prediction)
print("--- Kontakt AI: Müştəri Risk Analiz Sistemi ---")

def risk_analiz(musteri_data):
    # Müştəri məlumatları: [rəylərin_sayı, son_ziyarət_gunu, şikayət_balı]
    say, gun, sikayet_bal = musteri_data
    
    # Risk balı hesablamaq üçün formula
    # Əgər 30 gündən çox gəlməyibsə və şikayət balı yüksəkdirsə, risk 100%-dir
    risk = (sikayet_bal * 2) + (30 - min(gun, 30))
    
    if risk > 40:
        return "🔥 YÜKSƏK RİSK: Müştəri rəqibə keçə bilər! (Xüsusi endirim təklif et)"
    elif risk > 20:
        return "⚠️ ORTA RİSK: Müştəri narazıdır, əlaqə saxla."
    else:
        return "✅ STABİL: Müştəri məmnundur."

# Test üçün nümunə: [Rəy sayı, Son ziyarət (gün), Şikayət balı (1-10)]
musteriler = [
    [5, 45, 8], # Müştəri 1: Çoxdandır gəlmir və şikayəti çoxdur
    [2, 5, 2]   # Müştəri 2: Yeni və şikayəti azdır
]

for m in musteriler:
    print(f"\nMüştəri Data: {m}")
    print(risk_analiz(m))