# -*- coding: utf-8 -*-
import time
import random
import os
import sys

def ekrani_temizle():
    os.system('cls' if os.name == 'nt' else 'clear')

def yavas_yaz(metin, hiz=0.008):
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(hiz)
    print()

def ses(frekans, sure):
    if os.name == 'nt':
        import winsound
        winsound.Beep(frekans, sure)

def oyun_baslat():
    en_yuksek_skor = 0
    
    while True:
        ekrani_temizle()
        print("=" * 65)
        print("   🚀 CO2 ROCKET MASTER v9.0 - CYBERPUNK SPACEX EDITION 🚀   ")
        print("=" * 65)
        print(f"🏆 STRATOSFER REKORUN: {en_yuksek_skor:.2f} metre\n")
        
        # 1. GEZEGEN SEÇİMİ (Yerçekimi ve Atmosfer Etkisi)
        print("🪐 [KATEGORI 1] FIRLATMA CEPHESI (GEZEGEN)")
        print("1) Dunya [Standart G: 9.8 | Atmo: 1.0]\n2) Mars [Dusuk G: 3.7 | Atmo: 0.1]\n3) Ay [Sifira Yakin G: 1.6 | Atmo: 0.0]\n4) Titan [Agir G: 1.3 | Atmo: 1.5]\n5) Venus [Ezici G: 8.8 | Atmo: 90.0]\n6) Jupiter Uydusu Europa [G: 1.3 | Atmo: 0.0]\n7) Siber Siberon Gezegeni [Ekstrem G: 15.0 | Atmo: 0.5]")
        try: gezegen = int(input(">> Secim (1-7): "))
        except: continue
        
        # Gezegen Çarpanları (Yerçekimi , Atmosfer)
        g_kat, atm_kat = {1:(1.0, 1.0), 2:(0.38, 0.1), 3:(0.16, 0.0), 4:(0.14, 1.5), 5:(0.9, 5.0), 6:(0.13, 0.0), 7:(1.5, 0.5)}.get(gezegen, (1.0, 1.0))

        # 2. EKSTREM KIMYASAL YAKITLAR
        print("\n🧪 [KATEGORI 2] REAKTIF ENERJI (YAKIT)")
        print("1) %5 Ev Sirkesi [Zayif]\n2) Limon Tuzu Karisimi [Dengeli]\n3) %80 Konsantre Sirke Ruhu [Yuksek]\n4) Sanayi Tipi Tuz Ruhu [Agresif]\n5) Hidrojen Peroksit + Maya [Ekstrem]\n6) Sivi Karbondioksit + Nitro [Cilgin]\n7) Kuantum Siber-Plazma [Efsanevi]")
        try: yakit_secim = int(input(">> Secim (1-7): ")); yakit_gram = int(input(">> Yakit Miktari (Gram): "))
        except: continue
        
        # 3. GOVDE MATERYALLERI
        print("\n🚀 [KATEGORI 3] STRATOSFERIK GOVDE ZIRHI")
        print("1) Ince Pet Sise [Max 150 PSI]\n2) Mukavva + PVC [Max 240 PSI]\n3) Pleksiglas Polimer [Max 360 PSI]\n4) Havacilik Aluminyumu [Max 500 PSI]\n5) Titanyum AlaSim [Max 850 PSI]\n6) Karbon Nanotup Govde [Max 1300 PSI]\n7) Kuantum Enerji Kalkanli Zirh [Max 2500 PSI]")
        try: govde_secim = int(input(">> Secim (1-7): "))
        except: continue
        
        # 4. BURUN KONISI GEOMETRILERI
        print("\n📐 [KATEGORI 4] AERODINAMIK BURUN YAPISI")
        print("1) Kut Kapak\n2) Kuresel Burun\n3) Parabolik Koni\n4) Gotik Ogiv\n5) Sivri Elips\n6) Hiperbolik Supersonik\n7) Lazer Plazma Hava Yarici")
        try: koni_secim = int(input(">> Secim (1-7): "))
        except: continue
        
        # 5. KANATCIK (FIN) ENTEGRASYONU
        print("\n📐 [KATEGORI 5] DENGELEYICI KANATCIK TIPI")
        print("1) Dikdortgen\n2) Yamuk\n3) Geriye Kirik\n4) Delta Kanat\n5) Eliptik\n6) Izgara Tipi Grid Fin\n7) Yapay Zekali Hareketli Siber Fin")
        try: kanat_tipi = int(input(">> Secim (1-7): ")); kanat_sayisi = int(input(">> Kanatcik Sayisi: "))
        except: continue
        
        # 6. AKILLI PARASUT SEKANSI
        print("\n🪂 [KATEGORI 6] KURTARMA VE PARASUT FRENLERI")
        print("1) Cop Poseti\n2) Hafif Naylon\n3) Ripstop Kumas\n4) Saf Ipek\n5) Drogue Parasut\n6) Cift Asamali Supersonik Parasut\n7) Ters Atisli Roket Frenleme Sistemi (Retro-Thruster)")
        try: parasut_secim = int(input(">> Secim (1-7): ")); parasut_cap = int(input(">> Parasut Capi (cm): ")); parasut_zaman = float(input(">> Acilis Saniyesi (s): "))
        except: continue
        
        # 7. YAPAY ZEKA OTOPILOT CEKIRDEGI
        print("\n🤖 [KATEGORI 7] FLIGHT CORE (YAPAY ZEKA OTOPILOT)")
        print("1) Manuel Kontrol [Sifir Destek]\n2) Temel Sensor Yardimi [Orta Denge]\n3) SpaceX Falcon Algoritmasi [Yuksek Denge]\n4) NASA Deep Space AI [Ruzgari Yok Eder]\n5) Cyberpunk 2077 Siber-Core [%10 Itme Gucu Saglar]\n6) Jarvis Ucus Asistani [Mukenmel Zamanlama]\n7) Gemini Kanki Core [Tum Hatalari Otomatik Duzeltir!]")
        try: ai_secim = int(input(">> Secim (1-7): "))
        except: continue

        # --- ARKA PLAN FIZIK MOTORU ---
        max_psi, govde_agirlik = {1:(150,40), 2:(240,90), 3:(360,140), 4:(500,220), 5:(850,450), 6:(1300,350), 7:(2500,250)}.get(govde_secim, (360,140))
        basinc_kat, yanma_hizi = {1:(0.3,0.5), 2:(0.7,0.8), 3:(1.4,1.2), 4:(2.2,1.7), 5:(3.5,2.4), 6:(5.0,3.5), 7:(8.5,5.0)}.get(yakit_secim, (1.0,1.0))
        cd_burun = {1:1.5, 2:1.1, 3:0.8, 4:0.5, 5:0.3, 6:0.15, 7:0.05}.get(koni_secim, 0.8)
        cd_kanat = {1:0.5, 2:0.3, 3:0.4, 4:0.2, 5:0.1, 6:0.05, 7:0.01}.get(kanat_tipi, 0.3)
        
        # Yapay Zeka Etkileri
        ai_itme_bonusu = 1.15 if ai_secim == 5 else (1.30 if ai_secim == 7 else 1.0)
        ai_denge_bonusu = 5.0 if ai_secim in [4, 6, 7] else 1.0

        olusan_basinc = int((yakit_gram * basinc_kat) * 1.2)
        toplam_surtunme = ((cd_burun + (cd_kanat * kanat_sayisi)) * atm_kat) + 0.01
        toplam_kutle = govde_agirlik + yakit_gram + (kanat_sayisi * 12) + (parasut_cap * 0.3)

        ekrani_temizle()
        yavas_yaz("⚙️ CYBER-LAUNCH DIAGNOSTICS... VERILER ISLENIYOR...")
        print(f"📊 Toplam Kutle: {toplam_kutle:.1f}g | Hava Direnci: {toplam_surtunme:.2f} Cd")
        print(f"🧪 Tank Basinci: {olusan_basinc} PSI | Govde Toleransi: {max_psi} PSI")
        print("-" * 55)
        time.sleep(2)

        # 1. RISK KONTROL: GOVDE INFILAKI
        if olusan_basinc > max_psi:
            print("\n💥 KATASTROFIK YAPISAL HASAR! TANK RAMPADA PATLADI!")
            ses(100, 1500)
            time.sleep(3)
            continue

        # 2. RISK KONTROL: YAN RUZGAR VE TAKLA ATMA
        ruzgar = random.randint(0, 70) if atm_kat > 0 else 0
        denge_skoru = ((kanat_sayisi * 15) / (ruzgar + 1)) * ai_denge_bonusu
        if atm_kat > 0 and kanat_sayisi < 3:
            print("⚠️ DENGE KAYBI! Roket firlarken takla atip yere çakildi!")
            ses(200, 1000)
            time.sleep(3)
            continue
        elif ruzgar > 45 and denge_skoru < 1.5:
            print("🌪️ FIRTINA ETKISI! Roket ruzgarda savrulup parcalandi!")
            ses(250, 1000)
            time.sleep(3)
            continue

        # COUNTDOWN
        for i in range(3, 0, -1):
            ekrani_temizle()
            print(f"\n\n 🚀 CYBER LAUNCH COUNTDOWN: T-MINUS {i} 🚀")
            ses(1200, 70)
            time.sleep(0.5)

        ekrani_temizle()
        print("🚀 IGNITION SUCCESSFUL! ROKET STRATOSFERE CIKIYOR!\n")
        ses(1500, 300)

        # UCUS MOTORU HESAPLAMALARI
        itme = ((olusan_basinc * yanma_hizi * 1200) / toplam_surtunme) * ai_itme_bonusu
        zirve_irtifa = (itme / (toplam_kutle * g_kat))
        
        if zirve_irtifa < 10:
            print("🐌 AGIR KUTLE! Roket motoru govdeyi yerden kesemedi!")
            time.sleep(3)
            continue

        # Canlı Telemetri Tırmanış
        for t in range(1, 6):
            ekrani_temizle()
            print(f"🛰️ REAL-TIME TELEMETRY (STAGE 1) T+{t}s")
            print(f"📈 Irtifa: {(zirve_irtifa / 5) * t:.2f} Metre")
            print("-" * 40)
            print("\n" * (6 - t) + "        ⚡▲⚡\n        / \\\n       |🤖|\n        🔥🔥" + "\n" * t + "=" * 40)
            time.sleep(0.3)

        ekrani_temizle()
        print("📍 TEPE NOKTASI (APOGEE)! Kurtarma modulleri tetiklendi...")
        time.sleep(1.5)

        # PARASUT MEKANIZMASI
        parasut_ok = True
        if atm_kat == 0.0:
            mesaj = "🪂 Atmosfersiz ortam! Parasut acilamadi ama Retro-Thruster roketi dondurup dikey indirdi!" if parasut_secim == 7 else "❌ Atmosfer yok! Parasut hava olmadigi icin acilamadi, roket meteor gibi cakildi!"
            if parasut_secim != 7: parasut_ok = False
        elif parasut_zaman < 0.5 or parasut_zaman > 3.5:
            mesaj = "❌ Zamanlama hatasi! Parasut ya acilamadi ya da erken yirtildi!"
            parasut_ok = False
        else:
            fren = {1:0.4, 2:0.8, 3:1.2, 4:1.7, 5:2.3, 6:3.5, 7:5.0}.get(parasut_secim, 1.0)
            inis_hiz = (toplam_kutle * 20) / (parasut_cap * fren)
            if inis_hiz > 20:
                mesaj = f"💥 Parasut kucuk kaldi! Sert inis gerceklesti ({inis_hiz:.1f} km/h)!"
                parasut_ok = False
            else:
                mesaj = f"🪂 Kusursuz yumusak inis yapildi ({inis_hiz:.1f} km/h)."

        # Düşüş Telemetrisi
        for d in range(1, 6):
            ekrani_temizle()
            print(f"🛰️ TELEMETRI - INISH SEKANSI (STAGE 2)")
            print(f"📉 Kalan Mesafe: {zirve_irtifa - (zirve_irtifa/5)*d:.2f}m")
            print("-" * 40)
            if parasut_ok and d > 2:
                print("\n" * d + "       🪂\n       / \\\n       ---" + "\n" * (6 - d) + "=" * 40)
            else:
                print("\n" * d + "        ||\n        ▼" + "\n" * (6 - d) + "=" * 40)
            time.sleep(0.3)

        print("\n📊 === GOREV GORUNTULEME RAPORU ===")
        print(f"🦅 EN SECKIN IRTIFA: {zirve_irtifa:.2f} Metre")
        print(f"🪂 KURTARMA MODULU: {mesaj}")
        
        if parasut_ok:
            print("🥇 KUSURSUZ MISYON BASARILI!")
            if zirve_irtifa > en_yuksek_skor:
                print("👑 STRATOSFERIN YENI EFENDISI SENSIN!")
                en_yuksek_skor = zirve_irtifa
                ses(1500, 100); ses(1800, 150)
        else:
            print("🛑 GOREV BASARISIZ! Veriler kurtarilamadi.")

        print("\n" + "-" * 50)
        secim = input("Yeniden roket tasarlamak ister misin? (e/h): ").lower()
        if secim != 'e':
            break

if __name__ == "__main__":
    oyun_baslat()
