import sys
from mpyc.runtime import mpc

# Skapa säker heltalstyp (32-bit)
secint = mpc.SecInt()

async def main():
    # Kontrollera att input finns
    if len(sys.argv) < 2:
        print(f"Användning: python {sys.argv[0]} <hemligt_tal> -M 3 -I <id>")
        sys.exit(1)

    # Hämta inmatad siffra från kommandorad
    my_input = int(sys.argv[1])

    await mpc.start()

    # Konvertera till ett säkert tal och dela det
    secret_value = secint(my_input)
    shared_input = mpc.input(secret_value)

    # Summera alla deltagares inputs
    total = await mpc.output(sum(shared_input))
    print(f"[Part {mpc.pid}] Summan av alla inputs är: {total}")

    await mpc.shutdown()

mpc.run(main())
