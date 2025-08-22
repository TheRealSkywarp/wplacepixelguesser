from datetime import datetime, timedelta

# Chaque pixel prend 30 secondes à se recharger
DUREE_PAR_PIXEL = 30  # en secondes

def calcul_temps(pixels_a_recharger):
    total_secondes = pixels_a_recharger * DUREE_PAR_PIXEL
    heures = total_secondes // 3600
    minutes = (total_secondes % 3600) // 60
    secondes = total_secondes % 60
    return total_secondes, heures, minutes, secondes

def main():
    try:
        pixels_actuels = int(input("Combien de pixels as-tu actuellement ? "))
        pixels_max = int(input("Quel est ton stock maximum de pixels ? "))

        if pixels_actuels < 0 or pixels_max < 0:
            print("⚠️ Les valeurs doivent être positives.")
            return
        if pixels_actuels > pixels_max:
            print("⚠️ Tu ne peux pas avoir plus de pixels que ton stock maximum.")
            return

        pixels_a_recharger = pixels_max - pixels_actuels

        if pixels_a_recharger == 0:
            print("🎉 Ton stock est déjà plein !")
            return

        total_secondes, heures, minutes, secondes = calcul_temps(pixels_a_recharger)

        # Heure actuelle + temps de recharge
        maintenant = datetime.now()
        heure_fin = maintenant + timedelta(seconds=total_secondes)

        # Affichage toujours cohérent : heures, minutes et secondes affichées même si 0
        resultat = [
            f"{heures} heure{'s' if heures != 1 else ''}",
            f"{minutes} minute{'s' if minutes != 1 else ''}",
            f"{secondes} seconde{'s' if secondes != 1 else ''}"
        ]

        print(f"📉 Pixels à recharger : {pixels_a_recharger}")
        print("⏳ Temps total de recharge :", " ".join(resultat))
        print(f"🕒 Ton stock sera plein à : {heure_fin.strftime('%H:%M:%S')}")

    except ValueError:
        print("⚠️ Veille à entrer un nombre entier valide.")

if __name__ == "__main__":
    main()