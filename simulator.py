import os
import random

# --- Configuración Inicial ---
sack = 137500
specialnum = 67

# --- Contadores Globales ---
total_tiradas = 0
total_tokens = 0
racha_sin_token = 0
peor_racha = 0
historial_cofres = []  # Guarda en qué número de cofre global salió cada token


def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


def pedir_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("⚠️ Por favor, introduce un número positivo.")
                continue
            return valor
        except ValueError:
            print("⚠️ Error: Debes introducir un número válido.")


# --- Bucle Principal ---
while True:
    print("\n" + "=" * 42)
    print("       🎰  TOKEN SIMULATOR 2.0  🎰")
    print("=" * 42)
    print(f" 📦 Cofres abiertos: {total_tiradas:,} | 🪙 Tokens: {total_tokens}")
    print("-" * 42)
    print(" 1. 🎲 Abrir cofres (Tirar)")
    print(" 2. 📊 Ver estadísticas e historial de cofres")
    print(" 3. 🎒 Ver tamaño del saco y probabilidad")
    print(" 4. ⚙️  Cambiar tamaño del saco")
    print(" 5. 🔄 Resetear todos los contadores")
    print(" 0. 🚪 Salir")
    print("=" * 42)

    opc = pedir_entero("👉 Selecciona una opción: ")
    limpiar_pantalla()

    # OPCIÓN 1: TIRAR
    if opc == 1:
        veces = pedir_entero("¿Cuántos cofres quieres abrir?: ")
        if veces == 0:
            print("No has abierto ningún cofre.")
            continue

        tokens_tanda = 0
        cofres_premiados_tanda = []

        for i in range(1, veces + 1):
            total_tiradas += 1
            numero = random.randint(1, sack)

            if numero == specialnum:
                tokens_tanda += 1
                total_tokens += 1
                cofres_premiados_tanda.append(i)
                historial_cofres.append(total_tiradas)

                # Actualizar rachas
                if racha_sin_token > peor_racha:
                    peor_racha = racha_sin_token
                racha_sin_token = 0
            else:
                racha_sin_token += 1
                if racha_sin_token > peor_racha:
                    peor_racha = racha_sin_token

        print("\n" + "-" * 42)
        if tokens_tanda == 0:
            print(f"❌ Has abierto {veces:,} cofres.")
            print("Estás shope y no te has comido una mierda 💀")
        else:
            print(
                f"🎉 ¡BINGO! En {veces:,} cofres te han salido {tokens_tanda} token(s):"
            )
            for cofre in cofres_premiados_tanda:
                print(
                    f"   🪙 Token encontrado en el cofre #{cofre:,} de esta tirada."
                )
        print("-" * 42)

    # OPCIÓN 2: ESTADÍSTICAS E HISTORIAL
    elif opc == 2:
        print("\n📊 --- ESTADÍSTICAS GLOBALES ---")
        print(f"• Cofres totales abiertos: {total_tiradas:,}")
        print(f"• Tokens totales obtenidos: {total_tokens}")
        print(f"• Racha actual sin tokens: {racha_sin_token:,} cofres")
        print(f"• Peor racha sin tokens: {peor_racha:,} cofres")

        if total_tiradas > 0 and total_tokens > 0:
            media = total_tiradas / total_tokens
            print(f"• Media actual: 1 token cada {media:,.1f} cofres")

        print("\n📜 --- HISTORIAL DE COFRES CON TOKEN ---")
        if len(historial_cofres) == 0:
            print("Todavía no te ha salido ningún token.")
        else:
            for idx, cofre_global in enumerate(historial_cofres, start=1):
                print(
                    f"   #{idx} -> Salió en el cofre global número {cofre_global:,}"
                )

    # OPCIÓN 3: INFO DEL SACO Y PROBABILIDAD
    elif opc == 3:
        probabilidad = (1 / sack) * 100
        print("\n🎒 --- INFORMACIÓN DEL SACO ---")
        print(f"• Tamaño actual del saco: {sack:,} números (del 1 al {sack:,})")
        print(f"• Número premiado: {specialnum}")
        print(f"• Probabilidad por cofre: 1 entre {sack:,}")
        print(f"• Porcentaje individual: {probabilidad:.6f}%")
        print(
            f"• Cofres necesarios para ~50% de probabilidad acumulada: {int(sack * 0.693):,}"
        )

    # OPCIÓN 4: CONFIGURAR SACO
    elif opc == 4:
        nuevo_saco = pedir_entero(
            f"Introduce el nuevo tamaño del saco (actual {sack:,}): "
        )
        if nuevo_saco < specialnum:
            print(
                f"⚠️ El saco no puede ser más pequeño que el número premiado ({specialnum})."
            )
        else:
            sack = nuevo_saco
            print(f"✅ Tamaño del saco actualizado a {sack:,}.")

    # OPCIÓN 5: RESET
    elif opc == 5:
        confirmar = input(
            "¿Seguro que quieres borrar todos los datos? (s/n): "
        ).lower()
        if confirmar == "s":
            total_tiradas = 0
            total_tokens = 0
            racha_sin_token = 0
            peor_racha = 0
            historial_cofres.clear()
            print("🔄 Todos los contadores e historiales han sido reseteados.")
        else:
            print("Operación cancelada.")

    # OPCIÓN 0: SALIR
    elif opc == 0:
        print("👋 ¡Hasta la próxima!")
        break

    else:
        print("⚠️ Opción no válida. Elige un número del menú.")